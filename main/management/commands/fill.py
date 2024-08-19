from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Andrew', 'last_name': 'Tate'},
            {'first_name': 'Tristan', 'last_name': 'Tate'},
            {'first_name': 'Sanya', 'last_name': 'Belch'},
            {'first_name': 'Robert', 'last_name': 'Patison'}

        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create =[]
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(students_for_create)