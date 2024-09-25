# __init__.py
from models.engine.db_storage import DBStorage  # Adjust if needed
storage = DBStorage()
storage.reload()

