class Maths:
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a"""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent"""
        return base ** exponent

def main():
    # Example usage
    math = Maths()
    print("5 + 3 =", math.add(5, 3))
    print("10 - 4 =", math.subtract(10, 4))
    print("6 * 7 =", math.multiply(6, 7))
    print("15 / 3 =", math.divide(15, 3))
    print("2 ^ 3 =", math.power(2, 3))

if __name__ == "__main__":
    main() 