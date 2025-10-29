def hello():
    print("hi")
    def teja():
        print("inner")
    return teja
a=hello()
a()