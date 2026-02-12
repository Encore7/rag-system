create table if not exists documents (
  doc_key text primary key,
  arxiv_id text,
  source_url text,
  object_uri text,                 -- s3://bucket/key.pdf
  size_bytes bigint not null default 0,

  status text not null default 'NEW',  -- NEW, DOWNLOADED, PARSING, PARSED, FAILED
  retry_count int not null default 0,
  error_message text,

  lease_owner text,
  lease_expires_at timestamptz,
  parsing_started_at timestamptz,

  parser_version text,
  output_uri text,                  -- s3://bucket/processed/doc_key/...

  ingested_at timestamptz not null default now(),
  downloaded_at timestamptz,
  parsed_at timestamptz,
  last_seen_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_documents_status_retry_ingested
on documents (status, retry_count, ingested_at);

create index if not exists idx_documents_lease_exp
on documents (lease_expires_at);

create index if not exists idx_documents_arxiv
on documents (arxiv_id);

create table if not exists doc_nodes (
  node_id text primary key,
  doc_key text not null references documents(doc_key) on delete cascade,

  node_type text not null,            -- title/abstract/section/subsection/table/figure/equation/references/appendix
  title text,
  parent_node_id text references doc_nodes(node_id) on delete set null,
  order_index int not null default 0,

  section_path text,
  page_start int,
  page_end int,

  bbox_json jsonb,
  node_meta jsonb,

  created_at timestamptz not null default now()
);

create index if not exists idx_doc_nodes_doc
on doc_nodes (doc_key);

create index if not exists idx_doc_nodes_parent
on doc_nodes (parent_node_id);

create table if not exists elements (
  element_id text primary key,
  doc_key text not null references documents(doc_key) on delete cascade,
  node_id text references doc_nodes(node_id) on delete set null,

  element_type text not null,
  text text not null,

  page_start int,
  page_end int,
  reading_order int,

  bbox_json jsonb,
  prov_json jsonb,

  created_at timestamptz not null default now()
);

create index if not exists idx_elements_doc
on elements (doc_key);

create index if not exists idx_elements_node
on elements (node_id);

create index if not exists idx_elements_doc_order
on elements (doc_key, reading_order);
