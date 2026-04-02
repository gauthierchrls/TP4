"""

Charles Gauthier
407
TP5

"""


import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_mountains():
    y = SCREEN_HEIGHT / 2 + 40

    arcade.draw_triangle_filled(-10, y - 190, 100, y + 60, 200, y - 190, arcade.color.BATTLESHIP_GREY)

    arcade.draw_triangle_filled(100, y - 190, 250, y + 90, 400, y - 190, arcade.color.BATTLESHIP_GREY)

    arcade.draw_triangle_filled(300, y - 190, 500, y + 20, 700, y - 190, arcade.color.BATTLESHIP_GREY)

    arcade.draw_triangle_filled(640, y - 190, 775, y + 60, 950, y - 190, arcade.color.BATTLESHIP_GREY)


def draw_ground():
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3.5, arcade.csscolor.DARK_GREEN)


def draw_sun():
    arcade.draw_arc_filled(800, 600, 120, 120, arcade.color.YELLOW, 180, 180)


def draw_house():
    points = [(250, 150), (450, 150), (450, 300), (250, 300)]

    arcade.draw_polygon_filled(points, arcade.color.BRICK_RED)

    arcade.draw_triangle_filled(250, 300, 450, 300, 350, 380, arcade.color.DARK_BROWN)

    arcade.draw_lrbt_rectangle_filled(330, 370, 150, 220, arcade.color.SIENNA)

    arcade.draw_lrbt_rectangle_filled(270, 310, 220, 260, arcade.color.LIGHT_BLUE)

    arcade.draw_lrbt_rectangle_filled(390, 430, 220, 260, arcade.color.LIGHT_BLUE)

    arcade.draw_lrbt_rectangle_filled(365, 405, 300, 360, arcade.color.DARK_BROWN)

    arcade.draw_line(380, 360, 390, 390, arcade.color.LIGHT_GRAY, 3)

    arcade.draw_line(390, 390, 380, 420, arcade.color.LIGHT_GRAY, 3)

    arcade.draw_line(380, 420, 395, 450, arcade.color.LIGHT_GRAY, 3)

    arcade.draw_line(395, 450, 385, 480, arcade.color.LIGHT_GRAY, 3)

    arcade.draw_line(385, 480, 400, 510, arcade.color.LIGHT_GRAY, 3)


def draw_tree(x, y):
    arcade.draw_lrbt_rectangle_filled(x - 10, x + 10, y, y + 40, arcade.color.DARK_BROWN)

    arcade.draw_circle_filled(x, y + 70, 30, arcade.color.FOREST_GREEN)

    arcade.draw_point(x - 12, y + 75, arcade.color.RED, 7)

    arcade.draw_point(x + 10, y + 65, arcade.color.RED, 7)

    arcade.draw_point(x, y + 85, arcade.color.RED, 7)


def draw_ellipse():
    arcade.draw_ellipse_filled(120, 80, 200, 60, arcade.color.LIGHT_BLUE)


def draw_text_message():
    arcade.draw_text("Bienvenue à la maison de papiiiiiiii!", 20, 550, arcade.color.BLACK, 20)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

draw_mountains()
draw_ground()
draw_sun()
draw_house()
draw_tree(150, 120)
draw_tree(600, 130)
draw_ellipse()
draw_text_message()

arcade.finish_render()
arcade.run()
