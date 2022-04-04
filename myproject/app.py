
import random
       #     0       1         2     3
items = ['book','smartphone','ps5','xbox']
#print(len(items))
result = random.randint(0,len(items)-1)
#print(result)
#print(f'สินค้าที่ได้: {items[result]}')

#username = input("Enter username:")
#print("Username is: " + username)

print('โปรแกรมหาพื้นที่สี่เหลี่ยม')
sq1 = float(input("รับข้อมูลความกว้างเมตร:"))
print(f'ความกว้างคือ:{sq1} เมตร')
sq2 = float(input("รับข้อมูลความยาวเมตร:"))
print(f'ความยาวคือ:{sq2} เมตร')
result = sq1*sq2
print(f'ขนาดของพื้นที่:{result} ตารางเมตร')
