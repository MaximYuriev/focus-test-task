import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "task", [
        {
            "title": "string",
            "description": "string",
            "status": "Completed"
        },
        {
            "title": "string",
            "description": "string",
            "status": "In progress",
        },
        {
            "title": "string",
            "description": "string",
            "status": "Pending",
        }
    ]
)
async def test_create_task(
        api_client: AsyncClient,
        task: dict[str, str],
):
    response = await api_client.post("tasks/", json=task)
    assert response.status_code == 200
