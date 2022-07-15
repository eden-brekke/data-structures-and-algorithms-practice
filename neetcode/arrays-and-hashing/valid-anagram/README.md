# Valid Anagram

Given two strings 's' and 't', check if they are anagrams of each other. If they are return True and if they are not return False

## Examples

**1**
Input: s = anagram, t = granama
Output: True

**2**
Input: s = rat, t = car
Output: False

## Thought Process
So I'm thinking you can use a list here, loop through the first string "s" and add each character to a list. After that you'll want to loop through the second string "t" and check if each character is in the list, if it's not in the list then you can return false, if you make it through the loop without hitting that condition then you can return true.  
There is a flaw to this method because of edge cases, of duplicate letters.  
For example s = Cat and t = tacat  
This would actually still produce a true result which isn't true. I think to get around this you would want to use a dictionary instead.  
With this method each character would be a key and the value would be the number. So.  
Loop through first string "s" and add each character to a dictionary with the character being the key and the value being "1" IF the character is already a key within the dictionary, update the value of that key by 1.  
Then loop through the second string "t" and check if the key is in the dictionary, if it is then decrease the value by 1 and if the value of the key reaches -1 then return false. if any values remain above 0 then return false. if all values are 0 then return true.  

```python
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
```