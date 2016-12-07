import csv
import json
with open('data2.csv', 'r') as datacsv:
    readercsv = csv.DictReader(datacsv) 
    data_dict1, data_dict2, data_dict3, data_dict4 = {}, {}, {}, {}
    data_dict1_u, data_dict2_u, data_dict3_u, data_dict4_u = {}, {}, {}, {}
    data_2012, data_2013, data_2014, data_2015 = {}, {}, {}, {}
    for i in readercsv:
        if i['year'] == '2012':
            data_dict1.setdefault(i['country'], data_dict1.setdefault(i["institution"], {}))
        if i['year'] == '2013':
            data_dict2.setdefault(i['country'], {i["institution"]:0})
        if i['year'] == '2014':
            data_dict3.setdefault(i['country'], {i["institution"]:0})
        if i['year'] == '2015':
            data_dict4.setdefault(i['country'], {i["institution"]:0})
    data_2012['2012'] = data_dict1
    data_2013['2013'] = data_dict2
    data_2014['2014'] = data_dict3
    data_2015['2015'] = data_dict4

print(data_2012)