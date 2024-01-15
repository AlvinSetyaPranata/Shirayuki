from modules.core.base import *
from modules.core.graphic import *
from time import sleep
from random import choice


VORTEX = [('2', 3), ('6', 1), ('3', 3), ('7', 1), ('7', 0)]
NEXT_INTERVALS = [2+(x/10) for x in range(1, 9)]


def isBagFull():
	press("i")
	sleep(1)
	image_buffer = grab_image_in(82, 90, 100, 100)
	return detect_red(image_buffer)

def smart_farming():
	is_full = isBagFull()
	press('ESC')
	combo_length = len(VORTEX)
	counter = 0

	if not is_full:
		print("Begining to farming")

	while not is_full:
		for combo in VORTEX:
			press(combo[0])
			sleep(combo[1])

		sleep(choice(NEXT_INTERVALS))


		# Check bag in every 7 combo
		if counter == 7: 
			is_full = isBagFull()
			sleep(1)
			press("ESC")

		elif counter == 10:
			press(VORTEX[0][0])
			sleep(VORTEX[0][1])

			press(VORTEX[1][0])
			sleep(VORTEX[1][1])

			print("Re-casting Familia")
			press("9")

		elif counter == 13:
			press(VORTEX[0][0])
			sleep(VORTEX[0][1])

			press(VORTEX[1][0])
			sleep(VORTEX[1][1])


			print("Re-casting High Cycle")
			press("5")
			print("Re-casting Brave Aura")
			press("q")
			counter = 0
			continue


		counter += 1

	print("Bag fulled, farm is stopped")