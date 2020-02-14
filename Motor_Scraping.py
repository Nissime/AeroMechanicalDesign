import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#Extract data from https://database.rcbenchmark.com/motors
result = requests.get("https://database.rcbenchmark.com/motors")
value = []
data_headers = []
data_value = []
def find_all(a_string, sub):
    result = []
    k = 0
    while k < len(a_string):
        k = a_string.find(sub, k)
        if k == -1:
            return result
        else:
            result.append(k)
            k += 1 #change to k += len(sub) to not search overlapping results
    return result

class component_data:
    name = ''
    benchmarks = 0.0
    weight_g = 0.0
    shaft_diamater_mm = 0.0
    kv = 0.0
    magnatic_poles = 0.0

# print(result.status_code)
src = result.content
soup = BeautifulSoup(src,'lxml')
data = soup.find('div')
print(soup.find('div',class_="col-md-12"))
x = soup.find('div',class_="col-md-12")
# print(data)
#find all links in page :
# li nks = soup.find_all('container')
# print(links)
y = soup.find('components-index')
y_str = str(y)
idx_start = find_all(y_str,'[')
idx_end = find_all(y_str,']')
header_idxs = (idx_start[0],idx_end[0])
data_idxs = (idx_start[1],idx_end[1])
headers = y_str[header_idxs[0]:header_idxs[1]]
datas = y_str[data_idxs[0]:data_idxs[1]]
# header_data_idxs = split(headers,',')
header_values = re.findall('{.+?}',headers)
for i in header_values:
    list_att = re.findall('[^\"\"]*\w', i[0])
    value.append(i.split(',')[0].split(':')[1][1:-1])

data_values = re.findall('{.+?}',datas) #split all data in braces

df = pd.DataFrame()
df2 = pd.DataFrame()

FirstTime_list = True
for j in data_values:
    split_tempo = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', j)
    for k in split_tempo:
        data_temp = re.findall('[^\"\"]*\w',k)
        data_headers.append(data_temp[0])
        data_value.append(data_temp[1])
        

    df2 = pd.DataFrame.from_dict(dict(zip(data_headers,data_value)),orient='index').T

    if not(FirstTime_list):
        df = df.append(df2)
    if FirstTime_list:
        df = pd.DataFrame.from_dict(dict(zip(data_headers,data_value)),orient='index').T
        FirstTime_list = False
    data_headers=[]
    data_value=[]

print("here")

