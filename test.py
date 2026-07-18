from app import greet

def test_greet():
    assert greet("Jenkins") == "Hello, Jenkins! Welcome to Jenkins."
    print("Test passed!")

if __name__ == "__main__":
    test_greet()
