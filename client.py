import requests
import os
from urllib.parse import urljoin
import json

API_KEY = os.environ.get('ZUBIE_API_KEY', None)
CLIENT_ID = os.environ.get('ZUBIE_CLIENT_ID', None)


class RestAdapter(object):
    """Adapter for communicating with Zubie API"""

    def __init__(self, api_key=API_KEY, client_id=CLIENT_ID):
        self.base_url = 'https://api.zubiecar.com/api/v2/zinc/'
        self._api_key = api_key
        self._client_id = client_id
        self._headers = {'Zubie-Api-Key': api_key}
        self._params = {'client_id': client_id}

    def get(self, resource: str, *args, **kwargs) -> dict:
        """Base get method used for all api calls"""
        params = self._params.copy()  # Sets default parameters
        params.update(kwargs)  # Adds provided keyword arguments to the call
        url = urljoin(self.base_url, resource)
        return json.loads(requests.get(url=url, headers=self._headers, params=params).text)

    def get_devices(self, q=None) -> dict:
        """Lists all active and pending devices (vehicle connected hardware) in account."""
        resource = 'devices'
        return self.get(resource, q=q)

    def get_device(self, key: str) -> dict:
        """Get single device by key"""
        resource = 'device/{%s}' % key
        return self.get(resource)

    def get_groups(self, group_keys=None, show_inactive=False) -> dict:
        """Lists groups available in the account, based on the group permissions of the user.
        Groups are a way to provide hierarchical structure to account vehicles and restrict user permissions."""
        resource = 'groups'
        return self.get(resource, group_keys=group_keys, show_inactive=show_inactive)

    def get_vehicles(self, q=None, tag_keys=None, group_keys=None, cursor=None, size=None, expand=None) -> dict:
        """Lists Vehicles in account. Restricted based on API user's group permissions. :param q: Search vehicles by
        nickname or full VIN. :type q: str :param tag_keys: Restrict results to include only vehicles with these tag
        keys. Multiple tag values may be provided, treated as an OR in filter. :type tag_keys: str :param group_keys:
        Restrict results to include only vehicles that are members of these groups (or their descendants). :type
        group_keys: str :param cursor: The cursor string used for pagination, signifying the object ID where to start
        the results. :type cursor: str :param size: The number of results to return per call. Default 50 if not
        provided. :type size: str :param expand: Default: [] Items Enum:"tags" "groups" "devices" "last_trip"
        Optional list of expanded properties to include in results :type expand: str
        """
        resource = 'vehicles'
        return self.get(resource, q, tag_keys, group_keys, cursor, size, expand)

    def get_vehicle(self, vehicle_key: str) -> dict:
        """Retrieve a single vehicle by vehicle key"""
        resource = 'vehicle/{%s}' % vehicle_key
        return self.get(resource)

    def get_nearby_vehicles(self, lat: str, long: str, cursor=None, size=None) -> dict:
        """Get list of nearby vehicles, using a given GPS point. Restricted based on API user's group permissions.
        :param lat: Latitude of the point.
        :param long: Longitude of the point.
        :param: cursor: The cursor string used for pagination, signifying the object ID where to start the results.
        :type cursor: str
        :param size: The number of results to return per call. Default 5 if not provided
        :type size: str
        """
        resource = 'vehicles/nearby'
        return self.get(resource, lat, long, cursor, size)

    def get_trips(self, user_key=None, vehicle_key=None, started_after=None, started_before=None, tag_keys=None, cursor=None, size=None, expand=None) -> dict:
        resource = 'trips'
        return self.get(user_key, vehicle_key, started_after, started_before, tag_keys, cursor, size, expand)


if __name__ == '__main__':
    RA = RestAdapter()
    devices = RA.get_devices()
    groups = RA.get_groups()
    vehicles = RA.get_vehicles()
