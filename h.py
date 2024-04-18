
from main import func


def function_received_by_h(func):
    # convert from bytes 
    
    result_in_bytes = func()
    result = list(result_in_bytes)
    return result


print(function_received_by_h(func))