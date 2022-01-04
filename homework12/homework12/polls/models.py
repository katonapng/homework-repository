import datetime
from collections import defaultdict

import pytz
from django.db import models

utc = pytz.UTC


class DeadlineError(Exception):
    pass


class Homework(models.Model):
    text = models.CharField(max_length=30)
    deadline = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def __repr__(self) -> str:
        return super().__repr__()

    def is_active(self) -> bool:
        if not utc.localize(datetime.datetime.now()) <\
                datetime.timedelta(days=self.deadline) + self.created:
            raise DeadlineError


class Teacher(models.Model):
    homework_done = defaultdict(list)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def check_homework(self, homework_res):
        if len(homework_res.solution) >= 5:
            if homework_res not in self.homework_done[homework_res.homework]:
                self.homework_done[homework_res.homework].append(
                    (homework_res.author, self))
            return True
        return False

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

    def __repr__(self) -> str:
        return super().__repr__()

    @classmethod
    def reset_results(cls, homework_to_delete=None):
        if homework_to_delete is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework_to_delete)

    def create_homework(self, text: str, deadline: int) -> Homework:
        created = datetime.datetime.now()
        return Homework(text=text, deadline=deadline, created=created)


class Student(Teacher):
    def do_homework(self, homework: Homework, solution: str):
        try:
            homework.is_active()
        except DeadlineError:
            raise DeadlineError("You are late")
        return HomeworkResult(author=self, homework=homework,
                              solution=solution)


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ': ' + str(self.homework)

    def __repr__(self) -> str:
        return super().__repr__()

# Create your models here.
