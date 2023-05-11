def spell_help_single(name, target):
    new_string = name.replace(" ", "").lower()
    new_target = target.replace(" ", "").lower()
    output = list()
    for x in range(len(new_string)):
        for y in range(len(target)):
            if new_string[x] == new_target[y]:
                output.append(new_string[x])
                break

    for x in range(len(output)):
        for y in range(len(new_string)):
            if output[x] == new_string[y]:
                new_target = new_target.replace(output[x], '', 1)
                break

    if len(new_target) == 0:
        print(f"You CAN spell '{target}' with the player '{name}'!")
    else:
        print(f"You CANNOT spell '{target}' with the player '{name}'!")


def spell_help_list(p_list, target):
    new_target = target.replace(" ", "").lower()
    output = list()
    for x in range(len(p_list)):
        current_player = p_list[x]
        for y in range(len(current_player)):
            for z in range(len(new_target)):
                if current_player[y] == new_target[z]:
                    output.append(current_player[y])
                    break
        print(f"These are the characters for {current_player} that are also in the target word: {output}")

        for a in range(len(output)):
            for b in range(len(current_player)):
                if output[a] == current_player[b]:
                    new_target = new_target.replace(output[a], '', 1)
                    break

        if len(new_target) == 0:
            print(f"You CAN spell '{target}' with the player '{current_player}'!")
            break
        else:
            print(f"You CANNOT spell '{target}' with the player '{current_player}'!")

        new_target = target.replace(" ", "").lower()
        output = list()


if __name__ == '__main__':
    player_list = ["Nico Hoerner", "Matt Mervis", "Dansby Swanson", "Marcus Stroman", "Ian Happ", "Seiya Suzuki"]
    for x in range(len(player_list)):
        print(player_list[x])

    spell_help_list(player_list, "Astro")
    # spell_help_single("Nephew Ignore", "Winner")