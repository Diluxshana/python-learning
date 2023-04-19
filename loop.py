count = 0
while True:
    print(count)
    count += 1
    if count > 5:
        break
    else:
        print("count value reached %d" % (count))

for i in range(1, 10):
    print(i)
    if i % 5 == 0:
        break
    else:
        print("i value reached %d" % (i))

names = ["John", "Jane"]
foods = ["pizza", "sushi", "burgers"]
for name in names:
    for food in foods:
        print(name + " likes " + food)