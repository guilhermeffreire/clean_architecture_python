from typing import Type
from src.domain.use_cases import FindPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors

class FindPetController:
    def __init(self, find_pet_use_case: Type[FindPet]):
        self.find_pet_use_case = find_pet_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "pet_id" in query_string_params:
                pet_id = http_request.query["pet_id"]

                response = self.find_pet_use_case.find_by_id(pet_id=pet_id)

            elif "user_id" in query_string_params:
                user_id = http_request.body["user_id"]

                response = self.find_pet_use_case.find_by_user_id(user_id=user_id)
            else:
                response = self.find_pet_use_case.find_all_pets()

        else:
            http_error = HttpErrors.error_400()
            return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

        return HttpResponse(status_code=200, body=response["Data"])
