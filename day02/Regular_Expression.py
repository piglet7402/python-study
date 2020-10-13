import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina ', 'West virginia?']
def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()
        results.append(string)
    return results

print(clean_strings(states))