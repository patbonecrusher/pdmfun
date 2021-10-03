
from src.hello_world import hello_world, hello_world2



def test_hello_world():
    assert hello_world() == "hello world"


def test_hello_world2():
    assert hello_world2() == "hello world"

