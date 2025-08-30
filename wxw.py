import itertools
import random


def generate_cards():
    return [random.randint(1, 13) for _ in range(4)]


def evaluate_expression(expr):
    try:
        result = eval(expr)
        return abs(result - 24) < 1e-6
    except ZeroDivisionError:
        return False


def main():
    cards = generate_cards()
    print(f"抽到的牌点数: {cards}")

    operators = ['+', '-', '*', '/']
    expressions_set = set()

    for num_perm in itertools.permutations(cards):
        for op_comb in itertools.product(operators, repeat=3):
            a, b, c, d = num_perm
            op1, op2, op3 = op_comb

            expressions = [
                f"(({a} {op1} {b}) {op2} {c}) {op3} {d}",
                f"({a} {op1} ({b} {op2} {c})) {op3} {d}",
                f"{a} {op1} (({b} {op2} {c}) {op3} {d})",
                f"{a} {op1} ({b} {op2} ({c} {op3} {d}))",
                f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
            ]

            for expr in expressions:
                if evaluate_expression(expr):
                    expressions_set.add(expr)

    if expressions_set:
        print("找到以下表达式可以得到24:")
        for expr in expressions_set:
            print(expr)
    else:
        print("无法得到24。")


if __name__ == "__main__":
    main()