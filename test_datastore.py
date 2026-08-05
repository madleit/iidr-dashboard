# test_datastore.py

from app.chcclp import show_datastore
from app.parser import parse_datastore_details

raw_src = show_datastore(
        "CDC_SRC",
        "source"
    )

raw_tgt = show_datastore(
        "CDC_TGT",
        "target"
    )

result = parse_datastore_details(
    raw_src
)

print(result)
