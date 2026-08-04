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

    return {
        "datastores": parse_datastores(datastores_raw),
        "subscriptions": parse_subscriptions(subscriptions_raw),
        "monitor": parse_monitor(monitor_raw),
        "latency": parse_latency(latency_raw),
        "events": {
            "source": parse_events(source_events_raw),
            "target": parse_events(target_events_raw)
        }
    }
