#make a list of items that are have digits that never decrease from left to right
#take this list and only take those with doubles in them

start = 234208
end = 765869
answer = 0

#add our first passcode
#list_of_answerwers.append(234444)

#I want to check the items for doubles
#def double_check(list):
#    double_exists = False
#    for i in range(len(list) - 1):
#        if list[i] == list[i + 1]:
#            double_exists = True
#            break
#    if double_exists == True:
#        return True
#    else:
#        return False

#def convert_list_to_int(list): 
#      
#    # Converting integer list to string list 
#    s = [str(i) for i in list] 
#      
#    # Join list items using join() 
#    res = int("".join(s)) 
#      
#    return(res) 

#populate the stack
#for i in range(6):
#    sq.append(wl[i])
#abandoned because the deque was creating linked copies

#hopefully we dont have more steps that possibilities
#while 1 < 5:
#for i in range(50):
#    last = wl[-1]
#    compare = wl[-2]
#    last += 1
#
#    if compare > 9:
#        break
#
#    if last > 9:
#        compare += 1
#        last = compare
#        wl[-2] = compare
#        wl[-1] = last
#    elif last < compare:
#        wl[-1] = last
#        i -= 1
#    elif last == compare:
#        wl[-1] = last
#        i -= 1
#    else:
#        wl[-2] = compare
#        wl[-1] = last
#    list_of_answerwers.append(convert_list_to_int(wl))

#realized its triangle numbers, also its sorted

for i in range(start, end):
    password = [int(j) for j in str(i)]
    if password != sorted(password):
        continue

    for digit in password:
        if password.count(digit) >= 2:
            answer += 1
            break

print(answer)


def check_part_2(n):
    return list(n) == sorted(n) and 2 in map(n.count, n)

print(sum(check_part_2(str(n)) for n in range(234208, 765869)))