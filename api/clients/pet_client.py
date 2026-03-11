from requests import Response

from api.clients.http_client import HttpClient
from api.payloads.payloads import PetPostPayload, PetPayload


class PetClient:
    def __init__(self, base_url, client: HttpClient = None):
        self.client: HttpClient = client if client else HttpClient(base_url)
        self._update_pet_path = "/pet/{}"
        self._create_pet_path = "/pet"
        self._get_pet_path = "/pet/{}"

    def update_pet(self, payload: PetPostPayload) -> Response:
        path = self._update_pet_path.format(payload.pet_id)
        data = {"name": payload.name, "status": payload.status}
        return self.client.post(path, data=data)

    def create_pet(self, payload: PetPayload) -> Response:
        return self.client.post(self._create_pet_path, json=payload.model_dump())

    def get_pet(self, pet_id: int) -> Response:
        path = self._get_pet_path.format(pet_id)
        return self.client.get(path)
