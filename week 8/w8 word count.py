from sys import stdin
print(
    len(
        set(
            open(
                'input.txt',
                'r', encoding='utf8'
            )
            .read()
            .split()
        )
    )
)
