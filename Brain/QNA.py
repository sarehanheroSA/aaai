fileopen = open("Data\\API.txt", "r")
API = fileopen.read()
fileopen.close()
 
 
 
import openai
from dotenv import load_dotenv
openai.api_key = API
load_dotenv()
completion = openai.Completion()
 
def Questionans(question,chat_log = None):
    FileLog = open("Database\\Qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
 
    if chat_log is None:
        chat_log = chat_log_template
 
    prompt = f'{chat_log}You : {question}\nKhushi : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
 
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nKhushi : {answer}"
    FileLog = open("Database\\Qna_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
