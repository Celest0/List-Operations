data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = input()

#your code goes here
total=23+11+5+14+8+32+20+5

if color=="brown":
  print(int((data[0][0]+data[1][0])*100/total))

elif color=="blue":
  print(int((data[0][1]+data[1][1])*100/total))

elif color=="green":
  print(int((data[0][2]+data[1][2])*100/total))

elif color=="black":
  print(int((data[0][3]+data[1][3])*100/total))

else:
  print("st7awwa")

  #as you can see the code is a brute force because that was the main goal,to find the worst solution possible! #
