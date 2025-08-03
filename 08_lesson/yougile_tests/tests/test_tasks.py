import os
import pytest
import time
import uuid


class TestTaskAPI:

    def test_create_task_minimal(self, task_api, test_task):
        response = task_api.get_task(test_task)
        assert response.status_code == 200
        task_data = response.json()
        assert task_data["id"] == test_task
        assert task_data["title"].startswith("TestTask_")
        assert task_data["columnId"] == os.getenv("TEST_COLUMN_ID")

    def test_create_task_full(self, task_api):
        test_column_id = os.getenv("TEST_COLUMN_ID")
        if not test_column_id:
            pytest.skip("TEST_COLUMN_ID not set")

        title = f"FullTask_{uuid.uuid4().hex[:8]}"
        current_time = int(time.time() * 1000)
        start_date = current_time
        deadline = current_time + 3600000  # +1 hour

        response = task_api.create_task(
            title=title,
            column_id=test_column_id,
            description="Full test task",
            color="task-red",
            idTaskCommon=f"TASK-{uuid.uuid4().hex[:4]}",
            deadline={
                "deadline": deadline,
                "startDate": start_date,
                "withTime": True
            },
            timeTracking={
                "plan": 120,
                "work": 30
            },
            checklists=[
                {
                    "title": "Checklist 1",
                    "items": [
                        {"title": "Item 1", "isCompleted": False},
                        {"title": "Item 2", "isCompleted": True}
                    ]
                }
            ]
        )

        assert response.status_code in [200, 201]
        task_id = response["id"]

        get_response = task_api.get_task(task_id)
        full_task_data = get_response.json()
        assert full_task_data["title"] == title
        assert full_task_data["description"] == "Full test task"
        assert full_task_data["color"] == "task-red"
        assert "deadline" in full_task_data
        assert full_task_data["deadline"]["deadline"] == deadline
