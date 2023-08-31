from slither import Slither

s = Slither('.')

print('Printing derived contracts of A')
print(next(filter(lambda x: x.name == 'A', s.contracts)).derived_contracts)

print('Printing name of above derived contract')
print(next(filter(lambda x: x.name == 'A', s.contracts)).derived_contracts[0].name)

print('Printing references of A.a_main')
print(next(filter(lambda x: x.name == 'A', s.contracts)).functions[0].references)
