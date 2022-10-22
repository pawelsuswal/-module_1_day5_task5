from random import randint


def roll_a_dice(roll_data):
    error_text = "data for roll cacluation are incorrect!"
    number_of_throwns = 1
    dice_size = 1
    additional_modifier = 0

    if 'D' not in roll_data:
        return error_text

    if roll_data.count('D') > 1:
        return error_text

    roll_data_splited = roll_data.split('D')

    if not roll_data_splited[0].isnumeric() and roll_data_splited[0] != '':
        return error_text
    if len(roll_data_splited[0]) > 0:
        number_of_throwns = roll_data_splited[0]

    if len(roll_data_splited[1]) == 0:
        return error_text

    if '+' in roll_data_splited[1]:
        roll_data_splited += roll_data_splited[1].split('+')
        if not roll_data_splited[2].isnumeric():
            return error_text

        if not roll_data_splited[3].isnumeric():
            return error_text

        dice_size = roll_data_splited[2]
        additional_modifier = roll_data_splited[3]

    elif '-' in roll_data_splited[1]:
        roll_data_splited += roll_data_splited[1].split('-')
        if not roll_data_splited[2].isnumeric():
            return error_text

        if not roll_data_splited[3].isnumeric():
            return error_text

        dice_size = roll_data_splited[2]
        additional_modifier = '-' + roll_data_splited[3]
    else:
        if not roll_data_splited[1].isnumeric():
            return error_text
        dice_size = roll_data_splited[1]

    result = 0
    for roll_iter in range(number_of_throwns):
        result += randint(1, 6)
    return result + int(additional_modifier)


print(roll_a_dice('D6'))
print(roll_a_dice('2D6'))
print(roll_a_dice('2D6+10'))
print(roll_a_dice('2D6-10'))
print(roll_a_dice('D6+10'))
print(roll_a_dice('aD6+10'))
print(roll_a_dice('2Da+10'))
print(roll_a_dice('2D6+a0'))
print(roll_a_dice('2D6+'))

