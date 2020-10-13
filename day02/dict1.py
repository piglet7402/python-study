d = {'c': 3, 'a': 1, 'b': 2}
for key in d:
 print(key, end=' ')

for key in d:
 print(str(key) + ":" + str(d[key]), end=' ')

for key in d:
 print("{0}:{1}".format(key, d[key]), end=' ')

for key in d.keys():
 print("{0}:{1}".format(key, d[key]), end=' ')
 
for key, value in d.items():
 print("{0}:{1}".format(key, value), end=' ')