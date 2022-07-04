'''
Múltiplos padrões de busca

São separados com pipe (|)
  * ainda|mais | Encontra as palavras ainda e mais
  * ainda|mais|sem | Encontra as palavras ainda, mais e sem
  * [Aa]inda|[Mm]ais | Encontra as palavras ainda e mais, sejam elas iniciadas em letra maiúscula ou minúscula
  * pedra|[^a-z] | Encontra todas as palavras "pedra" e caracteres maiúsculos

  Exemplos com um trecho de No meio do caminho, de Carlos Drummond de Andrade
'''

import re

trecho = '''No meio do caminho tinha uma pedra
Tinha uma pedra no meio do caminho
Tinha uma pedra
No meio do caminho tinha uma pedra'''

#Todos os resultados de "tinha" (incluindo maiúsculas) ou "pedra":
re.findall(r"[Tt]inha|pedra", trecho)

#A quantidade de resultados
len(re.findall(r"[Tt]inha|pedra", trecho))