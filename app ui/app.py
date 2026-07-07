import streamlit as st

class app:
    st.title("Ai Study Coach")

    st.header("paste your notes")

    saved_note = {
    "notes_title": st.text_input("notes title",placeholder = "put note title here", label_visibility= "collapsed"),
    "notes" : st.text_area("notes", placeholder = "paste notes here", label_visibility= "collapsed")
    }
    if st.button('Quiz Generate'):
    #code for quiz generation 
        # TODO: add code to put questions into quiz array after quiz genraetion code made 
        quiz = []
        
        answers = []
        for i, question in enumerate(quiz):
            answer = st.text_area(question, placeholder = "answer here")
            answers.append(answer)

    if st.button('Grade Quiz'):
        #code for grading quiz 
        pass

    if st.button('weak topics'):
        #code for showing weak topics
        pass



