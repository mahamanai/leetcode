from solutions.pb_242 import is_anagram3 as f

class TestIsAnagram:
    def test_one(self):
        assert f('anagram', 'nagaram') == True

    def test_two(self):
        assert f('rat', 'car') == False
    
    def test_three(self):
        assert f('ccac', 'aacc') == False