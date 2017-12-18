import LevelMaker
from QQDancerLog import Logger

musicInfo= dict(
	 diffculty = 1,
     bpm =68.0,
     duration = 240,
     EnterTime = 1.1,
     seg0 = 80,
     seg1 = 160
	)

for i in range(64,65):
	musicInfo["bpm"] = i
	for j in range(1,11):
		musicInfo["diffculty"] = j
		LevelMaker.GenerateLevelFile("outlevel_"+str(i)+"_"+str(j)+".xml",musicInfo,Logger(""))