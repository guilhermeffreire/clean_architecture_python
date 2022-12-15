from typing import Type
from src.domain.use_cases import RegisterUser
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.main.interfaces import RoutesInterface


class RegisterUserController(RoutesInterface):
    def __init__(self, register_user_use_case: Type[RegisterUser]):
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if http_request.body:
            body_params = http_request.body.keys()

            if "name" and "password" in body_params:
                name = http_request.body["name"]
                password = http_request.body["password"]

                response = self.register_user_use_case(name=name, password=password)
            else:
                response = {"Success": False, "Data": None}

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            http_error = HttpErrors.error_422()

            return HttpResponse(status_code=http_error, body=http_error["body"])

        return HttpResponse(status_code=200, body=response["Data"])
