from django.core.management.base import BaseCommand
from courses.models import course, lesson , types
from datetime import timedelta

# run python manage.py populate_db to add to database
# enter courses names here 
course1 = 'algebra'
course2 = 'calculus'

# enter lessons details here
class Command(BaseCommand):
    help = 'Populate the database with test courses and lessons'

    def handle(self, *args, **kwargs):
        soft_course = course.objects.create(
            title=course1,
            description=f"A beginner-friendly course on {course1}",
            price=0,
            type=types.soft
        )

        hard_course = course.objects.create(
            title=course2,
            description=f"An in-depth guide to {course2}",
            price=100,
            type=types.hard
        )

        lesson.objects.create(
            course=soft_course,
            title="lesson1",
            description=f"Learn fundamentals and start with {course1} ",
            duration=timedelta(minutes=30),
            position=1
        )

        lesson.objects.create(
            course=soft_course,
            title="lesson2",
            description=f"Get better with complex and advanced concepts of {course1}",
            duration=timedelta(minutes=45),
            position=2
        )

        lesson.objects.create(
            course=hard_course,
            title="lesson1",
            description=f"Learn fundamentals and start with {course2} ",
            duration=timedelta(hours=1),
            position=1,
            content="Defining and using Django models."
        )

        lesson.objects.create(
            course=hard_course,
            title="lesson2",
            description=f"Get better with complex and advanced concepts of {course2}",
            duration=timedelta(hours=1, minutes=30),
            position=2,
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
