import csv
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://krittikaiitb.github.io/team')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
fields = ['Name','Title','Year']
rows = []
 
#s = soup.find('div', class_='row row-cols-sm-2 row-cols-1 justify-content-center')
#2019 year
s = soup.find('div', id='myTab-tabpane-2019')

names = s.find_all('h5')
titles = s.find_all('p')
count=1

for name in names:
    print(name.text)
    print(titles[count].text)
    rows.append([name.text,titles[count].text,2019])
    count += 1
    
#2020 year
s = soup.find('div', id='myTab-tabpane-2020')

names = s.find_all('h5')
titles = s.find_all('p')
count=1

for name in names:
    print(name.text)
    print(titles[count].text)
    rows.append([name.text,titles[count].text,2020])
    count += 1
    
#2021 year
s = soup.find('div', id='myTab-tabpane-2021')

names = s.find_all('h5')
titles = s.find_all('p')
count=1

for name in names:
    print(name.text)
    print(titles[count].text)
    rows.append([name.text,titles[count].text,2021])
    count += 1

s = soup.find('div', id='myTab-tabpane-2022')

names = s.find_all('h5')
titles = s.find_all('p')
count=1

for name in names:
    print(name.text)
    print(titles[count].text)
    rows.append([name.text,titles[count].text,2022])
    count += 1

##s = soup.find('div', class_='row row-cols-md-3 row-cols-2 justify-content-center')
## 
##names = s.find_all('h5')
##titles = s.find_all('p')
## 
##count=0
##for name in names:
##    print(name.text)
##    print(titles[count].text)
##    rows.append([name.text,titles[count].text,2022])
##    count += 1

# name of csv file 
filename = "krittika_team.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

