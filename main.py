from cadastro import ad
from leitura import show
from modifica import update

while(True):
    ok:int=int(input('\n1 para cadastrar produto\n2 para pesquisar produtos cadastrados\n3 para modificar um produto\n'))
    match(ok):
        case 1:
            ad()
        case 2:
            show()
        case 3:
            update()
        case _:
            print('\nação invalida\n')