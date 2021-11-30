import pytest
from homework6.oop_2 import DeadlineError, Student, Teacher


def test_Teacher_attributes():
    """Test teacher attributes"""
    opp_teacher = Teacher('Daniil', 'Shadrin')
    assert opp_teacher.first_name == 'Daniil' and \
        opp_teacher.last_name == 'Shadrin'


def test_Student_attributes():
    """Test student attributes"""
    lazy_student = Student('Roman', 'Petrov')
    assert lazy_student.first_name == 'Roman' and \
        lazy_student.last_name == 'Petrov'


def test_deadline_exception_function(teacher, student):
    """Test raising of DeadlineError"""
    oop_hw = teacher.create_homework('Learn OOP', 0)
    with pytest.raises(DeadlineError):
        student.do_homework(oop_hw, 'I have done this hw')


def test_homework_done_class_attribute(teacher, student):
    """Test that homework_done attribute is
    the same for class and instance of class"""
    oop_hw = teacher.create_homework('Learn OOP', 1)
    result_1 = student.do_homework(oop_hw, 'I have done this hw')
    teacher.check_homework(result_1)
    temp_1 = teacher.homework_done

    teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2
