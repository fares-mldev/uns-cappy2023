


def test_property_recursive(n):
    str_n = str(n)
    n_digits = len(str_n)

    def check_property(index):
        if index == n_digits:
            return True

        a = int(str_n[:n_digits - index])
        b = int(str_n[:n_digits - index][-1])

        passed = a % b == 0

        if not passed:
            return False
        else:
            return check_property(index + 1)

    return check_property(0)

numbers=(362,168)

for n in numbers:
    print(f'{n} { "passed" if test_property_recursive(n) else "didnt pass"}')