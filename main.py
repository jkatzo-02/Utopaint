#Imports
import pygame, os
pygame.init()
from pygame.locals import *

#Screen
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
screen_x, screen_y = screen.get_size()
canvas = pygame.Surface((screen_x, screen_y - 50))
pygame.display.set_caption('UtoPaint')
pygame.mouse.set_visible(False)
buttons_directory = os.path.join(os.path.dirname(__file__), 'Buttons')
colors_directory = os.path.join(os.path.dirname(__file__), 'Colors')

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
color_list = [red, orange, yellow, green, blue, indigo, violet, brown, black]
draw_color = blue
color_dictionary = {}
colors = ['red.png', 'orange.png', 'yellow.png', 'green.png', 'blue.png', 'indigo.png', 'violet.png', 'brown.png', 'black.png']
for i in range(len(colors)):
  color_dictionary[colors[i]] = color_list[i]

#Circles
circle_x = circle_y = circle_radius = 50
circle_radius_2 = 12.5
circle_x_2, circle_y_2 = screen_x // 2, screen_y // 2
circles = []
def new_circle(x, y):
  circles.append((x, y, draw_color))
over_circle = False
def clear():
  global circles
  circles = []
import_list = []

#Rectangles
paint_rect_w = paint_rect_h = erase_rect_w = erase_rect_h = cursor_rect_w = cursor_rect_h = clear_rect_w = clear_rect_h = 50
cursor_rect_x, paint_rect_x, erase_rect_x, clear_rect_x = 0, 50, 100, 150
#sliderRect = pygame.draw.rect(screen, black, pygame.Rect())
save_rect_x = screen_x - 50
toolbar_rect_y = screen_y - 50
option = 'select'
rectangles = []
def delete_circle(x,y,w,h):
  for i, circle in enumerate(circles):
    if (circle[0] - circle_radius_2 <= x <= circle[0] + circle_radius_2) and (circle[1] - circle_radius_2 <= y <= circle[1] + circle_radius_2):
      del circles[i]
      break

#Text
font = pygame.font.SysFont('timesnewroman', 12)
cancel_font = pygame.font.SysFont('timesnewroman', 10)
text_base = font.render('Control + Z to undo, Control + Y to redo', True, black)
text_base_continued = font.render('Right click to draw, Left click to move', True, black)
text_save_input = ''
text_save_instructions = font.render('Please enter new file name: ', True, black)
text_save_format = font.render('.png', True, black)
exceed_color = white
text_save_exceed = font.render('', True, exceed_color)
text_cancel = cancel_font.render('Cancel', True, black)
text_import = font.render('Select an Import Option', True, black)
text_import_label = font.render('Import', True, black)

#Text Rectangles
text_base_rect = text_base.get_rect()
text_base_rect.x, text_base_rect.y = 5, 55
text_base_continued_rect = text_base_continued.get_rect()
text_base_continued_rect.x, text_base_continued_rect.y = 5, 70
text_save_instructions_rect = text_save_instructions.get_rect()
text_save_instructions_rect.center = (screen_x // 2, (screen_y // 2) - 16)
text_save_input_rect = pygame.Rect(100, 100, text_save_instructions_rect.w, 16) 
text_save_input_rect.center = (screen_x // 2, screen_y // 2)
text_save_format_rect = text_save_format.get_rect()
text_save_format_rect.x, text_save_format_rect.y = (text_save_instructions_rect.x + text_save_instructions_rect.w) - (text_save_format_rect.w + 4), text_save_input_rect.y
text_save_exceed_rect = text_save_exceed.get_rect()
text_save_exceed_rect.x, text_save_exceed_rect.y = text_save_input_rect.x, text_save_input_rect.y + text_save_input_rect.h + 2
text_save_cancel_rect = pygame.Rect((text_save_instructions_rect.x + text_save_instructions_rect.w) - text_cancel.get_rect().w - 2, (text_save_instructions_rect.y - text_cancel.get_rect().h) - 4, text_cancel.get_rect().w + 2, text_cancel.get_rect().h + 2)
text_import_box = pygame.Rect(0, 0, 360, 200)
text_import_box.center = (screen_x // 2, screen_y // 2)
text_import_rect = text_import.get_rect()
text_import_rect.center = (screen_x // 2, text_import_box.y + 25)
import_middle_rect = pygame.Rect(0, 0, 100, 100)
import_middle_rect.center = (screen_x // 2, screen_y // 2)
import_left_rect = pygame.Rect(text_import_box.left + 15, import_middle_rect.y, 100, 100)
import_right_rect = pygame.Rect(text_import_box.right - 115, import_middle_rect.y, 100, 100)
text_import_cancel_rect = pygame.Rect((text_import_box.x + text_import_box.w) - text_cancel.get_rect().w - 2, (text_import_box.y - text_cancel.get_rect().h) - 2, text_cancel.get_rect().w + 2, text_cancel.get_rect().h + 2)
instructions_width = 36
selected_format = '.png'
format_list = ['.png', '.jpg', '.gif', '.tiff']
buttons_list_x = [cursor_rect_x, paint_rect_x, erase_rect_x, clear_rect_x, save_rect_x, None]
buttons_list_image = ['cursor.png', 'paint.png', 'erase.png', 'clear.png', 'save.png', 'import.png']
'''button_rect = []
buttonName = []
for index, button in enumerate(buttons_list_image):
    button_rect.append(button[:-4])
    button_rect[index] = button_rect[index] + 'Rect'
'''
rectangle_x = {}
for i in range(len(buttons_list_image)):
    rectangle_x[buttons_list_image[i]] = buttons_list_x[i]

#Images
setting_icon_rotation = 0

#Buttons
change = 0
open_colors = False
open_formats = False
save_state = True
save = False

#Saving / Importing
save_files_list = ['save1.csv', 'save2.csv', 'save3.csv']
save_files_display = ['No Save File Found', 'No Save File Found', 'No Save File Found']
for i in range(3):
  with open(save_files_list[i], 'w') as f:
    f.write('')
    
def blit_buttons(colors_open):
    for button in buttons_list_image:
        temporary_button = pygame.image.load(os.path.join(buttons_directory, button)).convert_alpha()
        if button != 'paint.png':
          temporary_button = pygame.transform.scale(temporary_button, [50, 50])
        else:
          temporary_button = pygame.transform.scale(temporary_button, [35, 35])
          temporary_button = pygame.transform.rotate(temporary_button, -45)
        if button == 'save.png':
          screen.blit(temporary_button, [rectangle_x[button], 0])
        elif button == 'import.png':
          screen.blit(temporary_button, [screen_x - 50, 50])
        else:
            if not colors_open:
                screen.blit(temporary_button, [rectangle_x[button], toolbar_rect_y])
            else:
                if button == 'erase.png':
                    screen.blit(temporary_button, [erase_rect_x, toolbar_rect_y])
                elif button == 'clear.png':
                    screen.blit(temporary_button, [clear_rect_x, toolbar_rect_y])
#Drawing Loop
running = True
while running:

  #Prerequisites
  keys = pygame.key.get_pressed()
  if keys[K_ESCAPE]:
    running = False
  if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_s]:
    option = 'save'
  if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_i]:
    option = 'import'
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if option == 'save':
      if event.type == pygame.KEYDOWN:
        if len(text_save_input) >= 15:
          instructions_width = 54
          text_save_exceed = font.render('Character limit is 15!', True, red)
          if event.key == pygame.K_BACKSPACE: 
            text_save_input = text_save_input[:-1]
        else:
          instructions_width = 36
          text_save_exceed = font.render('', True, white)
          if event.key == pygame.K_BACKSPACE:
            text_save_input = text_save_input[:-1]
          else:
            text_save_input += event.unicode
          if event.key == pygame.K_RETURN:
            #pygame.image.save(canvas, text_save_input[:-1] + selected_format)
            for index, file in enumerate(save_files_display):
              if file == 'No Save File Found':
                save_files_display[index] = text_save_input[:-1] + selected_format
                break
            try:
              for index, rect in enumerate([import_left_rect, import_middle_rect, import_right_rect]):
                data = os.path.getsize(save_files_list[index])
                if data == 0:
                  with open(save_files_list[index], 'w') as f:
                    for circle in circles:
                      x, y = circle[0], circle[1]
                      r, g, b = circle[2]
                      f.write(f"{x},{y},{r},{g},{b}\n")
                  save_state = False
                  option = 'select'
                  text_save_input = ''
                  break
            except Exception as e:
              print(f'Error saving: {e}')
            open_formats = False

  screen.fill(white)
  canvas.fill(white)

  #Define Border
  if circle_x < circle_radius:
    circle_x = circle_radius
  if circle_x > screen_x - circle_radius:
    circle_x = screen_x - circle_radius
  if circle_y < circle_radius:
    circle_y = circle_radius
  if circle_y > screen_y - circle_radius:
    circle_y = screen_y - circle_radius
  if circle_x_2 < circle_radius_2:
    circle_x_2 = circle_radius_2
  if circle_x_2 > screen_x - circle_radius_2:
    circle_x_2 = screen_x - circle_radius_2
  if circle_y_2 < circle_radius_2:
    circle_y_2 = circle_radius_2
  if circle_y_2 > screen_y - circle_radius_2:
    circle_y_2 = screen_y - circle_radius_2

  #Pre-Mouse
  mouse_x, mouse_y = pygame.mouse.get_pos()
  mouse_press = pygame.mouse.get_pressed()

  #Mouse Movements
  if (mouse_press[0] == True):
    over_circle = True
    circle_x_2, circle_y_2 = mouse_x, mouse_y
    if option == 'paint':
      new_circle(circle_x_2, circle_y_2)
    if (keys[K_RCTRL] or keys[K_LCTRL]) and keys[K_z]:
      del circles[-1]

  #Eraser
  if option == 'erase':
    for circle in circles:
      temporary_eraser_rect = pygame.draw.rect(screen, white, (circle[0] - circle_radius_2, circle[1] - circle_radius_2, circle_radius_2 * 2, circle_radius_2 * 2), 1)
      if (mouse_press[0] == True) and (temporary_eraser_rect.collidepoint((mouse_x, mouse_y))):
        delete_circle(circle[0] - circle_radius_2, circle[1] - circle_radius_2, circle_radius, circle_radius)

  #Trail
  for circle in circles:
    pygame.draw.circle(canvas, circle[2], circle[:2], circle_radius_2)
    pygame.draw.circle(screen, circle[2], circle[:2], circle_radius_2)

  #Circles
  #mouseCirc = pygame.draw.circle(screen, black, (circle_x_2, circle_y_2), circle_radius_2)
  
  #Buttons Collisions
  '''for index, rect in enumerate(button_rect):
    if (mouse_press[0] == True) and (rect.collidepoint((mouse_x, mouse_y))):
      option = button_rect[index][:-4]
      if option == 'save':
        save_state = True'''
  if (mouse_press[0] == True) and (cursor_rect.collidepoint((mouse_x, mouse_y))):
      option = 'select'
  if (mouse_press[0] == True) and (paint_rect.collidepoint((mouse_x, mouse_y))):
      option = 'paint'
  if (mouse_press[0] == True) and (erase_rect.collidepoint((mouse_x, mouse_y))):
      option = 'erase'
  if (mouse_press[0] == True) and (clear_rect.collidepoint((mouse_x, mouse_y))):
      option = 'clear'
  if (mouse_press[0] == True) and (save_rect.collidepoint((mouse_x, mouse_y))):
      option = 'save'
      save_state = True
  if (mouse_press[0] == True) and (import_rect.collidepoint((mouse_x, mouse_y))):
      option = 'import'

  #Rectangles
  toolbar_border_rect = pygame.draw.rect(screen, black, pygame.Rect(0, screen_y - 52, screen_x, screen_y), 2)
  toolbar_rect = pygame.draw.rect(screen, white, pygame.Rect(0, screen_y - 50, screen_x, screen_y))
  cursor_rect = pygame.draw.rect(screen, black, pygame.Rect(cursor_rect_x, toolbar_rect_y, cursor_rect_w, cursor_rectH), 1)
  paint_rect = pygame.draw.rect(screen, black, pygame.Rect(paint_rect_x, toolbar_rect_y, paint_rect_w, paint_rect_h), 1)
  erase_rect = pygame.draw.rect(screen, black, pygame.Rect(erase_rect_x, toolbar_rect_y, erase_rect_w, erase_rect_h), 1)
  clear_rect = pygame.draw.rect(screen, black, pygame.Rect(clear_rect_x, toolbar_rect_y, clear_rect_w, clear_rect_h), 1)
  save_rect = pygame.draw.rect(screen, white, pygame.Rect(save_rect_x, 0, clear_rect_w, clear_rect_h))
  import_rect = pygame.draw.rect(screen, white, pygame.Rect(screen_x - 50, 50, 50, 50))

  #Buttons
  blit_buttons(False)
  '''button_rect.append(button[:-4])
    button_rect[index] = button_rect[index] + 'Rect'
  '''

  #Color Buttons
  if open_colors == True:
    x = 0
    for color in colors:
      color_backgroud = white
      if color_dictionary[color] == draw_color:
        color_backgroud = gray
      color_button_rect = pygame.draw.rect(screen, color_backgroud, pygame.Rect(100 + x, screen_y - 50, 50, 50))
      color_button = pygame.image.load(os.path.join(colors_directory, color)).convert_alpha()
      color_button = pygame.transform.scale(color_button, [50, 50])
      screen.blit(color_button, [100 + x, screen_y - 50])
      x += 50
      erase_rect_x = 550
      clear_rect_x = 600
      blit_buttons(True)
      if (mouse_press[0] == True) and (color_button_rect.collidepoint((mouse_x, mouse_y))):
        draw_color = color_dictionary[color]
  else:
    erase_rect_x, clear_rect_x = 100, 150

  #File Format Dropdown
  if open_formats:
    temporary_format_rect = pygame.Rect(text_save_format_rect.x, text_save_format_rect.y + 18, text_save_format_rect.w + 4, 18)
    for i in range(len(format_list)):
        pygame.draw.rect(screen, black, temporary_format_rect, 1)
        temporary_format = font.render(format_list[i], True, black)
        screen.blit(temporary_format, (temporary_format_rect.x + 1, temporary_format_rect.y))
        if mouse_press[0] and temporary_format_rect.collidepoint((mouse_x, mouse_y)):
            selected_format = format_list[i]
            text_save_format = font.render(selected_format, True, black)
            screen.blit(text_save_format, text_save_format_rect)
            open_formats = False
        temporary_format_rect.y += temporary_format_rect.h

  #Settings Loading
  setting_icon = pygame.image.load(os.path.join(buttons_directory, 'settings.png')).convert_alpha()
  setting_icon = pygame.transform.scale(setting_icon, [50, 50])
  setting_icon_rotation += 1

  setting_icon_x, setting_icon_y = setting_icon.get_size()
  if (mouse_press[0] == True) and (mouse_x < setting_icon_x + 50 and mouse_x > setting_icon_x - 50) and (mouse_y < setting_icon_y + 50 and mouse_y > setting_icon_y - 50):
    screen.blit(text_base, text_base_rect)
    screen.blit(text_base_continued, text_base_continued_rect)
    if setting_icon_rotation >= 360:
      setting_icon_rotation = 0
    setting_icon = pygame.transform.rotate(setting_icon, setting_icon_rotation)
  setting_icon_rect = setting_icon.get_rect(center = [25, 25])
  pygame.time.delay(10)
  screen.blit(setting_icon, setting_icon_rect)

  #Mouse Loading
  #Default Mouse
  if (mouse_press[0] == False) and ((option == 'select') or (option == 'clear') or (option == 'save') or (option == 'import')):
    mouse_pointer = pygame.image.load(os.path.join(buttons_directory, 'cursor.png'))
    mouse_pointer = pygame.transform.scale(mouse_pointer, [50, 50])
    mouse_pointer_x, mouse_pointer_y = mouse_pointer.get_size()
    screen.blit(mouse_pointer, [mouse_x - ((mouse_pointer_x / 2) - 7.5), mouse_y - 5])
    open_colors = False
  if (mouse_press[0] == True) and (option == 'select'):
    mouse_pointer = pygame.image.load(os.path.join(buttons_directory, 'cursor(clenched).png'))
    mouse_pointer = pygame.transform.scale(mouse_pointer, [50, 50])
    mouse_pointer_x, mouse_pointer_y = mouse_pointer.get_size()
    screen.blit(mouse_pointer, [mouse_x - ((mouse_pointer_x / 2) - 8.25), mouse_y - 1.75])
    open_colors = False
  if (mouse_press[0] == True) and (over_circle == True) and (option == 'paint'):
    change = 1
    mouse_pointer = pygame.image.load(os.path.join(buttons_directory, 'paint.png'))
    mouse_pointer = pygame.transform.rotate(mouse_pointer, -45)
    mouse_pointer = pygame.transform.scale(mouse_pointer, [50, 50])
    mouse_pointer_x, mouse_pointer_y = mouse_pointer.get_size()
    screen.blit(mouse_pointer, [mouse_x - 15, mouse_y - 35])
    over_circle = False
    open_colors = True
  #Buttons Related to Mouse
  if option == 'erase':
    mouse_pointer = pygame.image.load(os.path.join(buttons_directory, 'erase.png'))
    mouse_pointer = pygame.transform.scale(mouse_pointer, [50, 50])
    mouse_pointer_x, mouse_pointer_y = mouse_pointer.get_size()
    screen.blit(mouse_pointer, [mouse_x - 15, mouse_y - 30])
    #Line below shouldn't be necessary, but when the eraser button is clicked, the colors don't dissapear.
    open_colors = False
  if option == 'paint':
    mouse_pointer = pygame.image.load(os.path.join(buttons_directory, 'paint.png'))
    mouse_pointer = pygame.transform.rotate(mouse_pointer, -45)
    mouse_pointer = pygame.transform.scale(mouse_pointer, [50, 50])
    mouse_pointer_x, mouse_pointer_y = mouse_pointer.get_size()
    screen.blit(mouse_pointer, [mouse_x - 15, mouse_y - 35])
  if option == 'clear':
    clear()
  if option == 'save':
    if (mouse_press[0] == True) and (text_save_cancel_rect.collidepoint((mouse_x, mouse_y))):
      option = 'select'
      open_formats = False
    if save_state == True:
      if (mouse_press[0] == True) and (text_save_format_rect.collidepoint((mouse_x, mouse_y))):
        open_formats = True
      pygame.draw.rect(screen, black, (text_save_instructions_rect.x - 2, text_save_instructions_rect.y - 2, text_save_instructions_rect.w + 2, instructions_width), 1)
      pygame.draw.rect(screen, white, (text_save_instructions_rect.x - 1, text_save_instructions_rect.y - 1, text_save_instructions_rect.w, instructions_width - 2))
      screen.blit(text_save_instructions, text_save_instructions_rect)
      screen.blit(text_save_format, text_save_format_rect)
      pygame.draw.rect(screen, red, text_save_cancel_rect)
      screen.blit(text_cancel, (text_save_cancel_rect.x + 1, text_save_cancel_rect.y + 2))
      pygame.draw.rect(screen, black, text_save_input_rect, 1) 
      text_save_output = font.render(text_save_input, True, black) 
      screen.blit(text_save_output, (text_save_input_rect.x + 5, text_save_input_rect.y + 1)) 
      text_save_input_rect.w = 100
      screen.blit(text_save_exceed, text_save_exceed_rect)
      screen.blit(mouse_pointer, [mouse_x - ((mouse_pointer_x / 2) - 7.5), mouse_y - 5])
      pygame.time.delay(50)
      
  if option == 'import':
    if (mouse_press[0] == True) and (text_import_cancel_rect.collidepoint((mouse_x, mouse_y))):
      option = 'select'
    pygame.draw.rect(screen, white, text_import_box)
    screen.blit(text_import, text_import_rect)
    pygame.draw.rect(screen, black, text_import_box, 1)
    pygame.draw.rect(screen, red, text_import_cancel_rect)
    screen.blit(text_cancel, (text_import_cancel_rect.x + 1, text_import_cancel_rect.y + 2))
    for index, rect in enumerate([import_left_rect, import_middle_rect, import_right_rect]):
      data = os.path.getsize(save_files_list[index])
      if data > 0:
        pygame.draw.rect(screen, green, rect)
        text_import_label = font.render(save_files_display[index], True, black)
      else:
        pygame.draw.rect(screen, red, rect)
        text_import_label = font.render(f'Save Slot {index + 1}', True, black)
      import_rectLabelsBtn = text_import_label.get_rect()
      import_rectLabelsBtn.center = (rect.centerx, rect.y + 115)
      screen.blit(text_import_label, import_rectLabelsBtn)
      if (mouse_press[0] == True) and (rect.collidepoint((mouse_x, mouse_y))):
        with open(save_files_list[index], 'r') as f:
          for line in f:
            try:
              x, y, r, g, b = map(int, line.strip().split(','))
              circles.append((x, y, (r, g, b)))
            except ValueError:
              continue
        option = 'select'
    screen.blit(mouse_pointer, [mouse_x - ((mouse_pointer_x / 2) - 7.5), mouse_y - 5])

  #Keys
  if (keys[K_RCTRL] or keys[K_LCTRL]) and keys[K_z]:
    if len(circles) > 0:
      temporary_circle_x = circles[-1][0]
      temporary_circle_y = circles[-1][1]
      temporary_circle_color = circles[-1][2]
      del circles[-1]
  if (keys[K_RCTRL] or keys[K_LCTRL]) and keys[K_y]:
    new_circle(temporary_circle_x, temporary_circle_y)
    circles[-1] = (temporary_circle_x, temporary_circle_y, temporary_circle_color)

  #Draws
  pygame.display.flip()
pygame.quit()

  #Citations
  #All images created by Jonah Katzowitz using https://www.piskelapp.com/
