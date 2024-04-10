# HR employee management:

employees = [                                                                          
    { "name" : "nandhu", "id" : "EMP001" , "age" : 23, "gender" : "Female", "salary" : 30000, "tech_known" : [ "python", "JS" , "java", "HTML", "CSS" ]},
    { "name" : "sai", "id" : "EMP002", "age" : 24, "gender" : "Male", "salary" : 35000, "tech_known" : [ "python" ]},
    { "name" : "mohan", "id" : "EMP003", "age" : 24, "gender" : "Male", "salary" : 20000, "tech_known" : [ "JS", "HTML", "CSS" ]},
    { "name" : "shiva", "id" : "EMP004", "age" : 25, "gender" : "Male", "salary" : 32000, "tech_known" : [ "python", "JS", "HTML", "CSS" ]},
    { "name" : "maruthi", "id" : "EMP005", "age" : 26, "gender" : "Male", "salary" : 34000, "tech_known" : [ "python", "JS" ]},
    { "name" : "pooja", "id" : "EMP006", "age" : 22, "gender" : "Female", "salary" : 29000, "tech_known" : [ "python", "JS" ]},
  ]

# print all employees:
for employee in employees:
    print(employee)

total_employees = len(employees)
print("Total_employees:",total_employees)#6
print()
# number of males and number of females

number_of_males = 0
number_of_females = 0

for employee in employees:
    if employee['gender'] == "Male":
        number_of_males = number_of_males + 1  
   


    if employee["gender"] == "Female":
        number_of_females = number_of_females + 1


print(f"Number of males are {number_of_males}")#4
print(f"Number of males are {number_of_females}")#2
print()


# calculate total salaries

total_salary = 0

for employee in employees:
    total_salary = total_salary + employee['salary']
print() 
print("Total_salaries:",total_salary)#180000
print()


# 3. give hike of 2000 to the employee whose age is less than 23

for employee in employees:
    if employee['age'] < 23:
        employee["salary"] = employee["salary"] + 2000
        print(employee['name'] , employee["salary"])#pooja 31000
        print()
#  4. give hike of 5% to the employees whose age = 25

for employee in employees:
    if employee['age'] == 25:
        employee["salary"] = employee["salary"] + employee["salary"] * 5 / 100
        print("Hike salary whom age==25 add 15% :",employee["name"], employee["salary"])#shiva 33600.0
print()
#after answer[nandhu 34500.0]  ,before[30000]    +4500==5%
#  5. find sum of female employees salary and male employees salary seperately
        
total_male_salary = 0
total_female_salary = 0

for employee in employees:
    if employee['gender'] == "Male":
        total_male_salary = total_male_salary + employee['salary']

    if employee['gender'] == 'Female':
        total_female_salary = total_female_salary + employee["salary"]


print()
print(f'Total males salary is {total_male_salary}')#122600.0
print(f'Total females salary is {total_female_salary}')#61000
total_salary = total_male_salary + total_female_salary#183600.0
print(f'Total salary {total_salary}')
print()
#  6. find names of employees who knows atleast 2 technologies
name_of_employees_who_known_atleast_2_tech = []

for employee in employees:
        if len(employee['tech_known']) >= 2:
            # print(employee["name"])
            name_of_employees_who_known_atleast_2_tech.append(employee["name"])

print("technologies knowns atleast 2 :",name_of_employees_who_known_atleast_2_tech)
print()
#answer:['nandhu', 'mohan', 'shiva', 'maruthi', 'pooja']


#  7. find employees who knows python, JS give them hike of 15%

for employee in employees:
    if "python" in employee['tech_known'] and "JS" in employee["tech_known"]:
        employee["salary"] = employee["salary"] + employee["salary"] * 15 /100
        print("technologies knowns who knows python and JS give hike 15%:",employee["name"], employee["salary"])
        
'''Answer:
 nandhu 34500.0
shiva 38640.0
maruthi 39100.0
pooja 35650.0
 '''   



#  8. find the name of employee who is having highest salary
        
highest_salary = 0
highest_salary_employee_name = ""

for employee in employees:
    if employee['salary'] > highest_salary:
            highest_salary = employee["salary"]
            highest_salary_employee_name = employee['name']
    print()
    print("Hihgest salary:",highest_salary , highest_salary_employee_name)
'''#line by line space is here to the answer:
34500.0 nandhu

35000 sai

35000 sai

38640.0 shiva

39100.0 maruthi

39100.0 maruthi'''
#  9. find the employees who knows only one technology and remove them
    
for employee in employees:
    if len(employee["tech_known"]) == 1:
        employees.remove(employee)
        print(f"removed employees are:  {employee['name']}")
        print()
       #Answer: removed employees are sai




#  10. add new emoployee name = Nandhu, id = EMP007,gender = Female , salary = 32000, tech_known = powerbi, python

new_employee = {"name" : 'bhavani', "id" : "EMP007", "gender" : "Female", "salary" : 100000, "tech_known" : ["python","HTML", "CSS","numpy"]}

employees.append(new_employee)
print("New employee added:",  employees)
print()
#answer:======
#New employee: [{'name': 'nandhu', 'id': 'EMP001', 'age': 23, 'gender': 'Female', 'salary': 34500.0, 'tech_known': ['python', 'JS', 'java', 'HTML', 'CSS']}, {'name': 'mohan', 'id': 'EMP003', 'age': 24, 'gender': 'Male', 'salary': 20000, 'tech_known': ['JS', 'HTML', 'CSS']}, {'name': 'shiva', 'id': 'EMP004', 'age': 25, 'gender': 'Male', 'salary': 38640.0, 'tech_known': ['python', 'JS', 'HTML', 'CSS']}, {'name': 'maruthi', 'id': 'EMP005', 'age': 26, 'gender': 'Male', 'salary': 39100.0, 'tech_known': ['python', 'JS']}, {'name': 'pooja', 'id': 'EMP006', 'age': 22, 'gender': 'Female', 'salary': 35650.0, 'tech_known': ['python', 'JS']}, {'name': 'bhavani', 'id': 'EMP007', 'gender': 'Female', 'salary': 100000, 'tech_known': ['python', 'HTML', 'CSS', 'numpy']}]
total_employees = len(employees)
print("length of employees:",  
    
    total_employees)
print()
#answer:6


# reamiining 5 , edit/update , add, delete
