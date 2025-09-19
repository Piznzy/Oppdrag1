import random

def main():
    hemmelig_tall = random.randint(1, 10)
    print("=== Gjettespill ===")
    print("Jeg tenker på et tall mellom 1 og 10.")

    forsøk = 0
    while True:
        gjett = int(input("Gjett tallet: "))
        forsøk += 1

        if gjett < hemmelig_tall:
            print("For lavt! Prøv igjen.")
        elif gjett > hemmelig_tall:
            print("For høyt! Prøv igjen.")
        else:
            print(f"Riktig! Du gjettet tallet på {forsøk} forsøk")
            break

if __name__ == "__main__":
    main()
