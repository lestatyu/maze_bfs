#!/usr/bin/env python
# -*- coding:utf-8 -*-

line01 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
line02 = [1, 0, 0, 1, 0, 0, 0, 1, 0, 1]
line03 = [1, 0, 0, 1, 0, 0, 0, 1, 0, 1]
line04 = [1, 0, 0, 0, 0, 1, 1, 0, 0, 1]
line05 = [1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
line06 = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
line07 = [1, 0, 1, 0, 0, 0, 1, 0, 0, 1]
line08 = [1, 0, 1, 1, 1, 0, 1, 1, 0, 1]
line09 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1]
line10 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
maze = [line01, line02, line03, line04, line05, line06, line07, line08, line09, line10]
maze_stack = [(1, 1)]


def go(direction):
    """

    :rtype : object
    """
    global maze_stack
    if maze_stack:
        peek = maze_stack[-1]
        if peek == (8, 8):
            print_path()
            return
        if direction == "D":
            if tuple([peek[0] + 1, peek[1]]) not in maze_stack:
                if maze[peek[0] + 1][peek[1]] == 0:
                    maze_stack.append(tuple([peek[0] + 1, peek[1]]))
                    go("D")
                else:
                    go("R")
            else:
                go("R")
        elif direction == "R":
            if tuple([peek[0], peek[1]+1]) not in maze_stack:
                if maze[peek[0]][peek[1] + 1] == 0:
                    maze_stack.append(tuple([peek[0], peek[1] + 1]))
                    go("D")
                else:
                    go("U")
            else:
                go("U")
        elif direction == "U":
            if tuple([peek[0]-1, peek[1]]) not in maze_stack:
                if maze[peek[0] - 1][peek[1]] == 0:
                    maze_stack.append(tuple([peek[0] - 1, peek[1]]))
                    go("D")
                else:
                    go("L")
            else:
                go("L")
        elif direction == "L":
            if tuple([peek[0], peek[1]-1]) not in maze_stack:
                if maze[peek[0]][peek[1] - 1] == 0:
                    maze_stack.append(tuple([peek[0], peek[1] - 1]))
                    go("D")
                else:
                    go_back()
            else:
                go_back()
        else:
            print("arg error!")


def go_back():
    global maze_stack
    if len(maze_stack) == 1:
        print("no path out")
        print_path()
        return
    peek = maze_stack[-1]
    peek_second = maze_stack[-2]
    if peek[0]-peek_second[0] == 1:
        maze_stack.pop()
        go("R")
    elif peek[0]-peek_second[0] == -1:
        maze_stack.pop()
        go("L")
    elif peek[1]-peek_second[1] == 1:
        maze_stack.pop()
        go("U")
    elif peek[1]-peek_second[1] == -1:
        maze_stack.pop()
        go_back()
    else:
        print("error")


def print_path():
    print(maze_stack)


go("D")
