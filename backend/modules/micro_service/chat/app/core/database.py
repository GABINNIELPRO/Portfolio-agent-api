import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ============================================================
# 1) Récupération dynamique de DATABASE_URL depuis l'env
# ============================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL n'est pas défini. "
        "Définis-le dans docker-compose.yml ou dans ton environnement."
    )

# Exemple attendu dans Docker :
# postgresql+psycopg2://raguser:ragpass@postgres:5432/ragdb

# Exemple pour RDS :
# postgresql+psycopg2://postgres:Password123@my-rds.us-east-1.rds.amazonaws.com:5432/postgres

# ============================================================
# 2) Création du moteur SQLAlchemy
# ============================================================

engine = create_engine(
    DATABASE_URL,
    future=True,
    pool_pre_ping=True,  # vérifie que la connexion est active
)

# ============================================================
# 3) Session local
# ============================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ============================================================
# 4) Base pour les modèles ORM
# ============================================================

Base = declarative_base()

# ============================================================
# 5) Fonction utilitaire (optionnelle)
# ============================================================

def get_db():
    db = SessionLocal() # creer une session a la base
    # SessionLocal() fabrique une session et c'est unstandard web
    try:
        yield db# equivalent à je donne la session à FastAPI pour qu’il l’utilise”
    finally:
        db.close()
# avec cette fonction la création des session se fait automatiquement
