import random
import uuid

import pytest
from assertpy import assert_that

from api.payloads.payloads import PetPostPayload
from api.responses.responses import PetResponse, UpdatePetResponse


@pytest.mark.parametrize(
    "updated_data",
    [
        {'name': str(uuid.uuid4())},
        {'status': "sold"},
        {'status': str(uuid.uuid4()), 'name': "pending"},
    ]
)
def test_update_pet(pet_client, create_pet_factory, faker, updated_data):
    pet = create_pet_factory()
    payload = PetPostPayload(
        pet_id=pet.id,
        name=updated_data.get("name") or pet.name,
        status=updated_data.get("status") or pet.status
    )
    response = pet_client.update_pet(payload)
    updated_pet = PetResponse(**pet_client.get_pet(pet.id).json())

    assert_that(response.status_code).is_equal_to(200)
    assert_that(updated_pet.name).is_equal_to(payload.name)
    assert_that(updated_pet.status).is_equal_to(payload.status)


def test_update_not_existing_pet(pet_client, create_pet_factory, faker, new_name, new_status):
    nonexistent_id = random.randint(10_000, 100_000)
    payload = PetPostPayload(
        pet_id=nonexistent_id,
        name=new_name,
        status=new_status,
    )
    response = UpdatePetResponse(**pet_client.update_pet(payload).json())

    assert_that(response.code).is_equal_to(404)
    assert_that(response.message).is_equal_to("not found")
