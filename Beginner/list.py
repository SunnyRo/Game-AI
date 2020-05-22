def main():
    number = [i for i in range(1, 11)]
    print(number)
    even = [i for i in range(1, 11) if (i % 2) == 0]
    print("even = {}".format(even))
    odd = [i for i in range(1, 11) if (i % 2) == 1]
    print("odd = {}".format(odd))
    combine = [i for i in range(1, 11) if (i % 2) == 0 and i > 5]
    print("even and greater than 5 = {}".format(combine))
    square = [i ** 2 for i in range(1, 11)]
    print("square = {}".format(square))
    remainder = [i ** 2 % 11 for i in range(1, 11)]
    print("remainder = {}".format(remainder))
    movies = [
        ("citizen kane", 1941),
        ("spririted away", 2001),
        ("its a wonderful life", 1946),
        ("gattaca", 1997),
        ("no country for old men", 2007),
        ("rear window", 1954),
        ("the lord of the rings: the fellowship of the ring", 2001),
    ]
    moviesBefore2000 = [title for (title, year) in movies if year < 2000]
    print("movies before 2000 = {}".format(moviesBefore2000))
    A = [1, 3, 5, 7]
    B = [2, 4, 6, 8]
    cartesian_product = [(a, b) for a in A for b in B]
    print("cartesian_product = {}".format(cartesian_product))


if __name__ == "__main__":
    main()
