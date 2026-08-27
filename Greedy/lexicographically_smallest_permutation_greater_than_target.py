# Problem Name: Lexicographically Smallest Permutation Greater Than Target
# Pattern Used: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: We count the frequency of each character in s and target. 
#                    Then we try to construct the smallest permutation greater than target by iterating from the end of target and 
#                    finding the next greater character.
# LeetCode: https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for ch in target:
            cnt[ord(ch) - ord('a')] -= 1

        for i in range(len(target) - 1, -1, -1):
            cur = ord(target[i]) - ord('a')
            cnt[cur] += 1

            # target[:i] cannot be formed.
            if any(x < 0 for x in cnt):
                continue

            # Find the smallest character greater than target[i].
            nxt = -1
            for c in range(cur + 1, 26):
                if cnt[c]:
                    nxt = c
                    break

            if nxt == -1:
                continue

            cnt[nxt] -= 1

            ans = list(target[:i])
            ans.append(chr(nxt + ord('a')))

            # Put the remaining characters in sorted order.
            for c in range(26):
                ans.extend(chr(c + ord('a')) * cnt[c])

            return ''.join(ans)

        return ""