import streamlit as st
import AI
class App:
    st.title("Ai Study Coach")

    st.header("paste your notes")
     
    saved_note = {
    "notes_title": st.text_input("notes title",placeholder = "put note title here", label_visibility= "collapsed"),
    "notes" : st.text_area("notes", placeholder = "paste notes here", label_visibility= "collapsed")
    }
    ai = AI()
    if st.button('Quiz Generate'):
        quiz = ai.generate_quiz(saved_note)
        # TODO: add code to put questions into quiz array after quiz genraetion code made 
        
        
        answers = []
        for i, word in enumerate(quiz):
            question = word["question"]
            answer = st.text_area(question, placeholder = "answer here")
            word["user_answer"] =answer

    if st.button('Grade Quiz'):
        #code for grading quiz 
        pass

    if st.button('weak topics'):
        #code for showing weak topics
        pass



