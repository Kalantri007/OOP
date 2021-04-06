class sample:
    count = 100
    #class atrribute
    def increase(self):
        sample.count += 11

v1 = sample()
v1.increase()

print (v1.count)

v1.increase()
print(sample.count)
