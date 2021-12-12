from abc import ABC


class Adapter(ABC):
    ...


class DeviceAdapter(Adapter):

    def __init__(self, **kwargs):
        pass