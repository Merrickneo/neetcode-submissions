class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make use of a dictionary to store the unique strings
        # we've seen so far
        # for each of them sort them in lexicographic order using .sort
        seen = {}
        for item in strs:
            sorted_str = "".join(sorted(item))
            if sorted_str not in seen:
                seen[sorted_str] = []
            seen[sorted_str].append(item)
        output = []
        for item in seen.values():
            output.append(item)
        return output