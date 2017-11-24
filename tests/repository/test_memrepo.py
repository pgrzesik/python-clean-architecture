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

    @pytest.fixture
    def repo(self, storagerooms):
        return MemRepo(storagerooms)

    def test_list_without_parameters(self, repo, storagerooms):
        assert repo.list() == storagerooms

    def test_list_with_unknown_filter_key(self, repo):
        with pytest.raises(KeyError):
            repo.list(filters={'name': 'value'})
