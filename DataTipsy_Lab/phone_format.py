customer_list = [
    {"customer_id": "001", "email": "thor@marvel.com", "mobile": "+66917589087"},
    {"customer_id": "002", "email": "spiderman@marvel.com", "mobile": "0847641758"},
    {"customer_id": "003", "email": "antman@marvel.com", "mobile": "089-983-1753"},
    {"customer_id": "004", "email": "dr.strange@marvel.com", "mobile": "083 983 7292"},
    {"customer_id": "005", "email": "hulk@marvel.com", "mobile": "091 789 3719"},
    {"customer_id": "006", "email": "black.panther@marvel.com", "mobile": "(+66)819840198"},
    {"customer_id": "007", "email": "captain.america@marvel.com", "mobile": "+66 90 1237 5890"}
]

event_registration = [
    {"email": "spiderman@marvel.com", "registration_date": "2021/10/8 12:12:45"},
    {"email": "thor@marvel.com", "registration_date": "2021/10/6 13:53:35"},
    {"email": "loki@marvel.com", "registration_date": "2021/11/13 16:39:27"},
    {"email": "black.widow@marvel.com", "registration_date": "2021/11/22 17:36:45"},
    {"email": "captain.america@mavel.com", "registration_date": "2021/11/30 18:38:23"}
]

phone = []
for i in customer_list:
  phone_number = i["mobile"]  
  phone.append(phone_number)

new_phone = []
for j in phone:
	cutnum_j = j.replace("+66", "0")
	new_phone.append(cutnum_j)   

new_format_phone = [] 
for k in new_phone:  
	for cut_string in ["(", ")", " ", "-"]: 
		newnew = k.replace(cut_string, "")
	new_format_phone.append(newnew)  

print(new_format_phone) 

 
	 