from solutions.pb_217 import containsDuplicate as f

class TestContainsDuplicate:
    def test_one(self):
        assert f([1,2,3,1]) == True

    def test_two(self):
        assert f([1,2,3,4]) == False

    def test_three(self):
        assert f([1,1,1,3,3,4,3,2,4,2]) == True