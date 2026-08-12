# Four Function Contracts

Write examples before implementation. Do not paste function bodies here.

| Function | Accepted input | Returned result | Invariant / non-goal | Failure or boundary examples |
|---|---|---|---|---|
| `next_head` | 目前蛇頭座標 `(x, y)`，方向向量 `(dx, dy)`。 | 新蛇頭座標 `(x + dx, y + dy)`。 | 不會改動輸入值 (Does not mutate input)。 | **一般範例：** `(5,5), (0,-1) -> (5,4)`<br>**邊界範例：** `(0,0), (-1,0) -> (-1,0)` (移出邊界；驗證是否出界並非此函式的目標)。 |
| `ate_food` | 蛇頭座標 `(x, y)`，食物座標 `(x, y)`。 | 布林值：若座標完全相同回傳 `True`，否則回傳 `False`。 | 精確的單元格相等 (Exact cell equality)。 | **一般範例：** `(2,3), (2,3) -> True`<br>**邊界範例：** `(2,3), (3,2) -> False` (相鄰但不相等)。 |
| `hit_wall` | 蛇頭座標 `(x, y)`，網格寬度 `width` (int)，網格高度 `height` (int)。 | 布林值：若蛇頭超出了 `0` 到 `width-1` / `height-1` 的範圍則回傳 `True`。 | 棋盤邊界是公開的 (Board edges are published)。 | **一般範例：** `(5,5), 10, 10 -> False`<br>**邊界範例：** `(10,5), 10, 10 -> True` (剛好越過 10x10 網格的右側邊界)。 |
| `advance_body` | 目前的身體串列 `[(x,y), ...]`，新蛇頭 `(x,y)`，是否成長 `grow` (bool)。 | 代表更新後蛇身的全新串列 (A new list)。 | 回傳新的串列 (Returns a new list)。 | **一般 (不成長)：** `[(2,2), (2,3)], (2,1), False -> [(2,1), (2,2)]`<br>**邊界 (成長)：** `[(2,2)], (2,1), True -> [(2,1), (2,2)]` (尾巴不會被移除)。 |

## Example-to-test bridge

For each function, convert at least one row above into a student-authored test. Write the expected observation before running it.
1. next_head 的測試

預期觀察： 函式應該乘上 cell_size 計算出正確的像素位移，且不應限制或阻擋負數值。

計畫的測試：
```python
def test_next_head_calculates_boundary_offset():
    # 準備 (Arrange)
    current_head = (0, 0)
    direction = (-1, 0) # 向左移動
    cell_size = 20
    # 執行 (Act)
    result = next_head(current_head, direction, cell_size)
    # 斷言 (Assert)
    assert result == (-20, 0)
```
2. ate_food 的測試

預期觀察： 函式應嚴格要求座標完全相符，不相等的座標應回傳 False。

計畫的測試：
```python
def test_ate_food_rejects_adjacent_cells():
    # 準備 (Arrange)
    head = (40, 60)
    food = (60, 40)
    # 執行 (Act)
    result = ate_food(head, food)
    # 斷言 (Assert)
    assert result is False
```
3. hit_wall 的測試

預期觀察： 當寬度為 640 時，X 座標來到 640 已經超出畫面右側邊界（因為從 0 開始，最大合法座標為 620），應回傳 True。

計畫的測試：

```python
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
```
4. advance_body 的測試

預期觀察： 當 grow 為 True 時，會插入新的蛇頭，並且保留舊的尾巴，使總長度增加 1。同時必須驗證原始的串列沒有被修改。

計畫的測試：
```python
def test_advance_body_retains_tail_when_growing():
    # 準備 (Arrange)
    current_body = [(40, 20)]
    new_head = (40, 0)
    # 執行 (Act)
    result = advance_body(current_body, new_head, grow=True)
    # 斷言 (Assert)
    assert result == [(40, 0), (40, 20)]
    assert current_body == [(40, 20)] # 驗證不變量：原始串列未被修改
```