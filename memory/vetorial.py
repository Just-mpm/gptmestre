# memory/vetorial.py

from chromadb import Client
from chromadb.config import Settings

chroma_client = Client(Settings(persist_directory='memory/db'))
collection = chroma_client.get_or_create_collection('copy_outputs')

def salvar_copy(id_copy, texto):
    collection.add(documents=[texto], ids=[id_copy])

def buscar_copies(query):
    return collection.query(query_texts=[query], n_results=3)
