### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #missing == to check for equality
      return True
    else #missing : 
      return False
   

  dif highest_card(self, card1 card2): #def not dif, missing comma between card1 and card2 in the var list for the function; indentation is incorrect
  if card1.value > card2.value:
    return card #returning wrong variable, should be card1
  else:
    return card2
  


def cards_total(self, cards): #incorrect indentation, function not part of the class
  total #variable not declared properly, needs to be set to zero here
  for card in cards:
    total += card.value
    return "You have a total of" + total #needs a print statement for total as a string,return function is inside the loop
