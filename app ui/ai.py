from openai import OpenAI
import json
class AI:
    
    def generate_quiz(self, notes):
        self.notes = notes 
        client = OpenAI()
        response = client.responses.create(
        model="gpt-5.4-mini",
        input= f"""
        From notes, make 5 quiz Qs.
        JSON only: question, answer, topic, difficulty, user_answer(just a field on the json the user will give this).
        Answers under 15 words.
        Notes: {notes}
        """,
        text={"format": {"type": "json_object"}},
        )

        quiz = json.loads(response.output_text)
        
        return quiz
    
    def grade_quiz(self, quiz):
        self.quiz = quiz
        client = OpenAI()
        response = client.responses.create(
        model="gpt-5.4-mini",
        input= f"""
        From the quiz, grade each user_answer against the answer.
        Return JSON only with: question, answer, user_answer, topic, difficulty, grade, feedback.
        Grade should be from 0 to 1.
        Feedback should be short.
        Quiz: {quiz}
        """,
        text={"format": {"type": "json_object"}},
        )

        feedback = json.loads(response.output_text)
        
        return feedback

    

    