"""
Gestión de tareas
"""

import uuid


class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.is_completed = False


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, description):
        if description is None or description == "":
            raise ValueError("desc vacia")
        id = str(uuid.uuid4())
        task = Task(id, description)
        self._tasks.append(task)

    def get_all_tasks(self):
        return self._tasks
    
    def remove_task(self, id):
        self._tasks = [t for t in self._tasks if t.id != id]
