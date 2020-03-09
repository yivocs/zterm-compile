from screen import Screen
from compiler import asm_code
from x16asm import machine_code
from x16vm import Axepu, cpu
from memory import memory
from drawer import draw_yz, draw_point, draw_char
from utils import read_zlang


log = print


def code(path):
    p = path
    zlang = read_zlang(p)
    asm = asm_code(zlang)
    c = machine_code(asm)
    return c


def mouse_down(x, y):
    print('on mouse down: x {}, y {}'.format(x, y))
    color = 188
    draw_point(x, y, color)
    # draw_yz()


def key_a_down():
    draw_char('A', 20, 20)


def key_x_down():
    draw_char('X', 40, 20)


def key_e_down():
    draw_char('E', 60, 20)


def key_1_down():
    draw_char('1', 80, 40)


def key_z_down():
    draw_yz()


def main():
    # c = code('draw_yz.a16')
    # length = len(c)
    # memory[:length] = c
    # log('memory length', len(memory))

    screen = Screen(500, 500, 25, 0.2, memory)
    screen.set_memory_begin_end(44512, 54512)
    screen.set_mouse_down_fun(mouse_down)
    screen.set_keydown_fun('a', key_a_down)
    screen.set_keydown_fun('x', key_x_down)
    screen.set_keydown_fun('e', key_e_down)
    screen.set_keydown_fun('1', key_1_down)
    screen.set_keydown_fun('z', key_z_down)
    screen.start()

    # cpu = Axepu(memory)
    # cpu.run()
    # z
    print(memory[65380:65390])


if __name__ == '__main__':
    main()
    # pass