class Calculator:   
    def add(self,*args):
        return sum(args)

a=input("Enter numbers: ").split()

nums=[int(n) for n in a]
c=Calculator()
result=c.add(*nums)
print(result)