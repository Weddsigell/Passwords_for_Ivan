from tkinter import *


def has_digit(str):
    return any(symbol.isdigit() for symbol in str)


def is_long(str):
    return len(str) >= 12


def has_letters(str):
    return any(symbol.isalpha() for symbol in str)


def has_upper_letters(str):
    return any(symbol.isupper() for symbol in str)


def has_lower_letters(str):
    return any(symbol.islower() for symbol in str)


def has_symbol(str):
    return any(not (symbol.isalpha() or symbol.isdigit()) for symbol in str)


def grade_pass(str):
    checklist = [
        has_digit,
        is_long,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbol
    ]
    score = 0

    for func in checklist:
        if func(str):
            score += 2

    return score


def validate(str):
    label ["text"] = f"Рейтинг вашего пароля: {grade_pass(str)}"
    return True


def main():
    root = Tk()
    root.title("Оценка пароля")
    root.geometry("300x80")

    check = (root.register(validate), "%P")
    field_pass = Entry(validate="key", validatecommand=check)
    field_pass.pack(anchor=N, padx=8, pady=8)
    global label
    label = Label(text="Рейтинг вашего пароля: 0")
    label.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
