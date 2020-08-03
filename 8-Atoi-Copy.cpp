//copy and study
class DFA {
private:
    string state = "start";
    unordered_map<string, vector<string>> table = {
            {"start", {"start", "sign", "num", "end"} },
            {"sign", {"end", "end", "num", "end"} },
            {"num", {"end", "end", "num", "end"} },
            {"end", {"end", "end", "end", "end"}}
    };

    int getState(char c) {
        if (c == ' ') return 0;
        if (c == '+' || c == '-') return 1;
        if (isdigit(c)) return 2;
        return 3;
    }

public:
    long long ans = 0;
    int sign = 1;
    bool get(const char c) {
        state = table[state][getState(c)];
        if (state == "num") {
            ans = ans * 10 + c - '0';
            ans = sign==1 ? min(ans,(long long)INT_MAX): min(ans,-(long long)INT_MIN);
        } else if (state == "sign"){
            if (c == '-') sign = -1;
        }
        return state != "end";
    }
};

class Solution {
public:
    int myAtoi(string str) {
        DFA dfa;
        for(char c:str)
            if (!dfa.get(c)) break;
        return dfa.sign*dfa.ans;
    }
};
