import pytest
from faker import Faker
from selenium import webdriver

from api.clients.pet_client import PetClient
from api.payloads.payloads import PetPayload, Category, Tag
from api.responses.responses import PetResponse
from pages.google_login_page import LoginPage


@pytest.fixture
def pet_client():
    return PetClient("https://petstore.swagger.io/v2")


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    yield LoginPage(driver, timeout=10)


@pytest.fixture
def create_pet_factory(pet_client, faker):
    def _make_pet(**kwargs):
        payload_data = {
            "id": faker.random_int(min=1, max=10000),
            "category": Category(
                id=faker.random_int(min=1, max=100), name=faker.word()
            ),
            "name": faker.first_name(),
            "photoUrls": [faker.image_url()],
            "tags": [Tag(id=faker.random_int(min=1, max=100), name=faker.word())],
            "status": "available",
        }

        payload_data.update(kwargs)

        payload = PetPayload(**payload_data)
        response = pet_client.create_pet(payload)

        assert response.status_code == 200, f"Failed to create pet: {response.text}"
        return PetResponse

    return _make_pet
