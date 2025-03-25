import math

print("The general formula for a quadratic equation is: Ax^2 + Bx + C = 0")
a = float(input("Enter the value of 'A': "))
b = float(input("Enter the value of 'B': "))
c = float(input("Enter the value of 'C': "))

inner = (b**2) - 4 * a * c

if inner < 0:
    print("No real roots exist (Discriminant is negative).")
else:
    det = math.sqrt(inner)
    x1 = (-b + det) / (2 * a)
    x2 = (-b - det) / (2 * a)
    print(f"The roots of the quadratic equation are {x1:.2} and {x2:.2}.")
    print("--------------------------------")
    

print("Solving Ax^3 + Bx^2 + Cx + D = 0")


A = float(input("Enter A: "))
B = float(input("Enter B: "))
C = float(input("Enter C: "))
D = float(input("Enter D: "))

if A == 0:
    print("This is not a cubic equation!")
else:
    p = (3 * A * C - B ** 2) / (3 * A ** 2)
    q = (2 * B ** 3 - 9 * A * B * C + 27 * A ** 2 * D) / (27 * A ** 3)
    delta = (q / 2) ** 2 + (p / 3) ** 3  

    if delta > 0:
        u = (-q / 2 + delta ** 0.5) ** (1/3)
        v = (-q / 2 - delta ** 0.5) ** (1/3)
        x1 = u + v - B / (3 * A)
        print(f"One real root: x = {x1}")

    elif delta == 0:  
        if q == 0:  
            x1 = -B / (3 * A)
            print(f"Triple real root: x = {x1}")
        else:
            u = (-q / 2) ** (1/3)
            x1 = 2 * u - B / (3 * A)
            x2 = -u - B / (3 * A)
            print(f"Two or three real roots: x1 = {x1}, x2 = {x2}")

    else:
        r = (-p / 3) ** 0.5
        theta = (1 / 3) * (3.14159 + abs(q) / (2 * r ** 3)) ** 0.5
        x1 = 2 * r * (theta) ** 0.5 - B / (3 * A)
        x2 = 2 * r * (theta + 2 * 3.14159 / 3) ** 0.5 - B / (3 * A)
        x3 = 2 * r * (theta + 4 * 3.14159 / 3) ** 0.5 - B / (3 * A)
        print(f"Three real roots: x1 = {x1}, x2 = {x2}, x3 = {x3}")
        

print("Solving Ax^4 + Bx^3 + Cx^2 + Dx + E = 0")

A = float(input("Enter A: "))
B = float(input("Enter B: "))
C = float(input("Enter C: "))
D = float(input("Enter D: "))
E = float(input("Enter E: "))

if A == 0:
    print("This is not a quartic equation!")
else:
    b1 = B / A
    c1 = C / A
    d1 = D / A
    e1 = E / A

    P = c1 - (3/8) * b1**2
    Q = d1 - (1/2) * b1 * c1 + (1/8) * b1**3
    R = e1 - (1/4) * b1 * d1 + (1/16) * b1**2 * c1 - (3/256) * b1**4

    a_cubic = 1
    b_cubic = 2 * P
    c_cubic = P**2 - 4 * R
    d_cubic = -Q**2

    def solve_cubic(a, b, c, d):
        for y in range(-100, 101):
            if a * y**3 + b * y**2 + c * y + d == 0:
                return y
        return None

    Y = solve_cubic(a_cubic, b_cubic, c_cubic, d_cubic)

    if Y is None:
        print("Cannot find a simple real root for the cubic equation.")
    else:
        R1 = (P + Y) ** 0.5
        R2 = (P - Y) ** 0.5

        quad1_a, quad1_b, quad1_c = 1, R1, (Q / R1 if R1 != 0 else 0)
        quad2_a, quad2_b, quad2_c = 1, -R1, (-Q / R1 if R1 != 0 else 0)

        def solve_quadratic(a, b, c):
            disc = b**2 - 4*a*c
            if disc >= 0:
                x1 = (-b + disc**0.5) / (2*a)
                x2 = (-b - disc**0.5) / (2*a)
                return x1, x2
            else:
                return None

        roots1 = solve_quadratic(quad1_a, quad1_b, quad1_c)
        roots2 = solve_quadratic(quad2_a, quad2_b, quad2_c)

        final_roots = []
        if roots1:
            final_roots.extend([r - b1/4 for r in roots1])
        if roots2:
            final_roots.extend([r - b1/4 for r in roots2])

        print("The roots of the quartic equation are:", final_roots)
