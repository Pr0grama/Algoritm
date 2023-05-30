def heapify(mas, n, i):
    biggest = i 
    l = 2 * i + 1  
    r = 2 * i + 2 
    if l < n and mas[i] < mas[l]:
        biggest = l
    if r < n and mas[biggest] < mas[r]:
        biggest = r
    if biggest != i:
        mas[i],mas[biggest] = mas[biggest],mas[i]
        heapify(mas, n, biggest)

def heapSort(mas):
    n = len(mas)
    for i in range(n, -1, -1):
        heapify(mas, n, i)
    for i in range(n-1, 0, -1):
        mas[i], mas[0] = mas[0], mas[i]
        heapify(mas, i, 0)

mas = [ 12, 11, 13, 5, 6, 7, 8, 10, 20, 35]
heapSort(mas)
n = len(mas)
for i in range(n):
    print ("%d" %mas[i]),