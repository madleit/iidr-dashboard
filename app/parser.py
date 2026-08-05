def parse_monitor(output):
    rows = []

    for line in output.splitlines():
        if "SYSLAB" in line:
            parts = line.split()

            rows.append({
                "subscription": parts[0],
                "state": " ".join(parts[1:3])
            })

    return rows


def parse_datastores(raw):
    items = []

    for line in raw.splitlines():
        if line.startswith("CDC_"):
            parts = line.split()

            items.append({
                "name": parts[0],
                "host": parts[1],
                "version": parts[2]
            })

    return items


def parse_subscriptions(raw):
    items = []

    for line in raw.splitlines():
        if line.startswith("SYSLAB"):
            parts = line.split()

            items.append({
                "subscription": parts[0],
                "source": parts[1],
                "target": parts[2]
            })

    return items


def parse_latency(raw):
    items = []

    for line in raw.splitlines():
        if line.startswith("SYSLAB"):
            parts = line.split()

            items.append({
                "subscription": parts[0],
                "latency": parts[-1]
            })

    return items


def parse_events(raw):

    items = []

    for line in raw.splitlines():

        line = line.strip()

        if not line:
            continue

        if not line[0].isdigit():
            continue

        parts = line.split()

        if len(parts) < 10:
            continue

        items.append({
            "row": parts[0],
            "event_id": parts[1],
            "type": parts[2],
            "message": " ".join(parts[9:])
        })

    return items


def extract_section(raw, start_marker, end_marker):
    start = raw.find(start_marker)

    if start == -1:
        return ""

    end = raw.find(
        end_marker,
        start + len(start_marker)
    )

    if end == -1:
        return raw[start:]

    return raw[start:end]


def parse_dashboard(raw):

    datastores_raw = extract_section(
        raw,
        "list datastores;",
        "connect datastore"
    )

    subscriptions_raw = extract_section(
        raw,
        "list subscriptions;",
        "monitor replication;"
    )

    monitor_raw = extract_section(
        raw,
        "monitor replication;",
        "select subscription"
    )

    latency_raw = extract_section(
        raw,
        "monitor subscription latency;",
        "list subscription events count 10 type source;"
    )

    source_events_raw = extract_section(
        raw,
        "list subscription events count 10 type source;",
        "list subscription events count 10 type target;"
    )

    target_events_raw = extract_section(
        raw,
        "list subscription events count 10 type target;",
        "exit;"
    )

    datastore_health_raw = extract_section(
        raw,
        "show datastore name CDC_SRC;",
        "exit;"
    )

    table_mappings_raw = extract_section(
        raw,
        "list table mappings;",
        "show datastore name CDC_SRC;"
    )

    table_mapping_details_raw = extract_section(
        raw,
        "show table mapping;",
        "exit;"
    )

    return {
        "datastores": parse_datastores(datastores_raw),
        "subscriptions": parse_subscriptions(subscriptions_raw),
        "monitor": parse_monitor(monitor_raw),
        "latency": parse_latency(latency_raw),
        "events": {
            "source": parse_events(source_events_raw),
            "target": parse_events(target_events_raw)
            },
        "datastore_health": parse_datastore_health(datastore_health_raw),
        "table_mappings": parse_table_mappings(table_mappings_raw),
        "table_mapping_details": parse_table_mapping_details(table_mapping_details_raw)
    }

def get_subscription_state(
    monitor_data,
    subscription="SYSLAB"
):

    for item in monitor_data:

        if (
            item.get(
                "subscription"
            ) == subscription
        ):
            return item.get(
                "state",
                "Unknown"
            )

    return "Unknown"

def parse_datastore_details(raw):

    datastore = {}

    for line in raw.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("PROPERTY"):
            continue

        if line.startswith("---"):
            continue

        if ":" not in line:
            continue

        key, value = line.split(
            ":",
            1
        )

        datastore[
            key.strip()
        ] = value.strip()

    return datastore

def parse_datastore_health(raw):

    source_lines = []
    target_lines = []

    current = None

    for line in raw.splitlines():

        if "show datastore name CDC_SRC" in line:
            current = "source"
            continue

        if "show datastore name CDC_TGT" in line:
            current = "target"
            continue

        if current == "source":
            source_lines.append(line)

        elif current == "target":
            target_lines.append(line)

    source = parse_datastore_details(
        "\n".join(source_lines)
    )

    target = parse_datastore_details(
        "\n".join(target_lines)
    )

    return {
        "source": source,
        "target": target
    }

def parse_table_mappings(raw):

    mappings = []

    capture = False

    for line in raw.splitlines():

        if "Table mappings for subscription" in line:

            capture = True
            continue

        if capture and line.startswith("SOURCE TABLE"):

            continue

        if capture and line.startswith("---"):

            continue

        if not capture:

            continue

        line = line.strip()

        if not line:

            continue

        if line.startswith("Repl >"):

            break

        parts = line.split()

        if len(parts) < 6:

            continue

        mappings.append(
            {
                "source_table": parts[0],
                "target_table": parts[1],
                "mapping_type": parts[2],
                "method": parts[3],
                "status": parts[4],
                "prevent_recursion": parts[5]
            }
        )

    return mappings

def parse_table_mapping_details(raw):

    details = {}

    current_section = "general"

    for line in raw.splitlines():

        line = line.rstrip()

        if not line:
            continue

        # Ignora cabeçalhos
        if line.startswith("PROPERTY"):
            continue

        if line.startswith("----------------"):
            continue

        if line.startswith("TARGET KEY"):
            current_section = "target_key"
            continue

        if line.startswith("REFRESH"):
            current_section = "refresh"
            continue

        if line.startswith("ROW-FILTERING"):
            current_section = "row_filtering"
            continue

        if line.startswith("CONFLICTS"):
            current_section = "conflicts"
            continue

        print(
            f"[{current_section}] {line}"
        )

        if ":" not in line:
            continue

        key, value = line.split(
            ":",
            1
        )

        key = key.strip()
        value = value.strip()

        if current_section == "general":

            mapping = {
                "Source Table": "source_table",
                "Target Table": "target_table",
                "Mapping Type": "mapping_type",
                "Method": "method",
                "Prevent Recursion": "prevent_recursion",
                "Status": "status"
            }

        elif current_section == "target_key":

            mapping = {
                "Index Mode": "index_mode"
            }

        elif current_section == "refresh":

            mapping = {
                "Row Subset Refresh": "row_subset_refresh",
                "Source WHERE clause": "source_where_clause",
                "Target WHERE clause": "target_where_clause"
            }

        elif current_section == "row_filtering":

            mapping = {
                "Row-filtering Expression": "row_filtering_expression",
                "Select/Omit Rows": "select_omit_rows"
            }

        elif current_section == "conflicts":

            mapping = {
                "Conflict Detection Columns":
                    "conflict_detection_columns",

                "Conflict Resolution Method":
                    "conflict_resolution_method",

                "Value Comparison Column":
                    "value_comparison_column",

                "User Exit (with Path)":
                    "user_exit"
            }

        else:

            mapping = {}

        if key in mapping:

            details[
                mapping[key]
            ] = value

    return details

def parse_column_mappings(raw):

    mappings = []

    capture = False

    for line in raw.splitlines():

        line = line.rstrip()

        if (
            "Column mappings for table mapping"
            in line
        ):
            capture = True
            continue

        if not capture:
            continue

        if line.strip().startswith("SOURCE"):
            continue

        if line.strip().startswith("---"):
            continue

        if not line.strip():
            continue

        if line.startswith("Repl >"):
            break

        parts = line.split()

        if len(parts) < 2:
            continue

        mappings.append(
            {
                "source_column": parts[0],
                "target_column": parts[1]
            }
        )

    return mappings