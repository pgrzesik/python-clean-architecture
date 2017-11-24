from rentomatic.domain.storageroom import StorageRoom


class MemRepo:
    SUPPORTED_OPERATORS = ['eq', 'gt', 'lt']

    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key += '__eq'

        key, operator = key.split('__')

        if operator not in self.SUPPORTED_OPERATORS:
            raise ValueError('Operator {} not supported'.format(operator))

        operator = '__{}__'.format(operator)

        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        if not filters:
            return self._entries

        result = []
        result.extend(self._entries)

        for key, value in filters.items():
            result = [e for e in result if self._check(e, key, value)]

        return [StorageRoom.from_dict(r) for r in result]
