import sqlite3, os, time
from typing import Optional, Dict, Any

_DB_PATH = os.environ.get("BIZBOT_DB", "bizbot.db")

def _conn():
    c = sqlite3.connect(_DB_PATH, check_same_thread=False)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    with _conn() as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            api_key TEXT PRIMARY KEY,
            customer_id TEXT,
            subscription_id TEXT,
            active INTEGER NOT NULL DEFAULT 0,
            updated_at INTEGER NOT NULL
        )""")
        con.commit()

def upsert_subscriber(api_key: str, customer_id: Optional[str], subscription_id: Optional[str], active: Optional[bool]=None):
    now = int(time.time())
    with _conn() as con:
        row = con.execute("SELECT api_key FROM subscribers WHERE api_key=?", (api_key,)).fetchone()
        if row:
            con.execute("""
                UPDATE subscribers
                   SET customer_id=COALESCE(?, customer_id),
                       subscription_id=COALESCE(?, subscription_id),
                       active=COALESCE(?, active),
                       updated_at=?
                 WHERE api_key=?""",
                (customer_id, subscription_id, int(active) if active is not None else None, now, api_key)
            )
        else:
            con.execute("""
                INSERT INTO subscribers(api_key, customer_id, subscription_id, active, updated_at)
                VALUES (?, ?, ?, ?, ?)""",
                (api_key, customer_id, subscription_id, int(active or 0), now)
            )
        con.commit()

def set_active(api_key: str, active: bool):
    upsert_subscriber(api_key, None, None, active)

def get_subscriber_by_api_key(api_key: str) -> Optional[Dict[str, Any]]:
    with _conn() as con:
        r = con.execute("SELECT * FROM subscribers WHERE api_key=?", (api_key,)).fetchone()
        return dict(r) if r else None

def list_subscribers(limit: int = 200) -> list[Dict[str, Any]]:
    with _conn() as con:
        rows = con.execute("SELECT * FROM subscribers ORDER BY updated_at DESC LIMIT ?", (limit,)).fetchall()
        return [dict(r) for r in rows]
