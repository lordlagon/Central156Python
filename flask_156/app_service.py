import json;

class AppService:
    
    tasks = [
        {
            "id": 1,
            "name": "Usa",
            "totalCases": 124565,
            "totalDeaths": 161156,
        },
        {
            "id": 2,
            "name": "Udddsa",
            "totalCases": 124565,
            "totalDeaths": 161156,
            
        },
        {
            "id": 3,
            "name": "brasil",
            "totalCases": 15545465,
            "totalDeaths": 1616,
            
        },
        
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON

    def create_task(self,task):
        tasksData = json.loads(self.tasksJSON)
        tasksData.append(task)
        self.tasksJSON = json.dumps(tasksData)
        return self.tasksJSON

    def update_task(self, request_task):
        tasksData = json.loads(self.tasksJSON)
        for task in tasksData:
            if task["id"] == request_task['id']:
                task.update(request_task)
                return json.dumps(tasksData);
        return json.dumps({'message': 'task id not found'});

    def delete_task(self, request_task_id):
        tasksData = json.loads(self.tasksJSON)
        for task in tasksData:
            if task["id"] == request_task_id:
                tasksData.remove(task)
                return json.dumps(tasksData);
        return json.dumps({'message': 'task id not found'});

