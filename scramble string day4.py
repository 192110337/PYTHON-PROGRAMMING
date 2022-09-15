def check(s1, s2):
    # calculates length
    n = len(s1)
    m = len(s2)
    dp = ([[False for i in range(m + 1)]
           for i in range(n + 1)])
    dp[0][0] = True
    for i in range(len(s1)):
        for j in range(len(s2) + 1):
            if (dp[i][j]):
                if ((j < len(s2) and
                     (s1[i].upper() == s2[j]))):
                    dp[i + 1][j + 1] = True
                if (s1[i].isupper() == False):
                    dp[i + 1][j] = True
    return (dp[n][m])
if _name_ == '_main_':
    s1 = "daBcd"
    s2 = "ABC"
    if (check(s1, s2)):
        print("YES")
    else:
        print("NO")
