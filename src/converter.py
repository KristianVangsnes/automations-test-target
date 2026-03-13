def convert_value(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        raise ValueError("convert_value expects a numeric value")


if __name__ == "__main__":
    print(convert_value("42"))
