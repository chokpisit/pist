import pandas as pd
import pygal as pg

data = pd.read_csv("bakery_update.csv")
listday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = {}

check = -1
dataafter = []

for i in range(len(data)):
    if data['Date'][i] not in dataafter:
        dataafter.append(data['Date'][i])
        check += 1
        check %= 7
    if listday[check] not in day:
        day[data['Date'][i]] = 1
    else:
        day[data['Date'][i]] += 1

bakery_chart = pg.Pie()
bakery_chart.title = 'Day highlight'
for i in day:
    bakery_chart.add(i, day[i])
bakery_chart.render_to_file('Day_bakery_chart.svg')
