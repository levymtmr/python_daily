cell_1_position = {"x": 1, "y": 1, "status_value": "flagged"}
cell_2_position = {"x": 1, "y": 2, "status_value": "clear"}
cell_3_position = {"x": 1, "y": 3, "status_value": "flagged"}


game_board = [cell_1_position, cell_2_position, cell_3_position]


def is_flagged(cell):
    if cell["status_value"] == "flagged":
        return True


def get_flagged_cells():
    flagged_cells = []
    for cell in game_board:
        if is_flagged(cell):
            flagged_cells.append(cell)
    return flagged_cells


print(get_flagged_cells())
