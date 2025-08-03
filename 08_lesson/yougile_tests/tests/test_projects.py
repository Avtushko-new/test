import uuid


class TestProjectsAPI:
    def test_create_project_positive(self, project_api):
        title = project_api.generate_unique_title()
        result = project_api.create(title)

        assert isinstance(result, dict), f"Expected dict, got {type(result)}"
        assert "id" in result, "Missing project ID"
        assert result["title"] == title, (
            f"Expected title '{title}', got '{result['title']}'"
        )

        # Additional check via GET
        get_response = project_api.get(result["id"])
        assert get_response.status_code == 200
        project_data = get_response.json()
        assert project_data.get("title") == title

    def test_get_project_positive(self, project_api, test_project):
        response = project_api.get(test_project)
        assert response.status_code == 200
        project_data = response.json()
        assert project_data["id"] == test_project
        assert "title" in project_data

    def test_update_project_positive(self, project_api, test_project):
        new_title = project_api.generate_unique_title("UpdatedProject")
        response = project_api.update(test_project, title=new_title)
        assert response.status_code in [200, 201]

        get_response = project_api.get(test_project)
        project_data = get_response.json()
        assert project_data["title"] == new_title

    def test_create_project_negative(self, project_api):
        response = project_api.create("")
        assert response.status_code == 400

    def test_get_project_negative(self, project_api):
        non_existent_id = str(uuid.uuid4())
        response = project_api.get(non_existent_id)
        assert response.status_code == 404

    def test_update_project_negative(self, project_api, test_project):
        response = project_api.update(test_project, title="")
        assert response.status_code == 400
