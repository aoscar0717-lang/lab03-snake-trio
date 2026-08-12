"""Add at least three trio-designed tests.

Write the expected result before running each test. Good targets include a
different direction, an exact board edge, growth by one segment, and proof that
the original body list is unchanged.
"""


def test_replace_with_a_meaningful_name() -> None:
    # Arrange: create the smallest state that proves one contract rule.
    # Act: call exactly one public function.
    # Assert: compare an observable result with your written expectation.
    raise NotImplementedError("Replace this scaffold with the trio's first test")

def test_next_head_calculates_boundary_offset():
    # 準備 (Arrange)
    current_head = (0, 0)
    direction = (-1, 0) # 向左移動
    cell_size = 20
    # 執行 (Act)
    result = next_head(current_head, direction, cell_size)
    # 斷言 (Assert)
    assert result == (-20, 0)

def test_ate_food_rejects_adjacent_cells():
    # 準備 (Arrange)
    head = (40, 60)
    food = (60, 40)
    # 執行 (Act)
    result = ate_food(head, food)
    # 斷言 (Assert)
    assert result is False

def test_hit_wall_detects_right_edge_crossing():
    # 準備 (Arrange)
    head = (640, 200)
    width = 640
    height = 480
    cell_size = 20
    # 執行 (Act)
    result = hit_wall(head, width, height, cell_size)
    # 斷言 (Assert)
    assert result is True

def test_advance_body_retains_tail_when_growing():
    # 準備 (Arrange)
    current_body = [(40, 20)]
    new_head = (40, 0)
    # 執行 (Act)
    result = advance_body(current_body, new_head, grow=True)
    # 斷言 (Assert)
    assert result == [(40, 0), (40, 20)]
    assert current_body == [(40, 20)] # 驗證不變量：原始串列未被修改
