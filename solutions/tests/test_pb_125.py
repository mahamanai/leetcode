from solutions.pb_125 import is_palindrome2 as f

class TestIsPalindrome:
    def test_one(self):
        assert f('A man, a plan, a canal: Panama') == True
    
    def test_two(self):
        assert f('race a car') == False

    def test_three(self):
        assert f(' ') == True