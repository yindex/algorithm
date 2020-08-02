class Solution {
public:
    int reverse(int x) {
        int max = 0x7fffffff, min = 0x80000000; 
        long rs=0;
        while (x) {
            rs = rs * 10 + x % 10;
            x /=10;
        }
        return rs > max || rs < min ? 0: rs;
    }
};
