# Last updated: 23/07/2026, 10:59:20
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Step 1: Length check
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        # Step 2: Traverse
        for c, w in zip(pattern, words):
            
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w
            
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c
        
        return True