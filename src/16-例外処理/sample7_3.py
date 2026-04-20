# 【例外処理の書き方】

### elseとfinallyを利用した例外処理
try:
    number = int(input('100を割る整数を入力してください:'))
    result = 100 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'正しい整数を入力してください。({e})')
else:
    print(f'計算結果は{result}です。')
    print('正常に計算が終了しました。')
finally:
    print('プログラムを終了します。')