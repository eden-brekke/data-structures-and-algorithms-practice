def containsDuplicate(self, nums: List[int]) -> bool:
      num_set = []
      for num in nums:
            if num in num_set:
                return True
            else:
                num_set.append(num)
      return False
