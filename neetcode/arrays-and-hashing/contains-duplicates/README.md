# Contains Duplicates

Given an array of integers return a boolean indicating whether there is a duplicate within the array (appearing at least twice) True is so, False if not. 

## Examples

**Example 1** 

```python
Input: nums = [1,2,3,1]
Output: True
```

**Example 2** 

```python
Input: nums = [1,2,3]
Output: False
```

**Example 3**

```python
Input: nums = [1,1,1,2,2,2,3,3,3]
Output: True
```

## Approaches

Off the top of my head my first thought is to use a set.  
For Loop through the given list, nums and check if each num is in the set, if it is then you can return true, if it is not then you can add the num to the set. If we exit the for loop without hitting the return true, we can safely return false as there were no duplicates. 

```python
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num) 
        return False
```