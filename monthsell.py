import pandas as pd
import pygal as pg

data = pd.read_csv("bakery_update.csv")
order = {}

month = '10'

for i in range(len(data)):
    check = data['Date'][i]
    if '2016' in check:
        if len(check) == 9:
            month = check[2:4]
            if check[2:4] == month:
                if month not in order:
                    order[month] = 1
                else:
                    order[month] += 1
        elif len(check) == 10:
            month = check[3:5]
            if check[3:5] == month:
                if month not in order:
                    order[month] = 1
                else:
                    order[month] += 1
    elif '2017' in check:
        if len(check) == 8:
            month = check[2]
            if check[2] == month:
                if month not in order:
                    order[month] = 1
                else:
                    order[month] += 1
        elif len(check) == 9:
            month = check[3]
            if check[3] == month:
                if month not in order:
                    order[month] = 1
                else:
                    order[month] += 1
chart = pg.Bar()
for i in order:
    if len(i) != 1:
        chart.add("Month " + i + " 2016", order[i])
    else:
        chart.add("Month " + i + " 2017", order[i])
chart.render_to_file('ordermonth_chart.svg')
