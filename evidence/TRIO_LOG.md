# Snake Trio Log

## Members and first roles

- Driver: 吳赫宥
- Navigator: 盧一君
- Tester / Recorder: 黃皆益

Rotate roles after each completed TODO.

## Gate record

| Gate | Driver | Navigator | Tester / Recorder | Observed result | Next action |
|---|---|---|---|---|---|
| Baseline | 吳赫宥 | 盧一君 | 黃皆益 | `NotImplementedError` on `next_head` | 實作 TODO 1，替換掉 raise 佔位符 |
| TODO 1 - next head | 吳赫宥 | 盧一君 | 黃皆益 | `next_head` 測試全數亮綠燈 | 提交 PR，並切換分支準備實作 TODO 2 |
| TODO 2 - food | 吳赫宥 | 盧一君 | 黃皆益 | `ate_food` 測試全數亮綠燈 | 提交 PR，並切換分支準備實作 TODO 3 |
| TODO 3 - wall | 吳赫宥 | 盧一君 | 黃皆益 | `hit_wall` 邊界測試亮綠燈 | 提交 PR，並切換分支準備實作 TODO 4 |
| TODO 4 - body | 吳赫宥 | 盧一君 | 黃皆益 | `advance_body` 測試與整合測試皆通過 | 提交 PR，準備啟動 Pygame 進行實機遊玩 |
| Playable run | 吳赫宥 | 盧一君 | 黃皆益 | 蘋果生成不碎機 | 修改game.py |

## Explain-back

1. Which function was easiest to test, and why?
`ate_food` 最容易測試。因為它的合約與邏輯最為單純，只需要使用 `==` 來判斷兩個 Tuple（蛇頭座標與食物座標）是否完全相等即可，不需要處理像素乘法或串列切片等複雜操作。
2. Which failing test gave the clearest clue?
最一開始的 `NotImplementedError: TODO 1: compute the next head` 給了最明確的線索。完整的 Traceback 加上錯誤訊息，精準地指出了程式在 `logic.py` 中停在哪一行，讓我們馬上知道必須先替換掉預設的佔位符。
3. What did your trio ask AI at L1, and what decision remained human-owned?
我們向 AI 詢問了 `pytest` 找不到模組的匯入錯誤（ImportError 解決方案），以及 Git 在發生「無關歷史紀錄合併拒絕」時的指令解法。然而，關於「該挑選哪些邊界數值來撰寫 Trio 專屬測試」以及「如何落實輪替開發與互相審查 PR」的決策，完全由我們小組成員自行主導與掌控。