from testproject.lib import try_me

def test_try_me():
    assert try_me(2) == "two"
    assert try_me(2.5) == "Please insert a valid integer between 0 and 20"
    assert try_me("Fake test") == "Please insert a valid integer between 0 and 20"
