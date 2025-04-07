import random
import string

# Função para gerar senha
def gerar_senha(tamanho, incluir_especiais):
    # Definir caracteres básicos (letras e números)
    caracteres = string.ascii_letters + string.digits
    
    # Adicionar caracteres especiais se o usuário quiser
    if incluir_especiais:
        caracteres += string.punctuation
    
    # Gerar a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Entrada do usuário
tamanho = int(input("Digite o tamanho da senha desejada: "))
opcao = input("Incluir caracteres especiais? (s/n): ").strip().lower()

# Converter resposta do usuário para booleano
incluir_especiais = opcao == 's'

# Gerar e exibir a senha
senha_gerada = gerar_senha(tamanho, incluir_especiais)
print(f"Sua senha gerada é: {senha_gerada}")
