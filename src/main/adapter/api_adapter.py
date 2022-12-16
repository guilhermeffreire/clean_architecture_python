from typing import Type
from src.main.interfaces import RoutesInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    http_request = HttpRequest(body=request.json)
    response = api_route.route(http_request)

    return response
