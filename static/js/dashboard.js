let dashboardData =
    null;

let currentEventTab =
    "source";

async function loadData() {

    try {

        const response =
            await fetch(
                "/dashboard-data",
                {
                    cache: "no-store"
                }
            );

        if (
            !response.ok
        ) {
            throw new Error(
                "Failed to load dashboard-data"
            );
        }

        dashboardData =
            await response.json();

        renderHealth(
            dashboardData
        );

	renderOverview(
    	    dashboardData
	);

	renderControlCard(
            dashboardData
	);

        renderDatastores(
            dashboardData.datastores || []
        );
	
	renderDatastoreHealth(
    	    dashboardData
	);

    renderDatastoreDetails(
            dashboardData
    );
    
    renderSubscriptions(
        dashboardData.subscriptions || []
    );

    renderMonitor(
        dashboardData.monitor || []
    );

    renderLatency(
        dashboardData.latency || []
    );

    renderEvents(
        dashboardData.events?.[currentEventTab] || []
    );
    } catch (error) {

        console.error(
            error
        );

        const errorHtml =
            '<div class="error-box">' +
            'Erro ao carregar dashboard-data.' +
            '</div>';

        document
            .getElementById("health")
            .innerHTML =
                errorHtml;
    }
}

document.addEventListener(
    "DOMContentLoaded",
    loadData
);

setInterval(
    loadData,
    30000
);
