print("f(x) = 4x³ + 7x - 5, x ≥ 0")
print("f(x) = 3x² - 5x + 1, x < 0")
print("g(x) = (f(x))² - f(x)")
print("h(x) = f(x) × g(x)")

isix = []
isif = []
isig = []
isih = []


ulang = 'Y'
while ulang.upper() == 'Y':
    n = int(input("Input banyak data n: "))

    for i in range(n):
        x = int(input(f"Input x ke-{i+1}: "))  
        isix.append(x)

        if x >= 0:
            f = 4 * x**3 + 7 * x - 5
        else:
            f = 3 * x**2 - 5 * x + 1
        isif.append(f)

        g = f**2 - f
        isig.append(g)

        h = f * g
        isih.append(h)

    print("-----------------------------------------------------------------")
    print("| No |     x     |    f(x)     |     g(x)      |      h(x)      |")
    print("-----------------------------------------------------------------")
    for i in range(n):
        print(f"| {i+1:>2} | {isix[i]:>9} | {isif[i]:>11} | {isig[i]:>13} | {isih[i]:>14} |")
    print("-----------------------------------------------------------------")
  
    ulang = input("\nInput nilai x lagi Y/N? ")
    if ulang.upper() == 'Y':
        isix = []
        isif = []
        isig = []
        isih = []
