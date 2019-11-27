def foldl(iterable, seed, f):
    accum = seed
    for elem in iterable:
        accum = f(accum, elem)
    return accum


test_list = ["hola", "como", "te", "va"]
expected_result = 12

assert foldl(test_list, 0, lambda seed, elem: seed + len(elem)) == 12
print("True!")
