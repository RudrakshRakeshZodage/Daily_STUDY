class Solution:
    def threeSum(self, a):
        a.sort()
        r = []
        n = len(a)

        for i in range(n - 2):
            if i > 0 and a[i] == a[i - 1]:
                continue

            l = i + 1
            h = n - 1

            while l < h:
                s = a[i] + a[l] + a[h]

                if s == 0:
                    r.append([a[i], a[l], a[h]])

                    while l < h and a[l] == a[l + 1]:
                        l += 1
                    while l < h and a[h] == a[h - 1]:
                        h -= 1

                    l += 1
                    h -= 1

                elif s < 0:
                    l += 1
                else:
                    h -= 1

        return r
