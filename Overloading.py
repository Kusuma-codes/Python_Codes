class Summation:
    def sum(self, *args):
        total = 0

        for num in args:
            total += num
        return total
        
s1 = Summation()
print(f"Sum of 3 numbers: {s1.sum(1,2,5)}")
print(f"Sum of 4 numbers: {s1.sum(5,5,1,1)}")