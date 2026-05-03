#Exercise 2 -Lab2
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("“Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    print("get User Input")
    userinput=input()
    strlist=userinput.split()
    float_list=[]
    for i in strlist():
        float_list.append(float(i))
    return float_list

def calc_average(List):
    print("calculation average")
    average= sum(List) / len(List)
    print("Average Temperature is" , average)
    return average

def find_min_max(List):
    print("find_min_max")

def sort_temperature (List):
    print("sort_temperature")

def calc_median_temperature (List):
    print("calc_median_temperature ")




def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    List = get_user_input()
    print(List)



if __name__ == "__main__":
    main()