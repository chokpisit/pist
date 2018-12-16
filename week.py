import pandas as pd
import pygal as pg

data = pd.read_csv("bakery_update.csv")
week = {}
total = 0

for i in range(len(data)):
    total += 1
    if data['Day'][i] not in week:
        week[data['Day'][i]] = 1
    else:
        week[data['Day'][i]] += 1

chart = pg.Pie()
for j in week:
    chart.add(j, week[j]/total*100)
chart.render_to_file('Week_chart.svg')
