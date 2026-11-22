from ..pricing import quote


def get_quote(req, ctx):
    return {"cents": quote(req["postal"], float(req["weight_kg"]), ctx.settings)}


def zone_rates(req, ctx):
    return ctx.rates.fetch_rates(req["zone"])


def bulk_quotes(req, ctx):
    return [{"cents": quote(i["postal"], float(i["weight_kg"]), ctx.settings)} for i in req["items"]]


def register(app, settings):
    app.route("GET", "/v1/rates")(get_quote)
    app.route("GET", "/v1/rates/{zone}")(zone_rates)
    if settings.get("features.bulk_quotes"):
        app.route("POST", "/v1/rates/bulk")(bulk_quotes)
