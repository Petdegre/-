#รหัสผ่าน = "
import random

password_facebook = "254"
result=""#เป็นค่าว่างเอาไว้เก็บผลลัพธ์

while result!=password_facebook:
    result=""
    for answer in range(len(password_facebook)):
        list_number=random.choice("0123456789")
        result="".join(list_number)+str(result)
        print("search=" ,result)
print("password is " , result)
