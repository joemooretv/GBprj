test_list = ['H', 'e', 'l', 'L', 0, 'H', 0]
test_tuple = tuple(test_list)
test_set = set(test_tuple)
test_frozen = frozenset({1, 2, 2, 4, 2})
test_dict = {'name': 'Paul', 'age': 27}

types_list = [25,
              'Test line',
              0,
              '0',
              True,
              None,
              b'hello',
              test_list,
              test_tuple,
              test_set,
              test_frozen,
              test_dict
              ]

for elem in types_list:
    print(type(elem))
