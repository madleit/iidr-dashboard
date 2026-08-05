from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi import Form
from fastapi.templating import Jinja2Templates


from app.auth import (
    authenticate_user,
    user_in_group
)

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

templates = Jinja2Templates(
    directory="templates"
)

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="iidr-dashboard-secret"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

def is_authenticated(
    request: Request
):

    return request.session.get(
        "authenticated",
        False
    )

@app.get("/")
def home():

    return RedirectResponse(
        "/dashboard"
    )

@app.get("/login")
async def login_page(
    request: Request
):

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )

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

@app.get(
    "/dashboard",
    response_class=HTMLResponse
)
def dashboard(
    request: Request
):

    if not request.session.get(
        "authenticated"
    ):
        return RedirectResponse(
            "/login",
            status_code=302
        )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

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
def dashboard_data(
    request: Request
):

    if not is_authenticated(
        request
    ):
        return RedirectResponse(
            "/login",
            status_code=302
        )

    raw = dashboard_data_raw()

    return parse_dashboard(raw)

@app.get("/dashboard-raw")
def dashboard_raw(
    request: Request
):

    if not is_authenticated(
        request
    ):
        return RedirectResponse(
            "/login",
            status_code=302
        )

    return {
        "output": dashboard_data_raw()
    }

@app.post("/start-mirroring")
def api_start_mirroring(
    request: Request
):

    if not request.session.get(
        "authenticated"
    ):
        return {
            "error":
                "Not authenticated"
        }

    return start_mirroring()

@app.post("/end-replication")
def api_end_replication(
    request: Request
):

    if not request.session.get(
        "authenticated"
    ):
        return {
            "error":
                "Not authenticated"
        }

    return end_replication()

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    if not authenticate_user(
        username,
        password
    ):
        return RedirectResponse(
            "/login",
            status_code=302
        )

    if not user_in_group(
        username,
        "cdc"
    ):
        return RedirectResponse(
            "/login",
            status_code=302
        )

    request.session[
        "authenticated"
    ] = True

    request.session[
        "username"
    ] = username

    return RedirectResponse(
        "/dashboard",
        status_code=302
    )

@app.get("/logout")
async def logout(
    request: Request
):

    request.session.clear()

    return RedirectResponse(
        "/login",
        status_code=302
    )