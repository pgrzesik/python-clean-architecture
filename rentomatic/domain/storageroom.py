from rentomatic.shared.domain_model import DomainModel


class StorageRoom:
    def __init__(self, code, size, price, latitude, longitude):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    @classmethod
    def from_dict(cls, dictionary):
        room = cls(**dictionary)
        return room


DomainModel.register(StorageRoom)
