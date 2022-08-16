from func import *
arq = 'contatos.txt'
if not checararquivo(arq):
    criararquivo(arq)
menu('Agenda de Contatos')
while True:
    opcao = opcoes(arq)
    if opcao == 0:
        break
