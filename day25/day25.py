DIVISOR = 20201227

def calc_loop_size(pub_key):
    subj_num = 7
    loop_size = 0
    k = 1
    while k != pub_key:
        k *= subj_num
        k %= DIVISOR
        loop_size += 1
    return loop_size


def calc_encrypt_key(subj_num, loop_size):
    k = 1
    for _ in range(loop_size):
        k *= subj_num
        k %= DIVISOR
    return k


def part1():
    card_pub_key = 17607508
    door_pub_key = 15065270
    card_loop_size = calc_loop_size(card_pub_key)
    card_encrypt_key = calc_encrypt_key(door_pub_key, card_loop_size)
    return card_encrypt_key


if __name__ == "__main__":
    print(f"Part 1:\n{part1()}")
