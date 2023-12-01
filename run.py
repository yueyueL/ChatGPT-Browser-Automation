from chatbot import ChatGPTClient
import time
import os


target_url = "https://chat.openai.com/?model=gpt-4"
chathead = ChatGPTClient(username="your_email@gmail.com", password="your_password", skip_login=False, incognito=False, headless=False, login_type="normal", user_data_dir='/path/to/your/user/', target_url=target_url)
time.sleep(3)  
prompts_p = "prompts/test1.txt"
with open(prompts_p, "r") as f:
    prompts = f.readlines()
    prompts = [p.strip() for p in prompts]

for i in range(0, len(prompts)):
    print(prompts[i])
    answer = chathead.interact(prompts[i])
    print(answer)
    time.sleep(5)
