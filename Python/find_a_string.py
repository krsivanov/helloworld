def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        variable = string[i:i+len(sub_string)]
        if  variable == sub_string:
            counter+=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
