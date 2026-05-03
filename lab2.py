#Exercise 2 -Lab2
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
def get_user_input():
    print("get User Input")
    userinput=input()
    strlist=userinput.split(",")
    float_list=[]
    for i in strlist:
        float_list.append(float(i))
    return float_list

def calc_average(List):
    print("calculation average")
    average= sum(List) / len(List)
    print("Average Temperature is" , average)
    return average

def find_min_max(List):
    print("find_min_max")
    temp_list=List.copy()
    temp_list.sort()
    print(temp_list[0] , temp_list[-1])

def sort_temperature (List):
    print("sort_temperature")
    sorted_list=sorted(List)
    print("sorted= " , sorted_list)
    return sorted_list

def calc_median_temperature (List):
    print("calc_median_temperature ")
    sorted_list=sorted(List)
    number=len(sorted_list)
    if number % 2 == 0:
        median = (sorted_list[number//2 - 1] + sorted_list[number//2]) / 2
    else:
        median = sorted_list[number//2]
    print("Median Temperature is:", median)
    return median


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    List = get_user_input()
    print(List)
    
    calc_average(List)
    find_min_max(List)
    sort_temperature(List)
    calc_median_temperature(List)

if __name__ == "__main__":
    main()