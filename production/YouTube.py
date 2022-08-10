import os
import glob
import shutil
import datetime
import moviepy.editor as mp
from moviepy.video.compositing.concatenate import concatenate_videoclips
import cv2
from pydub import AudioSegment


bgm_list = {1:'sample01', 2:'炎の挑戦', 3:'勝者', 4:'LockYou'}
BGM = bgm_list[3]



def remove(path):
  files = glob.glob(path)
  for p in files:
    os.remove(p)


# -----------main---------------------

# 削除
path = [
  '/production/media/videos/main/480p15/partial_movie_files/InteractiveDevlopment/*', 
  '/production/media/videos/main/1080p60/partial_movie_files/InteractiveDevlopment/*', 
  '/production/media/videos/thumbnail/480p15/partial_movie_files/InteractiveDevlopment/*',
  '/production/media/videos/shorts/480p15/partial_movie_files/InteractiveDevlopment/*',
  '/production/media/videos/shorts/1080p60/partial_movie_files/InteractiveDevlopment/*',
  '/production/media/images/main/*',
  '/production/media/texts/*',
  '/production/YouTube/*'
]
for n in range(len(path)):
  remove(path[n])

# タイトル・概要欄
ttl = '/production/概要欄/タイトル.txt'
text = '/production/概要欄/概要欄.txt'
youtube = '/production/YouTube'
shutil.copy(ttl, youtube)
shutil.copy(text, youtube)

# サムネイル
thum = '/production/media/images/thumbnail/InteractiveDevlopment_ManimCE_v0.7.0.png'
today = datetime.datetime.now()
png = youtube + '/{}月{}日 プロ野球ニュース.png'.format(today.month, today.day)
try:
  os.rename(thum, png)
except FileNotFoundError:
  print('サムネイルがありません')

# BGM
videoPath = '/production/media/videos/main/1080p60/InteractiveDevlopment.mp4'
samplePath = '/production/bgm/' + BGM +'.mp3'
bgmPath = '/production/bgm/bgm.mp3'
shutil.copy(samplePath, bgmPath)
cap = cv2.VideoCapture(videoPath)
time = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
sound = AudioSegment.from_file(bgmPath, format="mp3")
bgm = sound[:(time+1)*1000]
decreced = bgm - 15
decreced.export(bgmPath, format="mp3")
clip = mp.VideoFileClip(videoPath).subclip()
today = datetime.datetime.now()
video = '{}月{}日 プロ野球ニュース.mp4'.format(today.month, today.day)
clip.write_videofile(video, audio=bgmPath)
shutil.move(video,'./YouTube')

#ファイル開く
os.startfile(youtube)
