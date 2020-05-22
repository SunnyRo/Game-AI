def main():
    g = lambda x: 3 * x + 1
    full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
    print(full_name(" leonhard", "euler"))
    scifi_authors = [
        "Isaac Asimove",
        "Ray brabury",
        "Robert Heinlein",
        "Arthus C. clarke",
        "Frank Herbert",
        "Orson Scott card",
        "Douglas Adams",
    ]
    scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
    print(scifi_authors)


def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx = c"""
    return lambda x: a * x ** 2 + b * x + c


if __name__ == "__main__":
    main()
