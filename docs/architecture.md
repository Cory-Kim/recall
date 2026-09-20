# Architecture

RECALL is organized around a local pipeline:

```text
local files -> extraction -> SQLite index -> search -> cited results
```

The first release uses deterministic keyword search. Semantic embeddings and a local language model will be introduced only after ingestion, persistence, and source citations are dependable.

