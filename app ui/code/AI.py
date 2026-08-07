from openai import OpenAI
import json


class AI:

    def _init_(self):
        self.client = OpenAI()

    def generate_quiz(self, notes, difficulty):
        self.notes = notes
        self.difficulty = difficulty
        response = self.client.responses.create(
            model="gpt-5.4-mini",
            input=f"""JSON only: {{"quiz":[{{"question":"","answer":"","hint":"","topic":"","difficulty":"{difficulty}","user_answer":""}}]}}
            Create 5 {difficulty} questions from: {notes}
            Use consistent topics, LaTeX math in $...$, and hints only for hard questions.""",
            text={"format": {"type": "json_object"}},
        )

        # converts json file to list
        data = json.loads(response.output_text)

        return data["quiz"]

    def grade_quiz(self, quiz):
        self.quiz = quiz
        response = self.client.responses.create(
            model="gpt-5.4-mini",
            input=f"""
        Grade every quiz item.

        Return JSON only in this exact format:
        {{
        "graded_quiz": [
        {{
        "question": "",
        "answer": "",
        "user_answer": "",
        "topic": "",
        "difficulty": "",
        "grade": 0,
        "feedback": ""
        }}
        ]
        }}

        Quiz:
        {quiz}
        """,
            text={"format": {"type": "json_object"}},
        )

        # converts json file to list with dictionaries in each index
        feedback = json.loads(response.output_text)

        return feedback["graded_quiz"]

    def weak_topic_practice(self, notes, topics):
        self.notes = notes
        self.topics = topics
        response = self.client.responses.create(
            model="gpt-5.4-mini",
            input=f"""Return JSON only: {{"quiz":[{{"question":"","answer":"","topic":"","difficulty":"","user_answer":""}}]}}
            Create exactly 5 questions from the notes.
            Focus only on: {topics}
            Use specific, consistent topic names.
            Set user_answer to "".
            Format all math as LaTeX inside $...$.
            Notes: {notes}""",
            text={"format": {"type": "json_object"}},
        )

        # converts json file to list with dictionaries in each index
        data = json.loads(response.output_text)

        return data["quiz"]
