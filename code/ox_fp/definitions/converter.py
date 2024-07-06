"""
Solution to the converter problem.
"""

def convert(n: int) -> str:
    """
    Converts n (0 <= n < 10**6) to a string
    representation of the number in English.

    Args:
        n (int): integer between 0 and 10**6.
    
    Returns:
        str: string representation of the number in English.

    Raises:
        ValueError: if n is not between 0 and 10**6.        
    """
    endings = ['zero', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    powers_of_10 = ['', 'thousand', 'million']
    if n < 20:
        return endings[n]
    elif n < 100:
        if n % 10 == 0:
            return tens[n // 10 - 2]
        return tens[n // 10 - 2] + ' ' + endings[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return endings[n // 100] + ' hundred'
        return endings[n // 100] + ' hundred ' + convert(n % 100)
    for i in range(2, len(powers_of_10)):
        if n < 10**(3*i):
            if n % 10**(3*(i-1)) == 0:
                return convert(n // 10**(3*(i-1))) + ' ' + powers_of_10[i-1]
            return convert(n // 10**(3*(i-1))) + ' ' \
                    + powers_of_10[i-1] + ' ' \
                    + convert(n % 10**(3*(i-1)))
    raise ValueError("n must be less than 10**6")

if __name__ == "__main__":
    print(convert(0)) # zero
    print(convert(1)) # one
    print(convert(10)) # ten
    print(convert(11)) # eleven
    print(convert(20)) # twenty
    print(convert(21)) # twenty one
    print(convert(100)) # one hundred
    print(convert(101)) # one hundred one
    print(convert(1000)) # one thousand
    print(convert(1001)) # one thousand one
    print(convert(10000)) # ten thousand
    print(convert(10001)) # ten thousand one
    print(convert(100000)) # one hundred thousand
    print(convert(100001)) # one hundred thousand one
