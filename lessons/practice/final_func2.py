def max_key(inp_dict: dict[str, list[str]]) -> str:
    max_val: int = 0
    return_str: str = ""
    for key in inp_dict:
        sum: int = 0
        for num in inp_dict[key]:
            sum += num
        if sum > max_val:
            max_val = sum
            return_str = key
    return return_str


print(max_key({"a": [1, 2, 3], "b": [4, 5, 6]}))