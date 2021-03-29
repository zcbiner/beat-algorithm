class Solution:
    def contains(self, str1, str2):
        if str1 is None or str2 is None or len(str1) < len(str2):
            return False

        str1_str1 = str1 + str1

        if str2 in str1_str1:
            return True
        else:
            return False

if __name__ == "__main__":
    str1 = "AABCD"
    str2 = "CDAA"
    result1 = Solution().contains(str1, str2)
    print(result1)