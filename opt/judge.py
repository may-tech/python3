class Student:
    def __init__(self,name):
        self.name = name

    
    def calculate_avg(self,data):
        sum = 0
    
     #リストの格納
        for num in data:
            sum += num

        avg = sum/len(data)

        return avg

    def judge(self,avg):

        if(avg>=60):
            result = "passed"
        else:
            result = "failed"
        return result


#インスタンス化
a001 = Student("may")

#リストの代入
data = [70,50,65,90,30]

#平均点の算出、代入
avg = a001.calculate_avg(data)

#判定
result = a001.judge(avg)

print(data)
print(avg)
print(a001.name+" "+result)

