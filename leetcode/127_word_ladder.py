import string
from typing import List


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = [(beginWord, 0)]
        wordSet = set(wordList)

        while len(queue) != 0:
            word, level = queue.pop(0)

            if word == endWord:
                return level + 1

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    target = word[:i] + c + word[i+1:]
                    if target in wordSet:
                        queue.append((target, level + 1))
                        wordSet.remove(target)

        return 0
