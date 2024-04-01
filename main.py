from cadastro import ad
from leitura import show

while(True):
    ok:int=int(input('\n1 para cadastrar produto\n2 para pesquisar produtos cadastrados\n'))
    if(ok==1):
        ad()
    elif(ok==2):
        show()
    else:
        break