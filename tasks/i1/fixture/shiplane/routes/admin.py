def stats(req, ctx):
    return {t: ctx.store.count(t) for t in ("shipments", "outbox", "audit_log")}


def reload_config(req, ctx):
    return {"env": ctx.settings.env}


def register(app):
    app.route("GET", "/admin/stats")(stats)
    app.route("POST", "/admin/reload")(reload_config)
