"""
区間スケジューリング問題
N個の仕事があり、i(=0, 1, ・・・, N - 1)番目の仕事は時刻s[i]に開始し、
時刻t[i]に終了する。これらの中から自分が行う仕事をできるだけ多く選びたいとする。
ただし、時刻が重なっている複数の仕事を選ぶことはできない。
最大何個の仕事をこなすことができるか。
"""

"""
考え方
①まず「区間の終端時刻」が小さい順にソートする
<命題１>
最も終端時刻が早い区間をpとするとき、区間pを選択することは最適である。
<命題１の証明>
方針：任意の「区間の選び方」に対して、選ぶ区間の個数を減らすことなく、
その中に区間pが含まれるように変更を加えることができることを示す。

任意の区間の選び方xにおいて、「そのうち最も左にある区間」をp'とする。
このときpは「最も終端時刻の早い区間」であることより、
    区間pの終端時刻 <= 区間p'の終端時刻
を満たす。一方、xにおいてp'以外の任意の区間qに対して、
    区間p'の終端時刻 <= 区間qの開始時刻
を満たす。以上より、
    区間pの終端時刻 <= 区間qの開始時刻
を満たす。
よって、区間の選び方xにおいてp'をpと交換しても、
選んだ区間の個数を悪化させることなく、区間の重なりがない状態を保持できる。(証明終了)

以上より、次に以下の手順をふむ
②残っている区間のうち、終端時刻が早いものを選ぶ
③その選んだ区間と重なる区間を消す
"""

import operator

n = int(input())
st = list(list(map(int, input().split())) for _ in range(n))

#リストの任意の位置の値にしたがってソート
st = sorted(st, key = operator.itemgetter(1))

#print(st)

#貪欲に選ぶ
res = 0
current_end_time = 0
for i in range(n):
    #最後に選んだ区間とかぶるものは除く
    #print("current_end_time = " + str(current_end_time))
    if st[i][0] < current_end_time:
        continue
    res += 1
    current_end_time = st[i][1]
print(res)
