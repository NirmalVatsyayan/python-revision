value = 100
denominator = 10
d = {}

try:
    div = value/ denominator
    print(div)
    
    try:
        raise IOError
    except:
        print("nested except")

    print(d[1])
except ZeroDivisionError as e:
    denominator = denominator + 1
    div = value/ denominator
    print("Congrats !! your code have a ZeroDivisionError :)")
    print("recanculated value is ", div)
except IOError as e:
    print("its an awesome error !!")
    print("Congrats !! your code have a IOError :)")
except KeyError as e:
    print("Congrats !! your code have a KeyError :)")
except:
    print("Congrats !! your code have a bug :)")

print("hello world !!")
