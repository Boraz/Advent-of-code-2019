Day2 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0]

def calc():
  i = 0
  while Day2[i] != 99: #look for the exit code
    print('...')
    if Day2[i] == 1: # 1 for +
      print('more gravity...')
      p1 = Day2[i+1]
      p2 = Day2[i+2]
      p3 = Day2[i+3]
      added = Day2[p1]
      added = added + Day2[p2]
      Day2[p3] = added
      i = i + 4
      continue
    if Day2[i] == 2: # 2 for *
      print('fold gravity...')
      p4 = Day2[i+1]
      p5 = Day2[i+2]
      p6 = Day2[i+3]
      multiplied = Day2[p4]
      multiplied = multiplied * Day2[p5]
      Day2[p6] = multiplied
      i = i + 4
      continue
    else:
      print('Not Gravity, exiting until heat death')
      break

def main():
  print('Gravity Assist Assist Program')
  print('.............................')

main()
calc()
print('Finished! Answer is: ', Day2[0] )
print('')
input('Press Enter to Exit')