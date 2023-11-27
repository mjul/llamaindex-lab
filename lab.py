import logging
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os.path

STORAGE_PATH = "storage"
DATA_PATH = "data"

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH, exist_ok=True)
    documents = SimpleDirectoryReader(DATA_PATH).load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir=STORAGE_PATH)
else:
    storage_context = StorageContext.from_defaults(persist_dir=STORAGE_PATH)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("Can you summarize the abstracts of these papers?")
print(response)