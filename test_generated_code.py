import unittest
import ast

#load the generated function
def load_function_from_file(filename="generated_code.py"):
    with open(filename, "r") as file:
        tree = ast.parse(file.read())
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):  # Find the first function definition
                func_name = node.name
                namespace = {}
                exec(compile(tree, filename, 'exec'), namespace)
                return namespace[func_name]
    raise ValueError("No function found in generated_code.py")

# Test class
class TestGeneratedCode(unittest.TestCase):
    def test_average_function(self):
        # Load the function dynamically
        function = load_function_from_file()
        
        # Test the function with a sample input
        result = function([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)

    def test_average_empty_list(self):
        # Ensure the function handles an empty list gracefully
        function = load_function_from_file()
        with self.assertRaises(ZeroDivisionError):  # Expect a ZeroDivisionError
            function([])

    def test_average_negative_numbers(self):
        # Test with negative numbers
        function = load_function_from_file()
        result = function([-1, -2, -3, -4, -5])
        self.assertEqual(result, -3.0)

if __name__ == "__main__":
    unittest.main()
