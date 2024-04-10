# HR executive tasks in EMPLOYEE MANAGEMENT

dataset = [
    {"name":"mounika","id":"EMP001","age":23,"gender":"Female","salary":30000,"tech_known":["python","JS","java","HTML","CSS"]},
    {"name":"sai","id":"EMP002","age":24,"gender":"Male","salary":35000,"tech_known":["python"]},
    {"name":"vijay","id":"EMP003","age":24,"gender":"Male","salary":20000,"tech_known":["JS","HTML","CSS"]},
    {"name":"shiva","id":"EMP004","age":25,"gender":"Male","salary":32000,"tech_known":["python","JS","HTML","CSS"]},
    {"name":"hemanth","id":"EMP005","age":26,"gender":"Male","salary":34000,"tech_known":["python","JS"]},
    {"name":"pooja","id":"EMP006","age":22,"gender":"Female","salary":29000,"tech_known":["HTML","CSS"]},
]

females=0
males=0
Total_salaries=0
T_salary=[]
sum_salary=0
e_salaries=[]
emp_hike=0
t_female_salaries=0
t_male_salaries=0
Name_of_employees_name_Tech_known_atleat_two=[]
highest_salary=0
highest_salary_set_name=""
while True:

    print("choose numbers:\n")
    print("1.count number of males and females")
    print("2.Total salaries")
    print("3.employee Hike 2000 RS<23")
    print("4.employee hike 5% whose age =25")
    print("5.Sum male and female salaries seperately")
    print("6.find name of employees who knows 2 techologies")
    print("7.find employees who knows python, JS, java,HTML,CSS  give them Hike of 15% ")
    print("8.highest salary name")
    print("9.employee who knows only one technology and remove them")
    print("10.add employees")
    option=int(input("enter your option:"))
    print()
    if option==1:
        print("1.count number of males and females")
        for set in dataset:
            if set["gender"]=="Female":
                females+=1
            elif set["gender"]=="Male":
                males+=1
        print("males:",males)
        print("females:",females)
        print()   
    
    elif option==2:
        print("2.Total salaries")
        print()
        for set in dataset:
            
            '''if set["salary"]<36000:             #
                print("emp_salary",set["salary"])  #
                                                   #
                e_salaries.append(set["salary"])   #
        print(e_salaries)                  #
        Total_salaries=sum(e_salaries)     #
        print(Total_salaries)          #my own written the program'''
            #Tarun told
            if set["salary"]:              
                Total_salaries=Total_salaries+set["salary"]
                print(Total_salaries)
    elif option==4:
        print("4.employee hike 5% whose age =25")
        print()
        for set in dataset:
              if set["age"]==25:
                  employee=set["salary"]+set["salary"]*5/100
                 # # 33600.0   = 32000+32000*5
                  set["salary"]=employee
            #    print(set["salary"])#32000
                  print("Hike 5% add to age==25:",employee)#33600.0'''
                  print()
    elif option == 3:
        print("3.employee Hike 2000 RS<23")
        print()
        for set in dataset:
            if set["age"]<23:
                print(set["name"])
                
                set["salary"]= set["salary"]+2000
                print(set["name"],set["salary"])
    elif option==5:            
        print("5.Sum male and female salaries seperately")
        for set in dataset:
            if set["gender"]=="Male":
                
                t_male_salaries=t_male_salaries+set["salary"]
                print()
                
            if set["gender"]=="Female": #we can use if or elif in this line
                
                t_female_salaries=t_female_salaries+set["salary"]
                print()
            print("female_salaries:",t_female_salaries)
            print("Male_salariess:",t_male_salaries)
            print()
            Total_emp_salaries = t_male_salaries+ t_female_salaries
            print()
            print("Total employee salaries:",Total_emp_salaries)
            
    elif option == 6:
        print("6.find name of employees who knows 2 techologies")
        for set in dataset:
               if len(set["tech_known"])  >=  2:
            
                    print(set["name"])
                    #answer in list[ ]
                    Name_of_employees_name_Tech_known_atleat_two.append(set["name"])
        print("Name_of_employees_name_Tech_known_atleat_two:",Name_of_employees_name_Tech_known_atleat_two)
        print(type(Name_of_employees_name_Tech_known_atleat_two))

        print() 
    elif option == 7:
        print("7.find employees who knows python, JS, java,HTML,CSS  give them Hike of 15% ")
        for set in dataset:
            if "python" in set["tech_known"] or "JS" in set["tech_known"]:
                set["salary"] = set["salary"] + set["salary"] * 15 /100
                print(set["name"], set["salary"])
            print()#not given answers

    elif option==8:
        print("8.highest salary name")
        for set in dataset:
            if set["salary"] > highest_salary:
                
                highest_salary = set["salary"]
                #for high salary Name
                highest_salary_employee_name = set['name']
                
        print("Highest salary:",highest_salary, highest_salary_employee_name)        
        #35000 sai
    elif  option==9:
        print("9.employee who knows only one technology and remove them")
        for set in dataset:
            if len(set["tech_known"])==1:
                dataset.remove(set)
                print(f"removed employee are {set['name']}")

    
    elif option==11:
        print("edit employee")
        edit_employee=input("enter your employee:")
        if dataset:
            dataset.append({"name":"ani", "id":"EMPOO7","gender":"Female","salary": 10000,"tech_known":["python","HTML","CSS","NUMPY"]})
            print(dataset)
            total_employee=len(dataset)
            print(total_employee)
    elif option ==12:
        print("insert the employee details:")
        for set in dataset:#mandatory
        
                set["name"]="Kalyani"
                set["id"]="EMP008"
                set["age"]=23
                set["salary"]=20000
                set["gender"]="Female"
                set["tech_known"]=["AWS"]
                total_employee=len(dataset)
                print(total_employee)
                print(dataset)
                break
        print()
    elif option ==13:
        print("if you want to update key and value:")
        for set in dataset:
            if set["name"] == "hemanth":
                set.update({'age':29})
            print(set)
            highest_age=0
    elif option==14:
        print("with using input edit your new_employee details in dataset or set:")
        for set in dataset:
            dict={}
    
            size=int(input("enter your size:"))
            for i in range(size):
                key=input("enter your key:")
                value=input("enter your value:")
                #dict[key]=value
                print(dict)
            dataset.append(dict)
            
            print(dataset)
                
                



    elif option==10:
        print("10.add employees")
        #for set in dataset:
        new_employee={"name":"Bhavani", "id":"EMPOO7","gender":"Female","salary": 10000,"tech_known":["python","HTML","CSS","NUMPY"]}
        dataset.append(new_employee)       
        print(dataset)
        total_employee=len(dataset)
        print(total_employee)
        
        break
    # elif option==15:
    #     for set in dataset:
    #         print(set)
            
                
           









             



                 







               

                
                            




                
                
            
                
                

            

                








            
    
    
    