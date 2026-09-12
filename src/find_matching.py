#!/usr/bin/env python3

def find_matching(L, pattern):
    pass


def main():
    words = ["sensitive", "engine", "rubbish", "comment"]
    pattern = "en"
    matches = find_matching(words, pattern)
    print(f"Words containing '{pattern}': {matches}")
    print([words[i] for i in matches])


if __name__ == "__main__":
    main()
