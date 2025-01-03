class Fibonacci():
    # THIS IS A SIMPLE ONE
    # x: int = 0
    # y: int = 1
    # print(x)
    # print(y)
    # for fibo in range(10): #should run from (0-9 times)
    #     z = x + y
    #     print(z)
    #     x=y
    #     y=z

    """
    friday-3-jan 20:52
    what i tried to do was try to implement fibonacci in array. I don't know if it's the correct approach or soemthing. I think it worked lol. but it has printed in a way i did not expect. feels like magic.
    """
    x: int = [0,1]
    first_index = x[0]
    second_index = x[1]
    print(first_index, second_index)
    for i in range(10):
        z = first_index + second_index
        x.append(z)
        first_index = second_index
        second_index = z
        print(x)
    
