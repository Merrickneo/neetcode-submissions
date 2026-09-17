class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for string in strs:
            char_count = [0] * 26
            for char in string:
                spot = ord(char) - ord('a') 
                char_count[spot] += 1
            key = tuple(char_count)
            if key in word_dict:
                word_dict[key].append(string)
            else:
                word_dict[key] = [string]
        return [x for x in word_dict.values()]            
        