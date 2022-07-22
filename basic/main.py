from functools import reduce

#my_pets = ["sisi", "bibi", "titi", "carla"]


#def upper(x):
#    return x.upper()


#print(list(map(upper, my_pets)))

#my_strings = ["a", "b", "c", "d", "e"]
#my_numbers = [5, 4, 3, 2, 1]

#my_numbers.sort()
#print(list(zip(my_strings, my_numbers)))


#scores = [73, 20, 65, 19, 76, 100, 88]


#def passed(x):
#    return x > 50


#print(list(filter(passed, scores)))


#def accumulate(i, j):
#    result = i + j
#    return result


#print(reduce(accumulate, scores))


#my_list = [5, 4, 3]
#new_list = list(map(lambda x: x**2, my_list))
#print(new_list)


#a = [(0, 2), (4, 3), (9, 9), (10, -1)]

#a.sort(key=lambda x: x[1])
#print(a)

#def fib(number):
#    a = 0
#    b = 1
#    for i in range(number):
#        yield a
#        temp = a
#        a = b
#        b = temp + b


#for x in fib(20):
#    print(x)
def do_stuff(num):
    try:
        if num and num != " ":
            return int(num) + 5
        else:
            return "please enter number"
    except (ValueError) as err:
        return err
