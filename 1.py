#Python
import csv
with open ('vacancy.csv', encoding='uft-8') as file:
    reader= (csv.DictReader(file, delimetr=';' ))
    ro=[]
    comp=[]
    sal=[]
    wos=0
    for row in reader:
        if row['Role'] not in ro:
            ro.append(row['Role'])
            comp.append(row)
            sal.append(row)

    with open ('vacancy_news.csv', encoding= 'uft-8', newline='') as file:
        writer= (csv. DictReader(file, fieldnames=['Company','Role', 'Salary']))
        writer.writerhader()
        writer.writerows()