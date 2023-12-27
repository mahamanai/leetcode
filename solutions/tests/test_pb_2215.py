from solutions.pb_2215 import findDifference as f

class TestFindDifference:
    def test_one(self):
        assert f([1,2,3], [2,4,6]) == [[1,3],[4,6]]

    def test_two(self):
        assert f([1, 2, 3, 3], [1, 1, 2, 2]) == [[3],[]]