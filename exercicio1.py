'''
Expressões regulares - Disjunção
Usa-se as seguintes disjunções para fazer buscas textuais:

* Achar a quantidade de repetições de uma palavra, sendo ela escrita com letra maiúscula ou minúscula 
  [Aa]inda | para achar "Ainda, ainda"
  ma[ls]  | para achar "mal, mas""
  [0123456789] | para achar dígitos numéricos

  Exemplo de busca utilizando o poema Ainda que mal, de Carlos Drummond de Andrade
'''
import re

poema = """Ainda que mal pergunte,
ainda que mal respondas;
ainda que mal te entenda,
ainda que mal repitas;
ainda que mal insista,
ainda que mal desculpes;
ainda que mal me exprima,
ainda que mal me julgues;
ainda que mal me mostre,
ainda que mal me vejas;"""

#re.findall() - método findall() da biblioteca re para encontrar as buscas desejadas de acordo com os argumentos passados, sendo que:
#o primeiro parâmetro é a expressão regular (iniciada por 'r') e o segundo é a variável que contém o poema
#Para achar todas as ocorrências de "Ainda que mal":
re.findall(r"[Aa]inda que mal", poema)
#Se quiser a quantidade de ocorrências, usa-se o método len():
len(re.findall(r"[Aa]inda que mal", poema))

