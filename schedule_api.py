from bs4 import BeautifulSoup
import requests
class schedule_api:
    #give department code
    #return a dict
    #name as key, remian seats as value
    def get_department_remain(self):
        return 0

    #pass course id 
    #pass 0 if all section work
    #return remain num  
    def get_course_remain(self,course_id,section_id,_type):
        url = "https://classes.usc.edu/term-20201/course/"+str(course_id)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("404")
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")
        test = soup.find("table", {"class": "sections responsive"})
        num_total = 0
        
        #Search for section
        if section_id != 0:
            for child in test.children:
                # if not the header
                if child.attrs['class'] != ['headers']:
                    if child.attrs["data-section-id"] == str(section_id):
                        for section in child.children:

                            if section.attrs['class'] == ['type']:
                                
                                    # if the section is colsed
                                    if child.contents[5].attrs['class'] == ['registered']:
                                        if child.contents[5].contents[1].name == 'div':
                                            num_remain = 0
                                        else:
                                            remain = child.contents[5].contents[1].split(
                                                ' of ')
                                            num_remain = int(
                                                remain[1])-int(remain[0])
                                        num_total += num_remain
        else:
            for child in test.children:
                # if not the header
                if child.attrs['class'] != ['headers']:

                    
                    for section in child.children:

                        if section.attrs['class'] == ['type']:
                            if section.contents == [_type]:
                                # if the section is colsed
                                if child.contents[5].attrs['class'] == ['registered']:
                                    if child.contents[5].contents[1].name == 'div':
                                        num_remain = 0
                                    else:
                                        remain = child.contents[5].contents[1].split(
                                            ' of ')
                                        num_remain = int(
                                            remain[1])-int(remain[0])
                                    num_total += num_remain
        return num_total


