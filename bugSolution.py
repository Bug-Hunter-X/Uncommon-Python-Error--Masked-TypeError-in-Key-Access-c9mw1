def function_with_uncommon_bug_solution(data):
    try:
        key_value = data.get('key') #Use get to avoid KeyError
        if key_value is not None and isinstance(key_value,(int, float)): #check for type before operation
          result = key_value * 2
          return result
        else:
          return 0
    except:
        return None

# Example demonstrating the fixed function
data1 = {'key': 5}
data2 = {}
data3 = {'key': 'abc'}
data4 = {'key': 5.6}
print(function_with_uncommon_bug_solution(data1))  # Output: 10
print(function_with_uncommon_bug_solution(data2))  # Output: 0
print(function_with_uncommon_bug_solution(data3))  # Output: 0
print(function_with_uncommon_bug_solution(data4)) # Output: 11.2