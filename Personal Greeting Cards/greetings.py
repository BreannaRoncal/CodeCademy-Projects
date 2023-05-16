"""
Aisha's Greeting Card Company

You are a part of Aisha’s Greetings - a card printing company that prints greeting cards with a hint of personalization! 
You want to help Aisha create a system that generates cards based on customers’ requests.

You have been provided with two pre-filled card types:
  - happy_bday.txt: a card with a birthday message
  - thankyou_card.txt: a card file with a thank you message
"""

# Write your code below: 
from contextlib import contextmanager

# Aisha, the owner of Aisha’s Greetings, wants to create a program that will automatically generate pre-filled orders, using her custom greeting messages. 
# Use your knowledge of context managers to accomplish this goal!
@contextmanager
def generic(card_type, senders_name, recipient):
  card = open(card_type, 'r')
  to_write = open(f"{senders_name}_generic.txt", 'w')
  try:
    to_write.write(f"Dear {recipient},\n\n")
    to_write.write(card.read())
    to_write.write(f"\n\nSincerely, \n{senders_name}")
    yield to_write
  finally:
    card.close()
    to_write.close()



# Aisha’s Greetings also wants to print personalized cards! 
# This means that customers can tell Aisha’s Greetings the words they want in their card and we can print them.
class personalized:
  def __init__(self, senders_name, recievers_name):
    self.senders_name = senders_name
    self.recievers_name = recievers_name
    self.open_file = open(f"{senders_name}_personalized.txt", "w")
  
  def __enter__(self):
    self.open_file.write(f"Dear {self.recievers_name},\n\n")
    return self.open_file

  def __exit__(self, *exc):
    self.open_file.write(f"\n\nSincerely, \n{self.senders_name}")
    self.open_file.close()

  
# Test generic context manager
#with generic('thankyou_card.txt', 'Mwenda', #'Amanda') as new_card:
#  print('Card Generated!')

#with open('Mwenda.txt', 'r') as order1:
#  print(order1.read())


# Test personalized class
#with personalized('John', 'Michael') as order2:
#  order2.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")
  

# Create a nested with statement that generates these orders in one call.
with generic("happy_bday.txt", "Josiah", "Remy") as card1, personalized("Josiah", "Esther") as card2:
  card2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")



