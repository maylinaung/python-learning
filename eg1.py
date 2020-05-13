

def inputValue():
    input_str=input("Please Enter Your Town:")
    return input_str

def forTesting():
    str = inputValue()
    # for a in str:
    if(str=='hopin'):
       print("my native is:" +str.capitalize())
    elif(str=='quit'):
        quit()
    else:
       print("other native: " +str.capitalize())
    forTesting()


if __name__ == '__main__':
    forTesting()
