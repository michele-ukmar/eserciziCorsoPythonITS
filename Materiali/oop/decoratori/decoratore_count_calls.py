from decorators import count_calls

@count_calls
def function_example():
    print("Hello World!")

function_example()
function_example()
function_example()