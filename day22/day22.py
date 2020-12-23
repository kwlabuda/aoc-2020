import re

def get_decks():
    with open("day22.txt") as f:
        text = f.read().strip()
    s1, s2 = re.split(r"\n{2,}", text)
    lines1 = s1.split("\n")[1:]
    lines2 = s2.split("\n")[1:]
    deck1 = [int(line) for line in lines1]
    deck2 = [int(line) for line in lines2]
    return deck1, deck2


def part1():
    deck1, deck2 = get_decks()
    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)
        else:
            raise Exception("Two cards with same value")
    deck = deck1 + deck2
    return sum(deck[-n] * n for n in range(1, len(deck) + 1))


def play(deck1, deck2):
    seen = set()
    while len(deck1) > 0 and len(deck2) > 0:
        # check if card order has been seen
        card_order = (
            ",".join(str(c) for c in deck1) + "-" +
            ",".join(str(c) for c in deck2)
        )
        if card_order in seen:
            return True
        seen.add(card_order)
        # draw top cards
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        win = None
        if card1 <= len(deck1) and card2 <= len(deck2):
            # play recursive game
            win = play(deck1[:card1], deck2[:card2])
        else:
            # play normally
            win = card1 > card2
        # add cards to winner's deck
        if win:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    return len(deck2) == 0


def part2():
    deck1, deck2 = get_decks()
    play(deck1, deck2)
    deck = deck1 + deck2
    return sum(deck[-n] * n for n in range(1, len(deck) + 1))


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
    print(f"Part 2:\n{part2()}")
