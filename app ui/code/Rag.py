import json

from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

class Rag:

    def __init__(self):
        self.client = OpenAI()
        

    def chunk_text(self,text, chunk_size=1000):
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i : i + chunk_size]
            chunks.append(chunk)

        return chunks

    def get_embedding(self,text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small", input=text, encoding_format="float"
        )
        
        return response.data[0].embedding

    def embed_chunks(self,chunks):
        chunk_embeddings = []

        for chunk in chunks:
            embedding = self.get_embedding(chunk)

            chunk_embeddings.append({
                "text": chunk,
                "embedding": embedding
            })
        return chunk_embeddings

    def retrieve(self, query, embedded_chunks, amount):
        query_embedding = self.get_embedding(query)

        for chunk in embedded_chunks:
            similarity = cosine_similarity(
                [query_embedding],
                [chunk["embedding"]]
            )[0][0]

            chunk["similarity"] = similarity

        best_chunks = sorted(
            embedded_chunks,
            key = lambda chunk: chunk["similarity"], 
            reverse = True
        )[:amount]

        return best_chunks

    def rerank(self, query, candidates, amount):

        chunks_text = ""

        for i, chunk in enumerate(candidates):
            chunks_text += f"\nChunk {i}:\n{chunk['text']}\n"

        response = self.client.responses.create(
            model = "gpt-5.4-mini",
            input = f"""
            Rank the chunks by how useful they are for answering the query.
            Query:{query} Chunks:{chunks_text}Return JSON only:
            {{ "ranking": [{{"index": 0, "score": 0.0}}]}}
            Give every chunk a relevance score from 0 to 1."""
        )

        data = json.loads(response.output_text)

        ranking = sorted(
            data["ranking"],
            key = lambda item: item["score"],
            reverse = True
        )

        best_chunks = []

        for item in ranking[:amount]:
            best_chunks.append(
                candidates[item["index"]]
            )

        return best_chunks




