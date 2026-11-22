import sqlite3
import time

SCHEMA = """
CREATE TABLE IF NOT EXISTS shipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    postal TEXT NOT NULL,
    weight_kg REAL NOT NULL,
    status TEXT NOT NULL,
    created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS outbox (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    event TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    shipment_id INTEGER
);
"""


class Store:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.executescript(SCHEMA)

    def insert_shipment(self, postal, weight_kg, status="pending"):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO shipments (postal, weight_kg, status, created_at) VALUES (?, ?, ?, ?)",
                (postal, weight_kg, status, time.time()),
            )
        return cur.lastrowid

    def mark_labeled(self, shipment_id):
        with self.conn:
            self.conn.execute("UPDATE shipments SET status = 'labeled' WHERE id = ?", (shipment_id,))

    def mark_failed(self, shipment_id):
        with self.conn:
            self.conn.execute("UPDATE shipments SET status = 'label_failed' WHERE id = ?", (shipment_id,))
            self.conn.execute(
                "INSERT INTO outbox (shipment_id, event) VALUES (?, 'shipment.label_failed')", (shipment_id,)
            )

    def get_shipment(self, shipment_id):
        row = self.conn.execute(
            "SELECT id, postal, weight_kg, status FROM shipments WHERE id = ?", (shipment_id,)
        ).fetchone()
        return row and dict(zip(("id", "postal", "weight_kg", "status"), row))

    def count(self, table):
        assert table in ("shipments", "outbox", "audit_log")
        return self.conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]


class Audit:
    def __init__(self, store, settings):
        self.store = store
        self.enabled = bool(settings.get("features.audit"))

    def record(self, action, shipment_id=None):
        if not self.enabled:
            return
        with self.store.conn:
            self.store.conn.execute(
                "INSERT INTO audit_log (action, shipment_id) VALUES (?, ?)", (action, shipment_id)
            )
