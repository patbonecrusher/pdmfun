from pyramda import curry

@curry
def add(x:int, y:int) -> int:
    return x+y

def hello_world():
    return "hello world"

def main():
    """MY MAIN"""
    print(hello_world())

if __name__ == "__main__":
    # execute only if run as a script
    main()