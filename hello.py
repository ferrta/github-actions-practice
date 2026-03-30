def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    result = greet("DevOps")
    print(result)
    
    assert result == "Hello, DevOps!"
