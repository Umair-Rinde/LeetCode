import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_DIR = os.path.join(BASE_DIR, "python")

def create_problem(name):
    path = os.path.join(PROBLEMS_DIR, name)
    os.makedirs(path, exist_ok=True)

    files = {
        "que.md": f"# {name}\n\nProblem description here.\n",
        "sln.py": "class Solution:\n    def solve(self):\n        pass\n",
        "test.py": "if __name__ == \"__main__\":\n    from sln import Solution\n    sol = Solution()\n",
    }

    for file, content in files.items():
        file_path = os.path.join(path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)

    print(f"Problem '{name}' created successfully")

def list_problems():
    if not os.path.exists(PROBLEMS_DIR):
        print("No problems found")
        return

    for p in sorted(os.listdir(PROBLEMS_DIR)):
        print(p)

def help():
    print("""
Usage:
  python manage.py new <problem_name>
  python manage.py list

Examples:
  python manage.py new 1.two_sum
  python manage.py new 3.longest_substring
  python manage.py list
""")

def main():
    if len(sys.argv) < 2:
        help()
        return

    command = sys.argv[1]

    if command == "new":
        if len(sys.argv) < 3:
            print("Please provide problem name")
            return
        create_problem(sys.argv[2])

    elif command == "list":
        list_problems()

    else:
        help()

if __name__ == "__main__":
    main()
