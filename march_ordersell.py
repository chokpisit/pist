import pandas as pd

data = pd.read_csv("bakery_update.csv")
order = {}

for i in range(len(data)):
    check = data['Date'][i]
    if '2017' in check:
        if len(check) == 9 and check[3] == '3':
            if data['Item'][i] not in order:
                order[data['Item'][i]] = 1
            else:
                order[data['Item'][i]] += 1
        elif len(check) == 8 and check[2] == '3':
            if data['Item'][i] not in order:
                order[data['Item'][i]] = 1
            else:
                order[data['Item'][i]] += 1
print("***Order March***")
for j in order:
    print(j, order[j])
