import cmath

def quadratic_solver(a, b, c):
    if a == 0:
        raise ValueError("The coefficient 'a' must not be zero.")

    # Calculate the discriminant
    discriminant = cmath.sqrt(b * b - 4 * a * c)

    # Calculate the two solutions
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)

    return (x1, x2)

if __name__ == "__main__":
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    try:
        x1, x2 = quadratic_solver(a, b, c)
        print(f"The solutions are: x1 = {x1}, x2 = {x2}")
    except ValueError as e:
        print(e)
