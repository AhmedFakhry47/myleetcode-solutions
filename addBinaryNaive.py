class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # To be optimized
        sum_num = [int(i) for i in str(int(a) + int(b))][::-1]
        sum_num.append(0)
        for i in range(len(sum_num)-1):
            if sum_num[i] > 2:
                sum_num[i] = 1
                sum_num[i+1] +=1 
            if sum_num[i] > 1: 
                sum_num[i] = 0 
                sum_num[i+1] += 1 

        if sum_num[-1] == 0:
            sum_num.pop(-1)

        return ''.join([str(i) for i in sum_num][::-1])
