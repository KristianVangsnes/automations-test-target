def convert_value(x):
    try:
        return int(x)
    except ValueError as exc:
        raise ValueError(f"Invalid integer input: {x!r}") from exc


if __name__ == "__main__":
    print(convert_value("42"))
