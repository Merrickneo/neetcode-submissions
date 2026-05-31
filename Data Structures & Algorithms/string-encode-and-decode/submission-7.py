class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return None
        return "ascii".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == None:
            return []
        output = s.split("ascii")
        return output
