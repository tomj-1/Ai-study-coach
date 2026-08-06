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
        st.session_state.notes = saved_note
        st.session_state.quiz = ai.generate_quiz(saved_note)

    if "graded_quiz" not in st.session_state:
        st.session_state.graded_quiz = []

    if "graded" not in st.session_state:
        st.session_state["graded"] = False

    if st.button("Grade Quiz"):
        st.session_state["graded"] = True
        st.session_state.graded_quiz = ai.grade_quiz(st.session_state.quiz)
        path = "app ui/data/results.csv"
        df = pd.DataFrame(st.session_state.graded_quiz)
        # method for header names since when I delete data on the file it won't make a header next try
        file_needs_header = not os.path.exists(path) or os.path.getsize(path) == 0
        df.to_csv(path, mode="a", header=file_needs_header, index=False)

    # code to display feedback
    if st.session_state["graded"]:
        for i, item in enumerate(st.session_state.graded_quiz):
            st.markdown(f"Question {i + 1}")
            st.write(item["question"])

            st.write("Your answer:")
            st.write(item["user_answer"])

            st.write("Correct Answer")
            st.write(item["answer"])

            st.write(f"Grade: {item['grade'] * 100:.0f}")
            st.write(f"Feedback: {item['feedback']}")

            st.divider

        wrong_questions = []

        for item in st.session_state.graded_quiz:
            if item["grade"] == 0:
                wrong_questions.append(item)

        if st.button(
            "Retry Wrong Question",
            key="retry_wrong_questions_button",
        ):
            st.session_state.quiz = wrong_questions

    if "show_weak_topics" not in st.session_state:
        st.session_state.show_weak_topics = False
    if st.button("weak topics"):
        st.session_state.show_weak_topics = True
    if st.session_state.show_weak_topics:
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
                topic_names = weak_topics.index.tolist()

                selected_topics = []
                for index, topic in enumerate(topic_names):
                    checked = st.checkbox(topic, key=f"weak_topic{index}")

                    if checked:
                        selected_topics.append(topic)

                if st.button("pratice weak topics"):
                    st.session_state.quiz = ai.weak_topic_practice(
                        st.session_state.notes, selected_topics
                    )

    if st.session_state.quiz:
        st.title("Quiz: ")
        for i, word in enumerate(st.session_state.quiz):
            question = word["question"]
            answer = st.text_area(
                question, placeholder="answer here", key=f"answer_{i}"
            )
            word["user_answer"] = answer
