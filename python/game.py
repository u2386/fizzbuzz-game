#!/usr/bin/env python


def times(n):
    return lambda x: x % n == 0


def contains(n):
    return lambda x: n in str(x)


def and_(*predicates):
    def wrapped(n):
        result = True
        for pred in predicates:
            result &= pred(n)
        return result

    return wrapped


def always():
    return lambda _: True


def rule(predicate, action):
    def wrapped(*facts):
        if predicate(*facts):
            action(*facts)
            return True
        return False

    return wrapped


def any(*rules):
    def wrapped(*facts):
        for rule in rules:
            if not rule(*facts):
                continue
            return

    return wrapped


def all(*rules):
    def wrapped(*facts):
        for rule in rules:
            rule(*facts)

    return wrapped


def fizzbuzz(n):
    spec = any(
        rule(and_(times(3), times(5)), lambda _: print("fizzbuzz", end="")),
        rule(times(3), lambda _: print("fizz", end="")),
        rule(times(5), lambda _: print("buzz", end="")),
        rule(always(), lambda x: print(x, end="")),
    )
    spec = all(rule(contains("7"), lambda _: print("whizz", end="")), spec)

    for i in range(1, n):
        print(i, "", end="")
        spec(i)
        print()


def main():
    fizzbuzz(100)


if __name__ == "__main__":
    main()
