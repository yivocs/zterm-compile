from compiler import asm_code
from x16asm import machine_code
from x16vm import Axepu, cpu
from memory import memory
from utils import read_zlang

log = print


def code(zlang, d=None):
    if d is None:
        d = {}
    zlang = replaced_zlang(zlang, d)
    asm = asm_code(zlang)
    c = machine_code(asm)
    return c


def replaced_zlang(zlang, replace_dict):
    l = []

    for line in zlang.split('\n'):
        for k, v in replace_dict.items():
            if k in line:
                line = line.replace(k, v, 1)
        l.append(line)

    code = '\n'.join(l)
    return code


def draw_yz():
    zlang = read_zlang('draw_yz')
    c = code(zlang)
    length = len(c)
    memory[:length] = c
    zpu = Axepu(memory)
    zpu.run()
    # cpu.run()


def draw_char(char, x, y, color=255):
    zlang = read_zlang('draw_char')
    # draw_char('Z', 50, 50)
    char = f'\'{char}\''
    d = {
        '{position.x}': str(x),
        '{position.y}': str(y),
        '{char}': char,
        '{color}': str(color),
    }
    c = code(zlang, d)
    length = len(c)
    memory[:length] = c
    zpu = Axepu(memory)
    zpu.run()
    # cpu.run()


def draw_point(x, y, color):
    zlang = read_zlang('draw_point')
    # draw_char('Y', 50, 50)
    d = {
        '{position.x}': str(x),
        '{position.y}': str(y),
        '{color}': str(color),
    }
    c = code(zlang, d)
    length = len(c)
    memory[:length] = c
    zpu = Axepu(memory)
    zpu.run()
    # cpu.run()
