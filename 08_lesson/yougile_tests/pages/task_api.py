import logging
import requests

logger = logging.getLogger(__name__)


class TaskAPI:
    def __init__(self, base_url, api_key):
        self.base_url = f"{base_url}/tasks"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        logger.info("TaskAPI headers set")

    def create_task(self, title, column_id, **kwargs):
        data = {
            "title": title,
            "columnId": column_id,
            "completed": False,
            "color": "task-blue",
            **kwargs
        }

        logger.info(f"Creating task: {title} in column {column_id}")
        response = self.session.post(self.base_url, json=data)

        if response.status_code in [200, 201]:
            return {
                "id": response.json().get("id"),
                "title": title,
                "columnId": column_id
            }
        else:
            return response

    def get_task(self, task_id):
        logger.info(f"Getting task: {task_id}")
        return self.session.get(f"{self.base_url}/{task_id}")
