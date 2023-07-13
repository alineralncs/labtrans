from peewee import (
    TextField,
    IntegerField,
    FloatField
)       
import pandas as pd
import glob
from peewee import fn, JOIN
import os
from models.BaseModel import BaseModel
from models.BaseModel import db

class ViewResults(BaseModel):
    name = TextField()
    km = FloatField()
    distance = FloatField()
    highway = IntegerField()
    item = TextField()

    class Meta:
        database = db
        table_name = 'view_results'

    @classmethod
    def create_view(cls):
        view_query = """
            CREATE VIEW view_results AS
            SELECT name, km, distance, highway, item
            FROM Results
        """
        cls._meta.database.execute_sql(view_query)

    @classmethod
    def drop_view(cls):
        drop_query = "DROP VIEW IF EXISTS view_results"
        cls._meta.database.execute_sql(drop_query)
    @classmethod
    def get_highway_info(cls):
        sub_buraco = ViewResults.select(
            ViewResults.highway,
            ViewResults.km,
            fn.COUNT(ViewResults.item).alias('buraco')
        ).where(ViewResults.item == 'Buraco').group_by(ViewResults.highway, ViewResults.km)

        #print(sub_buraco)
        sub_remendo = ViewResults.select(
            ViewResults.highway,
            ViewResults.km,
            fn.COUNT(ViewResults.item).alias('remendo')
        ).where(ViewResults.item == 'Remendo').group_by(ViewResults.highway, ViewResults.km)

        sub_trinca = ViewResults.select(
            ViewResults.highway,
            ViewResults.km,
            fn.COUNT(ViewResults.item).alias('trinca')
        ).where(ViewResults.item == 'Trinca').group_by(ViewResults.highway, ViewResults.km)

        sub_placa = ViewResults.select(
            ViewResults.highway,
            ViewResults.km,
            fn.COUNT(ViewResults.item).alias('placa')
        ).where(ViewResults.item == 'Placa').group_by(ViewResults.highway, ViewResults.km)

        sub_drenagem = ViewResults.select(
            ViewResults.highway,
            ViewResults.km,
            fn.COUNT(ViewResults.item).alias('drenagem')
        ).where(ViewResults.item == 'Drenagem').group_by(ViewResults.highway, ViewResults.km)

        query = (ViewResults
                .select(
                    ViewResults.highway,
                    ViewResults.km,
                    sub_buraco.c.buraco.alias('buraco'),
                    sub_remendo.c.remendo.alias('remendo'),
                    sub_trinca.c.trinca.alias('trinca'),
                    sub_placa.c.placa.alias('placa'),
                    sub_drenagem.c.drenagem.alias('drenagem')
                )
                .join(sub_buraco, JOIN.LEFT_OUTER,
                    on=((ViewResults.highway == sub_buraco.c.highway) & (ViewResults.km == sub_buraco.c.km)))
                .join(sub_remendo, JOIN.LEFT_OUTER,
                    on=((ViewResults.highway == sub_remendo.c.highway) & (ViewResults.km == sub_remendo.c.km)))
                .join(sub_trinca, JOIN.LEFT_OUTER,
                    on=((ViewResults.highway == sub_trinca.c.highway) & (ViewResults.km == sub_trinca.c.km)))
                .join(sub_placa, JOIN.LEFT_OUTER,
                    on=((ViewResults.highway == sub_placa.c.highway) & (ViewResults.km == sub_placa.c.km)))
                .join(sub_drenagem, JOIN.LEFT_OUTER,
                    on=((ViewResults.highway == sub_drenagem.c.highway) & (ViewResults.km == sub_drenagem.c.km)))
                .group_by(ViewResults.highway, ViewResults.km)
                .order_by(ViewResults.highway, ViewResults.km))

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

