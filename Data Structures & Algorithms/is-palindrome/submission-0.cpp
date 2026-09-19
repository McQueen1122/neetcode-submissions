class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;

        while (right >= left) {
            if (!isalnum(s[right])) {
                right--;
                continue;
            }
            if (!isalnum(s[left])) {
                left++;
                continue;
            }
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            right--;
            left++;
        }
        return true;    
    }
};