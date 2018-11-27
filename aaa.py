"""Find The best Day sell"""
import csv
def main():
    data = csv.reader(open("bakery_update.csv"))
    dicday = {'Sunday':0, 'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0}
    data = [i for i in data]
    for i in range(1, len(data)):
        if data[i][1] in dicday:
            dicday[data[i][1]] += int(data[i][3])
    sorted_dic = sorted(dicday.items(), key=lambda x: x[1])
    sorted_dic.reverse()
    print(sorted_dic)
main()
