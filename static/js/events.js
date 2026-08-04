function renderEvents(data) {

    document
        .getElementById("events")
        .innerHTML =
            buildTable(data);
}

function showSourceEvents() {

    currentEventTab =
        "source";

    if (
        dashboardData
    ) {
        renderEvents(
            dashboardData.events?.source || []
        );
    }
}

function showTargetEvents() {

    currentEventTab =
        "target";

    if (
        dashboardData
    ) {
        renderEvents(
            dashboardData.events?.target || []
        );
    }
}
