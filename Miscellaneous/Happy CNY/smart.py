import os

mapping = {
    121993: 50,
    110306: 20,
    114820: 10,
    125945: 5,
    132199: 1
}

ascii_decimals = []

for i in range(1, 41, 1):
    folder_name = F"Angpow{i}"
    files = os.listdir(folder_name)

    size = 0

    for file in files:
        file_size = os.path.getsize(f"{folder_name}/{file}")
        size += mapping[file_size]

    ascii_decimals.append(size)

print("".join([chr(money) for money in ascii_decimals]))