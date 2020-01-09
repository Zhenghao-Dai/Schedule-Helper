import schedule_api as api

a = api.schedule_api()
print(a.get_course_remain("csci-103", 29900, "Lecture"))
