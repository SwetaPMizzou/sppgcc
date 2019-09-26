import pytest

from delete_assignment import  delete_assignment


def test_successful_delete_assignment():
    """
    Instructors can delete an assignment if it has already been uploaded
    """
    assert delete_assignment('assignment1')


def test_failed_delete_assignment():
    """
    Instructors will not be able to delete assignment if it has not been uploaded
    """
    assert delete_assignment('assignment4') == False
