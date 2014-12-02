#!/usr/bin/env python

import pcd8544.lcd as lcd
import sys

if __name__ == "__main__":
	lcd.init()
	lcd.set_contrast(190)
	if sys.argv[1] == 'text':
		lcd.locate(int(sys.argv[2]),int(sys.argv[3]))
		lcd.text(sys.argv[4])
	if sys.argv[1] == 'backlight':
		lcd.backlight(int(sys.argv[2]))
	if sys.argv[1] == 'cls':
		lcd.cls()