from app.embeddings.client import EmbeddingClient

client = EmbeddingClient()

embedding = client.embed("Python FastAPI AWS")

print(len(embedding))