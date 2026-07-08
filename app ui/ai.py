from openai import OpenAI
class ai:
    
    def generate_quiz(self, notes):
        self.notes = notes 
        client = OpenAI()
        #TODO: figure out json output 
        response = client.responses.create(
        model="gpt-5.4-mini",
        input= prompt,
        )
        
        prompt = f"""
        From notes, make 5 quiz Qs.
        JSON only: question, answer, topic, difficulty.
        Answers under 15 words.
        Notes: {notes}
        """
        return response.output_text

    

    