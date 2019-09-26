import pytest

from assignment
 import assign_student_grade


def test_successful_assignment():
    """
    Instructors assigns grade if score is greater than 40.
    """
    assert assign_student_grade(50)


def test_failed_assignment():
    """
 Instructors will not be able to assign grade if score is below 40.
    """
assert assign_student_grade(20) 
