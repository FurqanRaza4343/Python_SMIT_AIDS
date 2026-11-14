# # # a,b,c,d=[12,22,30,44,55]
# # # print(a)
# # a,b,c,*d = [10,20,30,40,50]
# # print(c)
# name,age,*_ = ['Monica',25,'Doctor','Brazil']
# print(name)
# print(age)
# print(_)
def add_three(a,b,c):
  return a+b+c
numbers = [5,10,15]
add_three(*numbers)