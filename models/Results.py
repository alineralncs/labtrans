from peewee import (
    TextField,
    IntegerField,
    DoubleField
)       
import pandas as pd
import glob
from peewee import fn, JOIN
import os
from models.BaseModel import BaseModel
from models.BaseModel import db

class Results(BaseModel):
    name = TextField()
    km = DoubleField()
    distance = DoubleField()
    highway = IntegerField()
    item = TextField()
    
    class Meta:
        table_name = 'results'

    @classmethod 
    def insert_data(cls):
        dir_csv = 'dados/*.csv'

        arquivos_csv = glob.glob(dir_csv)
       # print(arquivos_csv)

        dados = []
        registros = []

        for arquivo_csv in arquivos_csv:
            dataset = pd.read_csv(arquivo_csv)
            dados.append(dataset)

       # print(dados)

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

        tamanho_depois = Results.select().count()
        print("Totale de registros inseridos:", tamanho_depois)


    @classmethod
    def get_highway_info(cls):
        sub_buraco = Results.select(
            Results.highway,
            Results.km,
            fn.COUNT(Results.item).alias('buraco')
        ).where(Results.item == 'Buraco').group_by(Results.highway, Results.km)

        #print(sub_buraco)
        sub_remendo = Results.select(
            Results.highway,
            Results.km,
            fn.COUNT(Results.item).alias('remendo')
        ).where(Results.item == 'Remendo').group_by(Results.highway, Results.km)

        sub_trinca = Results.select(
            Results.highway,
            Results.km,
            fn.COUNT(Results.item).alias('trinca')
        ).where(Results.item == 'Trinca').group_by(Results.highway, Results.km)

        sub_placa = Results.select(
            Results.highway,
            Results.km,
            fn.COUNT(Results.item).alias('placa')
        ).where(Results.item == 'Placa').group_by(Results.highway, Results.km)

        sub_drenagem = Results.select(
            Results.highway,
            Results.km,
            fn.COUNT(Results.item).alias('drenagem')
        ).where(Results.item == 'Drenagem').group_by(Results.highway, Results.km)

        query = (Results
                .select(
                    Results.highway,
                    Results.km,
                    sub_buraco.c.buraco.alias('buraco'),
                    sub_remendo.c.remendo.alias('remendo'),
                    sub_trinca.c.trinca.alias('trinca'),
                    sub_placa.c.placa.alias('placa'),
                    sub_drenagem.c.drenagem.alias('drenagem')
                )
                .join(sub_buraco, JOIN.LEFT_OUTER,
                    on=((Results.highway == sub_buraco.c.highway) & (Results.km == sub_buraco.c.km)))
                .join(sub_remendo, JOIN.LEFT_OUTER,
                    on=((Results.highway == sub_remendo.c.highway) & (Results.km == sub_remendo.c.km)))
                .join(sub_trinca, JOIN.LEFT_OUTER,
                    on=((Results.highway == sub_trinca.c.highway) & (Results.km == sub_trinca.c.km)))
                .join(sub_placa, JOIN.LEFT_OUTER,
                    on=((Results.highway == sub_placa.c.highway) & (Results.km == sub_placa.c.km)))
                .join(sub_drenagem, JOIN.LEFT_OUTER,
                    on=((Results.highway == sub_drenagem.c.highway) & (Results.km == sub_drenagem.c.km)))
                .group_by(Results.highway, Results.km)
                .order_by(Results.highway, Results.km))

        result = query.dicts()
        md_results = []
        for row in result:
            if row['buraco'] is None:
                row['buraco'] = 0

            if row['remendo'] is None:
                row['remendo'] = 0

            if row['trinca'] is None:
                row['trinca'] = 0

            if row['placa'] is None:
                row['placa'] = 0

            if row['drenagem'] is None:
                row['drenagem'] = 0
            #print('a', row)
            md_results.append(row)
        # para verificar se está no video correto ver em cada rodovia qual video ele pertence
        #print(md_results)
        return md_results
    
    @classmethod    
    def export_csv(cls):
        md_results = cls.get_highway_info()

        for highway in md_results:
            filtered_results = [result for result in md_results if result['highway'] == highway['highway']]

            df = pd.DataFrame(filtered_results)

            columns = ['highway', 'km', 'buraco', 'remendo', 'trinca', 'placa', 'drenagem']
            df = df[columns]
            directory = 'dados_saida'
            file_name = os.path.join(directory, f'rodovia_{highway["highway"]}.csv')
            df.to_csv(file_name, index=False)
            
    @classmethod
    def find_incidence(cls, item):
        query = Results.select(
            Results.km, 
            Results.highway,
            fn.COUNT(Results.km).alias('incidencia')
        ).where(Results.item == item
        ).group_by(Results.km, Results.highway
        ).order_by(fn.COUNT(Results.km).desc()).limit(1)

        resultado = query.get()
        km_maior_incidencia = resultado.km
        incidencia = resultado.incidencia
        highway = resultado.highway

        return km_maior_incidencia, incidencia, highway
        
    @classmethod
    def delete_results(cls):
        Results.delete().execute()

   