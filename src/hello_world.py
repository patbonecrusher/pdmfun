from ppadb.client import Client as AdbClient

def hello_world():
    return "hello world"

def hello_world2():
    return "hello world2"

def main():
    """MY MAIN"""
    client = AdbClient(host="127.0.0.1", port=5037)
    print(client.version())

    print(hello_world())
    print(hello_world2())

if __name__ == "__main__":
    # execute only if run as a script
    main()
