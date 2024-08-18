# 目的
メタゲームの分析

## やりたいこと
- どんなデッキが勝っているか？
  - 参加人数の少ない大会でだけ結果を残していないか？少人数大会で優勝の結果は評価を下げ、規模の大きな大会のBest8などは評価したい。
  - 同じ人がランクインしてないか？

## 実現方法
1. 晴れる屋のパイオニアメタゲームにアクセスする
2. メタゲーム情報全体の取得
   - デッキ名
   - 使用率
   - 使用数


```mermaid
graph TD
    A[目的: メタゲームの分析]
    B[やりたいこと]
    C[どんなデッキが勝っているか？]
    D[少人数大会での優勝結果は評価を下げる]
    E[規模の大きな大会のBest8は評価する]
    F[同じ人がランクインしてないか？]
    G[実現方法]
    H[1. 晴れる屋のパイオニアメタゲームにアクセスする]
    I[2. メタゲーム情報全体の取得]
    J[デッキ名]
    K[使用率]
    L[使用数]

    A --> B
    B --> C
    C --> D
    C --> E
    B --> F
    A --> G
    G --> H
    G --> I
    I --> J
    I --> K
    I --> L
