####################################################################################
#
# input.py
#
# Demonstrate one use of recursion.  (Notice how the code gets simpler.)
#
#####################################################################################

def get_input_v1():
    word = input("Please enter a 5-letter word beginning with 'a': ")
    while (len(word) != 5 or word[0] != 'a'):
        if (len(word) != 5):
            print("The word must be exactly 5 letters long. Please try again.")
        elif (word[0] != 'a'):
            print("The word must begin with 'a'.  Please try again.")
        word = input("Please enter a 5-letter word beginning with 'a': ")
    print("Thank-you. (1)")
    return word
#get_input_v1()


def get_input_v2():
    while(True):
        word = input("Please enter a 5-letter word beginning with 'a': ")
        if (len(word) != 5):
            print("The word must be exactly 5 letters long. Please try again.")
        elif (word[0] != 'a'):
            print("The word must begin with 'a'.  Please try again.")
        else:
            break
    print("Thank-you. (2)")
    return word
# get_input_v2()
  
def get_input_v3():
    word = input("Please enter a 5-letter word beginning with 'a': ")
    if (len(word) != 5):
        print("The word must be exactly 5 letters long. Please try again.")
        return get_input_v3()
    elif (word[0] != 'a'):
        print("The word must begin with 'a'.  Please try again.")
        return get_input_v3()
    else:
        print("Thank-you. (3)")
        return word
# get_input_v3()

def count_down(counter):
    if (counter <= 0):
        print("Go!")
    else:
        print(counter)
        count_down(counter - 2)


count_down(9)
