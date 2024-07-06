def f(n):
    """
    int -> (Bool -> Bool)
    """
    binary = bin(n)[2:]
    return lambda b: binary[0] == "1" if b else binary[1] == "1"

def g(n):
    """
    int -> (Bool -> Bool) -> Bool
    """
    binary = bin(n)[2:]
    def output(func):
        if func == f(0): return binary[0] == "1"
        elif func == f(1): return binary[1] == "1"
        elif func == f(2): return binary[2] == "1"
        return binary[3] == "1"
    return output
