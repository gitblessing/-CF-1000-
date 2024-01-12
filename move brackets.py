for no_testcase in range(int(input())):
    n = int(input())
    brackets = str(input())
    n = "()"
    while "()" in brackets:
        brackets = brackets.replace(n,"")
        
    print(int(len(brackets)/2))