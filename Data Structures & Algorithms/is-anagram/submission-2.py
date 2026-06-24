class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        for i in range(0,len(s)):
            if s[i] not in hash1:
                hash1[s[i]]=1
            else:
                hash1[s[i]]+=1
        for j in range(0,len(t)):
            if t[j] not in hash2:
                hash2[t[j]]=1
            else:
                hash2[t[j]]+=1
        if hash1==hash2:
            return True
        else:
            return False
        

        