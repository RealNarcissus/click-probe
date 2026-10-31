"""Public helper module (probe F)."""

import os


def read_entry(name: str) -> str:
    path = os.path.join(os.getcwd(), "entries", name)
    with open(path) as f:
        return f.read()
