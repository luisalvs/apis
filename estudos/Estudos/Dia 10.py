# cores = ['amarelo', 'verde', 'azul', 'vermelho']
# valores = [10, 20, 30, 40]

# duas_listas = zip(cores, valores) # Zip é utilizado para fazer a junção de 2 ou mais listas 

# print(list(duas_listas))

# Criar uma lista a partir do input criado pelo usuário

frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuario.split(', ') # Convertendo para uma lista e dando uma espaço doa vez que encontra os parametros passados

print(frutas_lista)