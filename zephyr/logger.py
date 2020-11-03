# D. Cashon
# dcashonsmith@gmail.com
# Terminal

import curses
import pprint
import time

import obd
from obd.commands import __mode1__
from tabulate import tabulate


DESIRED_PARAMETERS = [
    obd.commands.SPEED,
    obd.commands.RPM,
    obd.commands.COOLANT_TEMP,
    #obd.commands.ENGINE_LOAD,
    #obd.commands.LONG_FUEL_TRIM_1,
    #obd.commands.MAF,
    #obd.commands.O2_B1S1,
    #obd.commands.O2_B1S2
]

HEADERS = [x.name for x in DESIRED_PARAMETERS]

connection = obd.OBD(fast=False)

myscreen = curses.initscr()

# non-block for user input
myscreen.nodelay(True)

curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
y,x = myscreen.getmaxyx()

# HEADER
myscreen.addstr("obd-subaru", curses.color_pair(1))

editwin = curses.newwin(curses.LINES - 2, curses.COLS - 2, 1, 0)

myscreen.refresh()

# display data
table = []
while True:
    cdata = []
    for param in DESIRED_PARAMETERS:
        res = connection.query(param)
        if res:
            cdata.append(res.value.magnitude)
        else:
            cdata.append('NULL')
    table.append(cdata)

    editwin.addstr(1,0, tabulate(table, headers=HEADERS))
    editwin.refresh()

    if len(table) > curses.LINES - 10:
        table.clear()
        editwin.clear()

    # close if user enters keypress
    if myscreen.getch() != -1:
        print(myscreen.getch())
        break

    time.sleep(1)        

curses.endwin()
