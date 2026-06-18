import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    
) 
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

messages=[ 
    {"role": "system", "content": "You are a helpful progammers assistant"}
]

print("AI Chat Assistant")
print("Type 'exit' to end the conversation.")
print("Type 'clear' to clear the screen.")
print("Conversation started. \n")

while True:
    message=input("User: ").strip()
    
    if message.lower()=="exit":
        print("Exiting Chat. Goodbye")
        break
    
    elif message.lower()=="clear":
        clear_screen()
        print("AI Chat Assistant")
        print("Conversation restarted. \n")
        messages=[
        {"role": "system", "content": "You are a helpful progammers assistant"}
        ]
        continue 
    if not message:
        continue
    
    messages.append({"role": "user", "content": message})
    
    try:
        chat_completion= client.chat.completions.create(
        model="gpt-5",
        messages=messages
         )
    except Exception as e:
        print(f" An Error occurred: {e}")
        continue
    
    reply=chat_completion.choices[0].message.content
    
    print(f"Response: {reply}")
    messages.append({"role": "assistant", "content": reply})