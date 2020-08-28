import os
import sqlite3
from contextlib import contextmanager
from typing import ContextManager

DATABASE_PATH = os.getenv("DATABASE_PATH")


@contextmanager
def database() -> ContextManager[sqlite3.Connection]:
    """A simple wrapper for the sqlite3 connection context manager."""
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        yield conn
