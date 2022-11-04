# Find two numbers in a sorted list which their sum is 45.

if __name__ == "__main__":
    my_list = [8, 10, 12, 13, 20, 25, 26, 33, 37, 38, 44, 53]
    target_sum = 45

    front = 0
    last = len(my_list) - 1
    while front <= last:
        sum = my_list[front] + my_list[last]
        if sum == target_sum:
            print(f"{my_list[front]} + {my_list[last]} = {target_sum}")
            last -= 1  # or front += 1
        elif sum > target_sum:
            last -= 1
        elif sum < target_sum:
            front += 1

