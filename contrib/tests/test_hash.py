from contrib.hash import RandomHash


def test_random_hash_call():
    hasher = RandomHash(length=8)
    result = hasher()
    assert len(result) == 8
    assert isinstance(result, str)
