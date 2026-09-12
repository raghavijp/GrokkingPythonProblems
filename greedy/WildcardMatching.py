def isMatch(s, p):
    sIdx = 0
    pIdx = 0
    starPos = -1
    matchPos = -1

    while sIdx < len(s):
        if pIdx < len(p) and (p[pIdx] == '?' or p[pIdx] == s[sIdx]):
            sIdx += 1
            pIdx += 1
        elif pIdx < len(p) and p[pIdx] == '*':
            starPos = pIdx
            matchPos = sIdx
            pIdx +=1
        elif starPos == -1:
            return False
        else:
            pIdx = starPos + 1
            matchPos +=1
            sIdx = matchPos

    for i in range(pIdx, len(p)):
        if p[i] != '*':
            return False

    return True


def main():
    ss = ["abc", "ab", "abc", "xy", "abcd"]
    ts = ["***", "??", "a?b", "x?**", "a*d"]

    for i in range(len(ss)):
        print(f"{i+1}. \ts: {ss[i]} \tt: {ts[i]}\n")
        print(f"\t PAttern match: {'TRUE' if isMatch(ss[i],ts[i]) else 'FALSE'}")

main()