def free_biscuits(table: dict[str, list[str]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for game in table:
        temp_list: list[str] = table[game]
        total_score: int = 0
        for elem in temp_list:
            total_score += elem
        if total_score == 100:
            result[game] = True
        else:
            result[game] = False
    return result

print(free_biscuits({"UNCvsDuke": [38, 20, 42] , "UNCvsState": [9, 51, 16, 23] }))