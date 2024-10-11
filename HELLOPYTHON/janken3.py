import random

def janken(num_players):
    # 勝敗をカウントする
    wins = [0] * num_players
    rounds = 3

    for _ in range(rounds):
        # 各プレイヤーの選択をランダムに生成
        choices = [random.randint(0, 2) for _ in range(num_players)]
        
        # 勝敗を判定
        round_results = []
        for i in range(num_players):
            if choices[i] == 0:
                hand = "グー"
            elif choices[i] == 1:
                hand = "チョキ"
            else:
                hand = "パー"
            round_results.append(hand)
        
        print("選択:", round_results)

        # 勝利者を判定
        unique_choices = set(choices)
        if len(unique_choices) == 1:
            result = "全員引き分け"
        elif len(unique_choices) == 3:
            result = "全員の勝敗がつかない"
        else:
            # 勝者を決める
            if (0 in choices and 1 in choices) and (2 not in choices):
                winners = [i for i in range(num_players) if choices[i] == 0]
            elif (1 in choices and 2 in choices) and (0 not in choices):
                winners = [i for i in range(num_players) if choices[i] == 1]
            elif (2 in choices and 0 in choices) and (1 not in choices):
                winners = [i for i in range(num_players) if choices[i] == 2]
            else:
                winners = []

            # 勝者をカウント
            for winner in winners:
                wins[winner] += 1
            
            result = "勝者: " + ", ".join(f"プレイヤー{winner + 1}" for winner in winners)

        print(result)

    # 最終結果を表示
    print("\n最終結果:")
    for i in range(num_players):
        print(f"プレイヤー{i + 1}の勝ち: {wins[i]}")

# 使用例
if __name__ == "__main__":
    num_players = int(input("参加者の人数を入力してください（3人以上）: "))
    if num_players < 3:
        print("3人以上の参加者を指定してください。")
    else:
        janken(num_players)
