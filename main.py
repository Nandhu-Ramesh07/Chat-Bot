from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = '''
Answer the question below

Here is the conversation History : {context}
Question : {question}
Answer :
'''

model = OllamaLLM(model='llama3.2:1b')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def conversation():
    context = ''
    print("Hi.. I am Sarah, How can I help you. Type exit to quit")
    while True:
        user_input = input("You : ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context" : context, "question" : user_input})
        print("Sarah : ",result)
        context += f"\nUser:{user_input}\nAI:{result}"

if __name__ == "__main__":
    conversation()