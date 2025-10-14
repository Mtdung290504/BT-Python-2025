def create_dict(max: int):
    target_dict = dict()
    for i in range(max):
        i += 1
        target_dict[i] = i**2
    print(f"Created dict(max={max}):", target_dict)
    return target_dict


def print_item(target_dict: dict):
    print("Dict items:")
    for key, val in target_dict.items():
        print(f"\t- Dict item: [{key}: {val}]")


def print_key(target_dict: dict):
    print("Dict keys:")
    for key in target_dict:
        print(f"\t- Dict key: [{key}]")


def print_value(target_dict: dict):
    print("Dict values:")
    for val in target_dict.values():
        print(f"\t- Dict value: [{val}]")
