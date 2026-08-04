function escapeHtml(value) {

    if (
        value === null ||
        value === undefined
    ) {
        return "";
    }

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}

function buildTable(data) {

    if (
        !data ||
        data.length === 0
    ) {
        return '<p class="no-data">No data</p>';
    }

    const columns =
        Object.keys(data[0]);

    let html =
        "<table>";

    html +=
        "<thead><tr>";

    columns.forEach(
        column => {
            html +=
                "<th>" +
                escapeHtml(column) +
                "</th>";
        }
    );

    html +=
        "</tr></thead>";

    html +=
        "<tbody>";

    data.forEach(
        row => {

            html +=
                "<tr>";

            columns.forEach(
                column => {
                    html +=
                        "<td>" +
                        escapeHtml(row[column]) +
                        "</td>";
                }
            );

            html +=
                "</tr>";
        }
    );

    html +=
        "</tbody></table>";

    return html;
}

function renderDatastores(data) {

    document
        .getElementById("datastores")
        .innerHTML =
            buildTable(data);
}

function renderSubscriptions(data) {

    document
        .getElementById("subscriptions")
        .innerHTML =
            buildTable(data);
}

function renderMonitor(data) {

    document
        .getElementById("monitor")
        .innerHTML =
            buildTable(data);
}

function renderLatency(data) {

    document
        .getElementById("latency")
        .innerHTML =
            buildTable(data);
}
