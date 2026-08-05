function renderTableMappings(data) {

    const mappings =
        data.table_mappings || [];

    if (
        mappings.length === 0
    ) {

        document
            .getElementById(
                "table-mappings"
            )
            .innerHTML =
                "No table mappings";

        return;
    }

    let html = `

<table class="data-table">

<thead>

<tr>
    <th>Source Table</th>
    <th>Target Table</th>
    <th>Type</th>
    <th>Method</th>
    <th>Status</th>
</tr>

</thead>

<tbody>
`;

    mappings.forEach(
        mapping => {

            html += `

<tr>
    <td>${mapping.source_table}</td>
    <td>${mapping.target_table}</td>
    <td>${mapping.mapping_type}</td>
    <td>${mapping.method}</td>
    <td>${mapping.status}</td>
</tr>
`;
        }
    );

    html += `
</tbody>
</table>
`;

    document
        .getElementById(
            "table-mappings"
        )
        .innerHTML = html;
}

function toggleTableMappingDetails() {

    const details =
        document.getElementById(
            "table-mapping-details"
        );

    if (
        details.style.display ===
        "none"
    ) {

        details.style.display =
            "block";

    } else {

        details.style.display =
            "none";
    }
}

function renderTableMappingDetails(data) {

    const details =
        data.table_mapping_details;

    if (!details) {

        document
            .getElementById(
                "table-mapping-details"
            )
            .innerHTML =
                "No table mapping details";

        return;
    }

    document
        .getElementById(
            "table-mapping-details"
        )
        .innerHTML = `

<div class="overview-grid">

    <div class="overview-item">
        <div class="overview-label">
            Source Table
        </div>
        <div class="overview-value">
            ${details.source_table || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Target Table
        </div>
        <div class="overview-value">
            ${details.target_table || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Mapping Type
        </div>
        <div class="overview-value">
            ${details.mapping_type || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Method
        </div>
        <div class="overview-value">
            ${details.method || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Status
        </div>
        <div class="overview-value">
            ${details.status || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Prevent Recursion
        </div>
        <div class="overview-value">
            ${details.prevent_recursion || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Index Mode
        </div>
        <div class="overview-value">
            ${details.index_mode || ""}
        </div>
    </div>

    <div class="overview-item">
        <div class="overview-label">
            Conflict Resolution
        </div>
        <div class="overview-value">
            ${details.conflict_resolution_method || ""}
        </div>
    </div>

</div>

`;
}

function toggleColumnMappings() {

    const mappings =
        document.getElementById(
            "column-mappings"
        );

    if (
        mappings.style.display ===
        "none"
    ) {

        mappings.style.display =
            "block";

    } else {

        mappings.style.display =
            "none";
    }
}

function renderColumnMappings(data) {

    const mappings =
        data.column_mappings || [];

    if (
        mappings.length === 0
    ) {

        document
            .getElementById(
                "column-mappings"
            )
            .innerHTML =
                "No column mappings";

        return;
    }

    let html = `

<table class="data-table">

<thead>

<tr>
    <th>Source Column</th>
    <th>Target Column</th>
</tr>

</thead>

<tbody>
`;

    mappings.forEach(
        mapping => {

            html += `

<tr>
    <td>${mapping.source_column}</td>
    <td>${mapping.target_column}</td>
</tr>
`;
        }
    );

    html += `
</tbody>
</table>
`;

    document
        .getElementById(
            "column-mappings"
        )
        .innerHTML = html;
}