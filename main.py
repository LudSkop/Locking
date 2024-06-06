def main():
    print("Ласкаво просимо в асистент бота!!!>>>")

    while True:
        user_input = input("Введіть вашу команду : >>> ").strip().lower()
        if user_input in ["exit", "close"]:
            print("До побачення!!!")
            break
        elif user_input == "привіт":
            print("Привіт чим можу допомогти?")
        else:
            print("Ви ввели некоректну команду!!!")


if __name__ == "__main__":
    main()
