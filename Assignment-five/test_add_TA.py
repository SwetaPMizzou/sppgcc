import pytest

from add_TA import  add_TA


def test_successful_remove_student():
    """
    Instructors can add students as TA if they are in the list of id list
    """
    assert add_TA(12345)


def test_failed_remove_student():
    """
    Instructors will not be able to add students as TA if they are not in the id list
    """
    assert add_TA(12345678) == False
