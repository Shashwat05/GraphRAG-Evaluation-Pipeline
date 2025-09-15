import json
from pathlib import Path

# configure paths
in_path = Path("E:/NLP/GraphRag_Eval/autoe/vector_rag/activity_local.json")      # source file
out_path = Path("E:/NLP/GraphRag_Eval/autoe/vector_rag/activity_local_top2.json")  # destination file

# load JSON array
with in_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

# basic validation
if not isinstance(data, list):
    raise ValueError("Input JSON must be a list (array) of entries")

# keep only first 2 entries
trimmed = data[:2]

# write new file (pretty-printed, UTF-8)
with out_path.open("w", encoding="utf-8") as f:
    json.dump(trimmed, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(trimmed)} entries to {out_path}")
