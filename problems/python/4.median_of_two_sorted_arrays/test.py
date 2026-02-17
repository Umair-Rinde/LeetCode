if __name__ == "__main__":
    from sln import Solution
    sol = Solution()
    # Example test cases
    print(sol.solve([1, 3], [2]))        # Output: 2.0
    print(sol.solve([1, 2], [3, 4]))     # Output: 2.5
    print(sol.solve([0, 0], [0, 0]))     # Output: 0.0
    print(sol.solve([], [1]))             # Output: 1.0