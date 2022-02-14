#9.1
list = [ ]
n = int(input("Ievadi skaitu: "))
for x in range(n):
  ele=int(input())
  list.append(ele)
list1=sum(list)/len(list)
print(list1)
