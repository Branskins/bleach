def runner_up_score(scores: list[int]) -> int:
    return sorted(set(scores))[-2]


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    print(runner_up_score(list(arr)))
