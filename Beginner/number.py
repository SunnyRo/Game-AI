
def main():
    a = 5
    print("type a")
    print(type(a))
    b = 5.3
    print("type b")
    print(type(b))
    c = 5 - 5j
    print("type c")
    print(type(c))
    print("real part {}".format(c.real))
    print("imaginary part {}".format(c.imag))

if __name__ == "__main__":
    main() 