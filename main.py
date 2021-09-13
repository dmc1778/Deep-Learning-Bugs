

def main():
    f = open("apis.txt", "r")
    bug_list = []
    lines = f.readlines()
    for bug in lines:
        bug_list.append(bug)
    bug_list = [item.strip() for item in bug_list]
    bug_list = set(bug_list)
    print(bug_list)

if __name__ == "__main__":
    main()
