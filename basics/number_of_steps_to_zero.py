# 1342. Number of Steps to Reduce a Number to Zero

# SIMPLE SOLUTION

def numberOfSteps(num: int) -> int:
  steps = 0
  while num>0:
    if num%2==0:
      num = num/2
      steps = steps+1
    else:
      num = num-1
      steps = steps +1
  
  return steps

# Solution using binary format: 
"""
Explanation
Let's take 14. It's binary representation is 1110. If we operate on this value, we get:

1) 1110 - Divide by 2
2) 111  - Subtract 1
3) 110  - Divide by 2
4) 11   - Subtract 1
5) 10   - Divide by 2
6) 1    - Subtract 1
When there's a 1 at the rightmost position, it costs two steps to remove it.
When there's a 0, it only cost one step to remove it.
The remaining 1 at step six only cost one step.
Then, the number of steps becomes:

Steps = (ones x 2) + (zeros x 1) - 1
Remember the last 1 costs only one step. So we subtract that additional step from the formula.

Python's bin(14) returns the string 0b1110, so we also subtract one step for that extra 0 at the leftmost position.
"""
def numberOfSteps(self, num: int) -> int:
  return 2 * bin(num).count('1') + bin(num).count('0') - 2

