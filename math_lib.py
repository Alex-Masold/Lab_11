#Сидоров Александр Алексеевич
from Point import Point


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def distanse(p1: Point, p2: Point) -> float:
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


def quadratic_solver(a:int, b:int, c:int) -> float:
    delta = b**2 - 4 * a * c
    if delta < 0:
        None
    elif delta == 0:
        return (-b / (2 * a),)
    else:
        return ((-b + delta**0.5) / (2 * a), (-b - delta**0.5) / (2 * a))

def geometric_sum(a, r, n) -> float:
    return a * (1 - r ** n) / (1 - r)