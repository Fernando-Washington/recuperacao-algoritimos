"""
3) Gerar Relatório (parâmetros opcionais e *args)

Objetivo:
Crie uma função chamada gerar_relatorio(*valores, titulo="Relatório Geral", subtitulo="Valores") que receba:
- Uma quantidade variável de números em *valores.
- Dois parâmetros opcionais titulo e subtitulo, com valores-padrão fornecidos.

A função deve:
1. Exibir o titulo e o subtitulo.
2. Calcular e exibir:
   - A soma de todos os valores.
   - A média dos valores.
   - O valor máximo e o valor mínimo.

Observação:
- Utilize funções built-in como sum(), max() e min().
- Se não houver valores em *valores, trate esse caso (por exemplo, exiba mensagem que não há valores).

Exemplo de Chamada:
    gerar_relatorio(10, 20, 30)
    gerar_relatorio(1.5, 2.5, 3.5, 4.5, titulo="Relatório Personalizado", subtitulo="Métricas Financeiras")

    # Exemplo de saída:
    # ====== Relatório Geral ======
    # Subtítulo: Valores
    # Soma: 60
    # Média: 20.0
    # Máximo: 30
    # Mínimo: 10
    # ----------------------------

Requisitos:
- Use parâmetros opcionais (titulo, subtitulo) e *args.
- Faça uso de funções built-in para facilitar a soma e a busca de maior/menor valor.
- Mostre os resultados de forma organizada.
"""
# Solution:
def exemplo():
    print("Exemplo de saída:")
    print("====== Relatório Geral ======")
    print("Subtítulo: Valores")
    print("Soma: 60")
    print("Média: 20.0")
    print("Máximo: 30")
    print("Mínimo: 10")
exemplo()

estilo = "======"

valores = []

titulo_input = input("Digite o seu título: \n")

sub_input = input("Digite o seu subtitulo: \n")

deseja_valores = input("Deseja inserior valores? \n").lower

if deseja_valores and "s" or "sim":
    ...
    

# fiz isso para tentar inteirar sobre a soma da média mas não consegui

def gerar_relatorio(titulo, subtitulo, *valores):
    
    _soma = sum(valores)
    _media = _soma / _minimo
    _maximo = max(valores)
    _minimo = min(valores)

    dicionario = {
    "Título" : estilo + titulo + estilo,
    "Subtítulo": subtitulo,
    "Soma": _soma,
    "Média": _media,
    "Méximo": _maximo,
    "Mínimo": _minimo,
    }

    print(dicionario)
    
gerar_relatorio(titulo = titulo_input, subtitulo = sub_input, *valores)