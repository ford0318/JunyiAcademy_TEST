# there are 3 bags: 
# a bag : pencil
# b bag : ball pen
# c bag : pencil & ball pen


def main(num):
    bag_a = ['pencil']
    bag_b = ['ball pen']
    bag_c = ['pencil','ball pen']
    bags = [bag_a,bag_b,bag_c]
    try:
        if len(bags[num-1]) == 1 and 'pencil' in bags[num-1]:
            return 'Because this bag is only one pencil inside, the other two, one is only ball pen inside the other one is mixed.'
        if len(bags[num-1]) == 1 and 'ball pen' in bags[num-1]:
            return 'Because this bag is only one ball pen inside, the other two, one is only pencil inside the other one is mixed.'
        if len(bags[num-1]) > 1:
            return 'Because this bag is mixed, the other two, one is one pencil inside, the other is one ball pen inside.'
    except:
        return main(eval(input("PLEASE ENTER NUMBER 1-3:")))
if __name__ == "__main__":
    result = main(eval(input("PLEASE ENTER NUMBER 1-3:")))
    print(result)