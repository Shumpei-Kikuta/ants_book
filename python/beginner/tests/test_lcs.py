from src.lcs import exec_lcs

def test_lsc1():
    n = 4
    m = 4
    s = "abcd"
    t = "becd"
    assert exec_lcs(s, t, n, m) == 3

def test_lsc2():
    n = 6
    m = 4
    s = "abkecd"
    t = "becd"
    assert exec_lcs(s, t, n, m) == 4

def test_lsc3():
    n = 1
    m = 1
    s = "a"
    t = "a"
    assert exec_lcs(s, t, n, m) == 1
