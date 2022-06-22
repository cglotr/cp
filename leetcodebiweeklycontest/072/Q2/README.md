# [2177\. Find Three Consecutive Integers That Sum to a Given Number](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/)

## Description

Difficulty: **Medium**  

Related Topics: [Math](https://leetcode.com/tag/math/), [Simulation](https://leetcode.com/tag/simulation/)


Given an integer `num`, return _three consecutive integers (as a sorted array)_ _that **sum** to_ `num`. If `num` cannot be expressed as the sum of three consecutive integers, return _an **empty** array._

**Example 1:**

```
Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
```

**Example 2:**

```
Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
```

**Constraints:**

*   0 <= num <= 10<sup>15</sup>


## Solution

Language: **Python3**

```python3
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        x = num // 3
        return [x-1, x, x+1]
```
