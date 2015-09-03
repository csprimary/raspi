import explorerhat
import random
import _thread
import pygame
from random import randint
from time import sleep
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
pos = mc.player.getTilePos()

pygame.init()
pygame.mixer.init()
a = pygame.mixer.Sound("/home/pi/Desktop/tune.wav")


green = 13
yellow = 4
red = 14
blue = 3
timer = 0.3

height= 10

mc.setBlock(pos.x-2, pos.y, pos.z + 10, block.DIAMOND_BLOCK)
mc.setBlock(pos.x+3, pos.y, pos.z + 10, block.DIAMOND_BLOCK)
mc.setBlock(pos.x+1, pos.y -2, pos.z + 10, block.WOOL.id, red)
mc.setBlock(pos.x-1, pos.y -2, pos.z + 10, block.WOOL.id, green)
mc.setBlock(pos.x, pos.y -2, pos.z + 10, block.WOOL.id, yellow)
mc.setBlock(pos.x+2, pos.y -2, pos.z + 10, block.WOOL.id, blue)

def red_block():
    height = 10
    while height>-2:
        mc.setBlock(pos.x+1, pos.y +height, pos.z + 10, block.WOOL.id, red)
        mc.setBlock(pos.x+1, pos.y +height+1, pos.z + 10, block.AIR.id)
        sleep(timer)
        height -=1
    mc.setBlock(pos.x+1, pos.y +height+1, pos.z + 10, block.AIR.id)

def green_block():
    height = 10
    while height>-2:
        mc.setBlock(pos.x-1, pos.y +height, pos.z + 10, block.WOOL.id, green)
        mc.setBlock(pos.x-1, pos.y +height+1, pos.z + 10, block.AIR.id)
        sleep(timer)
        height -=1
    mc.setBlock(pos.x-1, pos.y +height+1, pos.z + 10, block.AIR.id)
    
def yellow_block():
    height = 10
    while height>-2:
        mc.setBlock(pos.x, pos.y +height, pos.z + 10, block.WOOL.id, yellow)
        mc.setBlock(pos.x, pos.y +height+1, pos.z + 10, block.AIR.id)
        sleep(timer)
        height -=1
    mc.setBlock(pos.x, pos.y +height+1, pos.z + 10, block.AIR.id)

def blue_block():
    height = 10
    while height>-2:
        mc.setBlock(pos.x+2, pos.y +height, pos.z + 10, block.WOOL.id, blue)
        mc.setBlock(pos.x+2, pos.y +height+1, pos.z + 10, block.AIR.id)
        sleep(timer)
        height -=1
    mc.setBlock(pos.x+2, pos.y +height+1, pos.z + 10, block.AIR.id)

def buttongreenpressed(channel, event):
    mcg = Minecraft.create()
    blockingreencol = mcg.getBlock(pos.x-1, pos.y, pos.z + 10)
    if blockingreencol == block.WOOL.id:
	    mc.postToChat("Well Done!")
	    mcg.setBlock(pos.x-1, pos.y, pos.z + 10,block.WOOL.id,0)

def buttonyellowpressed(channel, event):
	mcy = Minecraft.create()
	blockinyellowcol = mcy.getBlock(pos.x, pos.y, pos.z + 10)
	if blockinyellowcol == block.WOOL.id:
		mc.postToChat("You're doing great!")
		mcy.setBlock(pos.x, pos.y, pos.z + 10,block.WOOL.id,0)
    

def buttonredpressed(channel, event):
	mcr = Minecraft.create()
	blockinredcol = mcr.getBlock(pos.x+1, pos.y, pos.z + 10)
	if blockinredcol == block.WOOL.id:
		mc.postToChat("Excellent!!")
		mcr.setBlock(pos.x+1, pos.y, pos.z + 10,block.WOOL.id,0)

def buttonbluepressed(channel, event):
	mcb = Minecraft.create()
	blockinbluecol = mcb.getBlock(pos.x+2, pos.y, pos.z + 10)
	if blockinbluecol == block.WOOL.id:
		mc.postToChat("Super work!")
		mcb.setBlock(pos.x+2, pos.y, pos.z + 10,block.WOOL.id,0)

sleep(5)
mc.postToChat("Ready")
sleep(1)
mc.postToChat("Steady")
sleep(1)
mc.postToChat("Go!")
sleep(1)
a.play(-1)

explorerhat.touch.five.pressed(buttongreenpressed)
explorerhat.touch.six.pressed(buttonyellowpressed)
explorerhat.touch.seven.pressed(buttonredpressed)
explorerhat.touch.eight.pressed(buttonbluepressed)

while True:
	choice = random.randint(0,4)
	if choice == 0:
		_thread.start_new_thread(red_block,())
	if choice ==1:
		_thread.start_new_thread(blue_block,())
	if choice ==2:
		_thread.start_new_thread(green_block,())
	if choice ==3:
		_thread.start_new_thread(yellow_block,())

	sleep(timer*2)

