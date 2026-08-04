function renderOverview(data)
{
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
        parseInt(
            latency?.latency || 999
        );

    const delta =
        Math.abs(
            sourceEvents -
            targetEvents
        );

    let score = 0;

    if (
        state ===
        "Mirror Continuous"
    )
    {
        score += 50;
    }

    if (
        latencyValue <= 5
    )
    {
        score += 25;
    }

    if (
        delta === 0
    )
    {
        score += 25;
    }

    let scoreClass =
        "score-red";

    if (score >= 90)
    {
        scoreClass =
            "score-green";
    }
    else if (score >= 60)
    {
        scoreClass =
            "score-yellow";
    }

    let syncStatus =
        "OUT OF SYNC";

    let syncColor =
        "score-red";

    if (delta === 0)
    {
        syncStatus =
            "IN SYNC";

        syncColor =
            "score-green";
    }

    document
        .getElementById("overview")
        .innerHTML =
`
<div class="overview-grid">

    <div class="overview-item">

        <div class="overview-label">
            Sync Status
        </div>

        <div class="overview-value ${syncColor}">
            ${syncStatus}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Event Delta
        </div>

        <div class="overview-value">
            ${delta}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Health Score
        </div>

        <div class="overview-value ${scoreClass}">
            ${score}%
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Source Events
        </div>

        <div class="overview-value">
            ${sourceEvents}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target Events
        </div>

        <div class="overview-value">
            ${targetEvents}
        </div>

    </div>

</div>
`;
}
