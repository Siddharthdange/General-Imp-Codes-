class Solution():
    
    def add_bin(a,b):
        sum1 = int(a,2)+int(b,2)
        return bin(sum1).replace("0b"," ")

if __name__ == "__main__":
    T=int(input())
    for i in range(T):
        a,b = input().split(" ")
        ob = Solution()
        answer = ob.add_bin(a,b)
        
        print(answer)
