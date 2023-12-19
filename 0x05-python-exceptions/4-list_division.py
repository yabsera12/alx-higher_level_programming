#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_new = []
    div = 0

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            my_list_new.append(div)
    return my_list_new

