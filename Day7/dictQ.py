# Question.1/2: remove duplicates and tell there frequency
""" a = [10,10,10,10,20,20,20,30,30,40,40,50]
d={}
for i in a:
    if i in d:
        d[i]+=1
        print(f"if--->{d[i]}, {i}")
    else:
        d[i]=1
        print(f"else--->{d[i], i}")
print(d) """

# Question.3: leetCode 771- jewels and stones

""" class Solution:
    def jewels_and_stones(self, jewels: str, stones: str) :
        d = {}

        # Count frequency of stones
        for i in stones:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        count = 0

        # Count frequency of jewels
        for i in d:
            if i in jewels:
                count += d[i]

        return count


s = Solution()
print(s.jewels_and_stones(jewels="zz", stones="ZZ")) """

# Question.4: leetCode 1832- Check if the sentence is pangram

""" class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for i in sentence:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        
        if len(d)>=26:
            return True
        else:
            return False


s = Solution()
print(s.checkIfPangram(sentence="wertyuioplkjhgfdsazxcvbnm")) """

# Question.5: leetCode 2351- first letter to appear twice

""" class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d.keys():
                return i
            else:
                d[i]=1

s = Solution()
print(s.repeatedCharacter(s="abccbaacz")) """

# Question.6: leetCode 1748- sum of unique elements

""" class Solution:
    def sumOfUnique(self, nums: list) -> int:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        ans=0
        for i in d:
            if d[i] == 1:
                ans+=i
        return ans

s = Solution()
print(s.sumOfUnique(nums=[1,2,3,2])) """