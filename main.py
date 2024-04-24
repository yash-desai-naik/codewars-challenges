from utils import create_df

data: list[int] = [1, 2, 3]


def main() -> None:
    name_: int = 2
    name_ = name_ + 1
    name_ = name_ + 1
    print(name_)
    create_df(data_=data)


if __name__ == '__main__':
    main()
