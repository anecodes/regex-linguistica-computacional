""" 
Negação na disjunção

A negação é definida pelo símbolo "^" entre colchetes [], e é apenas entre os colchetes que essa negação funciona
  * [^sS] | Todos os elementos exceto "s" e "S"
  * [^A-Z] | Todos os elementos exceto caracteres em letra maiúscula
  * x\^2 | Todos os elementos "x^2"

  Exemplo com o poema Ofertas de Aninha, de Cora Coralina
"""

import re

poema = '''
Eu sou aquela mulher
a quem o tempo muito ensinou.
Ensinou a amar a vida
e não desistir da luta,
recomeçar na derrota,
renunciar a palavras
e pensamentos negativos.
Acreditar nos valores humanos
e ser otimista.'''

#Todos os caracteres não minúsculos do poema:
re.findall(r"[^a-z]", poema)

#A quantidade deles:
len(re.findall(r"[^a-z]", poema))