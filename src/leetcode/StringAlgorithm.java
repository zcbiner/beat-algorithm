package leetcode;

public class StringAlgorithm {
    /*给定两个分别由字母组成的字符串A和字符串B，字符串B的长度比字符串A短。
    请问，如何最快地判断字符串B中所有字母是否都在字符串A里？*/
    public boolean isStringContain(String str1, String str2) {
        int hash = 0;// 如果字符数超过了32个，会溢出。
        for (int i = 0; i < str1.length(); i++) {
            hash |= 1 << (str1.charAt(i) - 'A');
        }
        for (int i = 0; i < str2.length(); i++) {
            if ((hash & (1 << (str2.charAt(i) - 'A'))) == 0) {
                return false;
            }
        }
        return true;
    }
    /*****************************/

    /*回文，英文palindrome，指一个顺着读和反过来读都一样的字符串，比如madam、我爱我，这样的短句在智力性、趣味性和艺术性上都颇有特色，中国历史上还有很多有趣的回文诗。
    那么，我们的第一个问题就是：判断一个字串是否是回文？*/
    public static boolean isPalindrome(String str) {
        int i = 0;
        int j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    /*****************************/

    /*将字符串转换为整数*/
    public static int str2int(String str) {
        int result = 0;
        int i = 0;
        boolean negative = false;
        int len = str.length();
        if (len > 0) {
            char firstChar = str.charAt(0);
            if (firstChar < '0') {
                if (firstChar == '-') {
                    negative = true;
                } else if (firstChar != '+') {
                    throw new NumberFormatException("error");
                }
                if (len == 1) {
                    throw new NumberFormatException("error");
                }
                i++;
            }

            while (i < len) {
                result *= 10;
                result += Character.digit(str.charAt(i++), 10);
            }
        }
        return negative ? -result : result;
    }
    /*****************************/

    /*字符串全排列*/
    public static void permutation(char[] chars, int start, int end) {
        if (start == end) {
            for (int i = 0; i <= end; i++) {
                System.out.print(chars[i]);
                System.out.print(" ");
            }
            System.out.println();
        } else {
            for (int i = start; i <= end; i++) {
                char temp = chars[start];
                chars[start] = chars[i];
                chars[i] = temp;
                permutation(chars, start + 1, end);
                temp = chars[start];
                chars[start] = chars[i];
                chars[i] = temp;
            }
        }
    }

    public static void main(String[] args) {
        char[] test = new char[]{'a', 'h', 'd', 'f'};
        permutation(test, 0, test.length - 1);
    }
}
