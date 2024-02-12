def smart_div(func):
    def inner(a, b):
        if b == 0:
            print("Cannot Divide By Zero!")
            return None
        return func(a, b)
    return inner

@smart_div
def div(a, b):
    return a / b

# Example usage:
result = div(6, 2)
print("Result:", result)

result = div(6, 0)
print("Result:", result)
