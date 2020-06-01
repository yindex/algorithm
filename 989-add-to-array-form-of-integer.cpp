#include <iostream>
#include <vector>

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
       vector<int> ad;
       while(K != 0) {
           ad.insert(ad.begin(), K%10);
           K/=10;
       }
       if (A.size() > ad.size())
            return bigAdd(A, ad);
       else
            return bigAdd(ad, A);
    }
    vector<int> bigAdd(vector<int> &A, vector<int> &B){
        int carry = 0;
        int pos = 0;
        for(pos = 0; pos < B.size(); pos++){
            A.at(A.size() - pos - 1) = A.at(A.size() - pos - 1) + B.at(B.size() - pos - 1) + carry;
            carry = A.at(A.size() - pos - 1) / 10;
            A.at(A.size() - pos - 1) = A.at(A.size() - pos - 1) % 10;
        }
        while(carry){
            if (pos >= A.size()) {
                A.insert(A.begin(), carry);
                carry = 0;
            } else {
                A.at(A.size() - pos - 1) = A.at(A.size() - pos - 1) + carry;
                carry = A.at(A.size() - pos - 1) / 10;
                A.at(A.size() - pos - 1) %= 10;
                pos++;
            }
        }
        return A;
    }
};
