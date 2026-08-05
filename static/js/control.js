async function startMirroring() {

    try {
	showToast(
            "Starting Replication",
            "Please wait...",
            true
	);

        const response =
            await fetch(
                "/start-mirroring",
                {
                    method: "POST"
                }
            );

        const result =
            await response.json();

        document
            .getElementById(
                "control-status"
            )
            .innerHTML =
                result.success
                    ? `✅ ${result.state}`
                    : `❌ ${result.state}`;

        await loadData();

    }
    catch (error) {

        console.error(error);

        document
            .getElementById(
                "control-status"
            )
            .innerHTML =
                "❌ Start failed";
    }
}

async function endReplication() {

    const confirmed =
        confirm(
            "Are you sure you want to end replication?"
        );

    if (!confirmed) {
        return;
    }

    try {
	showToast(
	    "Stopping Replication",
	    "Please wait...",
	    true
	);

        const response =
            await fetch(
                "/end-replication",
                {
                    method: "POST"
                }
            );

        const result =
            await response.json();

	showToast(
    	    "Replication Stopped",
            result.message,
            result.success
	);

        document
            .getElementById(
                "control-status"
            )
            .innerHTML =
                result.success
                    ? `✅ ${result.state}`
                    : `❌ ${result.state}`;

        await loadData();

    }
    catch (error) {

        console.error(error);

        document
            .getElementById(
                "control-status"
            )
            .innerHTML =
                "❌ Stop failed";
    }
}

function renderControlCard(data) {

    const monitor =
        data.monitor?.[0];

    const state =
        monitor?.state || "Unknown";

    const startButton =
        document.getElementById(
            "start-btn"
        );

    const stopButton =
        document.getElementById(
            "stop-btn"
        );

    const status =
        document.getElementById(
            "control-status"
        );

    if (
        state ===
        "Mirror Continuous"
    ) {

        startButton.disabled = true;

        stopButton.disabled = false;

        status.innerHTML =
            "🟢 Replication Running";
    }
    else {

        startButton.disabled = false;

        stopButton.disabled = true;

        status.innerHTML =
            `🔴 ${state}`;
    }
}

function showToast(
    title,
    message,
    success = true
) {

    const toast =
        document.createElement(
            "div"
        );

    toast.className =
        success
            ? "toast"
            : "toast toast-error";

    toast.innerHTML =`
<div class="toast-title">
${title}
</div>

<div class="toast-message">
${message}
</div>`
;

    document.body.appendChild(
        toast
    );

    setTimeout(
        () => {

            toast.classList.add(
                "toast-hide"
            );

            setTimeout(
                () => toast.remove(),
                500
            );

        },
        5500
    );
}
