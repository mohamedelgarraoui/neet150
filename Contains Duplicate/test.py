from main import Solution


def test_solution():
    sol = Solution()

    assert sol.hasDuplicate([1, 2, 5, 7]) == False
    assert sol.hasDuplicate([1, 1, 4]) == True