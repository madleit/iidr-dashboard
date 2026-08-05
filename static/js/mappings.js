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
