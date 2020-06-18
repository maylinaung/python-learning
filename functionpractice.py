def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False
def main():
    result = makes_twenty(10,10)
    print(result);
if __name__ == '__main__':
   main()