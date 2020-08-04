def test(i):
    if(i<=10):
        i=i+1
        test(i)
        #test(i)
        print("After Calling Test",i)

test(5)