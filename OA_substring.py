def substring(s,k):
    if len(s) == 0:
        return 0

    counter = set()
    i = 0
    j= 0
    max_len = 0
    res = set()

    while i < len(s) and j < len(s):
        if s[i] not in counter and i-j+1 <= k:
            counter.add(s[i])
            max_len = max(max_len, i-j)
            if (i-j+1) == k:
                res.add(s[j:i+1])
            i+=1

        else:
            counter.remove(s[j])
            j+=1

    print(res)
    return max_len+1

substring("awaglknagawunagwkwagl", 4)
