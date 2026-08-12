# AI Use Record - L1

L1 permits explanations, hints, counterexamples, test ideas, and traceback help. It does not permit AI to write or replace the four final function bodies.

| When | Person asking | Question or prompt | Hint received | Human decision and verification |
| 測試階段 (Step 07) | 吳赫宥 | "test 還沒有正確import" 及 "怎麼執行pytest" | AI 從檔案總管截圖中指出資料夾結構為 `snake_trio`，提示正確的匯入路徑應為 `from snake_trio.logic import ...`，並解說了 `pytest -k` 與 `-q` 參數的用法。 | 我比對了本地端的實際資料夾名稱，補上正確的 import 語句，並自行決定使用關鍵字過濾指令來逐一驗證我們寫的四個核心函式。 |
| Git 協作階段 | 吳赫宥 | "PR後忘記調分支怎麼辦" 以及 "能夠直接改道main上嗎" | AI 提醒直接推送到 main 會違反「每個 TODO 一個 PR」的作業規範，並提供了使用 `git reset --hard HEAD~1` 搭配 `git branch` 轉移 commit 的安全解法。 | 我們決定遵守規範不直接動 main 分支，依照指令將寫好的程式碼無痛轉移到正確的 feature 分支，並透過 `git status` 確認狀態後才發布 PR。 |
| 實機遊玩階段 | 吳赫宥 | 要求協助修改 `game.py`，將 `choose_food` 改為隨機生成版本 | AI 建議匯入 `random` 模組

If no AI was used, write: `No AI used.`
