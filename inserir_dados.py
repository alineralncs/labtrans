from Results import Results, db
import pandas as pd
import glob

dir_csv = 'dados\*.csv'

arquivos_csv = glob.glob(dir_csv)

dados = []
registros = []

for arquivo_csv in arquivos_csv:
    dataset = pd.read_csv(arquivo_csv)
    dados.append(dataset)

for datasets in dados:
    #print(datasets.info)
    for _, linha in datasets.iterrows():
        registros.append(
            {
                'name': linha['name'],
                'km': linha['km'],
                'distance': linha['distance'],
                'highway': linha['highway'],
                'item': linha['item']
            }
        )


print("Total de registros a serem inseridos:", len(registros))

try:
    with db.atomic():
        for i in range(0, len(registros), 1000):
            lote_registros = registros[i:i+1000]
            Results.insert_many(lote_registros).execute()
except pw.DatabaseError as e:
    print("Erro durante a inserção dos registros:", str(e))

# Tamanho dos dados após a inserção
tamanho_depois = Results.select().count()
print("Tamanho dos dados após a inserção:", tamanho_depois)