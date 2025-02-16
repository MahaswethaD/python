import random
user_action=input("enter a choice (paper,rock,scissor):")
possible_actions=['rock','paper','scissor']
if user_action not in possible_actions:
  print("enter a valid choice from  possible_actions")
else:
  computer_action=random.choice(possible_actions)
  print(f"\nYou chose {user_action},computer chose {computer_action}.\n")
  if user_action==computer_action:
    print("both are tie")
  elif user_action=='rock':
    if computer_action=='scissor':
      print("rock smashes scissor,rock won")
    else:
      print("paper covers rock,paper won")
  elif user_action=='paper':
      if computer_action=='scissor':
        print("scissor cuts paper,scissor won")
      else:
        print("paper covers rock ,paper won")
  elif user_action=='scissor':
      if computer_action=='paper':
        print("scissor cuts paper,paper won")
      else:
        print("rock smashes scissor ,rock won")