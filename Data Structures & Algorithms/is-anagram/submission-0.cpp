class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> repo;
        if(s.length() != t.length())
        {
            return false;
        }
        for(char i : s)
        {
            repo[i]++;
        }

        for(char j : t)
        {
           if(repo.find(j) == repo.end() || repo[j] == 0)
           {
                return false;
           }
           else
           {
                repo[j]--;
                if(repo[j] == 0)
                {
                    repo.erase(j);
                }
           }
        }
        if(!repo.empty())
        {
            return false;
        }
        else
            return true;

    }
};
