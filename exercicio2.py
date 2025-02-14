"""
2) Cadastro de Filmes

Objetivo:
Crie uma função chamada cadastrar_filmes() que simule um pequeno sistema de cadastro de filmes. Essa função deve:
- Utilizar uma tupla fixa chamada generos (por exemplo, ("Ação", "Comédia", "Drama", "Fantasia", "Terror")).
- Pedir ao usuário o título de 3 filmes e o índice do gênero (com base na tupla).
- Armazenar os dados em um dicionário, onde a chave é o título e o valor é o gênero (string).
- Ao final, exibir quantos filmes de cada gênero foram cadastrados.

Observação:
- Você pode usar uma lista para armazenar títulos antes de inseri-los no dicionário, mas não é obrigatório.
- A contagem de filmes por gênero pode ser feita percorrendo o dicionário ou usando outro dicionário auxiliar.

Exemplo de Chamada:
    cadastrar_filmes()
    # Durante a execução:
    # - O programa pede 3 filmes + índice do gênero
    # - Depois exibe quantos filmes de cada gênero foram cadastrados

Requisitos:
- Utilize ao menos uma tupla para gêneros.
- Armazene os filmes cadastrados em um dicionário.
- Exiba ao final um resumo da quantidade de filmes por gênero.
"""
# Solution:


def cadastrar_filmes():
    x = True

    count_acao = 0
    count_comedia = 0
    count_drama = 0
    count_fantasia = 0
    count_terror = 0

    while x == True:
        
        def menu():
            print("----------------")
            print("------Menu------")
            print("----------------")
            print("Use a listamento a seguir como parâmetro: ")
            print(("Ação", "Comédia", "Drama", "Fantasia", "Terror"))
        
        menu()
        
        
        filme_1 = input("Insira o primeiro filme: \n")
        genero_1 = input("Insira o indice do gênero do filme: \n").lower()
        
        filme_2 = input("Insira o segundo filme: \n")
        genero_2 = input("Insira o indoce do gênero do filme: \n").lower()
        
        filme_3 = input("Insira o terceiro filme: \n")
        genero_3 = input("Insira o indice do gênero do filme: \n").lower()
        
        dicionario_filmes = {
            "Filme 1": filme_1 , "Gênero": genero_1,
            "Filme 2": filme_2 , "Gênero": genero_2,
            "Filme 3": filme_3 , "Gênero": genero_3,
        }
        
        filmes_genero_total = {
            "Ação": count_acao,
            "Comédia": count_comedia,
            "Drama": count_drama,
            "Fantasia": count_fantasia,
            "Terror": count_terror,
        }
        
    while filmes_genero_total < 3:
        for i in dicionario_filmes:
            if i[1] == "acao" or "ação":     
                count_acao = + 1
                
            elif i[1] == "comedia" or "comédia":     
                count_comedia = + 1

            elif i[1] == "drama":     
                count_drama = + 1
                
            elif i[1] == "fantasia":     
                count_fantasia = + 1

            elif i[1] == "terror":     
                count_terror = + 1
            else:
                print("Tente novamente e insira um gênero dentro dos parâmetros.")  
                
        print(dicionario_filmes)
        print(filmes_genero_total)
             
        
cadastrar_filmes()