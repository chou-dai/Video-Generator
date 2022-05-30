import sqlite3
from data import Baseball
import datetime

day = datetime.datetime.now()


baseball = Baseball()







# 接続。なければDBを作成する。
conn = sqlite3.connect('baseball.db')
 
# カーソルを取得
c = conn.cursor()
 
# # テーブルを作成
# c.execute('CREATE TABLE all_game (id int(1), date date, home_team text, away_team text, home_score int, away_score int, inning text)')
# c.execute('DROP TABLE pitch')
# c.execute('CREATE TABLE pitch (id int(1), date date, win text, win_num text, lose text, lose_num text, save text, save_num text)')
# c.execute('DROP TABLE detail_game')
# c.execute('DROP TABLE pitch')
# c.execute('CREATE TABLE ranking (id int(1), date date, num text, team text, game_diff text)')
# c.execute('CREATE TABLE pitch (id int(1), date date, win_team text, win text, win_num text, lose_team text, lose text, lose_num text, save_team, save text text, save_num text)')
# c.execute('CREATE TABLE homerun (id int(1), date date, hr_id int, team text, player text, hr_num text)')
















#ゲーム
date, home_team, away_team, home_score, away_score, inning = baseball.all_game()
month = '{0:02d}'.format(int(date[:date.find('月')]))
date = '{0:02d}'.format(int(date[date.find('月')+1:date.find('日')]))
today = '{}-{}-{}'.format(day.year, month, date)

# n=0
# sql = "select * from all_game where date = '{}'".format(today)
# for row in c.execute(sql):
#   n=1
# if n==1:
#   a = "DELETE FROM all_game WHERE date = '{}'".format(today)
#   c.execute(a)

# for n in range(len(home_team)):
#   a = "INSERT INTO all_game VALUES ({}, '{}', '{}', '{}', {}, {}, '{}')".format(n, today, home_team[n].text, away_team[n].text, 0, away_score[n].text, inning[n].text)
#   c.execute(a)

# sql = "select * from all_game where date = '{}'".format(today)
# print("----試合結果------------------------------------------------")
# for row in c.execute(sql):
#   print(row)
# print("------------------------------------------------------------")




#ピッチャー
k=0

sql1 = "select * from pitch where date = '{}'".format(today)
for row in c.execute(sql1):
  k=1
if k==1:
  b = "DELETE FROM pitch WHERE date = '{}'".format(today)
  c.execute(b)

sql1 = "select * from homerun where date = '{}'".format(today)
for row in c.execute(sql1):
  k=1
if k==1:
  b = "DELETE FROM homerun WHERE date = '{}'".format(today)
  c.execute(b)

for n in range(len(home_team)):
  win, lose, save, home_hr, away_hr = baseball.detail_game(n)
  if len(save) == 0:
    st = ''
    s = ''
    sn = ''
  else:
    st = save[0].replace('[','').replace(']','')
    s = save[1]
    sn = save[2]
  if len(win) == 0:
    wt = ''
    w = ''
    wn = ''
    lt = ''
    l = ''
    ln = ''
  else:
    wt = win[0].replace('[','').replace(']','')
    w = win[1]
    wn = win[2]
    lt = lose[0].replace('[','').replace(']','')
    l = lose[1]
    ln = lose[2]

  if len(home_hr)==1:
    aa = "INSERT INTO homerun VALUES ({}, '{}', 0, '{}', '', '')".format(n, today, home_hr[0])
    c.execute(aa)
  else:
    for i in range(int(len(home_hr)/2)):
      aaa = "INSERT INTO homerun VALUES ({}, '{}', {}, '{}', '{}', '{}')".format(n, today, i+1, home_hr[0], home_hr[2*i+1], home_hr[2*i+2])
      c.execute(aaa)

  if len(away_hr)==1:
    cc = "INSERT INTO homerun VALUES ({}, '{}', 1, '{}', '', '')".format(n, today, away_hr[0])
    c.execute(cc)
  else:
    for i in range(int(len(away_hr)/2)):
      ccc = "INSERT INTO homerun VALUES ({}, '{}', {}, '{}', '{}', '{}')".format(n, today, i+1, away_hr[0], away_hr[2*i+1], away_hr[2*i+2])
      c.execute(ccc)


  b = "INSERT INTO pitch VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(n, today, wt, w, wn, lt, l, ln, st, s, sn)
  c.execute(b)
sql = "select * from pitch where date = '{}'".format(today)
print("-----投手成績-----------------------------------------------")
for row in c.execute(sql):
  print(row)
print("------------------------------------------------------------")

sql = "select * from homerun where date = '{}'".format(today)
print("-----ホームラン-----------------------------------------------")
for row in c.execute(sql):
  print(row)
print("------------------------------------------------------------")




# #順位
# c_rank, p_rank = baseball.ranking()
# n=0
# sql = "select * from ranking where date = '{}'".format(today)
# for row in c.execute(sql):
#   n=1
# if n==1:
#   a = "DELETE FROM ranking WHERE date = '{}'".format(today)
#   c.execute(a)
# for m in range(2):
#   if m == 0:
#     rank = c_rank
#   else:
#     rank = p_rank
#   for n in range(6):
#     a = "INSERT INTO ranking VALUES ({}, '{}', '{}', '{}', '{}')".format(m, today, rank[n][0], rank[n][1], rank[n][2])
#     c.execute(a)
# print("-----順位表-----------------------------------------------")
# print("-----セ・リーグ-----------------------------------------------")
# sql = "select * from ranking where date = '{}'AND id = 0".format(today)
# for row in c.execute(sql):
#   print(row)
# print("-----パ・リーグ-----------------------------------------------")
# sql = "select * from ranking where date = '{}'AND id = 1".format(today)
# for row in c.execute(sql):
#   print(row)
# print("------------------------------------------------------------")







 
# コミット
conn.commit()


# コネクションをクローズ
conn.close()