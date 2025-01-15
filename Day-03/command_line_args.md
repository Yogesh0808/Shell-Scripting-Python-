# Command Line Arguments in Python

Command line arguments allow users to pass values to a script when executing it from the command line or terminal. These arguments enable dynamic behavior and flexibility in programs without hardcoding values.

## Realtime Use Case Examples

Command line arguments are often used in real-world scenarios, such as:

1. **AWS IAM Management**: Passing the AWS IAM user ID as an argument when automating tasks related to user or policy management.
2. **Mathematical Operations**: Demonstrating basic arithmetic operations (addition, subtraction, multiplication) by passing numbers as arguments.
3. **Dynamic Configuration**: Allowing users to specify configuration values (e.g., filenames, options) directly when running a script.

Instead of hardcoding values or always using arguments, **modules** and **environment variables** can offer better alternatives for reusable and secure code.

---

## Using Command Line Arguments in Python

Python provides the `sys` module to access command line arguments via the `sys.argv` list:

```python
import sys

# Example: Reading operation type and numbers from arguments
operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
else:
    result = 'Invalid operation'

print(f'Result: {result}')

Execution Example:

bash
Copy code
python script.py add 10 5
# Output: Result: 15
Using Python Modules and Package Management
Instead of manually handling functionality in scripts, you can leverage Python’s extensive library of modules.

The Python Package Index (PyPI)
PyPI is a repository of software for the Python programming language. You can find, install, and publish packages using pip (Python’s package installer).

Installing a Package Using pip
bash
Copy code
pip install requests
Using a Module in Your Script
python
Copy code
import requests
response = requests.get('https://api.example.com')
print(response.status_code)
Environment Variables
Environment variables are used to store sensitive information, such as API tokens, passwords, and database URLs. This prevents exposing sensitive data in your code.

Setting an Environment Variable (Linux/Mac)
bash
Copy code
export API_KEY='your_api_key_here'
Accessing Environment Variables in Python
python
Copy code
import os
api_key = os.getenv('API_KEY')
if api_key:
    print('API key loaded successfully.')
else:
    print('API key not found.')
```

### Advantages of Using Environment Variables and Modules
- Security: Keeps sensitive information out of source code.
- Reusability: Modules encapsulate logic that can be reused across different scripts.
- Maintainability: Easier to manage and update configurations and dependencies.

By integrating these techniques, you create more robust, maintainable, and secure Python programs.

This preserves the correct syntax and formatting for use in a markdown file. Copy it into your `.md` file directly!





