from abc import ABC, abstractmethod

from core.model import Model


class RestAdapter(ABC):

    @property
    @abstractmethod
    def BASE_URL(self):
        ...

    @abstractmethod
    def get(self, *args, **kwargs):
        ...

    @abstractmethod
    def post(self, obj: Model):
        ...

    @abstractmethod
    def put(self, id_: int):
        ...

    @abstractmethod
    def delete(self, id_: int):
        ...


class RestAdapterV2(RestAdapter):
    BASE_URL = 'https://api.zubiecar.com/api/v2/zinc'

    def get(self):
        raise NotImplementedError

    def post(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, id_: int):
        pass

    def delete(self, id_: int):
        pass


if __name__ == '__main__':
    RestAdapterV2()
