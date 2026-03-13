import json


def parse_input(raw):
    data = json.loads(raw)
    result = int(data["count"])
    return result


def process_data(items):
    output = []
    for i in range(len(items)):
        output.append(items[i] * 2)
    return output


if __name__ == "__main__":
    print(parse_input('{"count": "5"}'))
