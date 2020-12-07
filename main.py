############### Blackjack Project #####################
import random 
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if 11 in cards and 10 in cards and len(cards) == 2:
      return 0
  if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score >21 and computer_score > 21:
    return "Te has pasado, has perdido"

  if user_score == computer_score:
    return "Empate"
  elif computer_score == 0:
    return "Perdiste, tu oponente tiene blackjack"
  elif user_score == 0:
    return "Ganaste con tu blackjack!!"
  elif user_score > 21:
    return "Te pasaste!! Has perdido! :("
  elif computer_score > 21:
    return "Tu oponente se pasó, has ganado"
  elif user_score > computer_score:
    return "Has ganado"
  else:
    return "Perdiste"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Tus cartas: {user_cards}, puntaje actual: {user_score}")
    print(f"  Primera carta de la computadora: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_answer = input("Teclea 'y' para obtener una nueva carta, o 'n' para pasar ")
      if user_answer == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Tu mano final: {user_cards}, tu puntaje final: {user_score}") 
  print(f"Cartas de la computadora: {computer_cards},  puntaje final: {computer_score}") 
  print(compare(user_score, computer_score))

while input("Deseas jugar nuevamente? Teclea 'y' o 'n': ") == "y":
  clear()
  play_game()
  





