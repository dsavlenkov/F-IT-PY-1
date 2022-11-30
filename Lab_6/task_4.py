import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    values = []
    dict_list = []

    with open(filename) as f:
        str_list = f.readlines()
        headers = str_list[0].rstrip().split(delimiter)

        for str_ in str_list[1:]:
            values.append(str_.rstrip().split(delimiter))

        for str_ in values:
            dict_ = {i: j for i, j in zip(headers, str_)}
            dict_list.append(dict_)

    return dict_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
