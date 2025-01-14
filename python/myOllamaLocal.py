#Requires packages:
#pip install langchain langchain-ollama  ollama

import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#Load Env variables
#load_dotenv()
context_variables = {"name": "Charlie", "user_id": 8675309}
name = context_variables.get("name", None)
    
template = """
    Answer the question below.

    here is the conversation history: {context}

    Question: {question}

    Answer:
"""
# notes about model files
# 
# llama3.2 has 3B parameters, is 2.0Gb in file size
# llama3.2:1b has 1B parameters, is about 1.3Gb in file size 
# other files wtih more parameters are 2x the size of 3.2:1b or larger, such as 
# llama3.1 which is 4.7Gb in size 
#
# to use a model it must be installed locally with the ollama pull command  

model = OllamaLLM(model="llama3.2:1b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    user_input = ""
    print("Welcome to your ollama chat bot. Type 'exit' to quit.")
    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Ollama Bot: ",result)
        context += f"\n{name}: {user_input}\nBot: {result}"


if __name__ == "__main__":
    handle_conversation()