class Solution:
    def get_sum(self, number: int) -> int:
        sum = 0
        for num in str(number):
            sum += int(num) ** 2

        return sum

    def isHappy(self, n: int) -> bool:
        # create history dictionary
        history = dict()

        # initialize number to n
        number = n
        while True:
            sum = self.get_sum(number)

            if sum == 1:
                return True

            if history.get(sum):
                return False

            history[sum] = True

            number = sum
