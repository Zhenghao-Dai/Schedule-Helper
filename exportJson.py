import requests
from bs4 import BeautifulSoup
import json
from schedule_api import* 
from concurrent.futures import ThreadPoolExecutor

file_name="course.json"
def store(data):
	with open(file_name,'w')as fw:
		json.dump(data,fw)
empty = {}
url = "https://classes.usc.edu/term-20203/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/51.0.2704.63 Safari/537.36'}
pool = ThreadPoolExecutor(128)
response = requests.get(url=url, headers=headers)
if response.status_code != 200:
    raise Exception("404")
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")
test = soup.find("ul", {"class": "sortable"})
for department in test.children:
   if department.name == "li":
        data_school = department.attrs["data-school"]
        data_title = department.attrs["data-title"]
        data_type = department.attrs["data-type"]
        data_code = department.attrs["data-code"]
        if data_type == "school" :
            pass
    
        else:
            a = schedule_api()
            print("now adding"+ data_title)
            department_course = a.get_list_departement_course(data_code)
            
            if not empty.get(data_school):
                empty[data_school] ={data_title: department_course}
            else:
                empty[data_school][data_title] = department_course
            
store(empty)


      
