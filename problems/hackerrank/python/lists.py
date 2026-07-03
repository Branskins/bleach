def run_commands(commands: list[str]) -> list[list[int]]:
    lst: list[int] = []
    outputs: list[list[int]] = []
    for command in commands:
        parts = command.split()
        op = parts[0]
        if op == "insert":
            lst.insert(int(parts[1]), int(parts[2]))
        elif op == "print":
            outputs.append(lst.copy())
        elif op == "remove":
            lst.remove(int(parts[1]))
        elif op == "append":
            lst.append(int(parts[1]))
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()
    return outputs


if __name__ == "__main__":
    n = int(input())
    commands = [input() for _ in range(n)]
    for result in run_commands(commands):
        print(result)
