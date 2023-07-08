from Results import Results
from peewee import fn, JOIN

km_query = Results.select(Results.highway).group_by(Results.highway)

# Obtendo os resultados da consulta
km_results = [result.highway for result in km_query]

# Imprimindo os valores de "km"
for km in km_results:
    print(km)

print('i', km)

sub_buraco = Results.select(
    Results.highway,
    Results.km,
    fn.COUNT(Results.item).alias('buraco')
).where(Results.item == 'buraco').group_by(Results.highway, Results.km)


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

# Iterar sobre o resultado
for row in result:
    # Verificar se o valor da contagem é None
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

    print(row)
