import pandas as pd

data = pd.read_csv("bakery_update.csv")
bakery = dict()

for i in range(len(data)):
    total += 1
    if data['Item'][i] not in bakery:
        bakery[data['Item'][i]] = 1
    else:
        bakery[data['Item'][i]] += 1

for j in bakery:
    print(j, bakery[j])
