

x=int(input("How many things u got on ur mind?: "))




tasks=[]
for i in range(1,x+1,1):	
	task=input(f"Enter the task number {i}: ")
	deadline=input(f"Enter the deadline for {task}: ")	
	tasks.append((task,deadline))

tasks=tasks.sort()
print(tasks)

"""

priority_list=[]
for tasks_and_deadlines in tasks:
	task,deadline=tasks_and_deadlines

"""
