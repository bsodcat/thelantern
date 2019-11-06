# The Lantern by Nicholas Achterberg
# 10:51 9/19/2019
#
# This is my first rogue-like game.
# The gameplay is focused around light, puzzles and fighting.
#
# I hope you enjoy :)

import libtcodpy as libtcod

from entity               import Entity
from input_handlers       import handle_keys
from map_objects.game_map import GameMap
from render_functions     import clear_all, render_all


def main():
    screen_w = 80
    screen_h = 50
    map_w = 80
    map_h = 45

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    player = Entity(int(screen_w / 2), int(screen_h / 2), '@', libtcod.white)
    npc = Entity(int(screen_w / 2 - 5), int(screen_h / 2), '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_w, screen_h, 'The Lantern', False)

    con = libtcod.console_new(screen_w, screen_h)

    game_map = GameMap(map_w, map_h)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, screen_w, screen_h, colors)

        libtcod.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move

            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
     main()