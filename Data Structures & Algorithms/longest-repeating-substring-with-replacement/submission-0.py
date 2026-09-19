class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left, right = 0, 0
        max_freq = 0
        output = 0
        while right < len(s):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
            right += 1
        return output
                

        