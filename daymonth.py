import pandas as pd
import pygal as pg

data = pd.read_csv("bakery_update.csv")
month10 = {}
month11 = {}
month12 = {}
month1 = {}
month2 = {}
month3 = {}
month4 = {}

check = ''
month = ''

for i in range(len(data)):
    check = data['Date'][i]
    if '2016' in check:
        if len(check) == 10:
            month = check[3:5]
            if month == '10':
                if data['Date'][i] not in month10:
                    month10[data['Date'][i]] = 1
                else:
                    month10[data['Date'][i]] += 1
            elif month == '11':
                if data['Date'][i] not in month11:
                    month11[data['Date'][i]] = 1
                else:
                    month11[data['Date'][i]] += 1
            elif month == '12':
                if data['Date'][i] not in month12:
                    month12[data['Date'][i]] = 1
                else:
                    month12[data['Date'][i]] += 1
        elif len(check) == 9:
            month = check[2:4]
            if month == '11':
                if data['Date'][i] not in month11:
                    month11[data['Date'][i]] = 1
                else:
                    month11[data['Date'][i]] += 1
            elif month == '12':
                if data['Date'][i] not in month12:
                    month12[data['Date'][i]] = 1
                else:
                    month12[data['Date'][i]] += 1

    elif '2017' in check:
        if len(check) == 8:
            month = check[2]
            if month == '1':
                if data['Date'][i] not in month1:
                    month1[data['Date'][i]] = 1
                else:
                    month1[data['Date'][i]] += 1
            elif month == '2':
                if data['Date'][i] not in month2:
                    month2[data['Date'][i]] = 1
                else:
                    month2[data['Date'][i]] += 1
            elif month == '3':
                if data['Date'][i] not in month3:
                    month3[data['Date'][i]] = 1
                else:
                    month3[data['Date'][i]] += 1
            elif month == '4':
                if data['Date'][i] not in month4:
                    month4[data['Date'][i]] = 1
                else:
                    month4[data['Date'][i]] += 1
        elif len(check) == 9:
            month = check[3]
            if month == '1':
                if data['Date'][i] not in month1:
                    month1[data['Date'][i]] = 1
                else:
                    month1[data['Date'][i]] += 1
            elif month == '2':
                if data['Date'][i] not in month2:
                    month2[data['Date'][i]] = 1
                else:
                    month2[data['Date'][i]] += 1
            elif month == '3':
                if data['Date'][i] not in month3:
                    month3[data['Date'][i]] = 1
                else:
                    month3[data['Date'][i]] += 1
            elif month == '4':
                if data['Date'][i] not in month4:
                    month4[data['Date'][i]] = 1
                else:
                    month4[data['Date'][i]] += 1

chart = pg.Bar()
chart.title = 'Month October'
for j in month10:
    day = j[:2]
    chart.add(day, month10[j])
chart.render_to_file('Month10_chart.svg')

chart = pg.Bar()
chart.title = 'Month November'
for j in month11:
    if len(j) == 10:
        day = j[:2]
        chart.add(day, month11[j])
    else:
        day = j[0]
        chart.add(day, month11[j])
chart.render_to_file('Month11_chart.svg')

chart = pg.Bar()
chart.title = 'Month December'
for j in month12:
    if len(j) == 10:
        day = j[:2]
        chart.add(day, month12[j])
    else:
        day = j[0]
        chart.add(day, month12[j])
chart.render_to_file('Month12_chart.svg')

chart = pg.Bar()
chart.title = 'Month January'
for j in month1:
    if len(j) == 9:
        day = j[:2]
        chart.add(day, month1[j])
    else:
        day = j[0]
        chart.add(day, month1[j])
chart.render_to_file('Month1_chart.svg')

chart = pg.Bar()
chart.title = 'Month February'
for j in month2:
    if len(j) == 9:
        day = j[:2]
        chart.add(day, month2[j])
    else:
        day = j[0]
        chart.add(day, month2[j])
chart.render_to_file('Month2_chart.svg')

chart = pg.Bar()
chart.title = 'Month March'
for j in month3:
    if len(j) == 9:
        day = j[:2]
        chart.add(day, month3[j])
    else:
        day = j[0]
        chart.add(day, month3[j])
chart.render_to_file('Month3_chart.svg')

chart = pg.Bar()
chart.title = 'Month April'
for j in month4:
    if len(j) == 9:
        day = j[:2]
        chart.add(day, month4[j])
    else:
        day = j[0]
        chart.add(day, month4[j])
chart.render_to_file('Month4_chart.svg')

