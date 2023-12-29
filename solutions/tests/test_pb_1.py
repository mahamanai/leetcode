from solutions.pb_1 import twoSum2 as f

class TestTwoSum:
    def test_one(self):
        assert f([2,7,11,15], 9) == [0, 1]

    def test_two(self):
        assert f([3,2,4], 6) == [1, 2]

    def test_three(self):
        assert f([3,3], 6) == [0, 1]