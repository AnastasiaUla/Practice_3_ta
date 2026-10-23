def recognize_mpa(word: str) -> bool:
    stack = []
    extra_b = False
    seen_b = False

    for symbol in word:
        if symbol == "a":
            if seen_b:
                return False

            stack.append("A")

        elif symbol == "b":
            seen_b = True

            if stack:
                stack.pop()
            else:
                extra_b = True

        else:
            return False

    return len(word) > 0 and (len(stack) > 0 or extra_b)


def main():
    tests = [
        "a",
        "b",
        "aaa",
        "bbb",
        "aab",
        "abb",
        "aabbb",
        "ab",
        "aabb",
        "aaabbb",
        "ba",
        "",
    ]

    for word in tests:
        result = "Accept" if recognize_mpa(word) else "Reject"
        print(f"{word!r:12} -> {result}")


if __name__ == "__main__":
    main()
