from tasks import TaskManager
import pytest

@pytest.fixture
def manager():
    return TaskManager()

def test_add_task(manager):
    manager.add_task("Task 1")
    tasks = manager.get_all_tasks()

    assert len(tasks) == 1
    assert tasks[0].description == "Task 1"
    assert not tasks[0].is_completed

@pytest.mark.parametrize(
        "tasks, length",
        [
         ([], 0),   
         (["Task 1"], 1),   
         (["Task 1", "Task 2", "Task 3"], 3),
        ]
)
def test_get_all_tasks(manager, tasks, length):
    for t in tasks:
        manager.add_task(t)
    
    assert len(manager.get_all_tasks()) == length

@pytest.mark.parametrize(
        "id_to_remove",
        [
            ("1"),
            ("2"),
            ("3"),
        ]
)
def test_remove_task_by_id(manager, id_to_remove, mocker):
    mock_uuid = mocker.patch("tasks.uuid.uuid4")
    mock_uuid.side_effect = ["1", "2", "3"]

    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")

    manager.remove_task(id_to_remove)

    list_tasks = manager.get_all_tasks()
    list_ids = [t.id for t in list_tasks]

    assert id_to_remove not in list_ids
    assert len(list_tasks) == 2

def test_add_task_empty_desc(manager):
    with pytest.raises(
        ValueError, match="desc vacia"
    ):
        manager.add_task("")

    assert len(manager.get_all_tasks()) == 0
