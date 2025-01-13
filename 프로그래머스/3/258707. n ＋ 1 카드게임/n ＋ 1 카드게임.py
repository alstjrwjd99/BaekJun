from collections import deque

def check(deck1, deck2, target):
    operand = set(deck2)
    for card in deck1:
        if target - card in operand:
            deck1.remove(card)
            deck2.remove(target-card)
            return True
    return False

def solution(coin, cards):
    hand = cards[:len(cards) // 3]
    deck = deque(cards[len(cards) // 3:])
    pending = []
    turn = 1
    while coin >= 0 and deck:
        pending.append(deck.popleft())
        pending.append(deck.popleft())
        
        if check(hand, hand, len(cards) + 1):
            pass
        elif coin >= 1 and check(hand, pending, len(cards) + 1):
            coin -= 1
        elif coin >= 2 and check(pending, pending, len(cards) + 1):
            coin -= 2
        else:
            break
        turn += 1
    return turn