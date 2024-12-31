def function_with_uncommon_bug(data):
    try:
        result = data['key'] * 2  # Access a key that might not exist
        return result
    except KeyError:
        return 0
    except TypeError:
        return None

# Example demonstrating the bug
data1 = {'key': 5}
data2 = {}
data3 = {'key': 'abc'}
print(function_with_uncommon_bug(data1))  # Output: 10
print(function_with_uncommon_bug(data2))  # Output: 0
print(function_with_uncommon_bug(data3))  # Output: None