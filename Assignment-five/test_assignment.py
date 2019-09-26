import pytest

from assignment
 import assign_student_grade


def test_successful_assignment():
    """
    Instructors can remove students that are in their class by their student ID
    """
    assert assign_student_grade(50)


def test_failed_assignment():
    """
    Instructors will not be able to remove students that are not enrolled in their class
    """
assert assign_student_grade(20) 
