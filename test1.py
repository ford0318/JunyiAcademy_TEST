def main(str1):
    strlist=[ x[::-1] for x in str1.split()]
    return " ".join(strlist)

if __name__ =="__main__":
    # reverse_str = main("junyiacamedy")
    # reverse_str = main("flipped class room is important")
    # print(reverse_str)
    print(main(input("請輸入文字句子:")))