class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        anagrams = []

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]
        
        for h in hashmap:
            anagrams.append(hashmap[h])
        
        return anagrams


                    
