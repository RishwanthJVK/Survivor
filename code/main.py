#initialisation
import random
import pygame
from sys import exit
import time
pygame.init()
pygame.display.set_caption('Survivor')
dimensions = pygame.display.Info()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((dimensions.current_w,dimensions.current_h-int((6/72)*dimensions.current_h)))

#importing

#images
home_page = pygame.image.load("../images/home page.png")
home_page = pygame.transform.scale(home_page,(dimensions.current_w,dimensions.current_h))
home_page_rect = home_page.get_rect(center = (int(dimensions.current_w/2),int(dimensions.current_h/2)))

game_over = pygame.image.load("../images/gameover.png")
game_over = pygame.transform.scale(game_over,(dimensions.current_w,dimensions.current_h))
game_over_rect = game_over.get_rect(center = (int(dimensions.current_w/2),int(dimensions.current_h/2)))

big = pygame.image.load('../images/homebig.png')
big_rect = big.get_rect(center = (int(dimensions.current_w/2),int(dimensions.current_h*(1/4))))

playbutton1 = pygame.image.load('../images/playbutton.png')
playbutton2 = pygame.transform.scale(playbutton1,((int((350/1280)*dimensions.current_w),int((163/720)*dimensions.current_h))))
playbutton = [playbutton1,playbutton2]
playbutton_index = 0
playbutton_rect = playbutton[playbutton_index].get_rect(center = (int(dimensions.current_w/2),int(dimensions.current_h*(2/3))))

leaderboardicon1 = pygame.image.load('../images/leaderboardicon.png')
leaderboardicon1 = pygame.transform.scale(leaderboardicon1,(int((150/1280)*dimensions.current_w),int((150/720)*dimensions.current_h)))
leaderboardicon2 = pygame.transform.scale(leaderboardicon1,(int((170/1280)*dimensions.current_w),int((170/720)*dimensions.current_h)))
leaderboardicon = [leaderboardicon1,leaderboardicon2]
leaderboardicon_index = 0
leaderboardicon_rect = leaderboardicon[leaderboardicon_index].get_rect(center = (int(dimensions.current_w*(1/6)),int(dimensions.current_h*(2/3))))
settingsicon1 = pygame.image.load('../images/settingsicon.png')
settingsicon1 = pygame.transform.scale(settingsicon1,(int((150/1280)*dimensions.current_w),int((150/720)*dimensions.current_h)))
settingsicon2 = pygame.transform.scale(settingsicon1,(int((163/1280)*dimensions.current_w),int((163/720)*dimensions.current_h)))
settingsicon = [settingsicon1,settingsicon2]
settingsicon_index = 0
settingsicon_rect = settingsicon[settingsicon_index].get_rect(center = (int(dimensions.current_w*(5/6)),int(dimensions.current_h*(2/3))))
background = pygame.image.load('../images/desert theme.png')
background = pygame.transform.scale(background,(dimensions.current_w,dimensions.current_h))
background_rect = background.get_rect(
			centerx=(int(dimensions.current_w / 2)),bottom = int(dimensions.current_h))
backicon1 = pygame.image.load('../images/backicon.png')
backicon1 = pygame.transform.scale(backicon1,(int((50/1280)*dimensions.current_w),int((57/720)*dimensions.current_h)))
backicon2 = pygame.image.load('../images/backicon2.png')
backicon2 = pygame.transform.scale(backicon2,(int((55/1280)*dimensions.current_w),int((63/720)*dimensions.current_h)))
backicon = [backicon1,backicon2]
backicon_index = 0
backicon_rect = backicon[backicon_index].get_rect(left = int((10/1280)*dimensions.current_w), top = int((5/720)*dimensions.current_h))
d_p1 = pygame.image.load('../images/plank.png')
d_p1 = pygame.transform.scale(d_p1,(int((250/1280)*dimensions.current_w),int((29/720)*dimensions.current_h)))
d_p1_rect = d_p1.get_rect(left = int(0.05*dimensions.current_w),top = int(0.3*dimensions.current_h))
d_p2 = pygame.image.load('../images/plank.png')
d_p2 = pygame.transform.scale(d_p2,(int((750/1280)*dimensions.current_w),int((29/720)*dimensions.current_h)))
d_p2_rect = d_p2.get_rect(left = int(0.2*dimensions.current_w),top = int(0.5*dimensions.current_h))
d_p3 = pygame.image.load('../images/plank.png')
d_p3 = pygame.transform.scale(d_p3,(int((600/1280)*dimensions.current_w),int((29/720)*dimensions.current_h)))
d_p3_rect = d_p3.get_rect(left = int(0.26*dimensions.current_w),top = int(0.7*dimensions.current_h))
d_p4 = pygame.image.load('../images/plank.png')
d_p4 = pygame.transform.scale(d_p4,(int((250/1280)*dimensions.current_w),int((29/720)*dimensions.current_h)))
d_p4_rect = d_p4.get_rect(right = int(dimensions.current_w*(1-0.05)),top = int(0.3*dimensions.current_h))
life_bar1 = pygame.image.load('../images/life_bar.png')
life_bar2 = pygame.image.load('../images/life_bar.png')
life_bar1_rect = life_bar1.get_rect(bottom = int(dimensions.current_h - (100/720)*dimensions.current_h), left = int((40/1280)*dimensions.current_w))
life_bar2_rect = life_bar2.get_rect(bottom = int(dimensions.current_h - (100/720)*dimensions.current_h), right = int(dimensions.current_w - (40/1280)*dimensions.current_w))
face_1 = pygame.image.load('../images/player1_face.png')
face_2 = pygame.image.load('../images/player2_face.png')
face_1 = pygame.transform.scale(face_1,(int((90/1280)*dimensions.current_w),int((88/720)*dimensions.current_h)))
face_2 = pygame.transform.scale(face_2,(int((90/1280)*dimensions.current_w),int((82/720)*dimensions.current_h)))
face_1_rect = face_1.get_rect(centery = int(life_bar1_rect.centery - (5/720)*dimensions.current_h), centerx = int(life_bar1_rect.centerx - (50/1280)*dimensions.current_w))
face_2_rect = face_2.get_rect(centery = int(life_bar2_rect.centery - (5/720)*dimensions.current_h), centerx = int(life_bar2_rect.centerx - (50/1280)*dimensions.current_w))
stand_1 = pygame.image.load('../images/player.png')
stand_1 = pygame.transform.scale(stand_1,(int((71/1280)*dimensions.current_w),int((98/720)*dimensions.current_h)))
stand_2 = pygame.image.load('../images/player 2.png')
stand_2 = pygame.transform.scale(stand_2,(int((69/1280)*dimensions.current_w),int((100/720)*dimensions.current_h)))
run1_1 = pygame.image.load('../images/run1.png')
run1_1 = pygame.transform.scale(run1_1,(int((90/1280)*dimensions.current_w),int((98/720)*dimensions.current_h)))
rrun1_1 = pygame.transform.flip(run1_1,True,False)
run2_1 = pygame.image.load('../images/run2.png')
run2_1 = pygame.transform.scale(run2_1,(int((88/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun2_1 = pygame.transform.flip(run2_1,True,False)
run3_1 = pygame.image.load('../images/run3.png')
run3_1 = pygame.transform.scale(run3_1,(int((91/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun3_1 = pygame.transform.flip(run3_1,True,False)
run4_1 = pygame.image.load('../images/run4.png')
run4_1 = pygame.transform.scale(run4_1,(int((77/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun4_1 = pygame.transform.flip(run4_1,True,False)
run5_1 = pygame.image.load('../images/run5.png')
run5_1 = pygame.transform.scale(run5_1,(int((85/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun5_1 = pygame.transform.flip(run5_1,True,False)
run6_1 = pygame.image.load('../images/run6.png')
run6_1 = pygame.transform.scale(run6_1,(int((83/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun6_1 = pygame.transform.flip(run6_1,True,False)
run_1 = [run1_1,run2_1,run3_1,run4_1,run5_1,run6_1]
rrun_1 = [rrun1_1,rrun2_1,rrun3_1,rrun4_1,rrun5_1,rrun6_1]
run_index_1 = 0
rrun_index_1 = 0
run1_2 = pygame.image.load('../images/run_1_2.png')
run1_2 = pygame.transform.scale(run1_2,(int((85/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun1_2 = pygame.transform.flip(run1_2,True,False)
run2_2 = pygame.image.load('../images/run_2_2.png')
run2_2 = pygame.transform.scale(run2_2,(int((82/1280)*dimensions.current_w),int((100/720)*dimensions.current_h)))
rrun2_2 = pygame.transform.flip(run2_2,True,False)
run3_2 = pygame.image.load('../images/run_3_2.png')
run3_2 = pygame.transform.scale(run3_2,(int((81/1280)*dimensions.current_w),int((100/720)*dimensions.current_h)))
rrun3_2 = pygame.transform.flip(run3_2,True,False)
run4_2 = pygame.image.load('../images/run_4_2.png')
run4_2 = pygame.transform.scale(run4_2,(int((83/1280)*dimensions.current_w),int((100/720)*dimensions.current_h)))
rrun4_2 = pygame.transform.flip(run4_2,True,False)
run5_2 = pygame.image.load('../images/run_5_2.png')
run5_2 = pygame.transform.scale(run5_2,(int((77/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun5_2 = pygame.transform.flip(run5_2,True,False)
run6_2 = pygame.image.load('../images/run_6_2.png')
run6_2 = pygame.transform.scale(run6_2,(int((77/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rrun6_2 = pygame.transform.flip(run6_2,True,False)
run_2 = [run1_2,run2_2,run3_2,run4_2,run5_2,run6_2]
rrun_2 = [rrun1_2,rrun2_2,rrun3_2,rrun4_2,rrun5_2,rrun6_2]
run_index_2 = 0
rrun_index_2 = 0
jump_1 = pygame.image.load('../images/jump_1.png')
jump_1 = pygame.transform.scale(jump_1,(int((73/1280)*dimensions.current_w),int((97/720)*dimensions.current_h)))
rjump_1 = pygame.transform.flip(jump_1,True,False)
j_1 = [jump_1,rjump_1]
jump_f1 = j_1[0]
jump_2 = pygame.image.load('../images/jump_2.png')
jump_2 = pygame.transform.scale(jump_2,(int((72/1280)*dimensions.current_w),int((99/720)*dimensions.current_h)))
rjump_2 = pygame.transform.flip(jump_2,True,False)
j_2 = [jump_2,rjump_2]
jump_f2 = j_2[0]
right_arrow1 = pygame.image.load('../images/right arrow.png')
right_arrow2 = pygame.transform.scale(right_arrow1,(int((250/1280)*dimensions.current_w),int((250/720)*dimensions.current_h)))
right_arrow = [right_arrow1,right_arrow2]
rindex = 0
right_arrow_rect = right_arrow[rindex].get_rect(right = int((1200/1280)*dimensions.current_w), centery = int((300/720)*dimensions.current_h))
left_arrow1 = pygame.image.load('../images/left arrow.png')
left_arrow2 = pygame.transform.scale(left_arrow1,(int((250/1280)*dimensions.current_w),int((250/720)*dimensions.current_h)))
left_arrow = [left_arrow1,left_arrow2]
lindex = 0
left_arrow_rect = left_arrow[lindex].get_rect(left = int((80/1280)*dimensions.current_w), centery = int((300/720)*dimensions.current_h))
start_button1 = pygame.image.load('../images/start button.png')
start_button2 = pygame.transform.scale(start_button1,(int((400/1280)*dimensions.current_w),int((227/720)*dimensions.current_h)))
start_button = [start_button1,start_button2]
sindex = 0
start_button_rect = start_button[sindex].get_rect(center = (int((640/1280)*dimensions.current_w), int((560/720)*dimensions.current_h)))
desert_mode = pygame.image.load('../images/desert_mode.png')
theme_list = [desert_mode]
theme_index = 0
theme_rect = theme_list[theme_index].get_rect(center = (int((640/1280)*dimensions.current_w),int((300/720)*dimensions.current_h)))
backb1 = pygame.image.load('../images/backb.png')
backb2 = pygame.transform.scale(backb1,(int((90/1280)*dimensions.current_w),int((90/720)*dimensions.current_h)))
bi = 0
backb = [backb1,backb2]
backb_rect = backb[bi].get_rect(center = (int((50/1280)*dimensions.current_w),int((50/720)*dimensions.current_h)))

#audio
theme = pygame.mixer.music.load('../audio/theme.wav')
pygame.mixer.music.play(-1)
click = pygame.mixer.Sound('../audio/click.wav')
ded = pygame.mixer.Sound('../audio/ded.wav')
jump = pygame.mixer.Sound('../audio/jump sound.wav')
shoot_sound = pygame.mixer.Sound('../audio/shooting sound.wav')
shoot_sound.set_volume(0.5)
hitting_sound = pygame.mixer.Sound('../audio/hit sound.wav')

#functional_variables
game_state = 'home_page'
fall_1 = 0
ground_1 = False
fall_2 = 0
ground_2 = False
facing_1 = False
facing_2 = False
bullet_list_1 = []
bullet_list_2 = []
wait_1 = wait_2 = 0
hit1 = 0
hit2 = 0
birth_1 = 5
birth_2 = 5
s_center = (int(dimensions.current_h/2),int(dimensions.current_w/2))



#text
life_font = pygame.font.Font(None,int((80/720)*dimensions.current_h))
life1 = life_font.render(str(birth_1),False,'Black')
life2 = life_font.render(str(birth_2),False,'Black')
life1_rect = life1.get_rect(bottom = int(life_bar1_rect.bottom - (5/720)*dimensions.current_h), left = int(face_1_rect.right + (20/1280)*dimensions.current_w))
life2_rect = life2.get_rect(bottom = int(life_bar2_rect.bottom - (5/720)*dimensions.current_h), left = int(face_2_rect.right + (20/1280)*dimensions.current_w))

#functions
def shoot(bullist):
	global bullet_1,bullet_2, hit1, hit2,bull_facing_1, bull_facing_2
	bullist_2 = bullist.copy()
	if bullist:
		for i in bullist:
			if i[1]:
				i[0].x += int(5/1280 * dimensions.current_w)
				i[2] += int(5/1280 * dimensions.current_w)
			else:
				i[0].x -= int(5/1280 * dimensions.current_w)
				i[2] += int(5/1280 * dimensions.current_w)
			if i[0].colliderect(player_1.sprite.rect) and i[3] == 2:
				hitting_sound.play()
				if i[1]:
					hit1 += int(20/1280 * dimensions.current_w)
				else:
					hit1 -= int(20/1280 * dimensions.current_w)
				bullist_2.remove(i)
			if i[0].colliderect(player_2.sprite.rect) and i[3] == 1:
				hitting_sound.play()
				if i[1]:
					hit2 += int(20/1280 * dimensions.current_w)
				else:
					hit2 -= int(20/1280 * dimensions.current_w)
				bullist_2.remove(i)
			if i[2] >= int(300/1280 * dimensions.current_w) and i in bullist_2:
				bullist_2.remove(i)
			if i[1] == 1:
				screen.blit(bullet_2,i[0])
			else:
				screen.blit(bullet_1, i[0])
		bullist = bullist_2
		return bullist
	else:
		return []
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = stand_1
		self.rect = self.image.get_rect(bottom = int(d_p1_rect.top - 100/720 * dimensions.current_h), left = random.randint(d_p1_rect.x,d_p2_rect.centerx))
	def player_inputs(self):
		global ground_1,stand_1,jump_f1, facing_1,run_index_1,rrun_index_1, background_rect, d_p1_rect, d_p2_rect, d_p3_rect, d_p4_rect, fall_1,game_state, wait_1, life_1, hit1
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			if not facing_1:
				jump_f1 = j_1[1]
				stand_1 = pygame.transform.flip(stand_1, True, False)
				facing_1 = True
			if ground_1:
				self.image = rrun_1[int(rrun_index_1)]
				rrun_index_1 += 0.3
				if rrun_index_1 > len(rrun_1):
					rrun_index_1 = 0
			if not ground_1:
				self.image = jump_f1
			self.rect.x += int(6/1280 * dimensions.current_w)
		if keys[pygame.K_a]:
			if facing_1:
				jump_f1 = j_1[0]
				stand_1 = pygame.transform.flip(stand_1, True, False)
				facing_1 = False
			if ground_1:
				self.image = run_1[int(run_index_1)]
				run_index_1 += 0.3
				if run_index_1 > len(run_1):
					run_index_1 = 0
			if not ground_1:
				self.image = jump_f1
			self.rect.x -= int(6/1280 * dimensions.current_w)
		if keys[pygame.K_w] and ground_1:
			jump.play()
			if facing_1:
				jump_f1 = j_1[1]
			else:
				jump_f1 = j_1[0]
			self.image = jump_f1
			fall_1 = -int(20/720 * dimensions.current_h)
			self.rect.y += fall_1
			ground_1 = False
		if keys[pygame.K_v]:
			wait_1 += 0.1
			if int(wait_1) == 2:
				shoot_sound.play()
				if not facing_1:
					hit1 += int(5/1280 * dimensions.current_w)
					bullet_list_1.append(
						[bullet_1.get_rect(right=player_1.sprite.rect.left, centery=player_1.sprite.rect.centery),
						 facing_1,0,1])
				else:
					hit1-= int(5/1280 * dimensions.current_w)
					bullet_list_1.append(
						[bullet_2.get_rect(left=player_1.sprite.rect.right, centery=player_1.sprite.rect.centery),
						 facing_1,0,1])
				wait_1 = 0
		if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_w] and ground_1:
			self.image = stand_1

	def destroy(self):
		global game_state, life1, birth_1, fall_1
		if self.rect.top in range(int(dimensions.current_h + 10/720 * dimensions.current_h),int(dimensions.current_h + 70/1280 * dimensions.current_h)):
			fall_1 = 0
		if self.rect.top in range(int(dimensions.current_h + 100/720 * dimensions.current_h),int(dimensions.current_h + 110/720 * dimensions.current_h)):
			ded.play()
		if self.rect.top > int(dimensions.current_h + 10000/720*dimensions.current_h):
			self.rect.bottom = int(d_p1_rect.top - 200/720 * dimensions.current_h)
			self.rect.left = random.randint(d_p1_rect.x, d_p2_rect.centerx)
			fall_1 = 0
			birth_1 -= 1
			life1 = life_font.render(str(birth_1), False, 'Black')
	def update(self):
		global fall_1, ground_1
		if not ground_1:
			fall_1 += int(1/720 * dimensions.current_h)
		else: fall_1 = 0
		self.rect.y += fall_1
		self.player_inputs()
		self.destroy()


class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('../images/player 2.png')
		self.rect = self.image.get_rect(bottom = int(d_p1_rect.top - 100/720 * dimensions.current_h), left = random.randint(d_p3_rect.centerx,d_p4_rect.x))
	def player_inputs(self):
		global rrun_index_2,run_index_2, ground_2,jump_2,jump_f2,stand_2, facing_2, background_rect, d_p1_rect, d_p2_rect, d_p3_rect, d_p4_rect, fall_2,game_state, wait_2, hit2
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			if not facing_2:
				jump_f2 = j_2[1]
				stand_2 = pygame.transform.flip(stand_2, True, False)
				facing_2 = True
			if ground_2:
				self.image = rrun_2[int(rrun_index_2)]
				rrun_index_2 += 0.3
				if rrun_index_2 > len(rrun_2):
					rrun_index_2 = 0
			if not ground_2:
				self.image = jump_f2
			self.rect.x += int(5/1280 * dimensions.current_w)
		if keys[pygame.K_LEFT]:
			if facing_2:
				jump_f2 = j_2[0]
				stand_2 = pygame.transform.flip(stand_2,True,False)
				facing_2 = False
			if ground_2:
				self.image = run_2[int(run_index_2)]
				run_index_2 += 0.3
				if run_index_2 > len(run_2):
					run_index_2 = 0
			if not ground_2:
				self.image = jump_f2
			self.rect.x -= int(5/1280 * dimensions.current_w)
		if keys[pygame.K_UP] and ground_2:
			jump.play()
			if facing_2:
				jump_f2 = j_2[1]
			else:
				jump_f2 = j_2[0]
			self.image = jump_f2
			fall_2 = -int(20/720 * dimensions.current_h)
			self.rect.y += fall_2
			ground_2 = False
		if keys[pygame.K_m]:
			wait_2 += 0.1
			if int(wait_2) == 2:
				shoot_sound.play()
				if not facing_2:
					hit2+=5
					bullet_list_2.append(
						[bullet_1.get_rect(right=player_2.sprite.rect.left, centery=player_2.sprite.rect.centery),
						 facing_2,0,2])
				else:
					hit2-=5
					bullet_list_2.append(
						[bullet_2.get_rect(left=player_2.sprite.rect.right, centery=player_2.sprite.rect.centery),
						 facing_2,0,2])
				wait_2 = 0
		if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_UP] and ground_2:
			self.image = stand_2


	def destroy(self):
		global game_state, life2, birth_2, fall_2
		if self.rect.top in range(int(dimensions.current_h + 10/720 * dimensions.current_h),int(dimensions.current_h + 70/720 * dimensions.current_h)):
			fall_2 = 0
		if self.rect.top in range(int(dimensions.current_h + 100/720 * dimensions.current_h),int(dimensions.current_h + 110/720 * dimensions.current_h)):
			ded.play()
		if self.rect.top >= int(dimensions.current_h + 10000/720 * dimensions.current_h):
			self.rect.bottom = int(d_p1_rect.top - 200/720 * dimensions.current_h)
			self.rect.left = random.randint(d_p3_rect.centerx, d_p4_rect.x)
			fall_2 = 0
			birth_2 -= 1
			life2 = life_font.render(str(birth_2), False, 'Black')
	def update(self):
		global fall_2, ground_2
		if not ground_2:
			fall_2 += int(1/720 * dimensions.current_h)
		else: fall_2 = 0
		self.rect.y += fall_2
		self.player_inputs()
		self.destroy()
player_1 = pygame.sprite.GroupSingle()
player_1.add(Player())
player_2 = pygame.sprite.GroupSingle()
player_2.add(Player2())

bullet_1 = pygame.image.load('../images/bullet.png')
bullet_2 = pygame.transform.flip(bullet_1,True,False)




#Game Loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if game_state == 'play' and event.type == pygame.KEYDOWN and ground_1:
			kes = pygame.key.get_pressed()
			if kes[pygame.K_s] and player_1.sprite.rect.bottom <= d_p2_rect.top+1:
				player_1.sprite.rect.y += int(30/720 * dimensions.current_h)
				ground_1 = False
		if game_state == 'play' and event.type == pygame.KEYDOWN and ground_2:
			kes = pygame.key.get_pressed()
			if kes[pygame.K_DOWN] and player_2.sprite.rect.bottom <= d_p2_rect.top+1:
				player_2.sprite.rect.y += int(30/720 * dimensions.current_h)
				ground_2 = False
		if game_state == 'play' and event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_m]:
				shoot_sound.play()
				if not facing_2:
					hit2 += int(5/1280 * dimensions.current_w)
					bullet_list_2.append(
						[bullet_1.get_rect(right=player_2.sprite.rect.left, centery=player_2.sprite.rect.centery),
						 facing_2,0,2])
				else:
					hit2 -= int(5/1280 * dimensions.current_w)
					bullet_list_2.append(
						[bullet_2.get_rect(left=player_2.sprite.rect.right, centery=player_2.sprite.rect.centery),
						 facing_2,0,2])
			if keys[pygame.K_v]:
				shoot_sound.play()
				if not facing_1:
					hit1 += int(5/1280 * dimensions.current_w)
					bullet_list_1.append(
						[bullet_1.get_rect(right=player_1.sprite.rect.left, centery=player_1.sprite.rect.centery),
						 facing_1,0,1])
				else:
					hit1-=int(5/1280 * dimensions.current_w)
					bullet_list_1.append(
						[bullet_2.get_rect(left=player_1.sprite.rect.right, centery=player_1.sprite.rect.centery),
						 facing_1,0,1])
	if game_state == 'home_page':
		pygame.mixer.music.set_volume(0.5)
		screen.blit(home_page, home_page_rect)
		screen.blit(playbutton[playbutton_index],playbutton_rect)
		screen.blit(leaderboardicon[leaderboardicon_index],leaderboardicon_rect)
		screen.blit(settingsicon[settingsicon_index],settingsicon_rect)
		screen.blit(big,big_rect)
		if playbutton_rect.collidepoint(pygame.mouse.get_pos()):
			playbutton_index = 1
			playbutton_rect = playbutton[playbutton_index].get_rect(
				center=(int(dimensions.current_w / 2), int(dimensions.current_h * (2 / 3))))
			if pygame.mouse.get_pressed()[0]:
				click.play()
				bullet_list_1.clear()
				bullet_list_2.clear()
				player_1.sprite.rect.bottom = int(d_p1_rect.top - 100/720 * dimensions.current_h)
				player_2.sprite.rect.bottom = int(d_p1_rect.top - 100/720 * dimensions.current_h)
				player_1.sprite.rect.left = random.randint(d_p1_rect.x, d_p2_rect.centerx)
				player_2.sprite.rect.left = random.randint(d_p3_rect.centerx, d_p4_rect.x)
				birth_1 = birth_2 = 5
				life1 = life_font.render(str(birth_1), False, 'Black')
				life2 = life_font.render(str(birth_2), False, 'Black')
				fall_1 = 0
				ground_1 = False
				fall_2 = 0
				ground_2 = False
				wait_1 = wait_2 = 0
				hit1 = 0
				hit2 = 0
				game_state = 'choose'
				time.sleep(1)

				continue

		else:
			playbutton_index = 0
			playbutton_rect = playbutton[playbutton_index].get_rect(
				center=(int(dimensions.current_w / 2), int(dimensions.current_h * (2 / 3))))
		if leaderboardicon_rect.collidepoint(pygame.mouse.get_pos()):
			leaderboardicon_index = 1
			leaderboardicon_rect = leaderboardicon[leaderboardicon_index].get_rect(
				center=(int(dimensions.current_w * (1 / 6)), int(dimensions.current_h * (2 / 3))))
		else:
			leaderboardicon_index = 0
			leaderboardicon_rect = leaderboardicon[leaderboardicon_index].get_rect(
				center=(int(dimensions.current_w * (1 / 6)), int(dimensions.current_h * (2 / 3))))
		if settingsicon_rect.collidepoint(pygame.mouse.get_pos()):
			settingsicon_index = 1
			settingsicon_rect = settingsicon[settingsicon_index].get_rect(
				center=(int(dimensions.current_w * (5 / 6)), int(dimensions.current_h * (2 / 3))))
		else:
			settingsicon_index = 0
			settingsicon_rect = settingsicon[settingsicon_index].get_rect(
				center=(int(dimensions.current_w * (5 / 6)), int(dimensions.current_h * (2 / 3))))
	if game_state == 'game_end':
		screen.blit(game_over,game_over_rect)
		if pygame.mouse.get_pressed()[0]:
			game_state = 'home_page'


	if game_state == 'play':
		pygame.mixer.music.set_volume(0.2)
		rel_center_x = int((player_1.sprite.rect.centerx + player_2.sprite.rect.centerx) / 2)
		rel_center_y = int((player_1.sprite.rect.centery + player_2.sprite.rect.centery) / 2)
		rel_center = (rel_center_x, rel_center_y)
		# background_rect.center = rel_center
		screen.blit(background,background_rect)
		screen.blit(backicon[backicon_index],backicon_rect)
		screen.blit(d_p1,d_p1_rect)
		screen.blit(d_p2,d_p2_rect)
		screen.blit(d_p3,d_p3_rect)
		screen.blit(d_p4,d_p4_rect)
		screen.blit(life1,life1_rect)
		screen.blit(life2,life2_rect)
		player_1.draw(screen)
		player_2.draw(screen)
		screen.blit(life_bar1,life_bar1_rect)
		screen.blit(life_bar2,life_bar2_rect)
		screen.blit(face_1,face_1_rect)
		screen.blit(face_2,face_2_rect)

		if backicon_rect.collidepoint(pygame.mouse.get_pos()):
			backicon_index = 1
			if pygame.mouse.get_pressed()[0]:
				click.play()
				time.sleep(1)
				game_state = 'choose'

		else:
			backicon_index = 0
		if player_1.sprite.rect.colliderect(d_p1_rect):
			if player_1.sprite.rect.bottom in range(int(d_p1_rect.top - 30/720 * dimensions.current_h), int(d_p1_rect.top + 30/720 * dimensions.current_h)):
				ground_1 = True
				player_1.sprite.rect.bottom = int(d_p1_rect.top + 1/720 * dimensions.current_h)

		elif player_1.sprite.rect.colliderect(d_p2_rect):
			if player_1.sprite.rect.bottom in range(int(d_p2_rect.top - 30/720 * dimensions.current_h), int(d_p2_rect.top + 30/720 * dimensions.current_h)):
				ground_1 = True
				player_1.sprite.rect.bottom = int(d_p2_rect.top + 1/720 * dimensions.current_h)

		elif player_1.sprite.rect.colliderect(d_p3_rect):
			if player_1.sprite.rect.bottom in range(int(d_p3_rect.top - 30/720 * dimensions.current_h), int(d_p3_rect.top + 30/720 * dimensions.current_h)):
				ground_1 = True
				player_1.sprite.rect.bottom = int(d_p3_rect.top + 1/720 * dimensions.current_h)

		elif player_1.sprite.rect.colliderect(d_p4_rect):
			if player_1.sprite.rect.bottom in range(int(d_p4_rect.top - 30/720*dimensions.current_h), int(d_p4_rect.top + 30/720 * dimensions.current_h)):
				ground_1 = True
				player_1.sprite.rect.bottom = int(d_p4_rect.top + 1/720*dimensions.current_h)
		else:
			ground_1 = False
		if player_2.sprite.rect.colliderect(d_p1_rect):
			if player_2.sprite.rect.bottom in range(int(d_p1_rect.top - 30/720 * dimensions.current_h), int(d_p1_rect.top + 30/720 * dimensions.current_h)):
				ground_2 = True
				player_2.sprite.rect.bottom = int(d_p1_rect.top + 1/720 * dimensions.current_h)

		elif player_2.sprite.rect.colliderect(d_p2_rect):
			if player_2.sprite.rect.bottom in range(int(d_p2_rect.top - 30/720 * dimensions.current_h), int(d_p2_rect.top + 30/720 * dimensions.current_h)):
				ground_2 = True
				player_2.sprite.rect.bottom = int(d_p2_rect.top + 1/720 * dimensions.current_h)

		elif player_2.sprite.rect.colliderect(d_p3_rect):
			if player_2.sprite.rect.bottom in range(int(d_p3_rect.top - 30/720 * dimensions.current_h), int(d_p3_rect.top + 30/720 * dimensions.current_h)):
				ground_2 = True
				player_2.sprite.rect.bottom = int(d_p3_rect.top + 1/720 * dimensions.current_h)

		elif player_2.sprite.rect.colliderect(d_p4_rect):
			if player_2.sprite.rect.bottom in range(int(d_p4_rect.top - 30/720 * dimensions.current_h), int(d_p4_rect.top + 30/720 * dimensions.current_h)):
				ground_2 = True
				player_2.sprite.rect.bottom = int(d_p4_rect.top + 1/720 * dimensions.current_h)
		else:
			ground_2 = False
		if not birth_1 or not birth_2:
			game_state = 'game_end'
		bullet_list_1 = shoot(bullet_list_1)
		bullet_list_2 = shoot(bullet_list_2)
		player_1.update()
		player_2.update()
		player_1.sprite.rect.x += hit1
		if hit1 > 0:
			hit1 -= int(1/1280 * dimensions.current_w)
		elif hit1 < 0:
			hit1 += int(1/1280 * dimensions.current_w)
		player_2.sprite.rect.x += hit2
		if hit2 > 0:
			hit2 -= int(1/1280 * dimensions.current_w)
		elif hit2 < 0:
			hit2 += int(1/1280 * dimensions.current_w)
	if game_state == 'choose':
		screen.blit(home_page,home_page_rect)
		screen.blit(right_arrow[rindex],right_arrow_rect)
		screen.blit(left_arrow[lindex],left_arrow_rect)
		screen.blit(start_button[sindex], start_button_rect)
		screen.blit(theme_list[theme_index],theme_rect)
		screen.blit(backb[bi],backb_rect)
		if right_arrow_rect.collidepoint(pygame.mouse.get_pos()):
			rindex = 1
			right_arrow_rect = right_arrow[rindex].get_rect(right=int((1200 / 1280) * dimensions.current_w), centery=int((300 / 720) * dimensions.current_h))
			if pygame.mouse.get_pressed()[0]:
				click.play()
		else:
			rindex = 0
			right_arrow_rect = right_arrow[rindex].get_rect(right=int((1200 / 1280) * dimensions.current_w), centery=int((300 / 720) * dimensions.current_h))
		if left_arrow_rect.collidepoint(pygame.mouse.get_pos()):
			lindex = 1
			left_arrow_rect = left_arrow[lindex].get_rect(left=int((80 / 1280) * dimensions.current_w), centery=int((300 / 720) * dimensions.current_h))
			if pygame.mouse.get_pressed()[0]:
				click.play()
		else:
			lindex = 0
			left_arrow_rect = left_arrow[lindex].get_rect(left=int((80 / 1280) * dimensions.current_w), centery=int((300 / 720) * dimensions.current_h))
		if start_button_rect.collidepoint(pygame.mouse.get_pos()):
			sindex = 1

			start_button_rect = start_button[sindex].get_rect(center=(int((640 / 1280) * dimensions.current_w), int((560 / 720) * dimensions.current_h)))
			if pygame.mouse.get_pressed()[0]:
				click.play()
				time.sleep(1)
				game_state = 'play'
		else:
			sindex = 0
			start_button_rect = start_button[sindex].get_rect(center=(int((640 / 1280) * dimensions.current_w), int((560 / 720) * dimensions.current_h)))
		if backb_rect.collidepoint(pygame.mouse.get_pos()) and game_state == 'choose':
			bi = 1
			backb_rect = backb[bi].get_rect(center = (int((50 / 1280) * dimensions.current_w),int((50 / 720) * dimensions.current_h)))
			if pygame.mouse.get_pressed()[0] and game_state == 'choose':
				click.play()
				time.sleep(1)
				game_state = 'home_page'
		else:
			bi = 0
			backb_rect = backb[bi].get_rect(center=(int((50 / 1280) * dimensions.current_w), int((50 / 720) * dimensions.current_h)))



	pygame.display.update()
	clock.tick(60)