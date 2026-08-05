from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.chcclp import (
        list_datastores,
        list_subscriptions,
        monitor_replication,
        monitor_latency,
        source_events,
        target_events,
        dashboard_data_raw,
        start_mirroring,
        end_replication
        )
from app.parser import (
        parse_monitor,
        parse_datastores,
        parse_subscriptions,
        parse_latency,
        parse_events,
        parse_dashboard
        )

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get("/")
def home():

    return {
        "status": "running"
    }

@app.get("/datastores")
def datastores():

    raw = list_datastores()

    return {
        "items": parse_datastores(raw)
    }

@app.get("/subscriptions")
def subscriptions():

    raw = list_subscriptions()

    return {
        "items": parse_subscriptions(raw)
    }

@app.get("/monitor")
def monitor():

    raw = monitor_replication()

    return {
        "items": parse_monitor(raw)
    }

@app.get("/dashboard",
         response_class=HTMLResponse)
def dashboard():

    with open(
        "templates/index.html"
    ) as f:

        return f.read()

@app.get("/latency")
def latency():

    raw = monitor_latency()

    return {
        "items": parse_latency(raw)
    }

@app.get("/events/source")
def events_source():

    raw = source_events()

    return {
        "items": parse_events(raw)
    }

@app.get("/events/target")
def events_target():

    raw = target_events()

    return {
        "items": parse_events(raw)
    }

@app.get("/dashboard-data")
def dashboard_data():

    raw = dashboard_data_raw()

    return parse_dashboard(raw)

@app.get("/dashboard-raw")
def dashboard_raw():

    return {
        "output": dashboard_data_raw()
    }

@app.post("/start-mirroring")
def api_start_mirroring():

    return start_mirroring()

@app.post("/end-replication")
def api_end_replication():

    return end_replication()
