# Red-to-Green Debug Log

Preserve one genuine failure. Do not invent a retrospective story after the test is green.

| Field | Trio record |
|---|---|
| Command that failed | `python -m pytest tests_public/test_snake_contract.py` |
| Exact failing test | `test_next_head_moves_exactly_one_cell` |
| Last useful line / observed fact | `E       NotImplementedError: TODO 1: compute the next head` |
| Expected behavior from the contract | 函式應根據目前座標、方向與格子大小，計算並回傳下一格的 `(x, y)` 座標。 |
| Smallest hypothesis | `next_head` 函式尚未實作，目前僅包含一個用來佔位的 `NotImplementedError` 例外拋出。 |
| Smallest code change | 刪除 `raise` 佔位符，替換為：`x, y = head; dx, dy = direction; return (x + dx * cell_size, y + dy * cell_size)` |
| Focused rerun command | `python -m pytest tests_public/test_snake_contract.py -k 'next_head' -q` |
| Focused result | `2 passed` |
| Full regression result | 全部綠燈 (All tests passed) |
| Commit or PR URL | `https://github.com/aoscar0717-lang/lab03-snake-trio/pull/1` |

## Explain-back

What evidence rules out at least one alternative cause?
終端機印出的 Traceback 精確指出了錯誤發生在 `src\snake_trio\logic.py:26` 的 `NotImplementedError`
