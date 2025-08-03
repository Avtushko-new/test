import uuid
import logging
import requests

logger = logging.getLogger(__name__)


class ProjectAPI:
    def __init__(self, base_url, api_key):
        self.base_url = f"{base_url}/projects"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        logger.info("ProjectAPI headers set")

    def create(self, title):
        data = {"title": title}
        logger.info(f"Creating project: {title}")
        response = self.session.post(self.base_url, json=data)

        if response.status_code in [200, 201]:
            return {
                "id": response.json().get("id"),
                "title": title
            }
        else:
            return response

    def get(self, project_id):
        logger.info(f"Getting project: {project_id}")
        return self.session.get(f"{self.base_url}/{project_id}")

    def update(self, project_id, title=None):
        data = {}
        if title is not None:
            data["title"] = title
        logger.info(f"Updating project {project_id} with data: {data}")
        return self.session.put(f"{self.base_url}/{project_id}", json=data)

    def generate_unique_title(self, prefix="TestProject"):
        return f"{prefix}{uuid.uuid4().hex[:6]}"
