import sqlite3
from data import Baseball
import datetime



baseball = Baseball()
date, home_team, away_team, home_score, away_score, inning = baseball.all_game()


day = datetime.datetime.now()
month = '{0:02d}'.format(int(date[:date.find('月')]))
date = '{0:02d}'.format(int(date[date.find('月')+1:date.find('日')]))
today = '{}-{}-{}'.format(day.year, month, date)


# 接続。なければDBを作成する。
conn = sqlite3.connect('./database/baseball.db')
 
# カーソルを取得
c = conn.cursor()
 
# テーブルを作成
# c.execute('CREATE TABLE all_game (id int(1), date date, home_team text, away_team text, home_score text, away_score text, inning text)')
# c.execute('CREATE TABLE pitch (id int(1), date date, win_team text, win_player text, win_num text, lose_team text, lose_player text, lose_num text, save_team, save_player text text, save_num text)')
# c.execute('CREATE TABLE homerun (id int(1), date date, hr_id int, team text, player text, hr_num text)')
# c.execute('CREATE TABLE ranking (id int(1), date date, num text, team text, game_diff text)')



def check(table):
  n = 0
  sql = "SELECT * FROM {} WHERE date = '{}'".format(table, today)
  for row in c.execute(sql):
    n = 1
  if n == 1:
    delete = "DELETE FROM {} WHERE date = '{}'".format(table, today)
    c.execute(delete)




# 全ての試合
check('all_game')

for n in range(len(home_team)):
  insert = "INSERT INTO all_game VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(n, today, home_team[n], away_team[n], home_score[n], away_score[n], inning[n])
  c.execute(insert)

show = "SELECT * FROM all_game WHERE date = '{}'".format(today)
print("\n----試合結果------------------------------------------------")
for row in c.execute(show):
  print(row)
print("------------------------------------------------------------")




f_t = open('C:/Users/c.daiki/Desktop/production/概要欄/タイトル.txt', 'w')
f_t.write('{}月{}日  プロ野球ニュース  '.format(day.month, day.day))
f_t.write('今日のホームラン')

f_g = open('C:/Users/c.daiki/Desktop/production/概要欄/概要欄.txt', 'w')
f_g.write('{}月{}日プロ野球ニュース\n\n'.format(day.month, day.day))
f_g.write('今日のホームラン\n')


# 勝利投手，敗戦投手，ホームラン
check('pitch')
check('homerun')

for i in range(len(home_team)):
  win, lose, save, home_hr, away_hr = baseball.detail_game(i)

  if len(save) == 0:
    save_team = ''
    save_player = ''
    save_num = ''
  else:
    save_team = save[0].replace('[','').replace(']','')
    save_player = save[1]
    save_num = save[2]

  if len(win) == 0:
    win_team = ''
    win_player = ''
    win_num = ''
    lose_team = ''
    lose_player = ''
    lose_num = ''
  else:
    win_team = win[0].replace('[','').replace(']','')
    win_player = win[1]
    win_num = win[2]
    lose_team = lose[0].replace('[','').replace(']','')
    lose_player = lose[1]
    lose_num = lose[2]
  
  insert = "INSERT INTO pitch VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, today, win_team, win_player, win_num, lose_team, lose_player, lose_num, save_team, save_player, save_num)
  c.execute(insert)
  

  if home_hr:
    if len(home_hr) == 1:
      insert = "INSERT INTO homerun VALUES ({}, '{}', 0, '{}', '', '')".format(i, today, home_hr[0])
      c.execute(insert)
    else:
      for j in range(int(len(home_hr)/2)):
        if j == 0:
          f_t.write(' [{}]{}'.format(home_hr[0], home_hr[2*j+1]))
          f_g.write('{}  {} {}'.format(home_hr[0], home_hr[2*j+1], home_hr[2*j+2]))
        else:
          f_t.write(',{}'.format(home_hr[2*j+1]))
          f_g.write(', {} {}'.format(home_hr[2*j+1], home_hr[2*j+2]))
        insert = "INSERT INTO homerun VALUES ({}, '{}', 0, '{}', '{}', '{}')".format(i, today, home_hr[0], home_hr[2*j+1], home_hr[2*j+2])
        c.execute(insert)
      f_g.write('\n')

  if away_hr:
    if len(away_hr) == 1:
      insert = "INSERT INTO homerun VALUES ({}, '{}', 1, '{}', '', '')".format(i, today, away_hr[0])
      c.execute(insert)
    else:
      for j in range(int(len(away_hr)/2)):
        if j == 0:
          f_t.write(' [{}]{}'.format(away_hr[0], away_hr[2*j+1]))
          f_g.write('{}  {} {}'.format(away_hr[0], away_hr[2*j+1], away_hr[2*j+2]))
        else:
          f_t.write(',{}'.format(away_hr[2*j+1]))
          f_g.write(', {} {}'.format(away_hr[2*j+1], away_hr[2*j+2]))
        insert = "INSERT INTO homerun VALUES ({}, '{}', 1, '{}', '{}', '{}')".format(i, today, away_hr[0], away_hr[2*j+1], away_hr[2*j+2])
        c.execute(insert)
      f_g.write('\n')

f_t.close()
f_g.write('\nプロ野球\nプロ野球結果\nプロ野球ニュース\nプロ野球速報\nプロ野球まとめ\nプログラミング\npython\nmanim\n制作段階')
f_g.close()

show = "select * from pitch where date = '{}'".format(today)
print("\n-----投手成績-----------------------------------------------")
for row in c.execute(show):
  print(row)
print("------------------------------------------------------------")

show = "select * from homerun where date = '{}'".format(today)
print("\n-----ホームラン---------------------------------------------")
for row in c.execute(show):
  print(row)
print("------------------------------------------------------------")








# 順位表
check('ranking')
c_rank, p_rank = baseball.ranking()


for i in range(2):
  if i == 0:
    rank = c_rank
  else:
    rank = p_rank
  for j in range(6):
    insert = "INSERT INTO ranking VALUES ({}, '{}', '{}', '{}', '{}')".format(i, today, rank[j][0], rank[j][1], rank[j][2])
    c.execute(insert)

print("\n----順位表--------------------------------------------------")
print("-------セ・リーグ-------------------------------------------")
show = "SELECT * FROM ranking WHERE date = '{}' AND id = 0".format(today)
for row in c.execute(show):
  print(row)
print("-------パ・リーグ-------------------------------------------")
show = "SELECT * FROM ranking WHERE date = '{}' AND id = 1".format(today)
for row in c.execute(show):
  print(row)
print("------------------------------------------------------------")













print('\n')


# コミット
conn.commit()

# コネクションをクローズ
conn.close()