
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "q82070002", "schedule")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

from bs4 import BeautifulSoup
import requests
url = "https://classes.usc.edu/term-20201/classes/csci/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/51.0.2704.63 Safari/537.36'}

response = requests.get(url=url, headers=headers)
if response.status_code != 200:
    raise Exception("404")
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")
test = soup.find("div", {"class": "course-table"})
for child in test.children:
    if child.string == None:
        course_id=child.attrs['id'].lower()
        course_html=child.find("table", {"class": "sections responsive"})
        
        for course in course_html.children:
            
            # if not the header
            if course.attrs['class'] != ['headers']:

                for section in course.children:
                    if section.attrs['class'] == ['type']:

                        # if the section is colsed
                        if course.contents[5].attrs['class'] == ['registered']:
                            if course.contents[5].contents[1].name == 'div':
                                num_remain = 0
                                print(
                                    course.attrs["data-section-id"]+section.string + str(num_remain))
                                sql = """INSERT INTO csci(course_id,
                                        section_id, remain_num, type)
                                        VALUES (%s, %s,%s,%s) """
                                cursor.execute(
                                    sql, (course_id, course.attrs["data-section-id"], str(num_remain), section.string))
                                # 提交到数据库执行
                                db.commit()
                            else:
                                remain = course.contents[5].contents[1].split(
                                    ' of ')
                                num_remain = int(
                                    remain[1])-int(remain[0])
                                sql = """INSERT INTO csci(course_id,
                                        section_id, remain_num, type)
                                        VALUES (%s, %s,%s,%s) """
                                cursor.execute(
                                    sql, (course_id, course.attrs["data-section-id"], str(num_remain), section.string))
                                # 提交到数据库执行
                                db.commit()


# 关闭数据库连接
db.close()    
