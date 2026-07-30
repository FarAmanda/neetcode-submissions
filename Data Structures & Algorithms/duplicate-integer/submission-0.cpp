class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> x;
        
        for(int i : nums)
        {
            if(x.find(i) == x.end())
            {
                x[i] = 1;
            }
            else return true;
        }
        return false;
    }
};
