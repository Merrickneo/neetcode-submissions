class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        hashmap to store the characters that are currently in the substring we are evaluating
        pointers to manipulate the window
        - prioritise moving the right
        - if we see a duplicate, we move the left + 1 (hashmap to see)
        + decrement that char count by 1

        Time complexity: O(n) process each character at most once
        Space complexuty: O(n) all could be unique
        '''
        left, right = 0, 0
        seen = {}
        n = len(s)
        max_length = 0
        while left <= right and right < n:
            while seen.get(s[right], 0) != 0:
                seen[s[left]] -= 1
                left += 1
            seen[s[right]] = seen.get(s[right], 0) + 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length


        