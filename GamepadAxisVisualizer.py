import pygame
import os
import win32api
import win32con
import win32gui
import sys
import ctypes
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"
os.environ['SDL_VIDEO_WINDOW_POS'] = "1400, 800"
width = 400
height = 400

# made by Reeven Vincent V. Ajero
# SET SCREEN POSITION 
X_POSITION = 25
Y_POSITION = 50


pygame.init()
screen = pygame.display.set_mode((width,height), pygame.NOFRAME)
#screen = pygame.display.set_mode((width,height)) 

# Screen Transparency
transparentColor = (255, 0, 128)  # Transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparentColor), 0, win32con.LWA_COLORKEY)

#Screen always on top
win32gui.SetWindowPos(
    hwnd, 
    win32con.HWND_TOPMOST, 
    0, 0, 0, 0, 
    win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
)

# Controller initialization
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print(f"Connected to: {controller.get_name()}")
else:
    print(f"NO CONTROLLER DETECTED")
    sys.exit(1)

scale_factor = 2.0
x = X_POSITION*scale_factor
y = Y_POSITION*scale_factor

# Vertial Bar position
l_bar_offset=10*scale_factor
bar_w = 10*scale_factor
max_h = 40*scale_factor
max_w = 20*scale_factor

# Horizontal Bar Position
xaxis_h = 10*scale_factor
xaxis_x = x
xaxis_y = y

running = True
while running:
    screen.fill(transparentColor)

    # Get axis from controller
    xaxis = controller.get_axis(0)
    lTrigger = controller.get_axis(4)
    lTrigger_norm = (lTrigger+1)/2
    rTrigger = controller.get_axis(5)
    rTrigger_norm = (rTrigger+1)/2
    
    # Right Trigger BG display
    bar_bg_r = pygame.Rect(x,y-max_h,bar_w, max_h)
    pygame.draw.rect(screen, pygame.Color(20,40,20), bar_bg_r)

    # Right Trigger display
    bar_h_r = max_h*rTrigger_norm
    bar_r = pygame.Rect(x,y-bar_h_r,bar_w, bar_h_r)
    pygame.draw.rect(screen, pygame.Color("green"), bar_r)

    # Left Trigger BG display
    bar_bg_r = pygame.Rect(x-l_bar_offset,y-max_h,bar_w, max_h)
    pygame.draw.rect(screen, pygame.Color(40,20,20), bar_bg_r)

    # Left Trigger display
    bar_h_l = max_h*lTrigger_norm
    bar_l = pygame.Rect(x-l_bar_offset,y-bar_h_l,bar_w, bar_h_l)
    pygame.draw.rect(screen, pygame.Color("red"), bar_l)

    # x axis BG display
    bar_x_bg = pygame.Rect(xaxis_x-max_w,xaxis_y,max_w*2, xaxis_h)
    pygame.draw.rect(screen, pygame.Color(20,20,20), bar_x_bg)

    # x axis positive display
    bar_w_x = max_w*xaxis
    bar_x = pygame.Rect(xaxis_x,xaxis_y,bar_w_x, xaxis_h)
    pygame.draw.rect(screen, pygame.Color("white"), bar_x)

    # x axis negative display
    if xaxis < 0:
        bar_w_x = max_w*xaxis*-1
        bar_x = pygame.Rect(xaxis_x-bar_w_x, xaxis_y, bar_w_x, xaxis_h)
        pygame.draw.rect(screen, pygame.Color("white"), bar_x)

    for event in pygame.event.get():

        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False































# made by Reeven Vincent V. Ajero
