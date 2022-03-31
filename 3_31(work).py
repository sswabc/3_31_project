#001
price_list=[32100,32150,32000,32500]
for i in range(0,4):
    print(1*i,price_list[i])

#002
price_list=[32100,32150,32000,32500]
for i in range(1,4):
    print(90+10*i,price_list[i])

#003 
for i in range(2002,2051,4):
    print(i)

#004

for i in range(10):
    print(i/10)

#005

ticker="btc_ktw"
t1=ticker.upper()
print(t1)

#006
file_name="보고서.xlsx"
file_name.endswith("xlsx")


#007
a="hello world"
a.split()
print(a.split())

#008
date="2020-05-01"
date.split("-")
print(date.split("-"))

#009
상장주식수="5,969,782,550"

#010
a="hello world"
a.split()
print(a.split())

#011
price=['20180728',100,130,140,150,160,170]
print(price[1:])

#012
num=[1,2,3,4,5,6,7,8,9,10]
print([2,4,6,8,10])

#013
리스트=[3,100,23,44]
for i in 리스트:
    if i %3==0:
        print(i)