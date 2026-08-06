class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict={}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if(s in strs_dict):
                strs_dict[s].append(strs[i])
            else:
                strs_dict[s] = [strs[i]]
        return (list( strs_dict.values()))
