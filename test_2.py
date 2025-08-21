from example2 import reverse_string

def test_reverse_normal():
    assert reverse_string("Joban") == "naboj"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_palindrome():
    assert reverse_string("mall") == "llam"

def test_reverse_numbers():
    assert reverse_string("12345") == "54321"
