
typedef struct Node {
    int value;
    int tag;

    Node(int v, int t) {
        this->value = v;
        this->tag = t;
    }
};

class Solution {
public:
    vector<Node> merge(vector<vector<int>>& nums) {
        vector<Node> data;
        while (true) {
            int max = -0xfffffff;
            int tag = -1;
            for (int i = 0; i < nums.size(); i++) {
                if (!nums.at(i).empty() && nums.at(i).back() > max) {
                    max = nums.at(i).back();
                    tag = i;
                }
            }
            if (tag == -1) break;
            data.emplace_back(max, tag);
            nums.at(tag).pop_back();
        }
        return data;
    }
    vector<int> slide(vector<Node> data, int tagCounts) {
        int windowLeft = 0;
        int windowRight = 0;
        int windowSize = data.front().value - data.back().value + 1;
        int windowTagCount = 0;
        vector<int> windowTag(tagCounts, 0);
        vector<int> window(2, 0);

        for(int index = 0; index < data.size(); index++) {
            Node node = data.at(index);
            windowTag.at(node.tag)++;//类型++
            windowTagCount += windowTag.at(node.tag) == 1 ? 1 : 0; //新类型加入

            while (windowTag.at(data.at(windowLeft).tag) > 1) {
                windowTag.at(data.at(windowLeft).tag)--;
                windowLeft++;
            }

            windowRight = index;

            if (windowTagCount == tagCounts) {
                if (windowSize >= (data.at(windowLeft).value - data.at(windowRight).value)) {
                    windowSize = data.at(windowLeft).value - data.at(windowRight).value;
                    window.at(0) = data.at(windowRight).value;
                    window.at(1) = data.at(windowLeft).value;;
                }
            }
        }
        return window;
    }
    vector<int> smallestRange(vector<vector<int>>& nums) {
        return this->slide(this->merge(nums), nums.size());
    }
};
