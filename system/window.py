# This is simple state machine.
import pygame

from system.event import Event

# Main clock.
clock = pygame.time.Clock()

# Pygame window variables.
surface: pygame.Surface = None
size: tuple = None
title: str = None

# Window events.
user_event = Event()
mouse_button_up_event = Event()
mouse_button_down_event = Event()
mouse_motion_event = Event()
keydown_event = Event()
keyup_event = Event()
quit_event = Event()


def set_mode(wsize: tuple, flags=0) -> pygame.Surface:
    """
    Sets size and flags for window.
    :param size: tuple[int, int].
    :param flags: int.
    :return: pygame.Surface.
    """
    global surface, size
    size = wsize
    surface = pygame.display.set_mode(size, flags)
    return surface


def set_title(wtitle: str) -> None:
    """
    Sets title for window.
    :param wtitle: Title of window.
    """
    global title
    title = wtitle
    pygame.display.set_caption(title)


def poll_events() -> None:
    """
    Polls events and notify subscribers of Events, wich are described above.
    """
    global quit_event, \
        keyup_event, \
        keydown_event, \
        mouse_motion_event, \
        mouse_button_down_event, \
        mouse_button_up_event

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_event.notify()
            quit(0)
        elif e.type == pygame.MOUSEBUTTONUP:
            mouse_button_up_event.notify(e.pos, e.button)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_down_event.notify(e.pos, e.button)
        elif e.type == pygame.MOUSEMOTION:
            mouse_motion_event.notify(e.pos, e.rel, e.buttons)
        elif e.type == pygame.KEYUP:
            keyup_event.notify(e.key, e.mod)
        elif e.type == pygame.KEYDOWN:
            keydown_event.notify(e.unicode, e.key, e.mod)
        elif e.type == pygame.USEREVENT:
            user_event.notify(e.code)


def clear(color: tuple = (255, 255, 255)) -> None:
    """
    Clear window surface.
    :param color: tuple[int, int, int, <int>].
    """
    global surface
    surface.fill(color)


def update(framerate=0) -> None:
    """
    Updates window and wait for next frame.
    :param framerate: int.
    """
    global clock
    pygame.display.update()
    clock.tick(framerate)


def get_elapsed_time() -> float:
    """
    Returns elapsed time as float seconds.
    :return: float.
    """
    global clock
    return clock.get_time() / 1000


set_title('Window')
