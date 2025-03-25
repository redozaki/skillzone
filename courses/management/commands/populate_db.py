from django.core.management.base import BaseCommand
from courses.models import course, lesson , types
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test courses and lessons'

    def handle(self, *args, **kwargs):
        soft_course = course.objects.create(
            title="Introduction to Python",
            description="A beginner-friendly course on Python programming.",
            price=0,
            type=types.soft
        )

        hard_course = course.objects.create(
            title="Advanced Django",
            description="An in-depth guide to Django development.",
            price=100,
            type=types.hard
        )

        lesson.objects.create(
            course=soft_course,
            title="lesson1",
            description="Learn variables, loops, and functions.",
            duration=timedelta(minutes=30),
            position=1,
            content="Introduction to Python programming."
        )

        lesson.objects.create(
            course=soft_course,
            title="lesson2",
            description="Lists, dictionaries, tuples, and more.",
            duration=timedelta(minutes=45),
            position=2,
            content="Understanding built-in data structures in Python."
        )

        lesson.objects.create(
            course=hard_course,
            title="lesson1",
            description="Learn about Django's ORM and models.",
            duration=timedelta(hours=1),
            position=1,
            content="Defining and using Django models."
        )

        lesson.objects.create(
            course=hard_course,
            title="lesson2",
            description="Learn about class-based views and templates.",
            duration=timedelta(hours=1, minutes=30),
            position=2,
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
