from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de connexion PostgreSQL (adaptée à ton système)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Fleurys@localhost/test_react"

# Créer l'engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base des modèles
Base = declarative_base()
