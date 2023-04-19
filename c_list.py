def c_list(name):
    if __name__ == '__c_list__':
        c_list()


# creating list
numbers = [1, 8, 3, 6, 9]
print(numbers)

word = ['Apple', 'pine apple', 'orange']
print(word)

print(numbers[0])  # print 1st element
print(numbers[-1])  # print last element
numbers[2] = 5  # change the elements
print(numbers)

numbers.append(10)  # add element to last
print(numbers)

numbers.extend([25, 11, 32, 4, 2, 15])  # add elements
print(numbers)

numbers.insert(2, 4)  # add element in 2nd position
print(numbers)

numbers.remove(1)  # remove no 1
print(numbers)

del numbers[2]  # remove 2nd position element
print(numbers)

item=numbers.pop(3) #remove 3rd position element
print(numbers)
print(item)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

