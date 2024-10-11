import random

def janken():
    # 勝敗をカウントする
    player1_wins = 0
    player2_wins = 0
    rounds = 3

    for _ in range(rounds):
        # プレイヤーとコンピュータの選択をランダムに生成
        player1_choice = random.randint(0, 2)  # 0: グー, 1: チョキ, 2: パー
        player2_choice = random.randint(0, 2)

        # 結果を判定
        if player1_choice == player2_choice:
            result = "引き分け"
        elif (player1_choice == 0 and player2_choice == 1) or \
             (player1_choice == 1 and player2_choice == 2) or \
             (player1_choice == 2 and player2_choice == 0):
            result = "あなたの勝ち"
            player1_wins += 1
        else:
            result = "コンピュータの勝ち"
            player2_wins += 1

        # 結果を表示
        hands = {0: "グー", 1: "チョキ", 2: "パー"}
        print(f"Aの手: {hands[player1_choice]}, Bの手: {hands[player2_choice]}, 結果: {result}")

    # 最終結果を表示
    if player1_wins > player2_wins:
        final_result = "Aの勝利！"
    elif player1_wins < player2_wins:
        final_result = "Bの勝利！"
    else:
        final_result = "全体として引き分け！"

    print(f"\n最終結果: Aの勝ち: {player1_wins}, Bの勝ち: {player2_wins}, {final_result}")

# 使用例
if __name__ == "__main__":
    janken()
