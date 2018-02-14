import os
for a in os.listdir('c:\windows\system32'):
	if a[-3:] == "exe":
		print a
