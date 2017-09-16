import leetcode.StringAlgorithm;

import java.util.Arrays;

/**
 * Created by zhong on 2017/8/4.
 */
public class MainTest {

    public static void main(String[] args) {
        String str1 = "ABCDEFGH";
        String str2 = "CDEI";
//        System.out.printf("result: " + isStringContain(str1, str2));

        System.out.printf("" + StringAlgorithm.str2int("-2365"));
    }

    private static boolean isStringContain(String str1, String str2) {
        int hash = 0;
        char[] chars1 = str1.toCharArray();
        char[] chars2 = str2.toCharArray();
        for (int i = 0; i < chars1.length; i++) {
            hash |= (1 << (chars1[i] - 'A'));
        }
        for (int i = 0; i < str2.length(); i++) {
            if ((hash & (1 << (chars2[i] - 'A'))) == 0) {
                return false;
            }
        }
        return true;
    }

    public boolean isEven(int num) {
        return num % 2 == 0;
    }

}
