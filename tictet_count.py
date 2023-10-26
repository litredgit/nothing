result_dict = {x: 0 for x in int(100)}
count = 0

while True:
    x = input(f"请输入第{count}张票的结果") 
    if x == 'end':
        break
    else:
        result_dict[x] += 1
        count += 1

print(f"统计结果如下\n共{count}张票")