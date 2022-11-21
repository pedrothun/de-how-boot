#%%
import requests
import json
import pandas as pd

#%%
url = 'https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv'
#ret = requests.get(url)
# %%
df = pd.read_csv(url,delimiter=';')

# %%
df.columns

# %%
df['Tipo Titulo'].unique()
# %%
def GetTitulo(df, tipo_do_titulo, data_vencimento):
    df = df.astype('string')
    sliced = df[((df['Tipo Titulo']==tipo_do_titulo) & (df['Data Vencimento'].str[-4:]==data_vencimento))].sort_values('Data Base',ascending=True).reset_index(drop=True)
    cols = ['Data Vencimento','Data Base']
    sliced[cols] = sliced[cols].apply(pd.to_datetime)
    return sliced
# %%
df3 = GetTitulo(df,'Tesouro Prefixado','2029')
#df3 = df2.astype('string')
cols = ['Taxa Compra Manha', 'Taxa Venda Manha','PU Compra Manha', 'PU Venda Manha', 'PU Base Manha']
df3[cols] = df3[cols].replace(',','.', regex=True).astype('float')
df4 = df3.drop(['Tipo Titulo','Data Vencimento','PU Base Manha'],axis=1)
df4.plot.line('Data Base',['PU Compra Manha','PU Venda Manha'],grid=True,figsize=(12,8))
# %%

