import requests
import pandas as pd
import collections
import sys

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofacil'
#url = sys.argv[1]

r = requests.get(url,verify=False)

#r.text
r_text = r.text.replace("\\r\\n","")
r_text = r_text.replace('"\r\n}',"")
r_text = r_text.replace('{\r\n  "html": "',"")
#r_text

df = pd.read_html(r_text)

#type(df)
#df[0]
#type(df[0])
df=df[0].copy()
#df.dtypes
df.columns
df.head()
df = df[df['Bola1'] == df['Bola1']]
df['Concurso'] = pd.to_numeric(df['Concurso'])
df.sort_values('Concurso',ascending=True)
#df.head()

df_smzed = df.melt(id_vars='Concurso',value_vars=['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15'],var_name = 'bola_id',value_name = 'bola_num_sort').sort_values(['Concurso','bola_id'],ascending=True)
df_smzed = df_smzed.reset_index(drop=True)
df_smzed.dtypes
#df.to_csv('./df.csv',sep=';')
#df_smzed = df_smzed[df_smzed['Concurso']<=100]
#df_smzed.to_csv('./df_smzed.csv',sep=';')
nr_pop = list(range(1, 26))
nr_pares = list(range(2,26,2))  #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
nr_impares = list(range(1,27,2)) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

demo = df['Concurso'].unique()
comb_concursos = []

for i in demo:
    v_pares = 0
    v_impares = 0
    v_primos = 0
    df_smzed_sliced = df_smzed[df_smzed['Concurso']==i]
    for index,row in df_smzed_sliced.iterrows():
        if row['bola_num_sort'] in nr_pares:
            v_pares += 1
        if row['bola_num_sort'] in nr_impares:
            v_impares += 1
        if row['bola_num_sort'] in nr_primos:
            v_primos += 1
    # print(i,str(v_pares)+'p', '--', str(v_impares)+'i', '--', str(v_primos)+'np')
    #k = ('Concurso-'+str(i)+' '+str(v_pares)+'p-'+str(v_impares)+'i-'+str(v_primos)+'np')
    k = (str(v_pares)+'p-'+str(v_impares)+'i-'+str(v_primos)+'np')
    comb_concursos.append(k)

df_smzed_frequency = df_smzed.groupby('bola_num_sort')['Concurso'].count()
df_smzed_frequency
max_concurso = df_smzed['Concurso'].max()
nr_freq = (df_smzed_frequency*100 / max_concurso).to_frame()
nr_freq = nr_freq.sort_values('Concurso',ascending = False)
nr_freq.reset_index(inplace=True)
nr_freq.columns = ['bola_num_sort','freq']

num_high_freq = nr_freq.iloc[0]['bola_num_sort']
num_low_freq = nr_freq.iloc[-1]['bola_num_sort']

counter = collections.Counter(comb_concursos)
comb_freq = pd.DataFrame(counter.items(),columns=['combinacao','freq'])
comb_freq['freq'] = comb_freq['freq']*100/comb_freq['freq'].sum()
comb_freq.head()
comb_freq = comb_freq.sort_values(by='freq',ascending=False)

print('''
O número mais frequente é o:  {}
O número menos frequente é o:  {}
A combinação de Pares, Ímpares e Primos mais frequente é: {} com a frequencia de: {}%
'''.format(num_high_freq, num_low_freq, comb_freq['combinacao'].values[0], int((comb_freq['freq'].values[0])))
)