from collections import defaultdict


def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList) # for O(1) lookup time

    if endWord not in wordSet:
        return []

    parents= defaultdict(list)
    #BFS start
    level = {beginWord}

    found = False

    while level and not found:
        next_level = set()

        for word in level:
            wordSet.discard(word)

        for word in level:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:] # word from 0 to upto i but excluding i , word from i+ 1 to end
                    if new_word in wordSet:
                        if new_word == endWord:
                            found = True
                        next_level.add(new_word)

                        parents[new_word].append(word)

        level = next_level

    if not found:
        return []

    #backtracking to build paths
    res = []

    def backtrackWords(word, path):

        if word == beginWord:
           res.append(path[::-1])
           return

        for p in parents[word]:
           backtrackWords(p, path + [p])

    backtrackWords(endWord, [endWord])
    return res


def main():
    beginWords = ["hit", "hit", "aab", "cat", "spin"]
    endWords = ["cog", "cog", "abb", "dog", "spot"]
    wordLists = [
        ["hot", "dot", "dog", "lot", "log", "cog"],
        ["hot", "dot", "dog", "lot", "log"],  # no cog
        ["aab", "abb", "aaa", "aba", "bbb"],
        ["cot", "cog", "dog", "dat", "dot"],
        ["spin", "spit", "spat", "spot", "span"]
    ]

    for i in range(len(beginWords)):
        print(i + 1, "\tBegin Word:", beginWords[i])
        print("\tEnd Word:", endWords[i])
        print("\tWord List:", wordLists[i])

        result = findLadders(beginWords[i], endWords[i], wordLists[i])
        print("\nShortest Ladders:", result)
        print("-" * 100)

if __name__ == "__main__":
    main()