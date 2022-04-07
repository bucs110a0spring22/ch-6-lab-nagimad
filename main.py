

import turtle

def seq3np1(n):
  count=0
  while(n != 1):
      if (n % 2)==0:
        n=n//2
      else:
          n=n*3+1
      count +=1
  return count
  
def drawGraph(iteration):
  
  turtledrawer= turtle.Turtle()
  turtledrawer.speed(0)
  turtledrawer.up()
  turtledrawer.goto(0,0)
  turtledrawer.down()
  drawer=turtle.Turtle()
  
  drawer.speed(0)
  wn=turtle.Screen()
  wn.setworldcoordinates(0,0,10,10)
  max_so_far=0

  for i in range(1,iteration +1 ):
    result= seq3np1(i)
    
    print("the number "+ str(i)+ " has " + str(result)+ " iterations.")
    if result > max_so_far:
      max_so_far=result
      drawer.clear()
      drawer.up()
      drawer.goto(i,max_so_far)
      drawer.write("max so far:"+ str(max_so_far))
    wn.setworldcoordinates(0,0,i+ 10, max_so_far + 10)
    turtle.goto(i,result)
  
  wn.exitonclick()

def main():
    upperbound = int(input(" upper bound:"))
    MINNUM=1
    while (MINNUM<upperbound):
        MINNUM +=1
        count = seq3np1(MINNUM)
        print( "number " + str(MINNUM)+ "has" + str(count)+ "iterations.")
    drawGraph(upperbound)
  
main()