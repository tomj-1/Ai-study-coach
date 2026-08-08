#Ai Study Coach

AI Study Coach is an app that turns notes or pdfs into quizzes it uses Open AI's API for quiz generation and Streamlit for the UI. 

## Features

-Paste notes or upload PDF
-Generate quizzes with Easy, Medium, or Hard difficulty
- RAG-based quiz generation
- Reranking of retrieved chunks
- duplicate-question detection
- AI grading and feedback
- Retry incorrect questions
- Weak-topic practice
- Accuracy analytics

## How it works

Quiz Generate From AI:
1. User's notes and difficulty are sent to OpenAI API in a promp
2. AI generates a quiz from the notes
3. Quiz is returned as a JSON, converted to a Python list and then displayed on Streamlit app

Quiz Generation From RAG:
1. Notes are split into chunks.
2. Each chunk is converted into an embedding.
3. The quiz topic is also embedded.
4. Cosine similarity retrieves the most relevant chunks.
5. A reranker improves the retrieved results.
6. The selected context is sent to the OpenAI API to generate the quiz.
7. Quiz is returned as a JSON, converted to a Python list and then displayed on Streamlit app

Grade Quiz
1.Answers are graded by AI and used for analytics.

## Tech Stack

- Python
- Streamlit
- OpenAI API
- OpenAI Embeddings
- Pandas
- scikit-learn
- pypdf

## Running Locally

Clone the repository:

```bash
git clone YOUR_REPO_URL
cd Ai-study-coach
```
## Setup

Install Dependencies:

```bash
pip install -r requirements.txt
```

Create a Streamlit secret File:

```text
.streamlit/secrets.toml
```
in file put:

```toml
OPENAI_API_KEY = "your-openai-api-key"
```

##Run App

```bash
streamlit run "app ui/code/App.py"
```
