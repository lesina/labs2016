#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while (wall_is_on_the_right() != True):
        if (wall_is_above() != True):
            move_up()
            fill_cell()
            move_down()
        if(wall_is_beneath() != True):
            move_down()
            fill_cell()
            move_up()
        move_right()
    if (wall_is_above() != True):
        move_up()
        fill_cell()
        move_down()
    if (wall_is_beneath() != True):
        move_down()
        fill_cell()
        move_up()


if __name__ == '__main__':
    run_tasks()