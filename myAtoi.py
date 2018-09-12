
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        res = []
        if not str:
            return 0
        if str[0] == '-' or str[0].isdigit():
            res.append(str[0])
            i = 1
            while i < len(str):
                if str[i].isdigit():
                    res.append(str[i])
                    i += 1
                else:
                    break

        elif str[0] == '+':
            # for i in range(1, len(str)):
            #     if str[i].isdigit():
            #         res.append(str[i])
            i = 1
            while i < len(str):
                if str[i].isdigit():
                    res.append(str[i])
                    i += 1
                else:
                    break
        res = ''.join(res)
        if res and res != '-':
            res = int(res)
        else:
            return 0
        max = 2147483648
        min = -2147483648
        if min <= res <= max - 1:
            return res
        else:
            if res > 0:
                return max - 1
            else:
                return min

if __name__ == '__main__':
    sol = Solution()

    str = '+-2'
    res = sol.myAtoi(str)
    print(res)



    a = pow(2,31)


