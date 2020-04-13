import json
file_name="suscrible_list.json"
def store(data):
	with open(file_name,'w')as fw:
		json.dump(data,fw)
def load():
	with open(file_name,'r')as f:
		data=json.load(f)
		return data
'''
old_json=load()
#old_json['econ-351 31231']=['zhengadsahd@co.']
if old_json.get("econ-351 31231"):
	old_json['econ-351 31231'].append("djasjaskhdi")
store(old_json)
print(load())'''

def poll_spot():
	old_json=load()
	for course_id in old_json:
		#if open ,send notfication, delete message fuc
			print(course_id)
			new_contact_info=[]
			for y in old_json[course_id]:
				#if remain =0
				
					new_contact_info.append(y)
			#assign to to dict
			old_json[course_id]=new_contact_info
	store(old_json)
				
				
def add(course,contact_info):
	old_json=load()
	if old_json.get(course):
		old_json[course].append(contact_info)
	else:
		old_json[course]=[contact_info]
	store(old_json)
