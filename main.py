import os


def folder(path):
    files = []
    for obj in os.listdir(path):
        obj_path = f"{path}/{obj}"
        if os.path.isdir(obj_path):
            temp = folder(obj_path)
            for file_name, file_ctime in temp:
                files.append((file_name, file_ctime))
        else:
            files.append((obj_path, os.path.getctime(obj_path)))
    return files


def main():
    path = input("Path: ")
    if not os.path.exists(path):
        print("\nError 1: Директории не существует")
        return -1
    files = sorted(folder(path), key=lambda element: element[1])
    files = sorted(files, key=lambda element: len(element[0]))
    try:
        with open("out.txt", "w") as file:
            for obj in files:
                file.write(f"{obj[0]}\n")
    except OSError as e:
        print(str(e))
        return -2
    return 0


if __name__ == "__main__":
    main()
