import pygame
import sys

pygame.init()

COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 180, 0)
COLOR_RED = (194, 24, 7)
COLOR_PINK = (255, 182, 193)
COLOR_BLACK = (0, 0, 0)

# Text setups + sfx setups
play_text = 'PLAY'
exit_text = 'EXIT'
GAME_NAME = 'Jogo sem nome aff'
background_song = pygame.mixer.Sound("assets/menu_assets/title.mp3")
decision_fx = pygame.mixer.Sound("assets/menu_assets/decision.ogg")
bg = pygame.image.load("assets/menu_assets/img.png")
pygame.mixer.Sound.play(background_song, loops=-1)

# Screen Setup
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption(GAME_NAME)

# Menu loop setup
main_menu = True
ins = True
game_clock = pygame.time.Clock()

play_sound_played = False
exit_sound_played = False


def button_animation(text, font, is_hovered, sound_played, other_sound_played):
    if is_hovered:
        text = text if text.startswith('- ') else '- ' + text
        button = font.render(text, True, COLOR_PINK)
        if not sound_played:
            decision_fx.play(0, 0)
            return button, True, False
    else:
        text = text.replace('- ', '')
        button = font.render(text, True, COLOR_WHITE)

    return button, sound_played, other_sound_played


while main_menu:
    # Menu background
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Mouse position
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    # Game name in Menu
    menu_font = pygame.font.Font('assets/menu_assets/SegaArcadeFont-Regular.ttf', 60)
    game_name = menu_font.render(GAME_NAME, True, COLOR_WHITE)
    game_name_rect = game_name.get_rect(center=(SCREEN_WIDTH//4.5, SCREEN_HEIGHT//4))

    # Options (play)
    play_font = pygame.font.Font('assets/menu_assets/SegaArcadeFont-Regular.ttf', 50)
    play_button = play_font.render(play_text, True, COLOR_WHITE)
    play_button_rect = play_button.get_rect()
    play_button_rect.center = (SCREEN_WIDTH//4.5, 420)

    play_button, play_sound_played, exit_sound_played = button_animation(play_text, play_font,
                                                                         play_button_rect.collidepoint(MENU_MOUSE_POS),
                                                                         play_sound_played, exit_sound_played)

    # Options (Exit)
    exit_button = play_font.render(exit_text, True, COLOR_WHITE)
    exit_button_rect = exit_button.get_rect()
    exit_button_rect.center = (SCREEN_WIDTH//4.5, 480)
    exit_button, exit_sound_played, play_sound_played = button_animation(exit_text, play_font,
                                                                         exit_button_rect.collidepoint(MENU_MOUSE_POS),
                                                                         exit_sound_played, play_sound_played)

    # Menu Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(MENU_MOUSE_POS):
                print("Play")
            if exit_button_rect.collidepoint(MENU_MOUSE_POS):
                main_menu = False

    # Draw items on screen
    screen.blit(game_name, game_name_rect)
    screen.blit(play_button, play_button_rect)
    screen.blit(exit_button, exit_button_rect)

    # Update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
sys.exit()
