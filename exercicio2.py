'''
Disjunção e intervalo

É possível definir intervalos para representar longas sequências de caracteres ou dígitos

* [abcdefghijklmnopqrstuvwxyz] | [a-z]
* [0123456789] | [0-9]
* [ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz] | [A-Za-z]
* [012345] | [0-5]

Exemplos:
'''
import re

descricao = 'Smartphone Samsung Galaxy A03 Core 32GB Preto 4G'
re.findall(r"[0-4]", descricao)
# ou
len(re.findall(r"[0-4]", descricao))

#Caracteres
re.findall(r"[a-e]", descricao)
# ou
len(re.findall(r"[a-e]", descricao))