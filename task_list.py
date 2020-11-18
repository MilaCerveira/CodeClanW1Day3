#chickens = [
#  { "name": "Margaret", "age": 2, "eggs": 0 },
#  { "name": "Hetty", "age": 1, "eggs": 2 },
#  { "name": "Henrietta", "age": 3, "eggs": 1 },
#  { "name": "Audrey", "age": 2, "eggs": 0 },
#  { "name": "Mabel", "age": 5, "eggs": 1 },


#def find_chicken_by_name( list, chicken_name ):
#  for chicken in list:
#    if chicken["name"] == chicken_name:
#      return chicken
#    else:
#      return "Not found"



tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
#if task == False:
   # for key value in completed():
      #  print task("status"+key)
        

1 Print a list of uncompleted tasks
 def uncompleted_tasks(tasks):
     incomplete_tasks=[]
     for task in tasks:
         if task["completed"] == False:
             incomplete_tasks.append(task)
     return incomplete_tasks

# print (uncompleted_tasks(tasks))

#2 Print a list of completed tasks

 def completed_tasks(tasks):
     complete_tasks=[]
     for task in tasks:
         if task["completed"] == True:
             complete_tasks.append(task)
     return complete_tasks

print (completed_tasks(tasks))

#3 Print a list of all the task decriptions

def task_descriptions(task):
    description_list =[]
    for task in tasks:
        description_list.append(task)
    return description_list
print(task_descriptions(task))

#4 Print a list of tasks where time taken is at least a given time
    
    





# def uncompleted_tasks( tasks, uncompleted ):
#       for tasks in list:
#     if chicken["name"] == chicken_name:
#       return chicken
#     else:
#       return "Not found"
# def find_chicken_by_name( list, chicken_name ):
#       for chicken in list:
#     if chicken["name"] == chicken_name:
#       return chicken
#     else:
#       return "Not found"






#for task in tasks:
#    if completed == false:
#        task = 

#res = True 
#for ele in test_dict: 
#    if not test_dict[ele]: 
#        res = False 
#        break


#for key, value in task():
#    print(key, 'is the key for the value', value)