#Imports
import pygame, random, math, os
pygame.init()
from pygame.locals import *

#Screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screenX, screenY = screen.get_size()
canvas = pygame.Surface((screenX, screenY - 50))
canvasX, canvasY = canvas.get_size()
pygame.display.set_caption('Jonah\'s AP CSP Principles - AP Project')
pygame.mouse.set_visible(False)
buttonsDir = os.path.join(os.path.dirname(__file__), 'Buttons')
colorsDir = os.path.join(os.path.dirname(__file__), 'Colors')

#Colors
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (143, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (222, 222, 222)
brown = (150, 75, 0)
colorArr = [red, orange, yellow, green, blue, indigo, violet, brown, black]
drawColor = blue
myDict = {}
colors = ['red.png', 'orange.png', 'yellow.png', 'green.png', 'blue.png', 'indigo.png', 'violet.png', 'brown.png', 'black.png']
for i in range(len(colors)):
  myDict[colors[i]] = colorArr[i]

#Circles
circleX = circleY = circRadius = 50
circRadius2 = 12.5
circleX2, circleY2 = screenX // 2, screenY // 2
circles = []
with open('circles.csv', 'w') as f:
  f.write('')
def newCirc(x, y):
  circles.append((x, y, drawColor))
overCirc = False
def clear():
  global circles
  circles = []
importList = []

#Rectangles
paintRectW = paintRectH = eraseRectW = eraseRectH = selectRectW = selectRectH = clearRectW = clearRectH = 50
selectRectX, paintRectX, eraseRectX, clearRectX = 0, 50, 100, 150
saveRectX = screenX - 50
toolbarRectY = screenY - 50
option = 'select'
rectangles = []
def delCirc_Rect(x,y,w,h):
  for i, circle in enumerate(circles):
    if (circle[0] - circRadius2 <= x <= circle[0] + circRadius2) and (circle[1] - circRadius2 <= y <= circle[1] + circRadius2):
      del circles[i]
      break

#Text
font = pygame.font.SysFont('timesnewroman', 12)
cancelFont = pygame.font.SysFont('timesnewroman', 10)
textBase = font.render('Control + Z to undo, Control + Y to redo', True, black)
textCont = font.render('Right click to draw, Left click to move', True, black)
textSave = font.render('Saving...', True, black)
textSaveInput = ''
textSaveInstructions = font.render('Please enter new file name: ', True, black)
textSaveFormat = font.render('.png', True, black)
exceedColor = white
textSaveExceed = font.render('', True, exceedColor)
textCancel = cancelFont.render('Cancel', True, black)
textRectBase = textBase.get_rect()
textRectBase.x, textRectBase.y = 5, 55
textRectCont = textCont.get_rect()
textRectCont.x, textRectCont.y = 5, 70
textRectSave = textSave.get_rect()
textRectSave.x, textRectSave.y = screenX - 55, 50
textRectSaveInstructions = textSaveInstructions.get_rect()
textRectSaveInstructions.center = (screenX / 2, (screenY / 2) - 16)
textRectSaveInput = pygame.Rect(100, 100, textRectSaveInstructions.w, 16) 
textRectSaveInput.center = (screenX / 2, screenY / 2)
textRectSaveFormat = textSaveFormat.get_rect()
textRectSaveFormat.x, textRectSaveFormat.y = (textRectSaveInstructions.x + textRectSaveInstructions.w) - (textRectSaveFormat.w + 4), textRectSaveInput.y
textRectSaveExceed = textSaveExceed.get_rect()
textRectSaveExceed.x, textRectSaveExceed.y = textRectSaveInput.x, textRectSaveInput.y + textRectSaveInput.h + 2
textRectCancel = pygame.Rect((textRectSaveInstructions.x + textRectSaveInstructions.w) - textCancel.get_rect().w - 2, (textRectSaveInstructions.y - textCancel.get_rect().h) - 4, textCancel.get_rect().w + 2, textCancel.get_rect().h + 2)
instructionsWidth = 36
formatArr = ['.png', '.jpg', '.gif', '.tiff']

#Images
settingIconRt = 0

#Buttons
change = 0
openColors = False
openFormats = False
saveState = True
save = False

#Drawing Loop
running = True
while running:

  #Prerequisites
  keys = pygame.key.get_pressed()
  if keys[K_ESCAPE]:
    running = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if option == 'save':
      if event.type == pygame.KEYDOWN:
        if len(textSaveInput) >= 15:
          instructionsWidth = 54
          textSaveExceed = font.render('Character limit is 15!', True, red)
          if event.key == pygame.K_BACKSPACE: 
            textSaveInput = textSaveInput[:-1]
        else:
          instructionsWidth = 36
          textSaveExceed = font.render('', True, white)
          if event.key == pygame.K_BACKSPACE:
            textSaveInput = textSaveInput[:-1]
          else:
            textSaveInput += event.unicode
          if event.key == pygame.K_RETURN:
            pygame.image.save(canvas, textSaveInput[:-1] + selectedFormat)
            try:
              with open('circles.csv', 'w') as f:
                for circle in circles:
                  x, y = circle[0], circle[1]
                  r, g, b = circle[2]
                  f.write(f"{x},{y},{r},{g},{b}\n")
              saveState = False
              option = 'select'
            except Exception as e:
              print(f'Error saving: {e}')
            openFormats = False

  screen.fill(white)
  canvas.fill(white)

  #Define Border
  if circleX < circRadius:
    circleX = circRadius
  if circleX > screenX - circRadius:
    circleX = screenX - circRadius
  if circleY < circRadius:
    circleY = circRadius
  if circleY > screenY - circRadius:
    circleY = screenY - circRadius
  if circleX2 < circRadius2:
    circleX2 = circRadius2
  if circleX2 > screenX - circRadius2:
    circleX2 = screenX - circRadius2
  if circleY2 < circRadius2:
    circleY2 = circRadius2
  if circleY2 > screenY - circRadius2:
    circleY2 = screenY - circRadius2

  #Pre-Mouse
  mouseX, mouseY = pygame.mouse.get_pos()
  mousePress = pygame.mouse.get_pressed()

  #Mouse Movements
  if (mousePress[0] == True):
    overCirc = True
    circleX2, circleY2 = mouseX, mouseY
    if option == 'paint':
      newCirc(circleX2, circleY2)
    if (keys[K_RCTRL] or keys[K_LCTRL]) and keys[K_z]:
      del circles[-1]

  #Eraser
  if option == 'erase':
    for circle in circles:
      erTempRect = pygame.draw.rect(screen, white, (circle[0] - circRadius2, circle[1] - circRadius2, circRadius2 * 2, circRadius2 * 2), 1)
      if (mousePress[0] == True) and (erTempRect.collidepoint((mouseX, mouseY))):
        delCirc_Rect(circle[0] - circRadius2, circle[1] - circRadius2, circRadius, circRadius)

  #Trail
  for circle in circles:
    pygame.draw.circle(canvas, circle[2], circle[:2], circRadius2)
    pygame.draw.circle(screen, circle[2], circle[:2], circRadius2)

  #Circles
  #mouseCirc = pygame.draw.circle(screen, black, (circleX2, circleY2), circRadius2)

  #Buttons Collisions
  if (mousePress[0] == True) and (selectRect.collidepoint((mouseX, mouseY))):
      option = 'select'
  if (mousePress[0] == True) and (paintRect.collidepoint((mouseX, mouseY))):
      option = 'paint'
  if (mousePress[0] == True) and (eraseRect.collidepoint((mouseX, mouseY))):
      option = 'erase'
  if (mousePress[0] == True) and (clearRect.collidepoint((mouseX, mouseY))):
      option = 'clear'
  if (mousePress[0] == True) and (saveRect.collidepoint((mouseX, mouseY))):
      option = 'save'
  if (mousePress[0] == True) and (importRect.collidepoint((mouseX, mouseY))):
      option = 'import'

  #Rectangles
  toolbarRectBorder = pygame.draw.rect(screen, black, pygame.Rect(0, screenY - 52, screenX, screenY), 2)
  toolbarRect = pygame.draw.rect(screen, white, pygame.Rect(0, screenY - 50, screenX, screenY))
  selectRect = pygame.draw.rect(screen, black, pygame.Rect(selectRectX, toolbarRectY, selectRectW, selectRectH), 1)
  paintRect = pygame.draw.rect(screen, black, pygame.Rect(paintRectX, toolbarRectY, paintRectW, paintRectH), 1)
  eraseRect = pygame.draw.rect(screen, black, pygame.Rect(eraseRectX, toolbarRectY, eraseRectW, eraseRectH), 1)
  clearRect = pygame.draw.rect(screen, black, pygame.Rect(clearRectX, toolbarRectY, clearRectW, clearRectH), 1)
  saveRect = pygame.draw.rect(screen, white, pygame.Rect(saveRectX, 0, clearRectW, clearRectH))
  importRect = pygame.draw.rect(screen, white, pygame.Rect(screenX - 50, 50, 50, 50))

  #Buttons
  selectButton = pygame.image.load(os.path.join(buttonsDir, 'cursor.png')).convert_alpha()
  selectButton = pygame.transform.scale(selectButton, [50, 50])
  screen.blit(selectButton, [selectRectX, toolbarRectY])
  paintButton = pygame.image.load(os.path.join(buttonsDir, 'paintbrush.png')).convert_alpha()
  paintButton = pygame.transform.scale(paintButton, [35, 35])
  paintButton = pygame.transform.rotate(paintButton, -45)
  screen.blit(paintButton, [paintRectX, toolbarRectY])
  eraseButton = pygame.image.load(os.path.join(buttonsDir, 'eraser.png')).convert_alpha()
  eraseButton = pygame.transform.scale(eraseButton, [50, 50])
  screen.blit(eraseButton, [eraseRectX, toolbarRectY])
  clearButton = pygame.image.load(os.path.join(buttonsDir, 'clear.png')).convert_alpha()
  clearButton = pygame.transform.scale(clearButton, [50, 50])
  screen.blit(clearButton, [clearRectX, toolbarRectY])

  #Save
  saveButton = pygame.image.load(os.path.join(buttonsDir, 'save.png')).convert_alpha()
  saveButton = pygame.transform.scale(saveButton, [50, 50])
  screen.blit(saveButton, [saveRectX, 0])

  #Import
  importButton = pygame.image.load(os.path.join(buttonsDir, 'import.png')).convert_alpha()
  importButton = pygame.transform.scale(importButton, [50, 50])
  screen.blit(importButton, [screenX - 50, 50])

  #Color Buttons
  if openColors == True:
    x = 0
    for color in colors:
      colorbg = white
      if myDict[color] == drawColor:
        colorbg = gray
      colorButtonRect = pygame.draw.rect(screen, colorbg, pygame.Rect(100 + x, screenY - 50, 50, 50))
      colorButton = pygame.image.load(os.path.join(colorsDir, color)).convert_alpha()
      colorButton = pygame.transform.scale(colorButton, [50, 50])
      screen.blit(colorButton, [100 + x, screenY - 50])
      x += 50
      eraseRectX = 550
      clearRectX = 600
      if (mousePress[0] == True) and (colorButtonRect.collidepoint((mouseX, mouseY))):
        drawColor = myDict[color]
  else:
    eraseRectX, clearRectX = 100, 150

  #File Format Dropdown
  if openFormats:
    tempRectFormat = pygame.Rect(textRectSaveFormat.x, textRectSaveFormat.y + 18, textRectSaveFormat.w + 4, 18)
    for i in range(len(formatArr)):
        pygame.draw.rect(screen, black, tempRectFormat, 1)
        tempFormat = font.render(formatArr[i], True, black)
        screen.blit(tempFormat, (tempRectFormat.x + 1, tempRectFormat.y))
        if mousePress[0] and tempRectFormat.collidepoint((mouseX, mouseY)):
            selectedFormat = formatArr[i]
            textSaveFormat = font.render(selectedFormat, True, black)
            screen.blit(textSaveFormat, textRectSaveFormat)
            openFormats = False
        tempRectFormat.y += tempRectFormat.h

  #Settings Loading
  settingIcon = pygame.image.load(os.path.join(buttonsDir, 'settings.png')).convert_alpha()
  settingIcon = pygame.transform.scale(settingIcon, [50, 50])
  settingIconRt += 1

  settingIconX, settingIconY = settingIcon.get_size()
  if (mousePress[0] == True) and (mouseX < settingIconX + 50 and mouseX > settingIconX - 50) and (mouseY < settingIconY + 50 and mouseY > settingIconY - 50):
    screen.blit(textBase, textRectBase)
    screen.blit(textCont, textRectCont)
    if settingIconRt >= 360:
      settingIconRt = 0
    settingIcon = pygame.transform.rotate(settingIcon, settingIconRt)
  settingIconRect = settingIcon.get_rect(center = [25, 25])
  pygame.time.delay(10)
  screen.blit(settingIcon, settingIconRect)

  #Mouse Loading
  #Default Mouse
  if (mousePress[0] == False) and ((option == 'select') or (option == 'clear') or (option == 'save')):
    mouseP = pygame.image.load(os.path.join(buttonsDir, 'cursor.png'))
    mouseP = pygame.transform.scale(mouseP, [50, 50])
    mousePX, mousePY = mouseP.get_size()
    screen.blit(mouseP, [mouseX - ((mousePX / 2) - 7.5), mouseY - 5])
    openColors = False
  if (mousePress[0] == True) and (option == 'select'):
    mouseP = pygame.image.load(os.path.join(buttonsDir, 'cursor(clenched).png'))
    mouseP = pygame.transform.scale(mouseP, [50, 50])
    mousePX, mousePY = mouseP.get_size()
    screen.blit(mouseP, [mouseX - ((mousePX / 2) - 8.25), mouseY - 1.75])
    openColors = False
  if (mousePress[0] == True) and (overCirc == True) and (option == 'paint'):
    change = 1
    mouseP = pygame.image.load(os.path.join(buttonsDir, 'paintbrush.png'))
    mouseP = pygame.transform.rotate(mouseP, -45)
    mouseP = pygame.transform.scale(mouseP, [50, 50])
    mousePX, mousePY = mouseP.get_size()
    screen.blit(mouseP, [mouseX - 15, mouseY - 35])
    overCirc = False
    openColors = True
  #Buttons Related to Mouse
  if option == 'erase':
    mouseP = pygame.image.load(os.path.join(buttonsDir, 'eraser.png'))
    mouseP = pygame.transform.scale(mouseP, [50, 50])
    mousePX, mousePY = mouseP.get_size()
    screen.blit(mouseP, [mouseX - 15, mouseY - 30])
    #Line below shouldn't be necessary, but when the eraser button is clicked, the colors don't dissapear.
    openColors = False
  if option == 'paint':
    mouseP = pygame.image.load(os.path.join(buttonsDir, 'paintbrush.png'))
    mouseP = pygame.transform.rotate(mouseP, -45)
    mouseP = pygame.transform.scale(mouseP, [50, 50])
    mousePX, mousePY = mouseP.get_size()
    screen.blit(mouseP, [mouseX - 15, mouseY - 35])
  if option == 'clear':
    clear()
  if option == 'save':
    if (mousePress[0] == True) and (textRectCancel.collidepoint((mouseX, mouseY))):
      option = 'select'
      openFormats = False
    if saveState == True:
      if (mousePress[0] == True) and (textRectSaveFormat.collidepoint((mouseX, mouseY))):
        openFormats = True
      textSave = font.render('Saving...', True, black)
      screen.blit(textSave, textRectSave)
      pygame.draw.rect(screen, black, (textRectSaveInstructions.x - 2, textRectSaveInstructions.y - 2, textRectSaveInstructions.w + 2, instructionsWidth), 1)
      pygame.draw.rect(screen, white, (textRectSaveInstructions.x - 1, textRectSaveInstructions.y - 1, textRectSaveInstructions.w, instructionsWidth - 2))
      screen.blit(textSaveInstructions, textRectSaveInstructions)
      screen.blit(textSaveFormat, textRectSaveFormat)
      pygame.draw.rect(screen, red, textRectCancel)
      screen.blit(textCancel, (textRectCancel.x + 1, textRectCancel.y + 2))
      pygame.draw.rect(screen, black, textRectSaveInput, 1) 
      textSaveOutput = font.render(textSaveInput, True, black) 
      screen.blit(textSaveOutput, (textRectSaveInput.x + 5, textRectSaveInput.y + 1)) 
      textRectSaveInput.w = 100
      screen.blit(textSaveExceed, textRectSaveExceed)
      mouseP = pygame.image.load(os.path.join(buttonsDir, 'cursor.png'))
      mouseP = pygame.transform.scale(mouseP, [50, 50])
      mousePX, mousePY = mouseP.get_size()
      screen.blit(mouseP, [mouseX - ((mousePX / 2) - 7.5), mouseY - 5])
      pygame.time.delay(50)
  if option == 'import':
    try:
      with open('circles.csv', 'r') as f:
        for line in f:
            try:
              x, y, r, g, b = map(int, line.strip().split(','))
              circles.append((x, y, (r, g, b)))
            except ValueError:
              continue
      option = 'select'
    except FileNotFoundError:
      print('No saved circles found')
  if mousePress[2] == True:
    circleX2 = mouseX
    circleY2 = mouseY

  #Keys
  if (keys[K_RCTRL] or keys[K_LCTRL]) and keys[K_z]:
    if len(circles) > 0:
      tempCircX = circles[-1][0]
      tempCircY = circles[-1][1]
      tempCircColor = circles[-1][2]
      del circles[-1]
  if (keys[K_RCTRL] or keys[K_LCTRL]) and keys[K_y]:
    newCirc(tempCircX, tempCircY)
    circles[-1] = (tempCircX, tempCircY, tempCircColor)

  #Experimental Collisions
  '''
  circDis = math.hypot(circleX - X2, circleY - Y2)
  if circDis <= circRadius + radius2:
    delCirc_Rect(circle[0] - circRadius2, circle[1] - circRadius2, circRadius, circRadius)
  '''

  #Draws
  pygame.display.flip()
pygame.quit()

  #Citations
  #All images created by Jonah Katzowitz using https://www.piskelapp.com/