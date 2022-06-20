
def add(a, b):
  p=int(input('Enter 1st no :'))
  q=int(input('Enter s2 nnd:'))
##
r=p+q
return r
  

    pass  # ...


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
