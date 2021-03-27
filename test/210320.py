# 1

def solution(table, languages, preference):

    languages_set = [[0]*6 for _ in range(5)]
    result_set = [0]*5

    for i in range(5):
        languages_set[i][0] = table[i].split()[0]
        languages_set[i][5] = table[i].split()[1]
        languages_set[i][4] = table[i].split()[2]
        languages_set[i][3] = table[i].split()[3]
        languages_set[i][2] = table[i].split()[4]
        languages_set[i][1] = table[i].split()[5]

    for i, v in enumerate(languages):
        for x in range(5):
            for y in range(1, 6):
                if languages_set[x][y] == v:  # 같은 문자열을 찾으면
                    result_set[x] += y * preference[i]
                    break
    #         else:
    #             print(languages_set[x], y, i, v)
    #             print(0)
    # print(result_set)

    max_val = max(result_set)
    answer = []
    for i, v in enumerate(result_set):
        if max_val == v:
            answer.append(languages_set[i][0])
    answer.sort()

    return answer[0]


# print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
#                ["PYTHON", "C++", "SQL"],
#                [7, 5, 5]))
# print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
#                ["JAVA", "JAVASCRIPT"],
#                [7, 5]))



# 2
def solution(inp_str):
    answer = []
    chk_condition_list = [0] * 4
    len_inp = len(inp_str)

    def chk_len():
        if not (8 <= len_inp <= 15):
            return 1

    def chk_condition(inp_str):
        special_char = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]
        flag = 0

        for inp in inp_str:
            if 65 <= ord(inp) <= 90:
                chk_condition_list[0] = 1
            elif 97 <= ord(inp) <= 122:
                chk_condition_list[1] = 1
            elif 48 <= ord(inp) <= 57:
                chk_condition_list[2] = 1
            elif inp in special_char:
                chk_condition_list[3] = 1
            else:
                flag = 1

        if flag:
            return 2

    def chk_condition_multi():
        if sum(chk_condition_list) < 3:
            return 3

    def chk_repeat(inp_str):
        pre_char = ''
        pre_repeat = 1
        for inp in inp_str:
            if pre_char == inp:
                pre_repeat += 1
                if pre_repeat == 4:
                    return 4
            else:
                pre_repeat = 1
            pre_char = inp

    def chk_same(inp_str):
        for i in range(len_inp):
            cnt = 0
            for j in range(i, len_inp):
                if inp_str[i] == inp_str[j]:
                    cnt += 1
                    if cnt == 5:
                        return 5

    if chk_len(inp_str):
        answer.append(1)
    if chk_condition(inp_str):
        answer.append(2)
    if chk_condition_multi():
        answer.append(3)
    if chk_repeat(inp_str):
        answer.append(4)
    if chk_same(inp_str):
        answer.append(5)

    if not answer:
        return [0]
    else:
        return answer

# print(solution("aaaaZZZZ"))
# print(solution("AaTa+!12-3"))


# 내가 나간 것보다 늦게 들어오고

def solution(enter, leave):

    len_person = len(enter)
    enter_idx = 0
    answer = [0] * (len_person + 1)
    in_meetingroom = [0] * (len_person + 1)

    for leave_num in leave:
        while enter_idx < len_person and enter[enter_idx] != leave_num:
            in_meetingroom[enter[enter_idx]] = 1
            enter_idx += 1

        if enter_idx < len_person and enter[enter_idx] == leave_num:
            enter_idx += 1

        in_meetingroom[leave_num] = 0

        cnt = 0
        for i, v in enumerate(in_meetingroom):
            if v:
                answer[i] += 1
                cnt += 1

        answer[leave_num] += cnt

        enter_idx += 1

    answer.pop(0)
    return answer


# print(solution([1,4,2,3], [2,1,3,4]))


# 2-1

def solution(program, flag_rules, commands):
    answer = []
    # rule_list = []

    def create_dict_to_rule():
        rule_dict = {}
        for flag_rule in flag_rules:
            flag_rule, arg = flag_rule.split()
            rule_dict[flag_rule] = arg
        return rule_dict

    rule_dict = create_dict_to_rule()

    def string_chk(command_value):
        for command_char in command_value:
            if not (65 <= ord(command_char) <= 90) or (97 <= ord(command_char) <= 122):
                return 0
        else:
            return 1

    def number_chk(command_value):
        for command_char in command_value:
            if not 48 <= ord(command_char) <= 57:
                return 0
        else:
            return 1

    for command in commands:
        command = command.split()

        if program != command[0]:
            answer.append(False)
            continue

        len_comm = len(command)
        command_idx = 1

        while command_idx < len_comm:

            cur_rule = command[command_idx]
            cur_type = rule_dict.get(cur_rule)


            if command_idx + 1 == len_comm:
                if cur_type != "NULL":
                    answer.append(False)
                    break

            if command_idx + 1 < len_comm:
                command_value = command[command_idx + 1]

            if cur_type == "NULL":
                command_value = ''

            if not cur_type:
                answer.append(False)
                break

            if cur_type == "STRING":
                if not string_chk(command_value):
                    answer.append(False)
                    break
            elif cur_type == "NUMBER":
                if not number_chk(command_value):
                    answer.append(False)
                    break
            else:
                if command_value:
                    answer.append(False)
                    break

            if "STRING" or "NUMBER":
                command_idx += 2
            else:
                command_idx += 1

        else:
            answer.append(True)

    return answer


print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))