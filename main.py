import random
import string

#Definir os caracteres disponiveis 
caracteres = string.ascii_letters + string.digits + string.punctuation

#Função para gerar a senha
def gerar_senha(tamanho):
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

#Entrada do usuario
tamanho = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho)

#Exibir a senha gerada
print(f"Sua senha gerada é : {senha_gerada}")