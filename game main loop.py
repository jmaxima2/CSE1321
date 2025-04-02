import pygame,sys

screen = pygame.display.set_mode((1280,720))
running = True
boppiFront = pygame.image.load("BoppiFront.png").convert_alpha()

introBackground = pygame.Surface((1280,720))
introBackground.fill((0,204,255))
introFlag = True
while introFlag:
   for event in pygame.event.get():
      screen.blit(introBackground,(0,0))
      introBackground.blit(boppiFront,(0,0))
      pygame.display.flip()
      if event.type == pygame.QUIT:
         sys.exit()

level1Background = pygame.Surface((1280,720))
level1Background.fill((204,255,204))
level1Flag = False
while level1Flag:
   for event in pygame.event.get():
      screen.blit(level1Background,(0,0))
      level1Background.blit(boppiFront,(0,0))
      pygame.display.flip()
      if event.type == pygame.QUIT:
         sys.exit()

level2Background = pygame.Surface((1280,720))
level2Background.fill((0,0,225))
level2Flag = False
while level2Flag:
   for event in pygame.even.get():
      screen.blit(level2Background,(0,0))
      level2Background.blit(boppiFront,(0,0))
      pygame.display.flip()
      if event.type == pygame.QUIT:
         sys.exit()

level3Background = pygame.Surface((1280,720))
level3Background.fill((0,51,0))
level3Flag = False
while level3Flag:
   for event in pygame.event.get():
      screen.blit(level3Background,(0,0))
      level3Background.blit(boppiFront,(0,0))
      pygame.display.flip()
      if event.type == pygame.QUIT:
         sys.exit()

level4Background = pygame.Surface((1280,720))
level4Background.fill((128,128,128))
level4Flag = False
while level4Flag:
   for event in pygame.event.get():
      screen.blit(level4Background,(0,0))
      level4Background.blit(boppiFront,(0,0))
      pygame.display.flip()
      if event.type == pygame.QUIT:
         sys.exit()

endgameBackground = pygame.Surface((1280,720))
endgameBackground.fill((128,128,128))
endgameFlag = False
while endgameFlag:
   for event in pygame.event.get():
      screen.blit(endgameBackground,(0,0))
      endgameBackground.blit(boppiFront,(0,0))
      pygame.display.flip()
      if event.type == pygame.QUIT:
         sys.exit()