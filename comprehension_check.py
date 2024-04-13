import app
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

def page_1():
    
    st.title("Comprehension Check in Multiple Languages - UNIT 3")

    # Define passages and questions in multiple languages
    passage = '''Selvi went to a garden. She saw a yellow flower on the tomato plant. 
    She went to pluck it. A bee came and said, “Please, leave it for me. It is my food” 
    She saw a red tomato on the tomato plant. She went to pluck it. A parrot came and said, 
    “Please, leave it for me. It is my food”. She saw a green leaf on the tomato plant. 
    A grasshopper came and said, “Please don’t pluck the leaf. It is my food.” 
    Watering the plant, Selvi said, “You provide food for all of us. Thank you very much”.
    '''
    
    # Language selection
    to_language = st.selectbox("Select Language", list(LANGUAGES.values()))
    result_passage = app.translator_function(passage, "en", app.language_mapping[to_language]).text

    questions_answers = {
    "questions": [
            {
                "question": "What did Selvi see on the tomato plant?",
                "choices": [
                    "Yellow flower",
                    "Red tomato",
                    "Green leaf",
                    "All of the above"
                ],
                "answer": "All of the above"
            },
            {
                "question": "Who asked Selvi to leave the yellow flower?",
                "choices": [
                    "Bee",
                    "Parrot",
                    "Grasshopper",
                    "None of the above"
                ],
                "answer": "Bee"
            },
            {
                "question": "What did Selvi say while watering the plant?",
                "choices": [
                    "Thank you",
                    "You provide food for all of us",
                    "Both A and B",
                    "None of the above"
                ],
                "answer": "Both A and B"
            },
            {
                "question": "What did the grasshopper ask Selvi?",
                "choices": [
                    "To leave the flower",
                    "To leave the tomato",
                    "To leave the leaf",
                    "To water the plant"
                ],
                "answer": "To leave the leaf"
            },
            {
                "question": "What did the bee say about the yellow flower?",
                "choices": [
                    "It is its food",
                    "It is poisonous",
                    "It is beautiful",
                    "It is harmful"
                ],
                "answer": "It is its food"
            },
            {
                "question": "What did Selvi pluck from the tomato plant?",
                "choices": [
                    "Flower",
                    "Tomato",
                    "Leaf",
                    "All of the above"
                ],
                "answer": "All of the above"
            }
        ]
}

    # Display the passage
    st.write("Read the following passage:")
    st.write(result_passage)

    # Initialize score
    score = 0

    # Display and check answers
    for question_data in questions_answers["questions"]:
        question = question_data["question"]
        result_question = app.translator_function(question, "en", app.language_mapping[to_language]).text
        choices = question_data["choices"]
        result_choices = [app.translator_function(choice, "en", app.language_mapping[to_language]).text for choice in choices]
        answer = question_data["answer"]
        result_answer = app.translator_function(answer, "en", app.language_mapping[to_language]).text
        user_answer = st.radio(result_question, result_choices)
        if user_answer == result_answer:
            score += 1

    # Display the score
    st.write(f"Your score: {score}/{len(questions_answers['questions'])}")
