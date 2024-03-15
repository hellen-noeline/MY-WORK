random=int(input())
def generate_numbers():
    return random.randint(1, 10), random.randint(1, 10)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def main():
    for _ in range(5):
        num1, num2 = generate_numbers()
        operation = random.choice(list(operations.keys()))

        result = operations[operation](num1, num2)

        print(f"Calculate: {num1} {operation} {num2}")

        user_answer = float(input("Your answer: "))

        if user_answer == result:
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {result}")

if __name__ == "__main__":
    main()