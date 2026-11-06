"""
Библиотека Ollama поддерживает передачу функций Python в качестве инструментов,
позволяя модели определять необходимость их вызова и генерировать параметры.
Это основа для создания агентов.
"""

import ollama

def add_two_numbers(a: int, b: int) -> int:
    """Сложение двух целых чисел"""
    return a + b

client = ollama.Client(host='http://dmitrbp-pc:11434')
response = client.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Сколько будет 10 + 10?'}],
    tools=[add_two_numbers],  # Передача ссылки на функцию
)

# Проверка, хочет ли модель вызвать инструмент
if response.message.tool_calls:
    for tool in response.message.tool_calls:
        if tool.function.name == 'add_two_numbers':
            # Выполнение фактической функции с использованием параметров, сгенерированных моделью
            result = add_two_numbers(**tool.function.arguments)
            print(f"Результат вызова инструмента: {result}")