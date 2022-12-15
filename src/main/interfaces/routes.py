from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RoutesInterface(ABC):
    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception("Should implement method: route")
