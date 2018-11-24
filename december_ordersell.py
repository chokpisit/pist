import pandas as pd

data = pd.read_csv("bakery_update.csv")
order = {}

for i in range(len(data)):
    check = data['Date'][i]
    if '2016' in check:
        if len(check) == 10 and check[3:5] == '12':
            if data['Item'][i] not in order:
                order[data['Item'][i]] = 1
            else:
                order[data['Item'][i]] += 1
        elif len(check) == 9 and check[2:4] == '12':
            month = check[2:4]
            if data['Item'][i] not in order:
                order[data['Item'][i]] = 1
            else:
                order[data['Item'][i]] += 1
print("***Order December***")
for j in order:
    print(j, order[j])
