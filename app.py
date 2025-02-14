import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')


# Load a pre-trained Hugging face model
chatbot = pipeline("text-generation", model="distilgpt2")

# Define healthcare-specific response logic
def healthCare_chatBot(user_input):
    # Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the Doctor?"
    elif "medication" in user_input:
        return "It is important to take medication as prescribed by the Doctor and on time.\nIf you have any concerns consult with the Doctor."
    elif "emergency" in user_input:
        return "Immediately contact the concerned authorities first without wasting time:\n1. Ambulance: 102/108\n2.Medical Assistance: 104\n3. Mental Health and Psychosocial Issues: 108\n4. Assistance to Senior Citizens: 14567\n5. Assistance to Physically Challenged: 1800-572-8980"
    else:
        # For other inputs, use the Hugging face model to generate a response
        response = chatbot(user_input, max_length=250, num_return_sequences=1, no_repeat_ngram_size=2)
        return response[0]['generated_text']


# Streamlit web app interface
def main():
    # Set up the web app title and input area
    st.title("AI Healthcare Assistant 🤖")
    st.write("Welcome to the AI Health assistant Chatbot")

    # Add a menu bar
    st.sidebar.title("Menu")
    menu_option = st.sidebar.radio("Choose an option", ["Chat", "About Us", "Important Links"])

    if menu_option == "Chat":
        # Display the simple text input for user queries
        user_input = st.text_input("How can I assist you today?")

        # Display chatbot response
        if st.button("Submit"):
            if user_input:
                st.write("User: ", user_input)
                with st.spinner("Processing your query, Please wait..."):
                    response = healthCare_chatBot(user_input)
                
                st.write("AI Health Assistant: ", response)
            else:
                st.write("Please enter a message to get a response.")
    
    elif menu_option == "About Us":
        st.sidebar.write("### About Us")
        st.write("""
        **AI Healthcare Assistant Chatbot:**
        This chatbot is designed to provide basic healthcare-related assistance.
        It uses advanced natural language processing model to generate responses.
        Note: This is not a substitute for professional medical advice.
        Always consult a healthcare professional for accurate diagnosis and treatment.
        """)
    
    elif menu_option == "Important Links":
        st.sidebar.write("### 🔗Important Links")
        st.write("""
        - [Project Git URL] (https://github.com/Hunter8394/MyProjects.git)
        - [Hugging Face Models] (https://huggingface.co/models)
        - [Streamlit Documentation] (https://docs.streamlit.io/)
        - [NLTK Documentation] (https://www.nltk.org/)
        """)

if __name__ == "__main__":
    main()