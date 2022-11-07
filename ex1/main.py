from pty import master_open
from xml.dom import NOT_SUPPORTED_ERR
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
df.head()

df_smzed = df.melt(id_vars='Concurso',value_vars=['Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15'],var_name = 'bola_id',value_name = 'bola_num_sort').sort_values(['Concurso','bola_id'],ascending=True)
df_smzed = df_smzed.reset_index(drop=True)
df_smzed.dtypes
df.to_csv('./df.csv',sep=';')
#df_smzed = df_smzed[df_smzed['Concurso']<=100]
df_smzed.to_csv('./df_smzed.csv',sep=';')
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
    k = ('Concurso-'+str(i)+' '+str(v_pares)+'p-'+str(v_impares)+'i-'+str(v_primos)+'np')
    comb_concursos.append(k)

df_smzed_frequency = df_smzed.groupby('bola_num_sort')['Concurso'].count()
df_smzed_frequency
max_concurso = df_smzed['Concurso'].max()
nr_freq = (df_smzed_frequency*100 / max_concurso).to_frame()
nr_freq = nr_freq.sort_values('Concurso',ascending = False)
nr_freq.reset_index(inplace=True)
nr_freq.columns = ['bola_num_sort','freq']
nr_freq.iloc[0]['bola_num_sort']
nr_freq.iloc[-1]['bola_num_sort']

comb = []
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0


for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
            v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
            v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
            v_22 += 1
        if row[campo] == 23:
            v_23 += 1
        if row[campo] == 24:
            v_24 += 1
        if row[campo] == 25:
            v_25 += 1
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-'+str(v_primos)+'np')


freq_nr = [
    [1, v_01],
    [2, v_02],
    [3, v_03],
    [4, v_04],
    [5, v_05],
    [6, v_06],
    [7, v_07],
    [8, v_08],
    [9, v_09],
    [10, v_10],
    [11, v_11],
    [12, v_12],
    [13, v_13],
    [14, v_14],
    [15, v_15],
    [16, v_16],
    [17, v_17],
    [18, v_18],
    [19, v_19],
    [20, v_20],
    [21, v_21],
    [22, v_22],
    [23, v_23],
    [24, v_24],
    [25, v_25]
]


freq_nr
freq_nr.sort(key=lambda tup: tup[1])
freq_nr[0]  # primeiro
freq_nr[-1]  # ultimo


counter = collections.Counter(comb)
resultado = pd.DataFrame(counter.items(), columns=['Combinacao', 'Frequencia'])
resultado['p_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum()
resultado = resultado.sort_values(by='p_freq')

print('''
O número mais frequente é o:  {}
O número menos frequente é o:  {}
A combinação de Pares, Ímpares e Primos mais frequente é: {} com a frequencia de: {}%
'''.format(freq_nr[-1][0], freq_nr[0][0], resultado['Combinacao'].values[-1], int((resultado['p_freq'].values[-1]*100)*100)/100)
)

