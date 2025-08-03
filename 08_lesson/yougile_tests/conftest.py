import pytest
import logging
import os
import uuid
from dotenv import load_dotenv
from pages.auth_manager import AuthManager
from pages.project_api import ProjectAPI
from pages.task_api import TaskAPI

# Load environment variables
load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"
LOGIN = os.getenv("YOUGILE_LOGIN")
PASSWORD = os.getenv("YOUGILE_PASSWORD")
COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
TEST_COLUMN_ID = os.getenv("TEST_COLUMN_ID")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def auth_manager():
    return AuthManager()


@pytest.fixture(scope="session")
def api_key(auth_manager):
    if not all([LOGIN, PASSWORD, COMPANY_ID]):
        pytest.fail(
            "Set YOUGILE_LOGIN, YOUGILE_PASSWORD, YOUGILE_COMPANY_ID in .env"
        )
    return auth_manager.get_api_key(BASE_URL, LOGIN, PASSWORD, COMPANY_ID)


@pytest.fixture(scope="module")
def project_api(api_key):
    return ProjectAPI(BASE_URL, api_key)


@pytest.fixture(scope="module")
def task_api(api_key):
    return TaskAPI(BASE_URL, api_key)


@pytest.fixture
def test_project(project_api):
    title = project_api.generate_unique_title()
    result = project_api.create(title)

    if not isinstance(result, dict) or "id" not in result:
        status = (result.status_code 
          if hasattr(result, 'status_code') else 'N/A')
        response = result.text if hasattr(result, 'text') else str(result)

        error_msg = (
            f"Project creation error\n"
            f"Status: {status}\n"
            f"Response: {response}"
        )
        pytest.fail(error_msg)

    project_id = result["id"]
    logger.info(f"Test project created: {project_id} ({result['title']})")

    yield project_id


@pytest.fixture
def test_task(task_api):
    if not TEST_COLUMN_ID:
        pytest.skip("TEST_COLUMN_ID not set in .env")

    title = f"TestTask_{uuid.uuid4().hex[:8]}"
    result = task_api.create_task(
        title=title,
        column_id=TEST_COLUMN_ID,
        description="Test task for automated tests"
    )

    if not isinstance(result, dict) or "id" not in result:
        error_msg = (
            f"Task creation error\n"
            f"Status: {result.status_code if hasattr(result, 'status_code') else 'N/A'}\n"
            f"Response: {result.text if hasattr(result, 'text') else str(result)}"
        )
        pytest.fail(error_msg)

    task_id = result["id"]
    logger.info(f"Test task created: {task_id}")

    yield task_id
