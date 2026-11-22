"""로컬 디버깅용 라우트. 필요할 때 app.py 에서 직접 붙여 쓴다."""


def dump_settings(req, ctx):
    return dict(ctx.settings._d)


def register(app):
    app.route("GET", "/debug/settings")(dump_settings)
