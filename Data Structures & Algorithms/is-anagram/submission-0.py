class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sort_string(s: str):
            s = list(s)
            s.sort()
            return s
        s = sort_string(s)
        t = sort_string(t)
        return s == t