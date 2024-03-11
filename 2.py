import csv
with open ('vacancy.csv', encoding='uft-8') as file:
    reader= (csv.DictReader(file, delimetr=';' ))
    reader=sorted(reader)
    print(f'{В компании ['Company'] })
    for row in reader:



    with open('vacancy_news.csv', encoding='uft-8', newline='') as file:
        writer = (csv.DictReader(file, fieldnames=['Company', 'Role', 'Salary']))
        writer.writerhader()
        writer.writerows()