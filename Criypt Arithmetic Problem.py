import itertools
def solve_cryptarithmetic():
    n = int(input("Enter number of input words (2 or 3): "))
    if n not in [2, 3]:
        print("Only 2 or 3 input words are supported.")
        return
    words = [input(f"Enter word {i+1}: ").strip().upper() for i in range(n)]
    result = input("Enter result word: ").strip().upper()
    letters = list(set(''.join(words + [result])))
    if len(letters) > 10:
        print("Too many unique letters (more than 10).")
        return
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[w[0]] == 0 for w in words + [result]):
            continue
        def word_to_num(w): return int(''.join(str(mapping[c]) for c in w))
        total = sum(map(word_to_num, words))
        if total == word_to_num(result):
            print("\nSolution Found:")
            for k in sorted(mapping): print(f"{k} = {mapping[k]}")
            expression = ' + '.join(str(word_to_num(w)) for w in words)
            print(f"\n{expression} = {word_to_num(result)}")
            return
    print("\nNo solution found.")
solve_cryptarithmetic()
