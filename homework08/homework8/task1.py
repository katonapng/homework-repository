from collections import defaultdict


class KeyValueStorage:
    def __init__(self, file) -> None:
        self.custom_dict = defaultdict(str)
        with open(file, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if value.lstrip('-').isdigit():
                    value = int(value)
                if key.lstrip('-').isdigit():
                    raise ValueError("Incorrect type of key value")
                if not hasattr(KeyValueStorage, key):
                    setattr(self, key, value)
                    self.custom_dict[key] = value

    def __getitem__(self, key):
        return self.custom_dict[key]
