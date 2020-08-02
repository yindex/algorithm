
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        vector<string> data(numRows);
        int row = 0;
        int slash = false;
        for (int i = 0; i < s.length(); i++) {
            data.at(row) += s.at(i);

            if (row == numRows - 1){
                slash = true;
            }
            if (row == 0) {
                slash = false;
            }

            if (!slash) {
                row++;
            } else {
                row--;
            }
        }
        string rs;
        for (int i = 0; i < numRows; i++) rs+= data.at(i);
        return rs;
    }
};
