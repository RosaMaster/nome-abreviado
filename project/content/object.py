import json

# Objeto JSON
data = {
  "nome": "Joao",
  "idade": 30,
  "cidade": "Sao Paulo"
}

print(type(data))
print('*************')

# Converter JSON para string
json_string = json.dumps(data)
print(type(json_string))

print(json_string)

# Converter string para JSON
data = json.loads(json_string)
nome = data["nome"]
print('*************')
print(type(data))
print(data)
print(data["nome"])

print('*************')
print(type(nome))
print(nome)