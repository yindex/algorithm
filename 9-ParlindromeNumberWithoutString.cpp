class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        if (x <= 9) return true;
        int degree = 1;
        while (x / degree >= 10) {
            degree *= 10;
        }
        std::cout << degree << std::endl;
        while (x != 0) {
            if ((x / degree) != (x % 10)) return false;
            x %= degree;
            x /= 10;
            degree /= 100;
        }
        return true;
    }
};
