fiboEnd = int(input("Enter the number to display th fibonacci series: "))
fiboSeries = []
sequence1 = 0
sequence2 = 1

def fibonacciSeries(fibonacci, seq1, seq2):
    i = 0
    for i in range(int(fibonacci)):
        seq2 = seq1 + seq2
        fiboSeries.append(seq2)
        seq1 = seq1 + seq2
        fiboSeries.append(seq1)
        print(str(seq1) + " " + str(seq2))
        i += 1
    return fiboSeries

print(fibonacciSeries(fiboEnd, sequence1, sequence2))
