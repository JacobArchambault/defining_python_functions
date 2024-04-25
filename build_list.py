def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items

# 1) Write a `build_list` function that takes an item and a number to include in a list
assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"

# 2) Ensure it provides a default count of 1
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"