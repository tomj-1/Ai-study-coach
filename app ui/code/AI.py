from openai import OpenAI
import json
class AI:
    
    def generate_quiz(self, notes):
        self.notes = notes 
        client = OpenAI()
        response = client.responses.create(
        model="gpt-5.4-mini",
        input= f"""
        Return JSON only with a "quiz" list.
        Each quiz item has: question, answer, topic, difficulty, user_answer.
        Make exactly 5 quiz items.
        Set user_answer to "".
        Notes: {notes}
        """,
        text={"format": {"type": "json_object"}},
        )

        # converts json file to list 
        data = json.loads(response.output_text)
        
        return data["quiz"]
    
    def grade_quiz(self, quiz):
        self.quiz = quiz
        client = OpenAI()
        response = client.responses.create(
        model="gpt-5.4-mini",
        input = f"""
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

        feedback = json.loads(response.output_text)
        
        return feedback["graded_quiz"]

    

    