# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for x in "ABCD":
#   print(x)

# for x in range(1, 100, 10):
#     print(x, end=" ")
# print()

# baris = 1
# while (baris < 4):
for baris in range(1, 6):

    for kolom in range(1, 6):
        char = "X"
        if baris % 2 == 0:
            char = "O"
            if kolom % 2 == 0:
                char = "X"
        else:
            char = "X"
            if kolom % 2 == 0:
                char = "O"
        
        print(char, end="")

    print()

    # kolom = 1
    # while(kolom <=50):
    #     print("-", end="")
    #     kolom = kolom + 5

    # baris = baris + 1
