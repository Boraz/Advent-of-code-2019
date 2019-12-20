#create a 4 item list: U D L R to hold the positions (set all to 0)
#create a list to hold visited locations: location and visited and crossed (set first location to 0,0,0,0)
#add the location and say we visited it
#once we finish all location calculate the closest one
#return the UDLR and calculate the distance

#current location = []
#visited list = []

#for each item in the list
	#input the items location (UDLR)
		#if U then += U:
		#elif D then += D:
		#elif L then += L:
		#elif R then += R:
		#else somethign went wrong:
	#check if the location has been visited
		#if visited = true, then crossed = true:
			#break
		#else:
			#add location to the visited list eg R75 = 0,0,0,57
			#set visited = true

#get the list of crossed locations
#sum each location and return the min sum


#ANNNND just watched a person do this in 5 min...

A,B = open('day_3_input.txt').read().split('\n')
A,B = [x.split(',') for x in [A,B]]

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
def get_points(A):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n): # I learned about the _ from this person, thanks!
            x += DX[d]
            y += DY[d]
            length += 1
            if (x,y) not in ans:
                ans[(x,y)] = length
    return ans

PA = get_points(A)
PB = get_points(B)
both = set(PA.keys())&set(PB.keys())
part1 = min([abs(x)+abs(y) for (x,y) in both])
part2 = min([PA[p]+PB[p] for p in both])
print(part1,part2)