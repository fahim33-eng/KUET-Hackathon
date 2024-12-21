from .database import engine
from . import models

def init_db():
    models.Base.metadata.create_all(bind=engine) 