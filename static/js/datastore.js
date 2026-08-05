function renderDatastoreHealth(data) {

    console.log(
	"DATASTORE HEALTH EXECUTOU"
    );	

    const source =
        data.datastore_health?.source;

    const target =
        data.datastore_health?.target;

    if (!source || !target) {

        document
            .getElementById(
                "datastore-health"
            )
            .innerHTML =
                "No datastore information";

        return;
    }

    const versionMatch =
        source.Version ===
        target.Version;

    document
        .getElementById(
            "datastore-health"
        )
        .innerHTML = `

<div class="overview-grid">

    <div class="overview-item">

        <div class="overview-label">
            Source
        </div>

        <div class="overview-value">
            ${source.Name}
        </div>

        <div class="health-sub">
            ${source.Database}
        </div>

        <div class="health-sub">
            ${source["Host Name"]}:${source.Port}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target
        </div>

        <div class="overview-value">
            ${target.Name}
        </div>

        <div class="health-sub">
            ${target.Database}
        </div>

        <div class="health-sub">
            ${target["Host Name"]}:${target.Port}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Version Match
        </div>

        <div class="overview-value">

            ${
                versionMatch
                    ? "✅"
                    : "ℹ"
            }

        </div>

        <div class="health-sub">

            ${
                versionMatch
                    ? "Same Version"
                    : "Different Versions"
            }

        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Source TLS
        </div>

        <div class="overview-value">
            ${source["TLS Encryption"]}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target TLS
        </div>

        <div class="overview-value">
            ${target["TLS Encryption"]}
        </div>

    </div>

</div>
`;
}
