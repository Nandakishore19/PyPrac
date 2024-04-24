import pytest
from sample import add

def test_add_num():
    assert add(1,2)==3
    assert add(1,-1) == 0
    assert add(-1,-1) == -2
def test_add_string():
    assert add("a","b") == "ab"

def test_add_list():
    assert add([1],[2]) == [1,2]

@pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])], ids=["num","String","List"])
def test_add_all(a,b,c):
    assert add(a,b) == c