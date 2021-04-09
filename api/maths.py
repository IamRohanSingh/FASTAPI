if __name__ == "__main__":
    def fibonacci(number):

        if number<0:
            print("invalid")
        elif number==0:
            return 0
        elif number==1 :
            return 1
        else:
            return (fibonacci(number-1) + fibonacci(number-2))

    def factorial(n):
        return 1 if (n==1 or n==0) else n * factorial(n - 1)


