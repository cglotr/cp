# [2305\. Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/)

## Description

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/), [Backtracking](https://leetcode.com/tag/backtracking/), [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/), [Bitmask](https://leetcode.com/tag/bitmask/)


You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the i<sup>th</sup> bag. You are also given an integer `k` that denotes the number of children to distribute **all** the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The **unfairness** of a distribution is defined as the **maximum** **total** cookies obtained by a single child in the distribution.

Return _the **minimum** unfairness of all distributions_.

**Example 1:**

```
Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
```

**Example 2:**

```
Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.
```

**Constraints:**

*   `2 <= cookies.length <= 8`
*   1 <= cookies[i] <= 10<sup>5</sup>
*   `2 <= k <= cookies.length`


## Solution

Language: **Go**

```go
var child []int
var ans int
​
func distributeCookies(cookies []int, k int) int {
    child = []int{}
    ans = 9223372036854775807
    for i := 0; i < k; i++ {
        child = append(child, 0)
    }
    dfs(cookies, k, 0)
    return ans
}
​
func dfs(cookies []int, k int, cookie int) {
    if cookie >= len(cookies) {
        cur := child[0]
        for _, v := range child {
            if v > cur {
                cur = v
            }
        }
        if cur < ans {
            ans = cur
        }
        return
    }
    for i := 0; i < k; i++ {
        child[i] += cookies[cookie]
        dfs(cookies, k, cookie + 1)
        child[i] -= cookies[cookie]
    }
}
```
