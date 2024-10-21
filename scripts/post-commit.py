import pylint.epylint as lint
import os

# Define the Pylint checks you selected
checks = 'C0301,C0103,R0903,W0611,C0411'

# Get all Python files in the root directory
def get_python_files():
    return [f for f in os.listdir('.') if f.endswith('.py')]

# Run Pylint on each Python file and print violations
def run_pylint():
    python_files = get_python_files()
    for file in python_files:
        print(f"\nRunning Pylint on {file}...\n")
        (stdout, stderr) = lint.py_run(f"{file} --disable=all --enable={checks}", return_std=True)
        print(stdout.getvalue())

if __name__ == '__main__':
    run_pylint()
