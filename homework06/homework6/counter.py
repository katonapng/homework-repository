"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


@classmethod
def reset_instances_counter(cls):
    temp = cls._count
    cls._count = 0
    return temp


@classmethod
def my_init(cls):
    cls._count += 1


@classmethod
def get_created_instances(cls):
    return cls._count


def instances_counter(cls):
    setattr(cls, '_count', 0)
    setattr(cls, '__init__', my_init)
    setattr(cls, 'get_created_instances',  get_created_instances)
    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
