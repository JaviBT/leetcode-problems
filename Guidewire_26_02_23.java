// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public static void main(String[] args) {
        System.out.println(String.format("RETURN: %d", solution(123)));
    };

    public static int solution(int N) {
        // Turn N into a string and split it into an array of characters to get the digits
        String[] digits = Integer.toString(N).split("");
        // Calculate the sum of the digits of N (sum_digits_N)
        int sum_digits_N = 0;
        for (String digit : digits) {
            sum_digits_N += Integer.parseInt(digit);
        }
        System.out.println(sum_digits_N);
        int i = 1;
        while (i < 99999) {
            // Calculate the sum of the digits of i (sum_digits_i)
            int sum_digits_i = 0;
            String[] digits_i = Integer.toString(i).split("");
            for (String digit : digits_i) {
                sum_digits_i += Integer.parseInt(digit);
                System.out.println(sum_digits_i);
            }
            // If the sum of the digits of i is twice the sum of the digits of N, return i
            if (sum_digits_i == 2 * sum_digits_N) {
                return i;
            }
            i++;
        }
        return -1;
    };
}

class Solution2 {
    public static void main(String[] args) {
        System.out.println(solution2(1,2,3,4));
    };

    public static int solution2(int A, int B, int C, int D) {
        int valid_times = 0;
        int[] digits = {A, B, C, D};
        Arrays.sort(digits);
        // Check all possible times
        for (int i = 0; i < 24; i++) {
            for (int j = 0; j < 60; j++) {
                String clock = String.format("%02d%02d", i, j);
                int[] clock_digits = new int[4];
                for (int k = 0; k < 4; k++) {
                    clock_digits[k] = Integer.parseInt(clock.substring(k, k + 1));
                }
                Arrays.sort(clock_digits);
                if (Arrays.equals(digits, clock_digits)) {
                    valid_times++;
                }
            }
        }
        return valid_times;
    }
}