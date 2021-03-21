class Solution:
    def contains(self, str1, str2):
        if str1 is None or str2 is None or len(str1) < len(str2):
            return False
        
        # 字符串不可变。转换成list操作。
        list1 = list(str1)
        list1_size = len(list1)

        for i in range(list1_size):
            # 进行一次循环移位
            temp = list1[0]
            for j in range(1, list1_size):
                list1[j - 1] = list1[j]
            list1[list1_size - 1] = temp
        
            print(list1)
            temp_str = "".join(list1)
            if str2 in temp_str:
                return True
        
        return False

if __name__ == "__main__":
    str1 = "AABCD"
    str2 = "CDAA"
    result1 = Solution().contains(str1, str2)
    print(result1)