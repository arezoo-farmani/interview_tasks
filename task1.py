# Find similar numbers in a list.

if __name__=="__main__":
    my_list = [25, 79, 86, 120, 79, 456, 58, 79, 86, 25]

    repeat_dict = dict()
    for index, number in enumerate(my_list):
        if number in repeat_dict.keys():
            repeat_dict[number].append(index)
        else:
            repeat_dict[number] = [index]

for key, value in repeat_dict.items():
    if len(value) > 1:
        print(f"Number {key} was found {len(value)} times at indices: {value}")
