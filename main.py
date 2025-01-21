import pgzrun
from pgzero.keyboard import keyboard
from pgzero.actor import Actor
from pgzero.screen import Screen
from pgzero.rect import Rect

screen: Screen
# Screen size
WIDTH = 800
HEIGHT = 600

Y0 = 300

# Hero animation setup
hero_frames = {
    "idle": [f"player/idle/player-idle-{i}" for i in range(1, 9)],
    "run": [f"player/run/player-run-{i}" for i in range(1, 7)],
    "jump": [f"player/jump/player-jump-{i}" for i in range(1, 5)],
}

ant_frames = [f"enemies/ant/ant-{i}" for i in range(1, 9)]

acorn_frames = [f"items/acorn/acorn-{i}" for i in range(1, 4)]

# Load the hero Actor with the first idle frame
hero = Actor(hero_frames["idle"][0], (200, Y0))

ant = Actor(ant_frames[0], (400,Y0))

acorns = []
for i in range(1):
    acorn = Actor(acorn_frames[0], (600,Y0))
    acorns.append(acorn)

# Animation state variables
hero_idle_index = 0
hero_run_index = 0
hero_jump_index = 0
hero_is_jumping = False
hero_animation_timer = 0.2  # Time between animation frames
hero_velocity_y = 0
current_timer = 0.0

current_ant_timer = 0.0
ant_animation_timer = 0.2  # Time between animation frames
ant_index = 0

current_acorn_timer = 0.0
acorn_animation_timer = 0.2  # Time between animation frames
acorn_index = 0

# Game variables
menu_active = True
game_over = False
sound_on = True

# Variables
score = 0


# Button rectangles for the main menu
buttons = {
    "play": Rect((300, 200), (200, 50)),
    "sound": Rect((300, 280), (200, 50)),
    "exit": Rect((300, 360), (200, 50)),
}

# Draw function
def draw():
    screen.clear()
    if menu_active:
        # Draw the main menu
        screen.draw.text("MAIN MENU", center=(WIDTH / 2, 100), fontsize=50, color="white")
        screen.draw.filled_rect(buttons["play"], "blue")
        screen.draw.text("Play", center=buttons["play"].center, fontsize=30, color="white")
        screen.draw.filled_rect(buttons["sound"], "blue")
        sound_text = "Sound: ON" if sound_on else "Sound: OFF"
        screen.draw.text(sound_text, center=buttons["sound"].center, fontsize=30, color="white")
        screen.draw.filled_rect(buttons["exit"], "blue")
        screen.draw.text("Exit", center=buttons["exit"].center, fontsize=30, color="white")

        screen.draw.text("Collect the acorns and avoid the ants", center=(WIDTH / 2, HEIGHT/2 + 200), fontsize=50, color="white")

    elif game_over:
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=50, color="red")
    else:
        #screen.blit("background", (0, 0))
        ant.draw()
        for acorn in acorns:
            acorn.draw()
        hero.draw()

        # Draw the score at the top of the screen
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")

# Update function
def update(dt):
    global current_timer, hero_idle_index, hero_run_index, menu_active, ant_index, current_ant_timer
    global hero_is_jumping, hero_velocity_y, hero_jump_index
    global acorn_index, current_acorn_timer
    global game_over, score

    if game_over or menu_active:
        if keyboard.space:
            menu_active = False
        return

    # Update animation timer
    current_timer += dt
    if current_timer >= hero_animation_timer:
        current_timer = 0.0


        if hero_velocity_y != 0:
            hero_jump_index = (hero_jump_index + 1) % len(hero_frames["jump"])
            hero.image = hero_frames["jump"][hero_jump_index]
        elif not (keyboard.left or keyboard.right):
            hero_idle_index = (hero_idle_index + 1) % len(hero_frames["idle"])
            hero.image = hero_frames["idle"][hero_idle_index]
        else:
            hero_run_index = (hero_run_index + 1) % len(hero_frames["run"])
            hero.image = hero_frames["run"][hero_run_index]


    # Move the hero
    if keyboard.left:
        hero.x -= 2
        hero.scale = -1
    if keyboard.right:
        hero.x += 2
        hero.scale = 1

    if keyboard.up and hero_velocity_y == 0:
        hero.image = hero_frames["jump"][0]
        hero_velocity_y = 8

    # physics of jump
    hero.y = hero.y - hero_velocity_y
    hero_velocity_y = hero_velocity_y - dt*10
    if hero.y >= Y0:
        hero.y = Y0
        hero_velocity_y = 0

    current_ant_timer += dt
    if current_ant_timer >= ant_animation_timer:
        current_ant_timer = 0.0
        ant_index = (ant_index + 1) % len(ant_frames)
        ant.image = ant_frames[ant_index]

    current_acorn_timer += dt
    if current_acorn_timer >= acorn_animation_timer:
        current_acorn_timer = 0.0
        acorn_index = (acorn_index + 1) % len(acorn_frames)
        for acorn in acorns:
            acorn.image = acorn_frames[acorn_index]

    if hero.colliderect(ant):
        game_over = True
        return

    for acorn in acorns:
        if hero.colliderect(acorn):
            score += 1
            acorns.remove(acorn)


# Handle mouse clicks for the menu buttons
def on_mouse_down(pos):
    global menu_active, sound_on
    if menu_active:
        if buttons["play"].collidepoint(pos):
            menu_active = False  # Start the game
        elif buttons["sound"].collidepoint(pos):
            sound_on = not sound_on  # Toggle sound
        elif buttons["exit"].collidepoint(pos):
            exit()  # Exit the game

# Run the game
pgzrun.go()
