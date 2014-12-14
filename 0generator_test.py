def test_numbers():
    for n in [2, 4, 6, 8, 10]:
        yield n_greater_than_zero, n

def n_greater_than_zero(n):
    assert n > 0
