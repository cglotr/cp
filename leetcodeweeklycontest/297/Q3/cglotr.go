var child []int
var ans int

func distributeCookies(cookies []int, k int) int {
    child = []int{}
    ans = 9223372036854775807
    for i := 0; i < k; i++ {
        child = append(child, 0)
    }
    dfs(cookies, k, 0)
    return ans
}

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
