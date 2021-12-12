from abc import ABC, abstractmethod


class RestAdapter(ABC):

    @property
    @abstractmethod
    def BASE_URL(self):
        ...

    def get(self):
        ...


class RestAdapterV2(RestAdapter):
    BASE_URL = 'https://api.zubiecar.com/api/v2/zinc'

    def get(self):
        super().get()


if __name__ == '__main__':
    RestAdapterV2()
