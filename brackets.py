def check_string_brackets(input_string):
    h, o = 0,0
    while h < len(input_string) and o>=0:
        if "(" == input_string[h]:
            o += 1
        else:
            o -= 1
            i +=1
            if 0 == o:
                print("YES")
            else:
                print("NO")
check_string_brackets()
