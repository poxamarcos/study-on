import random

# Definindo a string de caracteres que serão utilizados para gerar a senha
caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz101103107109113127131137139149151157163167173179181191193197199211223227229233239241251257263269271277281283293307311313173313373734935335936737337938338939740140941942143143343944344945746146346747948749149950350952152354154755756356957157758759359960160761361761963164364765365966167367768369170170971972773373974375175776176977378779780981182182382782983985385785986387788188388790791191992993794194795396797197798399997!@#$%^&*()_-+=][}{/.,<>?"

# Definindo a quantidade de vezes que a senha será embaralhada
quantidade_embaralho = 10
# Inicializando a variável senha
senha = 1

# Loop para embaralhar a senha várias vezes
while senha < quantidade_embaralho:
    # Transformando a string de caracteres em uma lista para poder embaralhá-la
    lista_caracteres = list(caracteres)
    # Embaralhando os caracteres na lista
    random.shuffle(lista_caracteres)
    # Juntando os caracteres embaralhados de volta em uma string
    string_embaralhada = ''.join(lista_caracteres)
    # Incrementando o contador de senha
    senha = senha + 1

# Selecionando os primeiros 14 caracteres da senha embaralhada como senha final
senha_final = string_embaralhada[:14]

# Imprimindo a senha final
print(senha_final)
