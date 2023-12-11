def square(n):
    i = 0
    while i<=n:
        yield 2**i
        i+=1

if __name__ == "__main__":
    inp = int(input())
    for i in square(inp):
        print(i)
        