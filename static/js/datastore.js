function renderDatastoreHealth(data) {

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

function toggleDatastoreDetails() {

    const details =
        document.getElementById(
            "datastore-details"
        );

    if (
        details.style.display ===
        "none"
    ) {

        details.style.display =
            "block";

    }
    else {

        details.style.display =
            "none";
    }
}

function renderDatastoreDetails(data) {

    const source =
        data.datastore_health?.source;

    const target =
        data.datastore_health?.target;

    if (!source || !target) {

        document
            .getElementById(
                "datastore-details"
            )
            .innerHTML =
                "No datastore details available";

        return;
    }

    document
        .getElementById(
            "datastore-details"
        )
        .innerHTML = `

<div class="overview-grid">

    <div class="overview-item">

        <div class="overview-label">
            Source Description
        </div>

        <div class="health-sub">
            ${source.Description}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target Description
        </div>

        <div class="health-sub">
            ${target.Description}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Source Platform
        </div>

        <div class="health-sub">
            ${source.Platform}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target Platform
        </div>

        <div class="health-sub">
            ${target.Platform}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Source Type
        </div>

        <div class="health-sub">
            ${source.Type}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target Type
        </div>

        <div class="health-sub">
            ${target.Type}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Source Multi User
        </div>

        <div class="health-sub">
            ${source["Multi-User Configuration"]}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target Multi User
        </div>

        <div class="health-sub">
            ${target["Multi-User Configuration"]}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Source Table Identification
        </div>

        <div class="health-sub">
            ${source["Table Identification"]}
        </div>

    </div>

    <div class="overview-item">

        <div class="overview-label">
            Target Table Identification
        </div>

        <div class="health-sub">
            ${target["Table Identification"]}
        </div>

    </div>

</div>

`;
}