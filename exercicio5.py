'''
Marcadores de início e fim de linha

Marcados nas expressões regulares com os caracteres especiais ^ e $
 * ^Ainda | Todos "Ainda" no início da linha/frase
 * ^[Tt]inha | Todos "Tinha" ou "tinha" no início da linha/frase
 * pedra$ | Todos "pedra" no fim da linha/frase 
'''

'''
Marcador de palavra

O caractere especial "\b" representa os caracteres que marcam o limite de uma palavra
  * Espaço, pontuação, início e fim de strings

  * \b[Aa]\b | Todos os artigos definidos femininos singulares
  * \b[Mm]ente\b | Todas as ocorrências dos verbos -mente/-Mente
  * \bainda que\b | Todas as ocorrências da expressão "ainda que"
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

re.findall(r"\bainda que\b", poema)