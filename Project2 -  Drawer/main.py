#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import pygame
from pygame.locals import *


def parse_figure(arg):
    if 'color' in arg:
        if arg['color'] in palette:
            final_color = Color(palette[arg['color']])
        else:
            if arg['color'][0] == '#':
                final_color = Color(arg['color'])
            else:
                final_color = arg['color']
                final_color = final_color.replace('(', '')
                final_color = final_color.replace(')', '')
                final_color = final_color.split(',')
                final_color = (int(final_color[0]),
                               int(final_color[1]), int(final_color[2]))
    else:
        final_color = Color(palette[fg_color])

    if arg['type'] == 'point':
        screen.set_at((arg['x'], arg['y']), final_color)

    if arg['type'] == 'polygon':
        pygame.draw.polygon(screen, final_color, arg['points'], 2)

    if arg['type'] == 'rectangle':
        pygame.draw.rect(screen, final_color, (arg['x'] - arg['width']
                         / 2, arg['y'] - arg['height'] / 2, arg['width'], arg['height']), 2)

    if arg['type'] == 'square':
        pygame.draw.rect(screen, final_color, (arg['x'] - arg['size']
                         / 2, arg['y'] - arg['size'] / 2, arg['size'],
                         arg['size']), 2)

    if arg['type'] == 'circle':
        pygame.draw.circle(screen, final_color, (arg['x'], arg['y']),
                           arg['radius'], 2)

    pygame.display.update()


def parse_screen(arg):
    width = arg['width']
    height = arg['height']
    bg_color = arg['bg_color']
    global fg_color
    fg_color = arg['fg_color']

    resolution = (width, height)
    pygame.display.set_mode(resolution)
    global screen
    screen = pygame.display.get_surface()
    screen.fill(Color(palette[bg_color]))
    pygame.display.update()


def parse_palette(arg):
    global palette
    palette = arg


def file_reader(data):
    value = data['Palette']
    parse_palette(value)
    value = data['Screen']
    parse_screen(value)
    value = data['Figures']
    for figure in value:
        parse_figure(figure)


def main():
    arguments = sys.argv
    flag = 0
    output_file = None
    json_file = ''

    if len(arguments) < 2:
        print('No arguments, give input json file!')
        return

    for (index, element) in enumerate(arguments):
        if index == 0:
            continue
        if element == '-o' or element == '--output':
            flag = 1
            continue
        if flag == 1:
            output_file = element
            flag = 0
            continue
        json_file = element

    if flag == 1:
        print('Couldnt get the name of output file')
        return

    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except IOError:
        print('There is no such json file')
        return

    pygame.init()
    pygame.display.set_caption('Project 2 - python')
    file_reader(data)
    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
    finally:
        if output_file is not None:
            pygame.image.save(screen, output_file + '.png')

    pygame.display.quit()
    sys.exit(0)


if __name__ == '__main__':
    main()
