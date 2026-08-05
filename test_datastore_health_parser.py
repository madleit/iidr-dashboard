# test_datastore_health_parser.py

from app.chcclp import datastore_health_raw
from app.parser import parse_datastore_health

raw = datastore_health_raw()

result = parse_datastore_health(
    raw
)

print(result)
