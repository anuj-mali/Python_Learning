import pytest

from source.school import Classroom, Teacher, Student, TooManyStudents

# Assuming your_module contains the provided classes and exceptions

@pytest.fixture
def empty_classroom():
    teacher = Teacher("Professor Snape")
    students = []
    course_title = "Potions"
    return Classroom(teacher, students, course_title)

@pytest.fixture
def full_classroom():
    teacher = Teacher("Professor McGonagall")
    students = [Student(f"Student{i}") for i in range(1, 11)]
    course_title = "Transfiguration"
    return Classroom(teacher, students, course_title)

def test_add_student(empty_classroom):
    new_student = Student("Harry Potter")
    empty_classroom.add_student(new_student)
    assert len(empty_classroom.students) == 1
    assert empty_classroom.students[0] == new_student

def test_add_student_raises_exception(full_classroom):
    with pytest.raises(TooManyStudents):
        new_student = Student("Hermione Granger")
        full_classroom.add_student(new_student)

def test_remove_student(full_classroom):
    student_name = "Student3"
    full_classroom.remove_student(student_name)
    assert len(full_classroom.students) == 9
    assert all(student.name != student_name for student in full_classroom.students)

def test_change_teacher(empty_classroom):
    new_teacher = Teacher("Professor Dumbledore")
    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher == new_teacher

# Parameterized test to cover multiple scenarios
@pytest.mark.parametrize("initial_students, expected_count", [
    ([], 0),
    ([Student("Ron Weasley")], 1),
    ([Student(f"Student{i}") for i in range(1, 6)], 5),
])
def test_initial_student_count(empty_classroom, initial_students, expected_count):
    empty_classroom.students = initial_students
    assert len(empty_classroom.students) == expected_count
