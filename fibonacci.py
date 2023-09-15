#9. Write a program to sum the first 50 fibonacci sequence

def fibonacci(n):
    fibonacci_list = [0, 1]
    count = 0

    for i in fibonacci_list:
        next_term = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_term)
        count += 1
        if count == n-2:
            break
    print(f"This is the sum of the first 50 fibonacci, \n{fibonacci_list[-1]}")


def main():
    fibonacci(n = 50)



if __name__ == "__main__":
    main()