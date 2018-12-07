from playground import version_happiness


def test_version_happiness():
    assert version_happiness().startswith(':')
