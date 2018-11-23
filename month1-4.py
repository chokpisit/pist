import pandas as pd

data = pd.read_csv("bakery_update.csv")
dictmonth = {}

for i in range(len(data)):
	check = data['Date'][i]
	if '2017' in check:
		if len(check) == 9:
			month = check[3]
			if month not in dictmonth:
				dictmonth[month] = 1
			else:
				dictmonth[month] += 1
		else:
			month = check[2]
			if month not in dictmonth:
				dictmonth[month] = 1
			else:
				dictmonth[month] += 1
print(dictmonth)
