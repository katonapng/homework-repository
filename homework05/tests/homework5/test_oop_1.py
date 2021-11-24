from homework5.oop_1 import Student, Teacher


def test_Teacher_attributes():
    """Testing positive case """
    teacher = Teacher('Din', 'Djarin')
    assert teacher.first_name == 'Din' and teacher.last_name == 'Djarin'


def test_Student_attributes():
    """Testing positive case """
    student = Student('Baby', 'Yoda')
    assert student.first_name == 'Baby' and student.last_name == 'Yoda'


def test_create_homework_attributes(teacher):
    expired_homework = teacher.create_homework('Lift a rock', 0)

    assert str(expired_homework.deadline) == '0:00:00' and \
           expired_homework.text == 'Lift a rock'


def test_create_homework_as_func(teacher):
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('Defend yourself from clones', 5)
    assert str(oop_homework.deadline) == '5 days, 0:00:00'


def test_active_homework(teacher, student):
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('Defend yourself from clones', 5)
    assert student.do_homework(oop_homework) is oop_homework


def test_expired_homework(teacher, student):
    expired_homework = teacher.create_homework('Lift a rock', 0)
    assert student.do_homework(expired_homework) is None
