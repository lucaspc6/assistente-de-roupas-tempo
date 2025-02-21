import requests  # Importa a biblioteca requests para fazer chamadas à API

# Chave da API para acessar os dados do OpenWeatherMap
api_key = "e02a7cf39056d69ca7908e899910decc"

# Função que sugere uma roupa com base na temperatura em Celsius
def escolherRoupa(temp):
    if temp <= 0:
        print("Está MUITO FRIO, vá de jaqueta de couro impermeável.")
    elif temp <= 10:
        print("Está frio, vá de jaqueta comum.")
    elif temp <= 20:
        print("Está fresco, pode usar uma camiseta.")
    else:
        print("Está calor, vá de regata.")

# URLs da API do OpenWeatherMap para buscar a previsão do tempo em três cidades
# O ID de cada cidade é fornecido pela API

# ID de Nova York (EUA) = 5039192
chamadaNY = f"https://api.openweathermap.org/data/2.5/weather?id={5039192}&appid={api_key}"

# ID de Ohio (EUA) = 5165418
chamadaOh = f"https://api.openweathermap.org/data/2.5/weather?id={5165418}&appid={api_key}"

# ID do Rio de Janeiro (Brasil) = 3451189
chamadaRJ = f"https://api.openweathermap.org/data/2.5/weather?id={3451189}&appid={api_key}"

# Fazendo as requisições para obter os dados do clima de cada cidade
reqNy = requests.get(chamadaNY).json()  # Requisição para Nova York
reqOh = requests.get(chamadaOh).json()  # Requisição para Ohio
reqRJ = requests.get(chamadaRJ).json()  # Requisição para Rio de Janeiro

# Obtém o dicionário que contém os dados de temperatura para Nova York
keyValueNy = reqNy['main']  # A chave 'main' contém informações como temperatura, pressão e umidade

# Itera sobre os valores do dicionário de temperatura para extrair a temperatura em Kelvin
for valor in keyValueNy.values():
    temperaturaNy = valor - 273.15  # Converte de Kelvin para Celsius
    print(f"Temperatura em Nova York: {temperaturaNy:.2f}ºC")
    escolherRoupa(temperaturaNy)  # Chama a função para sugerir uma roupa
    break  # Sai do loop após processar a primeira temperatura relevante

print()  # Adiciona uma linha em branco para melhor visualização

# Obtém o dicionário que contém os dados de temperatura para Ohio
keyValueOh = list(reqOh.items())[3][1]  # Acessa a temperatura na estrutura retornada pela API

# Itera sobre os valores do dicionário para extrair a temperatura em Kelvin
for valor in keyValueOh.values():
    temperaturaOh = valor - 273.15  # Converte de Kelvin para Celsius
    print(f"Temperatura em Ohio: {temperaturaOh:.2f}ºC")
    escolherRoupa(temperaturaOh)
    break  # Sai do loop após processar a temperatura

print()  # Linha em branco para separar a saída

# Obtém o dicionário que contém os dados de temperatura para o Rio de Janeiro
keyValueRj = list(reqRJ.items())[3][1]  # Acessa a temperatura na estrutura retornada pela API

# Itera sobre os valores do dicionário para extrair a temperatura em Kelvin
for valor in keyValueRj.values():
    temperaturaRj = valor - 273.15  # Converte de Kelvin para Celsius
    print(f"Temperatura no Rio de Janeiro: {temperaturaRj:.2f}ºC")
    escolherRoupa(temperaturaRj)
    break  # Sai do loop após processar a temperatura