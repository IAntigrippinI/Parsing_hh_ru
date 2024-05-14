from collecting_data import collect_data
from find_sim_fum import find_similar
from config import INFO_TEXT


def start():
    print("in start")
    print(INFO_TEXT)
    for i in range(1, 3):
        specialization_for_find = input("Ввод: ")
        if specialization_for_find == "exit":
            break
        elif specialization_for_find.isdigit():
            collect_data(int(specialization_for_find))
        else:
            print(find_similar(specialization_for_find.lower()))


def main():
    start()


if __name__ == "__main__":

    import os

    if not os.path.exists("data"):
        os.makedirs("data")
    main()
