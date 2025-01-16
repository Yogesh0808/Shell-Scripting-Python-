## Lists in Python

Lists are a fundamental data type in Python used to store collections of elements. They are mutable, meaning their contents can be changed after they are created. Lists are ordered sequences, meaning elements have a specific order, and can be accessed by their index.

**Key Points**

* Lists are used to store collections of elements of any data type.
* Lists are mutable, meaning their elements can be added, removed, or modified after creation.
* Lists are ordered sequences, meaning elements have a specific order and can be accessed by their index (starting from 0).

**List vs. Tuples**

Lists are generally more memory-intensive than tuples due to their dynamic size. Tuples, on the other hand, have a fixed size and cannot be resized or modified after creation. This makes tuples more memory-efficient.

**List Functions**

* `append(element)`: Adds an element to the end of the list.
* `pop()`: Removes and returns the last element of the list. By default, `pop()` removes the last element, but you can specify an index to remove an element at a specific position.
* `insert(index, element)`: Inserts an element at a specified index in the list.
* `index(element)`: Returns the index of the first occurrence of an element in the list. Raises a `ValueError` if the element is not found.
* `remove(element)`: Removes the first occurrence of an element from the list. Raises a `ValueError` if the element is not found.

**List Operations Example**

```python
fruits = ["apple", "banana", "cherry"]

# Get the length of the list
list_length = len(fruits)
print(f"Number of fruits: {list_length}")  # Output: Number of fruits: 3

# Remove an element from the list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

### Heterogeneous Data Types
Lists can store elements of different data types within the same list.

```python
mixed_list = [10, "Hello", 3.14]
print(mixed_list)  # Output: [10, "Hello", 3.14]