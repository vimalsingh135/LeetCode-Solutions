class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)

        if s_len < total_len:
            return []

        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        result = []

        # Try each of the word_len possible starting offsets
        for i in range(word_len):
            left = i
            count = 0
            window = {}

            for j in range(i, s_len - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    # Too many of this word -> shrink from the left
                    while window[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Found a valid concatenation
                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # Word not in words at all -> reset window entirely
                    window = {}
                    count = 0
                    left = j + word_len

        return result