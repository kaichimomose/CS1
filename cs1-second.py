some_list = [1, 2, 3, 4, 5]
print(some_list)

some_list.append("Hi!")
print(some_list)

first_list = some_list[0]
last_list = some_list[-1]

subset = some_list[1:-1]
print(subset)

another_subset = some_list[::2]
print(another_subset)

shouldnt_be_famous = "Nicholas Cage"
first_letter = shouldnt_be_famous[0]
print(first_letter)

split_it_up = shouldnt_be_famous.split(" ")
print(split_it_up)

split_it_up = shouldnt_be_famous.split("C")
# C is gone
print(split_it_up)

msg = "Hi!"

if msg in some_list:
    print("yes!")
