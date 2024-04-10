#help('modules') #all modules ravadaniki code
#
'''import random
attributes=dir(random)
print(attributes)'''

#all functions and method (methods are not __)
#Example
# import random
# res=random.randint(1,10)
# print(res)

#Tast Management Project
#datatypes,operator,conditional statement,iterative statement, transfer statement,enumerate()
#Flow
#1.input like select the option
#a.Add a Task
#b.View all Tasks
#c.Mark a task if it ccompleted
#d.Unmark a task
#e.ddelete
#f.exit

from datetime import datetime
tasks=[]
while True:
    print("option: \n")
    print("1.Add A Task")
    print("2.View a Tasks")
    print("3.Mark a Task As Completed")
    print("4.Unmark a Task")
    print("5.Delete a Task")
    print("6.Edit")
    print("7.exit")
    choice=int(input("select an option from above:"))


    if choice==1:
        task_description = input("enter your task:")
        date_str=input("enter your date (format: yyyy-mm-dd:) :")
        date= datetime.strptime(date_str, "%Y-%m-%d") if date_str else None   #  #strp
        tasks.append({"task_description": task_description,"date": date,"completed": False})
        print("Task added successful...!")
        
    elif choice==2:
            if tasks:
                for index, task in enumerate(tasks,1):
                    status = "($)" if task["completed"] == True else "( )"#["completed"]it is dict 
                    date = task["date"] if task["date"] else None
                    print(f"{index}.{status} {task['task_description']}  {date}")
            else:
                print("Your task list empty..!")
    elif choice==3:
            if tasks:
                for index, task in enumerate(tasks,1):
                    if task["completed"] ==True:
                        status ="($)"
                    else:
                        status ="( )" 
                    print(f"{index}, {status} {task['task_description']}")
                task_number =int(input("enter your task number to mark as completed:"))
                if task_number>=1 and task_number<=len(tasks):#>>>=== 1 <=task_number <=len(tasks) the Best code ===<<<<
                    tasks[task_number-1]["completed"]= True 
                    print("task marked as completed")
                else:
                    print("Invalied task number...!")
            else:
                  print("your tasks list is empty...!")
    elif choice==4:
            if tasks:
                for index, task in enumerate(tasks, 1):
                    if task["completed"]== True:
                        status ="($)"
                    else:
                        status="( )"
                    print(f"{index},{status} {task['task_description']}")
                task_number =int(input("enetr your task number to unmark:"))
                if 1<= task_number<=len(tasks):
                    tasks[task_number-1]["completed"] =False 
                    print("task unmared as not completed succefully..!")
                else:
                    print("Invalid task number...!") 
            else:
                print("your tasks list is empty...!")
    elif choice==5:
            if tasks:
                for index, task in enumerate(tasks, 1):
                    if task["completed"]== True:
                        status ="($)"
                    else:
                        status="( )"
                    print(f"{index},{status} {task['task_description']}")
                task_number =int(input("enetr your task number to delete:"))
                if 1<= task_number<=len(tasks):
                    del tasks[task_number-1]

                    print("task deleted succefully..!")
                else:
                    print("Invalied task number..!")
            else:
                print("your tasks list is empty")        
    elif choice==6:
            if tasks:
                for index, task in enumerate(tasks,1):
                    if task["completed"]==True:
                        status = "($)"
                    else:
                        status=  "( )"
                    print(f"{index}.{status} {task['task_description']}")
                task_number =int(input("enter your task number to edit:"))
                if 1<=task_number<=len(tasks):       
                    task= tasks[task_number-1]  
                    print("1.edit task_description")
                    print("2.edit task date") 
                    print("3.edit task status")
                    edit_choice=int(input("select what you want to edit:"))
                    if edit_choice == 1:
                        new_description=input("enter your new task description:")
                        task['task_description']= new_description
                        print(f"task description updated..! {new_description}")
                    elif edit_choice==2:
                        new_date_str=input("enter your new_date code format(yyyy-mm-dd):")
                        new_date=datetime.strptime(new_date_str, "%Y-%B-%d").strftime("%Y-%B-%d")if new_date_str else None
                        task["date"] =new_date
                        print(f"task date successfully{new_date}") 
                    elif edit_choice==3:
                        task["completed"]=not task["completed"] 
                        print("task Marked /Unmarked successfully")

                    else:
                        print("Invalid choice")
            else:
                print("invalied Task Number")
       
    elif choice==7:
        print("exited successfully from Task Management..!")
        break
    else:
        print("you choosen Invalid option..!")
        break     

                   
                 
                   

         
                        



                            
