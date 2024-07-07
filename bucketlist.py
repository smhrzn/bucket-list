 def add(task):
    n=input("Enter a task :")
    task.append(n)
    return task
    
def view(task):
    o=0
    for i in task:
        o=o+1
        print(o,".",i)
    
def delete_task(task):
    n=int(input("Enter which task to delete :"))
    del task[n-1]
    return task
    
def main():
    task=[]
    while True:
        user=input("Press 'y'to accept, Press 'd' to delete, Press 'v' to view else press any key to exit")
        conv=user.capitalize()
        if conv=="Y":
            task=add(task)
        elif conv=="V":
            view(task)
        elif conv=="D":
            task=delete_task(task)
        else:
            break
        
main()
        
