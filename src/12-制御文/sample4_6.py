# 【match文 - パターンマッチング】
"""
# IF文のサンプル
action = 'draw'

if action == 'draw':
    result = '描く'
elif action == 'write':
    result = '書く'
elif action == 'erase':
    result = '消す'
else:
    result = 'その他'
print(result)
"""

# if文のコードをmatch文で置き換えた場合
action = 'draw'

match action:
    case 'drow':
        result = '描く'
    case 'write':
        result = '書く'
    case 'erase':
        result = '消す'
    case _:
        result = 'その他'
print(result)