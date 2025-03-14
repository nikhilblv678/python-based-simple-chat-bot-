# -*- coding: utf-8 -*-
"""simple_chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10jazbaqYZMCAeK6qm_bokKk1fdq7V3AG
"""

!pip install openai
import openai
from openai import OpenAI

# Define your OpenAI API Key
openai.api_key = "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"

def chat_with_gpt(prompt, model="gpt-4"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def chatbot_conversation():
    print("ChatGPT Chatbot is ready! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")

def handle_faqs(user_input):
    faqs = {
        # Greetings and Wishes
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! What can I do for you?",
        "good morning": "Good morning! How can I help?",
        "good afternoon": "Good afternoon! What brings you here today?",
        "good evening": "Good evening! How can I assist?",
        "how are you?": "I'm just a bot, but I'm here to help! How about you?",
        "happy birthday": "Thank you! I hope it's a great day for the person you're celebrating.",
        "happy new year": "Happy New Year! Wishing you all the best.",
        "merry christmas": "Merry Christmas! Hope you're enjoying the festive season.",
        "goodbye": "Goodbye! Have a great day.",

                # Wishes for Teachers or Sirs
        "good morning sir": "Good morning, sir! Wishing you a great day ahead.",
        "good afternoon teacher": "Good afternoon, teacher! Hope you’re doing well.",
        "happy teacher's day": "Happy Teacher's Day! Thank you for your guidance and support.",
        "thank you teacher": "You're welcome! Teachers like you make learning inspiring.",
        "good evening sir": "Good evening, sir! How can I assist you today?",

        # Wishes for Father
        "happy father's day": "Happy Father's Day! Wishing your father a wonderful day.",
        "good morning dad": "Good morning, Dad! Hope you have a fantastic day.",
        "thank you father": "You're welcome! Fathers deserve all the gratitude.",
        "happy birthday dad": "Happy Birthday, Dad! Wishing him happiness and health.",
        "good night father": "Good night, Father! Sweet dreams.",

        # Wishes for Mother
        "happy mother's day": "Happy Mother's Day! Wishing your mom all the love and joy.",
        "good morning mom": "Good morning, Mom! Have a beautiful day.",
        "thank you mom": "You're welcome! Moms are the best!",
        "happy birthday mom": "Happy Birthday, Mom! May her day be filled with love and laughter.",
        "good night mother": "Good night, Mother! Rest well.",

        # Wishes for Brother
        "happy birthday brother": "Happy Birthday, Brother! Wishing him all the best.",
        "good morning bro": "Good morning, bro! Have a great day.",
        "thank you brother": "You're welcome! Brothers always have our backs.",
        "good night brother": "Good night, Brother! Sleep tight.",
        "congrats bro": "Congratulations, bro! Wishing him continued success.",

        # Wishes for Sister
        "happy birthday sister": "Happy Birthday, Sister! Hope her day is as amazing as she is.",
        "good morning sis": "Good morning, sis! Have a fantastic day.",
        "thank you sister": "You're welcome! Sisters make life special.",
        "good night sister": "Good night, Sister! Sweet dreams.",
        "congrats sis": "Congratulations, sis! So proud of her achievements.",

        # Wishes for Grandfather
        "happy birthday grandfather": "Happy Birthday, Grandfather! Wishing him health and happiness.",
        "good morning grandpa": "Good morning, Grandpa! Hope he has a great day.",
        "thank you grandpa": "You're welcome! Grandpas are full of wisdom and love.",
        "good night grandfather": "Good night, Grandfather! Sleep well.",
        "happy anniversary grandpa": "Happy Anniversary, Grandpa! Wishing him and Grandma many more happy years together.",

        # Wishes for Grandmother
        "happy birthday grandmother": "Happy Birthday, Grandmother! May her day be filled with love.",
        "good morning grandma": "Good morning, Grandma! Have a lovely day.",
        "thank you grandma": "You're welcome! Grandmas are the sweetest.",
        "good night grandmother": "Good night, Grandmother! Rest well.",
        "happy anniversary grandma": "Happy Anniversary, Grandma! Wishing her and Grandpa endless happiness together.",

        # Python
        "what is python?": "Python is a high-level, interpreted programming language known for its simplicity and versatility.",
        "how do i install python?": "You can install Python from the official website: https://www.python.org/downloads/",
        "what is a python dictionary?": "A dictionary in Python is a collection of key-value pairs that is unordered and mutable.",
        "what are python functions?": "Functions in Python are reusable blocks of code defined using the `def` keyword.",
        "what is python used for?": "Python is used for web development, data analysis, artificial intelligence, scientific computing, and more.",

        # Machine Learning
        "what is machine learning?": "Machine learning is a branch of AI that enables systems to learn from data and improve performance over time.",
        "what are the types of machine learning?": "Machine learning types include supervised, unsupervised, and reinforcement learning.",
        "what is supervised learning?": "Supervised learning uses labeled data to train models to make predictions.",
        "what is unsupervised learning?": "Unsupervised learning identifies patterns in data without labels.",
        "what is reinforcement learning?": "Reinforcement learning trains models to make decisions by rewarding desired behaviors.",

        # Deep Learning
        "what is deep learning?": "Deep learning is a subset of machine learning that uses neural networks with many layers to analyze complex data.",
        "what are neural networks?": "Neural networks are computational models inspired by the human brain, used in deep learning.",
        "what is a convolutional neural network?": "A convolutional neural network (CNN) is a type of neural network designed for image recognition and processing.",
        "what is recurrent neural network?": "A recurrent neural network (RNN) is designed to handle sequential data, like time series or text.",
        "what is backpropagation?": "Backpropagation is an algorithm used to train neural networks by adjusting weights based on error gradients.",

        # Artificial Intelligence
        "what is artificial intelligence?": "Artificial intelligence (AI) is the simulation of human intelligence in machines that can perform tasks requiring intelligence.",
        "what is the turing test?": "The Turing Test evaluates a machine's ability to exhibit behavior indistinguishable from a human.",
        "what is natural language processing?": "Natural Language Processing (NLP) enables machines to understand, interpret, and generate human language.",
        "what are ai applications?": "AI applications include chatbots, recommendation systems, autonomous vehicles, and healthcare diagnostics.",
        "what is a chatbot?": "A chatbot is an AI-powered application designed to simulate human-like conversations.",

        # Human Thinking
        "what is human thinking?": "Human thinking involves reasoning, problem-solving, and decision-making processes.",
        "how do humans learn?": "Humans learn through observation, practice, and integrating new knowledge with existing information.",
        "what is critical thinking?": "Critical thinking involves analyzing and evaluating information to make logical decisions.",
        "what is creativity?": "Creativity is the ability to generate original ideas by connecting different concepts.",
        "what is emotional intelligence?": "Emotional intelligence is the ability to recognize, understand, and manage emotions in oneself and others.",

                # Wishes for Friends
        "happy birthday friend": "Happy Birthday, my friend! Wishing you a year full of joy and success.",
        "good morning friend": "Good morning, friend! Hope your day is as awesome as you are.",
        "thank you friend": "You're welcome, my friend! Always here to help.",
        "good night friend": "Good night, friend! Sweet dreams.",
        "congrats friend": "Congratulations, friend! So happy for you.",

        # Wishes for Colleagues
        "good morning colleague": "Good morning, colleague! Let's have a productive day.",
        "happy work anniversary": "Happy work anniversary! Wishing you continued success.",
        "congratulations colleague": "Congratulations on your achievement, colleague! Well deserved.",
        "thank you colleague": "You're welcome, colleague! It's great working with you.",
        "good night colleague": "Good night, colleague! Rest well and see you tomorrow.",

        # Wishes for Boss or Manager
        "good morning boss": "Good morning, boss! Ready to make today productive.",
        "thank you boss": "Thank you, boss! I appreciate your leadership and support.",
        "happy work anniversary boss": "Happy work anniversary, boss! Thanks for guiding us.",
        "happy birthday boss": "Happy Birthday, boss! Wishing you a fantastic day.",
        "good night boss": "Good night, boss! See you tomorrow.",

        # Wishes for Spouse (Husband/Wife)
        "happy anniversary spouse": "Happy Anniversary, my love! Here's to many more years of happiness.",
        "good morning love": "Good morning, my love! I hope you have a wonderful day ahead.",
        "thank you love": "You're welcome, my dear! Always here for you.",
        "happy birthday spouse": "Happy Birthday, my dear! Wishing you all the love in the world.",
        "good night love": "Good night, love! Sleep well.",

        # Wishes for Teachers or Professors
        "thank you professor": "You're welcome, Professor! Your teachings inspire us every day.",
        "good morning professor": "Good morning, Professor! Hope you have a great day ahead.",
        "happy teacher's day professor": "Happy Teacher's Day, Professor! Thank you for being so inspiring.",
        "happy birthday professor": "Happy Birthday, Professor! Wishing you a wonderful day.",
        "good night professor": "Good night, Professor! Rest well.",

        # Wishes for Neighbors
        "good morning neighbor": "Good morning, neighbor! Hope you have a pleasant day.",
        "thank you neighbor": "You're welcome, neighbor! It's a pleasure to help.",
        "happy birthday neighbor": "Happy Birthday, neighbor! Wishing you a day full of joy.",
        "good night neighbor": "Good night, neighbor! Sleep tight.",
        "happy holidays neighbor": "Happy Holidays, neighbor! Hope you enjoy the season.",

        # Wishes for Loved Ones (General)
        "good morning my love": "Good morning, my love! Wishing you a day full of happiness.",
        "happy birthday my love": "Happy Birthday, my love! I wish you the best today and always.",
        "thank you my dear": "You're welcome, my dear! I'm here whenever you need me.",
        "good night my love": "Good night, my love! Sweet dreams and rest well.",

        # Miscellaneous
        "what is the internet of things?": "The Internet of Things (IoT) refers to interconnected devices that communicate and exchange data over the internet.",
        "what is blockchain?": "Blockchain is a decentralized digital ledger that records transactions across a network securely.",
        "what is cloud computing?": "Cloud computing provides on-demand access to computing resources over the internet.",
        "what is big data?": "Big data refers to large and complex datasets that require advanced tools for storage and analysis.",
        "what is data science?": "Data science combines statistics, programming, and domain knowledge to analyze and interpret data."
    }

    return faqs.get(user_input.lower(), "I'm sorry, I don't have an answer for that. Can you rephrase or ask something else?")

def chatbot_with_faq():
    print("ChatGPT Chatbot is ready! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Check FAQs
        faq_response = handle_faqs(user_input)
        if faq_response:
            print(f"Chatbot: {faq_response}")
        else:
            # Use ChatGPT for other queries
            response = chat_with_gpt(user_input)
            print(f"Chatbot: {response}")

def chat_with_custom_bot(prompt, system_message, model="gpt-4"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def custom_chatbot():
    system_message = "You are a travel guide chatbot. Provide helpful and friendly advice about travel destinations."
    print("Custom Chatbot is ready! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Safe travels! Goodbye!")
            break
        response = chat_with_custom_bot(user_input, system_message)
        print(f"Chatbot: {response}")

# chatbot_with_faq()
# custom_chatbot()
#openai.api_key = "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"

chatbot_with_faq()
custom_chatbot()

