from llama_index.llms.ollama import Ollama
from llama_index.embeddings.clip import ClipEmbedding
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext

import qdrant_client
from llama_index.core import SimpleDirectoryReader

Settings.llm = Ollama(model="llama3.2:latest", request_timeout=120.0)
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)
Settings.image_embed_model = ClipEmbedding()

# Create a local Qdrant vector store
try:
    client._client._flock_file.close()
    client = qdrant_client.QdrantClient(path="qdrant_img_db")
except:
    client = qdrant_client.QdrantClient(path="qdrant_img_db")

text_store = QdrantVectorStore(
    client=client, collection_name="text_collection"
)
image_store = QdrantVectorStore(
    client=client, collection_name="image_collection"
)
storage_context = StorageContext.from_defaults(
    vector_store=text_store, image_store=image_store
)

# Create the MultiModal index
documents = SimpleDirectoryReader("test_data").load_data()
index = MultiModalVectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
)

# — then query with Scout driving the answers —
query_engine = index.as_query_engine()


def query_model(input:str) -> dict:
    """
    Given user input, return model response as dictionary.
    """
    response = query_engine.query(input)
    for node in response.source_nodes:
        print(f"File ID: {node.metadata.get('file_name')}, Score: {node.score:.2f}\nContent: {node.text[:200]}...\nMetadata: {node.metadata}")
        print("----------------------------------------")
    print("\n\n")
    files = []
    for node in response.source_nodes:
        f = {}
        f['file_path'] = node.metadata.get('file_path')
        f['file_type'] = node.metadata.get('file_type')
        f['file_name'] = node.metadata.get('file_name')
        files.append(f)
    return {
        "response": response,
        "files": files
    }