""" 412. FizzBuzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true."""

class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1,n+1):
            if(i%15==0):
                result.append("FizzBuzz")
            elif(i%5==0):
                result.append("Buzz")
            elif(i%3 == 0):
                result.append("Fizz")
            else:
                result.append(str(i))
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(15)) 