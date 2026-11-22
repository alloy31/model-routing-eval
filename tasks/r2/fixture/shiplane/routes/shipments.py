from ..errors import LabelFailed, TransientError
from ..pricing import quote


def create_shipment(req, ctx):
    price = quote(req["postal"], req["weight_kg"], ctx.settings)
    sid = ctx.store.insert_shipment(req["postal"], req["weight_kg"])
    try:
        ctx.labels.post_label({"id": sid, "postal": req["postal"], "price": price})
    except TransientError as exc:
        ctx.store.mark_failed(sid)
        ctx.audit.record("label_failed", sid)
        raise LabelFailed(str(exc)) from exc
    ctx.store.mark_labeled(sid)
    ctx.audit.record("labeled", sid)
    return {"id": sid, "price": price}


def get_shipment(req, ctx):
    return ctx.store.get_shipment(int(req["id"]))


def register(app):
    app.route("POST", "/v1/shipments")(create_shipment)
    app.route("GET", "/v1/shipments/{id}")(get_shipment)
    app.route("GET", "/v1/shipment/{id}")(get_shipment)  # 구버전 경로 호환
