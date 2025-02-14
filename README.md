# AI Healthcare Assistant Chatbot 🤖

## 📌 Overview
The **AI Healthcare Assistant Chatbot** is an interactive chatbot designed to provide basic healthcare-related assistance. It utilizes **Natural Language Processing (NLP)** techniques with the **Hugging Face DistilGPT-2 model** to generate responses, along with rule-based logic for specific healthcare-related queries.

🚨 **Note:** This chatbot is **not** a substitute for professional medical advice. Always consult a healthcare professional for accurate diagnosis and treatment.

---

## ⚡ Features
- Provides **general healthcare-related responses**
- Recognizes **specific medical keywords** and gives predefined responses
- Utilizes **Hugging Face DistilGPT-2** for generating responses
- Simple and interactive **Streamlit-based web interface**
- Includes **emergency contact details**

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** (for UI)
- **NLTK** (for text processing)
- **Hugging Face Transformers** (DistilGPT-2 model)

---

## 🚀 Installation & Setup
Follow these steps to run the chatbot locally:

### 1️⃣ Clone the Repository
```sh
git clone (https://github.com/Hunter8394/MyProjects.git)
cd git-folder-name
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```
streamlit run app.py
```

---

## 🔹 Usage
1. Open the **Streamlit web app**.
2. Enter your health-related query in the text input box.
3. Click **Submit** to receive a response.
4. Use the **sidebar menu** to navigate between sections:
   - **Chat**: Interact with the chatbot.
   - **About Us**: Learn more about the project.
   - **Important Links**: Access useful resources.

---

## 📜 Predefined Responses
The chatbot provides predefined responses for specific keywords:
| Keyword      | Response |
|-------------|------------------------------------------------------|
| symptom | "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice." |
| appointment | "Would you like to schedule an appointment with the Doctor?" |
| medication | "It is important to take medication as prescribed by the Doctor and on time." |
| emergency | "Immediately contact emergency services: 102/108 (Ambulance), 104 (Medical Assistance), etc." |

For other queries, the chatbot uses **Hugging Face's DistilGPT-2 model** to generate responses.

---

## 📌 Important Links
- [GitHub Repository](https://github.com/Hunter8394/MyProjects.git)
- [Hugging Face Models](https://huggingface.co/models)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [NLTK Documentation](https://www.nltk.org/)

---

## 👥 Contributors
- **Your Name** - [GitHub Profile](https://github.com/Hunter8394)

Feel free to contribute and improve the project! 🚀

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

