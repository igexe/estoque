import pandas as pd

def ad(ref=0):
    codigo=1
    try:
        estoque_df=pd.read_csv('teste.csv')
        codigo=estoque_df['codigo'].iloc[-1]+1
    except FileNotFoundError:
        db=open('teste.csv','w')
        db.close()
        estoque_df=pd.DataFrame({
            'codigo':[codigo],
            'marca':[input('\ndigite a marca do produto:\n')],
            'produto':[input('\ndigite o nome do produto:\n')],
            'idade':[input('\ndigite\nadt se o produto for adulto\ninf se o produto for infantil\n')],
            'sexo':[input('\ndigite\nmasc so o produto for masculino\nfem se o produto for feminino\n')],
            'quantidade':[int(input('\ndigite quantidade de produtos chegaram:\n'))],
            'valor':[float(input('\ndigite o valor do produto:\n'))],
            'referencia':[input('\ndigite a referencia do produto:\n')]
        })
        estoque_df.to_csv('teste.csv',index=False)
        return 0

    if ref==0:
        estoque_df=estoque_df._append({
                'codigo':codigo,
                'marca':input('\ndigite a marca do produto:\n'),
                'produto':input('\ndigite o nome do produto:\n'),
                'idade':input('\ndigite\nadt se o produto for adulto\ninf se o produto for infantil\n'),
                'sexo':input('\ndigite\nmasc so o produto for masculino\nfem se o produto for feminino\n'),
                'quantidade':int(input('\ndigite quantidade de produtos chegaram:\n')),
                'valor':float(input('\ndigite o valor do produto:\n')),
                'referencia':input('\ndigite a referencia do produto:\n')
            },ignore_index=True)
        estoque_df.to_csv('teste.csv',index=False)
        return 0

    estoque_df=estoque_df._append({
            'codigo':codigo,
            'marca':input('\ndigite a marca do produto:\n'),
            'produto':input('\ndigite o nome do produto:\n'),
            'idade':input('\ndigite\nadt se o produto for adulto\ninf se o produto for infantil\n'),
            'sexo':input('\ndigite\nmasc so o produto for masculino\nfem se o produto for feminino\n'),
            'quantidade':int(input('\ndigite quantidade de produtos chegaram:\n')),
            'valor':float(input('\ndigite o valor do produto:\n')),
            'referencia':ref
        },ignore_index=True)

    estoque_df.to_csv('teste.csv',index=False)
    