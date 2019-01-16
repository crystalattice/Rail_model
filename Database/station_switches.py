from string import ascii_lowercase

switches = []
for i in range(1, 5):
    for x in ascii_lowercase[:2]:
        switches.append("{}{}".format(i, x))

if __name__ == "__main__":
    print(switches)
