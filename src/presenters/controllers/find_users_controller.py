from typing import Type
from src.domain.use_cases import FindUsers
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors

class FindUsersController:
    def __init__(self, find_users_use_case: Type[FindUsers]):
        self.find_users_use_case = find_users_use_case


    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params:
                user_id = http_request.query["user_id"]
                response = self.find_users_use_case.find_by_id(user_id=user_id)
            else:
                response = self.find_users_use_case.find_all_users()

            if not response:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()

                return HttpResponse(status_code=http_error, body=http_error["body"])

            return HttpResponse(status_code=200, body=response["Data"])

        http_error=HttpErrors.error_400()

        return HttpResponse(status_code=http_error, body=http_error["body"])


