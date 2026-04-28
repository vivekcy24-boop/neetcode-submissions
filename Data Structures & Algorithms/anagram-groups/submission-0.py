class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        
        for word in strs:
            key = ''.join(sorted(word))  # sorted key
            
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(word)
        
        return list(anagram_map.values())