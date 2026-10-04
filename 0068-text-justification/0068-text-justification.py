class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(words)

        while i < n:
            j = i
            line_len = 0
            # pack greedily: line_len = letters only, (j - i) = minimum spaces
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            count = j - i
            gaps = count - 1
            spaces = maxWidth - line_len

            if j == n or gaps == 0:
                # last line or single word: left-justify
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                q, r = divmod(spaces, gaps)
                parts = []
                for k in range(gaps):
                    parts.append(words[i + k])
                    parts.append(" " * (q + (1 if k < r else 0)))
                parts.append(words[j - 1])
                line = "".join(parts)

            res.append(line)
            i = j

        return res