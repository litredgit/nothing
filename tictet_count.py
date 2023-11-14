def input_value() -> tuple[dict, int]:
    count = 0
    result_dict = {}
    while True:
        name = input(f"{count + 1}: ") 
        if isinstance(name, str):#防呆
            if name == 'end':
                break
            else:
                result_dict[name] = result_dict.get(name,0) + 1
                count += 1
        else:
            print(f"请输入字母！\n")
    return result_dict, count

def print_output(result: dict, count: int):
    print(f"\n统计结果如下\n共{count}张票\n")
    for name, name_count in result.items():
        print(f"{name}: {name_count}")
       
        
if __name__ == "__main__":

    print(f"请按顺序输入各张票的结果\n")
    result_dict, count = input_value()
    print_output(result_dict, count)