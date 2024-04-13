import pandas as pd
from leitura import search

def update():
    find=select()
    if find==0:
        print('\nação cancelada\n')
        return 0

    estoque_df=pd.read_csv('teste.csv')
    act=int(input('\n1 para modificar nome produto\n2 para modificar marca\n3 para modificar quantidade\n4 para modificar valor\n'))

    match(act):
        case 1:
            estoque_df.loc[estoque_df['codigo']==find,'produto']=str(input('\ndigite nome do produto\n'))
            print('\n'+str(estoque_df.loc[estoque_df['codigo']==find])+'\n')
            estoque_df.to_csv('teste.csv',index=False)
            print('\nação concluida\n')
            return 0

        case 2:
            estoque_df.loc[estoque_df['codigo']==find,'marca']=str(input('\ndigite marca do produto\n'))
            print('\n'+str(estoque_df.loc[estoque_df['codigo']==find])+'\n')
            estoque_df.to_csv('teste.csv',index=False)
            print('\nação concluida\n')
            return 0

        case 3:
            estoque_df.loc[estoque_df['codigo']==find,'quantidade']=int(input('\ndigite quantidade do produto\n'))
            print('\n'+str(estoque_df.loc[estoque_df['codigo']==find])+'\n')
            estoque_df.to_csv('teste.csv',index=False)
            print('\nação concluida\n')
            return 0

        case 4:
            estoque_df.loc[estoque_df['codigo']==find,'valor']=float(input('\ndigite valor do produto\n'))
            print('\n'+str(estoque_df.loc[estoque_df['codigo']==find])+'\n')
            estoque_df.to_csv('teste.csv',index=False)
            print('\nação concluida\n')
            return 0

        case _:
            print('\nação invalida\nrecomeçando o processo\n')
            update()
            return 0

def select():
    estoque_df=pd.read_csv('teste.csv')
    finds=search()

    if type(finds) is int or type(finds) is str:
        print('\nnenhum produto encontrado\n')
        return 0
    
    if len(finds)>1:
        for i in finds:
            print('\n')
            print(estoque_df.loc[estoque_df['codigo']==i])
        
        find=int(input('\ndos resultados apresentados digite o codigo desejado\n'))

    if len(finds)==1:
        find=finds[0]

    print(estoque_df.loc[estoque_df['codigo']==find])

    if int(input('\nesse é o produto desejado:\n1 para sim\n2 para não\n'))==1:
        return find

    return 0
