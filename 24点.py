import itertools
import random

card_map = {
    'A': 1,
    'J': 11,
    'Q': 12,
    'K': 13,
}


def generate_cards():
    return [random.randint(1, 13) for _ in range(4)]


def input_cards():
    """从用户输入获取牌面"""
    while True:
        try:
            user_input = input("请输入4张牌（用空格分隔，如: A 5 J 8）: ")
            cards_input = user_input.upper().split()

            if len(cards_input) != 4:
                print("请输入恰好4张牌!")
                continue

            cards = []
            for card in cards_input:
                if card in card_map:
                    cards.append(card_map[card])
                elif card.isdigit() and 2 <= int(card) <= 10:
                    cards.append(int(card))
                else:
                    raise ValueError(f"无效的牌面: {card}")

            return cards

        except ValueError as e:
            print(f"输入错误: {e}")
        except KeyboardInterrupt:
            print("\n程序退出")
            exit()


def display_cards(cards):
    """将数字转换为牌面显示"""
    reverse_map = {v: k for k, v in card_map.items()}
    display_list = []
    for card in cards:
        if card in reverse_map:
            display_list.append(reverse_map[card])
        else:
            display_list.append(str(card))
    return display_list


def evaluate_expression(expr):
    try:
        result = eval(expr)
        return abs(result - 24) < 0.0001
    except ZeroDivisionError:
        return False


def find_24_expressions(cards):
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

    return expressions_set


def solve_24(cards):
    card_display = display_cards(cards)
    print(f"抽到的牌: {' '.join(card_display)}")
    print(f"对应的数字: {cards}")

    expressions_set = find_24_expressions(cards)

    if expressions_set:
        print("找到以下表达式可以得到24:")
        for i, expr in enumerate(expressions_set, 1):
            # 将表达式中的数字替换为牌面显示
            formatted_expr = expr
            for num in cards:
                if num in card_map.values():
                    letter = [k for k, v in card_map.items() if v == num][0]
                    formatted_expr = formatted_expr.replace(str(num), letter)
            print(f"{i}. {formatted_expr}  (原始: {expr})")
    else:
        print("无法得到24。")

    return expressions_set


def main():
    """主程序"""
    print("24点游戏")

    while True:
        print("\n选择模式:")
        print("1. 随机生成牌")
        print("2. 手动输入牌")
        print("3. 退出")

        choice = input("请输入选择 (1/2/3): ")

        if choice == '1':
            cards = generate_cards()
            solve_24(cards)

        elif choice == '2':
            cards = input_cards()
            solve_24(cards)

        elif choice == '3':
            print("游戏结束!")
            break

        else:
            print("无效选择，请重新输入!")


if __name__ == "__main__":
    main()