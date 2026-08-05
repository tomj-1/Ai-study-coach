import streamlit as st
import pandas as pd
import AI
import os


class App:
    st.title("Ai Study Coach")

    st.header("paste your notes")

    saved_note = {
        "notes_title": st.text_input(
            "notes title",
            placeholder="put note title here",
            label_visibility="collapsed",
        ),
        "notes": st.text_area(
            "notes", placeholder="paste notes here", label_visibility="collapsed"
        ),
    }
    ai = AI.AI()

    # using session states to save values so they aren't lost on reruns
    if "quiz" not in st.session_state:
        st.session_state.quiz = []

    if st.button("Quiz Generate"):
        st.session_state.quiz = ai.generate_quiz(saved_note)

    if st.session_state.quiz:
        for i, word in enumerate(st.session_state.quiz):
            question = word["question"]
            answer = st.text_area(
                question, placeholder="answer here", key=f"answer_{i}"
            )
            word["user_answer"] = answer

    if st.button("Grade Quiz"):
        gradedQuiz = ai.grade_quiz(st.session_state.quiz)
        # displays the json text
        st.json(gradedQuiz)
        path = "app ui/data/results.csv"
        df = pd.DataFrame(gradedQuiz)
        df.to_csv(path, mode="a", header=not os.path.exists(path), index=False)

    if st.button("weak topics"):
        path = "app ui/data/results.csv"
        if not os.path.exists(path):
            # displays as a red message
            st.error("No results file found")
        else:
            try:
                results = pd.read_csv(path)
            except pd.errors.EmptyDataError:
                st.success("No weak topics")
            else:
                topic_averages = results.groupby("topic")["grade"].mean()
                # uses boolean filtering to keep topics with averages below 70%
                weak_topics = topic_averages[(topic_averages * 100) < 70].sort_values()
                st.dataframe(weak_topics)
