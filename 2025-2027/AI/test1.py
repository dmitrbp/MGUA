from ollama import Client
from pydantic import BaseModel

class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]

client = Client(host='http://localhost:11434')
response = client.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Расскажи о Канаде.'}],
    format=Country.model_json_schema(),  # Принудительный вывод в этом формате
)

# Разбор в объект Pydantic
country = Country.model_validate_json(response.message.content)
print(country)
# Вывод: name='Canada' capital='Ottawa' languages=['English', 'French']