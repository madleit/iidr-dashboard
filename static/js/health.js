function getStatusVisual(state) {

    if (
        state === "Mirror Continuous"
    ) {
        return {
            icon: "🟢",
            cssClass: "status-green"
        };
    }

    if (
        state &&
        state !== "Unknown"
    ) {
        return {
            icon: "🟠",
            cssClass: "status-yellow"
        };
    }

    return {
        icon: "🔴",
        cssClass: "status-red"
    };
}

function getLatencyClass(latencyValue) {

    if (
        latencyValue === "N/A"
    ) {
        return "status-red";
    }

    const value =
        parseInt(
            latencyValue,
            10
        );

    if (
        Number.isNaN(value)
    ) {
        return "status-red";
    }

    if (
        value > 30
    ) {
        return "status-red";
    }

    if (
        value > 5
    ) {
        return "status-yellow";
    }

    return "status-green";
}

function getEventPercent(count) {

    return Math.min(
        count * 10,
        100
    );
}

function renderHealth(data) {

    const sub =
        data.subscriptions?.[0];

    const monitor =
        data.monitor?.[0];

    const latency =
        data.latency?.[0];

    const sourceEvents =
        data.events?.source?.length || 0;

    const targetEvents =
        data.events?.target?.length || 0;

    const state =
        monitor?.state || "Unknown";

    const latencyValue =
        latency?.latency || "N/A";

    const statusVisual =
        getStatusVisual(state);

    const latencyClass =
        getLatencyClass(latencyValue);

    const sourcePercent =
        getEventPercent(sourceEvents);

    const targetPercent =
        getEventPercent(targetEvents);

    const lastUpdate =
        new Date()
            .toLocaleTimeString();

    const subscriptionName =
        sub?.subscription || "N/A";

    const sourceName =
        sub?.source || "N/A";

    const targetName =
        sub?.target || "N/A";

    document
        .getElementById("health")
        .innerHTML =
`
<div class="health-title">
    ${statusVisual.icon} ${escapeHtml(subscriptionName)}
</div>

<div class="health-grid">

    <div class="health-item">
        <div class="health-label">
            Status
        </div>

        <div class="health-value ${statusVisual.cssClass}">
            ${escapeHtml(state)}
        </div>
    </div>

    <div class="health-item">
        <div class="health-label">
            Latency
        </div>

        <div class="health-value ${latencyClass}">
            ${escapeHtml(latencyValue)}
        </div>

        <div class="health-sub">
            seconds
        </div>
    </div>

    <div class="health-item">
        <div class="health-label">
            Source
        </div>

        <div class="health-value">
            ${escapeHtml(sourceName)}
        </div>
    </div>

    <div class="health-item">
        <div class="health-label">
            Target
        </div>

        <div class="health-value">
            ${escapeHtml(targetName)}
        </div>
    </div>

    <div class="health-item">
        <div class="health-label">
            Source Events
        </div>

        <div class="counter-value">
            ${sourceEvents}
        </div>

        <div class="mini-bar">
            <div
                class="mini-bar-fill"
                style="width:${sourcePercent}%">
            </div>
        </div>
    </div>

    <div class="health-item">
        <div class="health-label">
            Target Events
        </div>

        <div class="counter-value">
            ${targetEvents}
        </div>

        <div class="mini-bar">
            <div
                class="mini-bar-fill"
                style="width:${targetPercent}%">
            </div>
        </div>
    </div>

</div>

<div class="last-update">
    Last Update: ${escapeHtml(lastUpdate)}
</div>
`;
}
