"""
Использование интерфейса chat с передачей списка сообщений с ролями позволяет реализовать
многоходовой диалог
"""
from ollama import Client

client = Client(host='http://dmitrbp-pc:11434')
response = client.chat(
    model='llama3.1',
    messages=[
        {'role': 'user', 'content': 'Почему небо голубое?'}
    ]
)

print(response.message.content)