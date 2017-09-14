def fibinacci(starts=1, end=2):
    if starts == 1 and end == 2:
        print("%s" % (starts))
        print("%s" % (end))
    sumOfSE = starts + end
    print("%s" % (sumOfSE))
    if sumOfSE < 100:
        fibinacci(end, sumOfSE)


fibinacci()
