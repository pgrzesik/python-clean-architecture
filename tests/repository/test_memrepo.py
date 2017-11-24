import pytest

from rentomatic.repository.memrepo import MemRepo
from rentomatic.shared.domain_model import DomainModel


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
    def second_storageroom(self):
        return {
            'code': '123456',
            'size': 400,
            'price': 59,
            'longitude': '0.0999999',
            'latitude': '51.7541111'
        }

    @pytest.fixture
    def storagerooms(self, first_storageroom, second_storageroom):
        return [first_storageroom, second_storageroom]

    @pytest.fixture
    def repo(self, storagerooms):
        return MemRepo(storagerooms)

    def _assert_results(self, domain_models_list, data_list):
        assert len(domain_models_list) == len(data_list)
        assert all(isinstance(dm, DomainModel) for dm in domain_models_list)
        assert set(dm.code for dm in domain_models_list) == \
            set(d['code'] for d in data_list)

    def test_list_without_parameters(self, repo, storagerooms):
        assert repo.list() == storagerooms

    def test_list_with_unknown_filter_key(self, repo):
        with pytest.raises(KeyError):
            repo.list(filters={'name': 'value'})

    def test_list_with_unknown_filter_operator(self, repo):
        with pytest.raises(ValueError):
            repo.list(filters={'price__in': [20, 30]})

    def test_list_with_price_filter(
            self, repo, second_storageroom, first_storageroom):
        self._assert_results(
            repo.list(filters={'price': 59}), [second_storageroom])
        self._assert_results(
            repo.list(filters={'price__lt': 40}), [first_storageroom])
