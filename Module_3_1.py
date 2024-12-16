calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    tuple_string = (len(string), string.upper(), string.lower())
    return tuple_string

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [x.lower() for x in list_to_search]
    if string in list_to_search:
        contains = True
    else:
        contains = False
    return contains

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)