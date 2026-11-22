from types import SimpleNamespace

from . import settings as settings_mod
from .clients.geocode_client import GeocodeClient
from .clients.http import Http
from .clients.label_client import LabelClient
from .clients.rates_client import RatesClient
from .routes import admin, rates, shipments
from .store import Audit, Store


class App:
    def __init__(self):
        self.routes = []

    def route(self, method, path):
        def deco(fn):
            self.routes.append((method, path, fn))
            return fn
        return deco

    def dispatch(self, method, path, req, ctx):
        for m, p, fn in self.routes:
            if m == method and p == path:
                return fn(req, ctx)
        raise LookupError(f"{method} {path}")


def healthz(req, ctx):
    return {"ok": True}


def _no_network(method, url, body, timeout):
    raise ConnectionError("no transport configured")


def create_app(settings=None, transport=_no_network):
    settings = settings or settings_mod.load()
    app = App()
    shipments.register(app)
    rates.register(app, settings)
    app.route("GET", "/healthz")(healthz)
    if settings.get("features.admin_api"):
        admin.register(app)
    http = Http(settings, transport)
    store = Store()
    ctx = SimpleNamespace(
        settings=settings,
        store=store,
        audit=Audit(store, settings),
        labels=LabelClient(http, settings),
        rates=RatesClient(http, settings),
        geocode=GeocodeClient(http, settings),
    )
    return app, ctx


if __name__ == "__main__":
    app, ctx = create_app()
    print(f"shiplane[{ctx.settings.env}] routes={len(app.routes)}")
