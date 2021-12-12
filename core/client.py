from abc import ABC, abstractmethod
from urllib.parse import urljoin
import requests
import settings
import logging
import logging.config

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)

class Client(ABC):

    @property
    @abstractmethod
    def BASE_URL(self):
        ...

    @abstractmethod
    def get(self, *args, **kwargs):
        ...

    @abstractmethod
    def post(self):
        ...

    @abstractmethod
    def put(self, id_: int):
        ...

    @abstractmethod
    def delete(self, id_: int):
        ...


class RestClientV2(Client):
    BASE_URL = 'https://api.zubiecar.com/api/v2/zinc/'
    CLIENT_ID = settings.ZUBIE_CLIENT_ID
    API_KEY = settings.ZUBIE_API_KEY
    headers: dict = {'Zubie-Api-Key': API_KEY}
    params: dict = {'client_id': CLIENT_ID}

    def get(self, resource: str, **kwargs):
        params = self.params.copy()
        params.update(**kwargs)
        url = urljoin(self.BASE_URL, resource)
        logging.debug(url)
        return requests.get(url=url, headers=self.headers, params=params)

    def list(self):
        pass

    def post(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, id_: int):
        pass

    def delete(self, id_: int):
        pass


if __name__ == '__main__':
    rest_client = RestClientV2()
    response = rest_client.get('devices')