# File Operations

File operations such as reading, writing, and deleting files are essential tasks that can be performed using various scripting languages. Below is a detailed overview of these operations and how they can be handled using shell scripting and Python.

## Shell Scripting for File Operations

*If you want to **read**, **write**, or **delete** a file, you need to know shell scripting.*

### Key Concepts

- **Shell**: Used to handle files in Linux-based systems.
- **Powershell**: Used for handling files in Windows-based systems.

### Challenges

- You must maintain separate scripts for Linux (Shell Scripting) and Windows (Powershell Scripting).

### Best Practice

Using **Python** is recommended for file operations because it supports both Linux and Windows, eliminating the need for separate scripts.

## File Operations in Python

Python provides built-in functions to perform file operations such as reading and writing files.

### Common File Operations

1. **Open a File**

   ```python
   with open("/path/to/file") as file:
       # Perform file operations

2. **Read a File**

Read Entire File
```python
content = file.read()
```
3. Read All Lines
```python
lines = file.readlines()
```
4. **Read a Single Line**
```python
line = file.readline()
```
5. **Write to a File**
```python
with open("/path/to/file", "w") as file:
    file.write("Your content here")
```

## Updating Configuration Files Example
Below is an example of updating the server.conf file to change the value of max_connections from 200 to 500.

1. Steps
Read the File Use the read() method to read the file's content.
```
python

with open("server.conf", "r") as file:
    lines = file.readlines()
```
2. Modify the Content Update the required configuration by modifying the list of lines.

```python
updated_lines = []
for line in lines:
    if "max_connections" in line:
        updated_lines.append("max_connections = 500\n")
    else:
        updated_lines.append(line)
```

3. Write Back the Changes Open the file in write mode and save the updated content.

```python
with open("server.conf", "w") as file:
    file.writelines(updated_lines)
```

### Advantages of Using Python
- Cross-platform support (Linux and Windows).
- Simple and efficient file handling with built-in functions.
