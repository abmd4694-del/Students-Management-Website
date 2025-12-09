# Usage:
# python manage.py shell
# >>> exec(open('load_sample.py').read())
from student_app.models import Student
if Student.objects.count() == 0:
    sample = [
        ('Abhiram MD', 'abhiram@example.com', 21, 'CSE'),
        ('Rahul Menon', 'rahul@example.com', 22, 'ECE'),
        ('Sneha Nair', 'sneha@example.com', 20, 'IT')
    ]
    for name,email,age,dept in sample:
        Student.objects.create(name=name,email=email,age=age,department=dept,image='students/default.jpg')
    print('Sample students created')
else:
    print('Students already exist')
