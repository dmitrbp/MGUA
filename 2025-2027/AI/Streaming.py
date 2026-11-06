"""
Для интерактивных приложений включите stream=True, и модель будет возвращать текст по мере генерации,
что повышает удобство для пользователя
"""
from ollama import Client

client = Client(host='http://dmitrbp-pc:11434')
stream = client.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Расскажи короткую историю'}],
    stream=True
)

for chunk in stream:
    # Каждый chunk содержит фрагмент содержимого
    print(chunk.message.content, end='', flush=True)