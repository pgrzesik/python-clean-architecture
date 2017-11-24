import pytest

from rentomatic.repository.memrepo import MemRepo


class TestMemrepo:
    @pytest.fixture
    def first_storageroom(self):
        return {
            'code': '123',
            'size': 215,
            'price': 39,
            'longitude': '-0.0999999',
            'latitude': '51.7541111'
        }

    @pytest.fixture
    def second_storageroom():
        return {
            'code': '123456',
            'size': 400,
            'price': 59,
            'longitude': '0.0999999',
            'latitude': '51.7541111'
        }

    @pytest.fixture
    def storagerooms(first_storageroom, second_storageroom):
        return [first_storageroom, second_storageroom]

    def test_list_without_parameters(self, storagerooms):
        repo = MemRepo(storagerooms)

        assert repo.list() == storagerooms
