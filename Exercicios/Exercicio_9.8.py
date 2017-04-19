# -*- coding: utf-8 -*-

"""
Modifique o programa anterior para também receber o número de 
caracteres por linha e o número de páginas por folhas pela linha
de comando.
"""

print("=" * 60)

import sys


def verifica_pagina(arquivo, linha, pagina):
    if(linha == LINHAS):
        rodapé = "= %s - Página: %d =" % (NOME_DO_ARQUIVO, pagina)
        arquivo.write(rodapé.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina


def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha + "\n")
    return verifica_pagina(arquivo, nlinhas + 1, pagina)

if len(sys.argv) != 4:
    print("\nPython larguras linhas")
    sys.exit(1)    

NOME_DO_ARQUIVO = sys.argv[1]
LARGURA = int(sys.argv[2])
LINHAS = int(sys.argv[3])

entrada = open(NOME_DO_ARQUIVO, encoding="utf-8")
saída = open("saida_paginada.txt", "w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saída, linha, linhas, pagina)
            linha = ""
        linha += p + " "
    if(linha != ""):
        linhas, pagina = escreve(saída, linha, linhas, pagina)

# Para imprimir o número na última página
while(linhas != 1):
    linhas, pagina = escreve(saída, "", linhas, pagina)

entrada.close()
saída.close()

print("=" * 60)