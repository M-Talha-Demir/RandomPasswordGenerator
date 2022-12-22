import random
import numpy as np

alphabetUpper = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alphabetUpper = alphabetUpper.split(", ")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
specialChar = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|",
               '\\', ":", ";", '"', "'", "<", ",", ">", ".", "?", "/"]


password_lenght = random.randint(12, 16)

print(f"Password Lenght is {password_lenght}")

q = np.random.multinomial(password_lenght, [1/4.]*4)

while 0 in q:
    q = np.random.multinomial(password_lenght, [1 / 4.] * 4)

upper, lower, number, special = q
print(f"Password will contain {upper} upper, {lower} lower, {number} number and {special} special character.")

def generatePassword(upper, lower, number, special):
    global alphabetUpper
    global numbers
    global specialChar
    password = ""
    for i in range(upper):
        password +=str(random.choice(alphabetUpper))
    for i in range(lower):
        password +=str(random.choice(alphabetUpper).lower())
    for i in range(number):
        password +=str(random.choice(numbers))
    for i in range(special):
        password +=str(random.choice(specialChar))
    x = [i for i in password]


    #randomize the order
    random.shuffle(x)
    password = ''.join(x)

    return password


print(f"Your Password is {generatePassword(upper, lower, number, special)}")
print(f"Your Alternative Password is {generatePassword(upper, lower, number, special)}")
print(f"Your Second Alternative Password is {generatePassword(upper, lower, number, special)}")
