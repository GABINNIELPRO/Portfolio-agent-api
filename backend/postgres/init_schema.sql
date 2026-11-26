-- ============================================
-- Création du type ENUM document_status
-- ============================================
DO $$ BEGIN
    CREATE TYPE document_status AS ENUM ('uploaded', 'extracted', 'described', 'chunked', 'indexed');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- ============================================
-- Table conversations (DOIT ÊTRE CRÉÉE EN PREMIER)
-- ============================================
-- CREATE TABLE IF NOT EXISTS conversations (
--     id UUID PRIMARY KEY,
--     title TEXT,
--     created_at TIMESTAMP NOT NULL DEFAULT NOW(),
--     updated_at TIMESTAMP NOT NULL DEFAULT NOW()
-- );


-- ============================================
-- Table document_chunks
-- ============================================
CREATE TABLE IF NOT EXISTS document (
    id UUID PRIMARY KEY,
    document_id INT,
    file_text TEXT,
    embedding VECTOR(3072)
);

-- ============================================
-- Table search_results
-- ============================================
CREATE TABLE IF NOT EXISTS search_results (
     id UUID PRIMARY KEY,
     query TEXT NOT NULL,
     k INT NOT NULL DEFAULT 1,
     document_ids TEXT[],
     document_texts TEXT[],
     distances FLOAT[]
 );

-- ============================================
-- Table document_responses (DÉPEND DE conversations)
-- ============================================
-- CREATE TABLE IF NOT EXISTS document_responses (
--     id UUID PRIMARY KEY,
--     conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
--     document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
--     user_query TEXT NOT NULL,
--     generated_response TEXT NOT NULL,
--     top_k_chunk_ids UUID[],
--     chunk_texts TEXT[],
--     distances FLOAT[],
--     model_name VARCHAR NOT NULL DEFAULT 'gpt-4o-mini',
--     average_distance FLOAT,
--     min_distance FLOAT,
--     created_at TIMESTAMP NOT NULL DEFAULT NOW(),
--     updated_at TIMESTAMP NOT NULL DEFAULT NOW()
-- );


-- ============================================
-- Index pour la vitesse (recommandés)
-- ============================================
-- CREATE INDEX IF NOT EXISTS idx_documents_status
--     ON documents(status);

-- CREATE INDEX IF NOT EXISTS idx_chunks_docid
--     ON document_chunks(document_id, chunk_index);

-- -- Index pour accélérer la recherche d'embeddings
-- CREATE INDEX IF NOT EXISTS idx_embeddings_vector
--     ON document_chunks USING ivfflat (embedding vector_cosine_ops);

-- CREATE INDEX IF NOT EXISTS idx_images_vector
--     ON images USING ivfflat (embedding vector_cosine_ops);

-- -- Index pour accélérer les recherches par requête dans search_results
-- CREATE INDEX IF NOT EXISTS idx_search_results_query
--     ON search_results(query);

-- -- Index pour optimiser la recherche de réponses par document dans document_responses
-- CREATE INDEX IF NOT EXISTS idx_responses_docid
--     ON document_responses(document_id);
