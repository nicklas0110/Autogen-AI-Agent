import ollama

def generate_code(task_description):
    response = ollama.generate(
        model='codegemma',
        prompt=task_description,
        options={
            'num_predict': 128,
            'temperature': 0,
            'top_p': 0.9,
            'stop': ['<|file_separator|>'],
        },
    )
    # Extract the code from the 'response' key
    if 'response' in response:
        return response['response']  # The generated code is here
    else:
        raise ValueError(f"Unexpected response format: {response}")

def save_code_to_file(code, filename="generated_code.py"):
    # Remove Markdown code block delimiters
    code = code.strip('`').replace("```python", "").replace("```", "").replace("python", "").strip()

    # Remove everything after '**Example Usage:**' if it exists
    if "**Example Usage:**" in code:
        code = code.split("**Example Usage:**")[0].strip()

    # Save the cleaned code to a file
    with open(filename, "w") as file:
        file.write(code)

    print(f"Code has been saved to {filename}")

def main():
    task = "Write a Python function that takes a list of numbers and returns the average of the numbers."
    code = generate_code(task)
    print("Generated Code:\n", code)

    # Save the code to a file
    save_code_to_file(code)

if __name__ == "__main__":
    main()
