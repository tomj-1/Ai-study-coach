from openai import OpenAI


class Rag:

    def chunk_text(text, chunk_size=1000):
        chunks = []

        for i in range(0, len(text), chunk_size):
            chunk = text[i : i + chunk_size]
            chunks.append(chunk)

        return chunks

    def get_embedding(text):
        client = OpenAI()
        response = client.embeddings.create(
            model="text_embedding-3-small", input=text, encoding_format="float"
        )

        return response.data[0].embedding
