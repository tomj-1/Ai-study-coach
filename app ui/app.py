import streamlit as st
import AI
class App:
    st.title("Ai Study Coach")

    st.header("paste your notes")
     
    saved_note = {
    "notes_title": st.text_input("notes title",placeholder = "put note title here", label_visibility= "collapsed"),
    "notes" : st.text_area("notes", placeholder = "paste notes here", label_visibility= "collapsed")
    }
    ai = AI.AI()

    #using session states to save values so trhey aren't lost on reruns 
    if "quiz" not in st.session_state:
        st.session_state.quiz = []
    
    if st.button('Quiz Generate'):
        st.session_state.quiz = ai.generate_quiz(saved_note) 
    
    if st.session_state.quiz:
        for i, word in enumerate(st.session_state.quiz):
            question = word["question"]
            answer = st.text_area(question, placeholder = "answer here",key=f"answer_{i}")
            word["user_answer"] = answer

    if st.button('Grade Quiz'):
        st.text_area(ai.grade_quiz(quiz))

    if st.button('weak topics'):
        #code for showing weak topics
        pass



