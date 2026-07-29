class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyMap = {}
        for char in s:
            if char not in frequencyMap:
                frequencyMap[char] = 1
            else:
                frequencyMap[char]+=1
        
        for char in t:
            if char not in frequencyMap:
                return False
            else:
                frequencyMap[char] -=1
        for char,freq in frequencyMap.items():
            print(freq)
            if freq !=0:
                return False
        return True    