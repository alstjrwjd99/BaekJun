def solution(commands):
    answer = []

    # 초기화
    parent = {(r, c): (r, c) for r in range(1, 51) for c in range(1, 51)}
    value = {(r, c): 'EMPTY' for r in range(1, 51) for c in range(1, 51)}

    def find(cell):
        """Find the representative cell of the group."""
        if parent[cell] != cell:
            parent[cell] = find(parent[cell])
        return parent[cell]

    def union(cell1, cell2):
        """Union two cells into the same group."""
        root1, root2 = find(cell1), find(cell2)
        if root1 != root2:
            # 병합 시 값 동기화
            if value[root1] == 'EMPTY':
                parent[root1] = root2
            else:
                parent[root2] = root1

    def update_cell(r, c, new_value):
        """Update a specific cell or its group with a new value."""
        root = find((r, c))
        value[root] = new_value

    def update_all(old_value, new_value):
        """Update all cells with a specific value."""
        for cell in value:
            if value[cell] == old_value:
                value[cell] = new_value

    def merge_cells(r1, c1, r2, c2):
        """Merge two cells into one group."""
        cell1, cell2 = (r1, c1), (r2, c2)
        if find(cell1) != find(cell2):
            union(cell1, cell2)

    def unmerge_cell(r, c):
        """Unmerge a cell and restore its previous state."""
        root = find((r, c))
        original_value = value[root]
        group_cells = [cell for cell in value if find(cell) == root]

        for cell in group_cells:
            parent[cell] = cell
            value[cell] = 'EMPTY'

        value[(r, c)] = original_value

    def print_cell(r, c):
        """Add the value of a cell to the answer."""
        root = find((r, c))
        answer.append(value[root])

    # 명령어 처리
    for command in commands:
        cmd = command.split()
        if cmd[0] == "UPDATE":
            if len(cmd) == 4:
                update_cell(int(cmd[1]), int(cmd[2]), cmd[3])
            else:
                update_all(cmd[1], cmd[2])
        elif cmd[0] == "MERGE":
            merge_cells(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
        elif cmd[0] == "UNMERGE":
            unmerge_cell(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "PRINT":
            print_cell(int(cmd[1]), int(cmd[2]))

    return answer