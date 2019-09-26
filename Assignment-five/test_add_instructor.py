
import pytest
from add_instructor import add_instructor
def test_success_add_instructor():
"""
A system admin can add someone as an instructor if their user type is 'instructor'
"""
assert add_instructor('Sean Goggins', 'instructor')
def test_fail_add_instructor():
"""
A system admin will not be able to add a user as an instructor if their type is not 'instructor'
"""
assert add_instructor('Sweta Praharaj', 'student') == False
