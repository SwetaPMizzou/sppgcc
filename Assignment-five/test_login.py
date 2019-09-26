import pytest

from instructorLogin import instructorLogin

def test_login_success():
    """
    The Admin user can login with a password value of 'password'
    """
    assert instructorLogin( 'instructor', 'instructor' ) == True

def test_login_fail():
    """
    The Admin user login will fail with an invalid password
    """
    assert instructorLogin( 'instructor', 'student' ) == False
