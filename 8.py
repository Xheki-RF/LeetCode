class Solution:
    def myAtoi(self, s: str) -> int:
        min_num, max_num = -2 ** 31, 2 ** 31 - 1
        s = s.strip()
        i, n = 0, len(s)

        sign = 1
        
        if s[0] == "-" and i < n:
            sign = -1
            i += 1
        elif s[0] == "+" and i < n:
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (max_num - digit) // 10:
                return [min_num, max_num][sign == 1]
            
            result = result * 10 + digit
            i += 1
        
        return result * sign


print(Solution().myAtoi('42'))
