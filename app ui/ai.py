from openai import OpenAI
class ai:
    
    def generate_quiz(self, notes):
        self.notes = notes 
        client = OpenAI()
        response = client.responses.create(
        model="gpt-5.4-mini",
        input= f"""
        From notes, make 5 quiz Qs.
        JSON only: question, answer, topic, difficulty.
        Answers under 15 words.
        Notes: {notes}
        """,
        text={"format": {"type": "json_object"}},
        )
        
        return response.output_text

    

    