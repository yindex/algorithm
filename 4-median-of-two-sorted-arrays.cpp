class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int i = 0;
        int j = 0;
        int left, right;
        if ((nums1.size() + nums2.size()) % 2 == 0) {
            left = (nums1.size() + nums2.size()) / 2 - 1;
            right = (nums1.size() + nums2.size()) / 2;
        } else {
            right = left = (nums1.size() + nums2.size()) / 2;
        }
        int step = 0;
        double mid = 0;
        while (i < nums1.size() && j < nums2.size()) {
            double temp = 0;
            if (nums1[i] < nums2[j]) {
                temp = nums1[i];
                i++;
            } else {
                temp = nums2[j];
                j++;
            }

            if (step == left) {
                mid += temp;
            }
            if (step == right) {
                mid += temp;
            }
            step++;
        }
        if (step <= right){
            while (i < nums1.size()) {

                if (step == left) {
                    mid += nums1[i];
                }
                if (step == right) {
                    mid += nums1[i];
                }
                i++;
                step++;

            }

            while (j < nums2.size()) {


                if (step == left) {
                    mid += nums2[j];
                }
                if (step == right) {
                    mid += nums2[j];
                }
                step++;
                j++;

            }
        }
        return mid/2.0;
    }
};