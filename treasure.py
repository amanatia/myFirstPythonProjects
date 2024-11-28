print('''<=======]}======
    --.   /|
   _\"/_.'/
 .'._._,.'
 :/ \{}/
(L  /--',----._
    |          \\
   : /-\ .'-'\ / |
snd \\, ||    \|
     \/ ||    ||
     
     Welcome to treasure island!
     Your task is to find the treasure.
     ''')

print("You find yourself inside a cave. In the cave there are two doors. A blue one and a red one. ")

decision = input("Which one are you choosing? Type 'Blue' or 'Red'")

if decision == "red" or decision == "Red":
  
  print("inside the door you now see a big lake")
  
  lake = input("Do swim or do you wait? Type 'Swim' or 'Wait'")
  if lake == "Swim" or lake == "swim":
    print("Now you find yourself at a crossroad")
    
    road = input("Do you go left or right? Type 'left' of 'right'")
    
    if road == "left" or road == "Left":
      print("You just found the treasure!!/n")
      print('''                                                         ,jf
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"''')
    else : 
      print("You Lost!")
      
  else : 
    print("You Lost")
    
else: 
  print("You Lost!")
      
    

