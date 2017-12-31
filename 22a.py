best = 999999

def solve(boss):

    def turn(player_moves, player_health, player_mana, boss_health, boss_attack, shield_turns, poison_turns, recharge_turns, mana_spent):
        global best

        if mana_spent > best:
            return 999999
        
        if poison_turns > 0:
            boss_health -= 3

        if boss_health < 1:
            best = min(best, mana_spent)
            return mana_spent

        mana = player_mana + (101 if recharge_turns > 0 else 0)

        shield_turns = max(0, shield_turns - 1)
        poison_turns = max(0, poison_turns - 1)
        recharge_turns = max(0, recharge_turns - 1)        

        if not player_moves:
            player_damage = max(1, boss_attack - (7 if shield_turns > 0 else 0))
            if player_damage >= player_health:
                return 999999
            return turn(not player_moves, player_health - player_damage, mana, boss_health, boss_attack, shield_turns, poison_turns, recharge_turns, mana_spent)

        moves = [999999]

        if mana > 52:
            moves.append(turn(not player_moves, player_health, mana - 53, boss_health - 4, boss_attack, shield_turns, poison_turns, recharge_turns, mana_spent + 53))
        if mana > 72:
            moves.append(turn(not player_moves, player_health + 2, mana - 73, boss_health - 2, boss_attack, shield_turns, poison_turns, recharge_turns, mana_spent + 73))
        if mana > 112 and shield_turns == 0:
            moves.append(turn(not player_moves, player_health, mana - 113, boss_health, boss_attack, 6, poison_turns, recharge_turns, mana_spent + 113))
        if mana > 172 and poison_turns == 0:
            moves.append(turn(not player_moves, player_health, mana - 173, boss_health, boss_attack, shield_turns, 6, recharge_turns, mana_spent + 173))
        if mana > 228 and recharge_turns == 0:
            moves.append(turn(not player_moves, player_health, mana - 229, boss_health, boss_attack, shield_turns, poison_turns, 5, mana_spent + 229))

        best = min(best, min(moves))

        return min(moves)

    return turn(True, 50, 500, boss[0], boss[1], 0, 0, 0, 0)

with open('input_22.txt', 'r') as f:
    boss = [int(line.split()[-1]) for line in f]
    print(solve(boss))