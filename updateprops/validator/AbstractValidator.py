from abc import ABC, abstractmethod


class AbstractValidator(ABC):

    @abstractmethod
    def validate(self):
        pass

    @staticmethod
    def something():
        print("do something")
