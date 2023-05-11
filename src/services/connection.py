import os
import sqlite3

DIRNAME = os.path.dirname(__file__)

try:
    CONNECTION = sqlite3.connect(os.path.join(
        DIRNAME, '../services/high_scores.db'))
except FileNotFoundError:
    pass
