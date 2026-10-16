"""Full-text search: store.build_fts + search_documents (FTS5) over the SAMPLE corpus.

The `db` fixture is built via backlot.importer.byo.load, which builds every source's own FTS
index, so
these exe