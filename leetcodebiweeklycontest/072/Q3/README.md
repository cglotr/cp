# [2178\. Maximum Split of Positive Even Integers](https://leetcode.com/problems/maximum-split-of-positive-even-integers/)

## Description

Difficulty: **Medium**  

Related Topics: [Math](https://leetcode.com/tag/math/), [Greedy](https://leetcode.com/tag/greedy/)


You are given an integer `finalSum`. Split it into a sum of a **maximum** number of **unique** positive even integers.

*   For example, given `finalSum = 12`, the following splits are **valid** (unique positive even integers summing up to `finalSum`): `(12)`, `(2 + 10)`, `(2 + 4 + 6)`, and `(4 + 8)`. Among them, `(2 + 4 + 6)` contains the maximum number of integers. Note that `finalSum` cannot be split into `(2 + 2 + 4 + 4)` as all the numbers should be unique.

Return _a list of integers that represent a valid split containing a **maximum** number of integers_. If no valid split exists for `finalSum`, return _an **empty** list_. You may return the integers in **any** order.

**Example 1:**

```
Input: finalSum = 12
Output: [2,4,6]
Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
(2 + 4 + 6) has the maximum number of integers, which is 3\. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.
```

**Example 2:**

```
Input: finalSum = 7
Output: []
Explanation: There are no valid splits for the given finalSum.
Thus, we return an empty array.
```

**Example 3:**

```
Input: finalSum = 28
Output: [6,8,2,12]
Explanation: The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24). 
(6 + 8 + 2 + 12) has the maximum number of integers, which is 4\. Thus, we return [6,8,2,12].
Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.
```

**Constraints:**

*   1 <= finalSum <= 10<sup>10</sup>


## Solution

Language: **Python3**

```python3
class Solution:
    def maximumEvenSplit(self, final_sum: int) -> List[int]:
        if final_sum % 2 != 0:
            return []
        want = final_sum // 2
        ans = []
        x = 1
        cur_sum = 0
        while cur_sum + x <= want:
            ans.append(x)
            cur_sum += x
            x += 1
        ans[-1] += want - cur_sum
        return [i * 2 for i in ans]
```
