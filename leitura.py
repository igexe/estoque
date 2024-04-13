import pandas as pd
from cadastro import ad

def search():

    estoque_df=pd.read_csv('teste.csv',dtype={'referencia':str})
    action:int=int(
        input('\n1 para fazer a busca por codigo\n2 para busca por referência\n3 para busca por marca\n4 para buscar por quantidade\n5 para buscar por valor\n')
        )
    
    match(action):
        case 1:
            busca=int(input('\ndigite o codigo do produto a ser encontrado\n'))
            elements=estoque_df.loc[estoque_df['codigo']==busca]
            finds=elements['codigo'].tolist()
            
            if len(finds)==0:
                return 1

            return finds

        case 2:
            busca=input('\ndigite a referência a ser encontrada\n')
            elements=estoque_df.loc[estoque_df['referencia']==str(busca)]
            finds=elements['codigo'].tolist()
            
            if len(finds)==0:
                return str(busca)

            return finds

        case 3:
            busca=input('\ndigite a marca dos produtos a serem encontrados\n')
            elements=estoque_df.loc[estoque_df['marca']==busca]
            finds=elements['codigo'].tolist()

            if len(finds)==0:
                return 2

            return finds

        case 4:
            busca=int(input('\ndigite a quantidade para ver produtos com quantidade menor ou igual\n'))
            elements=estoque_df.loc[estoque_df['quantidade']<=busca]
            finds=elements['codigo'].tolist()
            
            if len(finds)==0:
                return 3

            return finds

        case 5:
            busca=float(input('\ndigite o valor para ver produtos com valor menor igual\n'))
            elements=estoque_df.loc[estoque_df['valor']<=busca]
            finds=elements['codigo'].tolist()
            
            if len(finds)==0:
                return 4

            return finds

        case _:
            print('\nação não encontrada por favor selecione uma opção valida\n')
            return search()


def show():
    estoque_df=pd.read_csv('teste.csv')
    finds=search()
    
    if type(finds) is int:
        match(finds):
            case 1:
                print('\ncodigo não cadastrado\n')
                return 0
            case 2:
                print('\nmarca não cadastrada\n')
                return 0
            case 3:
                print('\nnenhum produto com essa quantidade ou menos\n')
                return 0
            case _:
                print('\nnenhum produto com esse valor ou menor')

    if type(finds) is str:
        if int(input('\nreferencia: '+str(finds)+' não cadastrada\ndeseja cadaastrar produto?\n1 para sim\n0 para não\n'))==1:
            ad(str(finds))

        return 0

    for i in finds:
        print('\n')
        print(estoque_df.loc[estoque_df['codigo']==i, ['codigo','marca','produto','quantidade','valor','referencia']])