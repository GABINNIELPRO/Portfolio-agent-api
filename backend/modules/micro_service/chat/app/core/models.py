import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import (Column, String, Integer, DateTime, ForeignKey, Text,
Enum as SAEnum, ARRAY, Float
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import VECTOR
from .database import Base


# =====================================================================
# ENUM STATUS
# =====================================================================
# class DocumentStatus(str, Enum): # Un Enum sert à limiter les valeurs possibles à une liste fixe de choix.
#     uploaded = "uploaded"
#     extracted = "extracted"
#     described = "described"
#     chunked = "chunked"
#     indexed = "indexed"


# # =====================================================================
# # TABLE conversations
# # =====================================================================
# class Conversation(Base):
#     # Nom de la table
#     __tablename__ = "conversations"

#     # Metadonnées
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     title = Column(Text, nullable=True)
#     created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
#     updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

#     # Relation vers document_responses
#     responses = relationship("DocumentResponse",back_populates="conversation",cascade="all, delete-orphan")


# =====================================================================
# DOCUMENT CHUNKS
# =====================================================================
class Document(Base):
    # Nom de la table
    __tablename__ = "document"

    # Metadonnées
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(Integer, nullable=False)
    file_text = Column(Text, nullable=False)
    embedding = Column(VECTOR(3072), nullable=True)
 

# =====================================================================
# SEARCH RESULTS
# =====================================================================
class SearchResult(Base):
     # Nom de la table
    __tablename__ = "search_results"

     # Metadonnées
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query = Column(Text, nullable=False)
    k = Column(Integer, nullable=False, default=1)
    document_ids = Column(ARRAY(Text))
    document_texts = Column(ARRAY(Text))
    distances = Column(ARRAY(Float))


# # =====================================================================
# # DOCUMENT RESPONSES
# # =====================================================================
# class DocumentResponse(Base):
#     # Nom de la table
#     __tablename__ = "document_responses"

#     # Metadonnées
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     conversation_id = Column(UUID(as_uuid=True),ForeignKey("conversations.id", ondelete="CASCADE"),nullable=False)
#     document_id = Column(UUID(as_uuid=True),ForeignKey("documents.id", ondelete="CASCADE"),nullable=False)
#     user_query = Column(Text, nullable=False)
#     generated_response = Column(Text, nullable=False)
#     top_k_chunk_ids = Column(ARRAY(UUID(as_uuid=True)))
#     chunk_texts = Column(ARRAY(Text))
#     distances = Column(ARRAY(Float))
#     model_name = Column(String, nullable=False, default="gpt-4o-mini")
#     average_distance = Column(Float)
#     min_distance = Column(Float)
#     created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
#     updated_at = Column(DateTime, nullable=True)

#     # Relations
#     document = relationship("DocumentMetadata", back_populates="responses")
#     conversation = relationship("Conversation", back_populates="responses")
