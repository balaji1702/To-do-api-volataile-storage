from enum import Enum
from typing import Optional
from fastapi import FastAPI
#some comman for testing 
app = FastAPI()
from pydantic import BaseModel
task_list=[]
class Priority(Enum):
    High="HIGH PRIORITY"
    Low="LOW PRIORITY"
class Status(Enum):
    pending="PENDING"
    completed="COMPLETED"
    
class Task(BaseModel):
    task_name: str
    description: str  
    priority :Priority
    status: Status

@app.post("/create-task")
def create_task(new_task:Task):
     task=new_task.dict()
     
     task_list.append(task)
     print(task_list)
     return {"msg":"suceesfully added"}
@app.get("/get-task")
def get_task():
    
    return task_list
@app.get("/get-task-by-PRIORITY")
def filter_by_priority(q: Priority):
    Priority_res=[]
    for i in task_list:
        if(i["priority"]==q):
            Priority_res.append(i)

            
        
    return Priority_res

@app.get("/get-task-by-status")
def filter_by_status(q:Status):
    Priority_res=[]
    for i in task_list:
        if(i["status"]==q):
            Priority_res.append(i)

            
        
    return Priority_res
@app.put("/task_update_status/{taskname}")
def update_status(taskname:str,q:Status):
    for i in task_list:
        if(i["task_name"]==taskname):
            i["status"]=q
            return {"msg":f"status updated to {q}"} 

    return {"msg":"something not good"}

@app.delete("/delete-task")
def delete_task(task_name:str):
    for i in task_list:
        if(i["task_name"]==task_name):
            task_list.remove(i)
            return{"msg":"deleted sucessfully"}
    return{"msg":"given task name not found"}
    


