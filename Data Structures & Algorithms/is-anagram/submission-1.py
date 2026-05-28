class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen1 = []
        seen2 = []

        for char in s:
            seen1.append(char)

        for char in t:
            seen2.append(char)

        return sorted(seen1) == sorted(seen2)
        