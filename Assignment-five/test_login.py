import pytest

from instructorLogin import instructorLogin

def test_login_success():
    """
    The instructor can login with a password value of 'password'
    """
    assert instructorLogin( 'instructor', 'instructor' ) == True

def test_login_fail():
    """
    The instructor login will fail with an invalid password
    """
    assert instructorLogin( 'instructor', 'student' ) == False
