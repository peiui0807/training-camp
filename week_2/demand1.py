#第一題
def calculate(min,max):
    count=0 
    for i in range(min, max+1):
        count=count+i
    print(count)
    
calculate(1,3)
calculate(4,8)

#第二題
def avg(data):
    total=0
    for i in range(data["count"]):
        total+=data["employees"][i]["salary"]
    print(total/data["count"])

avg({
    "count":3,
    "employees":[
        {"name":"John",
        "salary":30000},
        {"name":"Bob",
        "salary":60000},
        {"name":"Jenny",
        "salary":50000},
    ]
})

#第三題
def maxProduct(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(i==0 and j==1):
                current=nums[i]*nums[j]
            else:
                if(nums[i]*nums[j]>current):
                     current=nums[i]*nums[j]
    print(current)

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])

#第四題
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                result=[i,j]
    print(result)

result=twoSum([2, 11, 7, 15], 9)

#第五題
def maxZeros(nums):
    count=0
    maxcount=0
    for i in range(len(nums)):
        if(nums[i]==0):
            count=count+1
        else:
            count=0
        if(maxcount<count):
            maxcount=count
    print(maxcount)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])

