import pygame as pg
from numpy import zeros, int32, int16
import time
from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile


def make_effects(sound, samples_per_second = None):
    if samples_per_second is None:
        samples_per_second = pg.mixer.get_init()[0]

    # Make a Pedalboard object, containing multiple plugins:
    board = Pedalboard([Chorus(), Reverb(room_size=0.25)])

    a1 = pg.sndarray.array(sound)
    # Run the audio through this pedalboard!
    effected = board(a1, samples_per_second)

    sound2 = pg.sndarray.make_sound(effected.astype(int16))
    return sound2


def make_echo(sound, samples_per_second = None, mydebug=True):
    """returns a sound which is echoed of the last one."""
    if samples_per_second is None:
        samples_per_second = pg.mixer.get_init()[0]

    echo_length = 10

    a1 = pg.sndarray.array(sound)
    if mydebug:
        print(f"SHAPE1: {a1.shape}")

    length = a1.shape[0]

    # myarr = zeros(length+12000)
    myarr = zeros(a1.shape, int32)

    if len(a1.shape) > 1:
        # mult = a1.shape[1]
        size = (a1.shape[0] + int(echo_length * a1.shape[0]), a1.shape[1])
        # size = (a1.shape[0] + int(a1.shape[0] + (echo_length * 3000)), a1.shape[1])
    else:
        # mult = 1
        size = (a1.shape[0] + int(echo_length * a1.shape[0]),)
        # size = (a1.shape[0] + int(a1.shape[0] + (echo_length * 3000)),)

    if mydebug:
        print(int(echo_length * a1.shape[0]))
    myarr = zeros(size, int32)

    if mydebug:
        print(f"size {size}")
        print(myarr.shape)
    myarr[:length] = a1
    # print(myarr[3000:length+3000])
    # print(a1 >> 1)
    # print("a1.shape %s" % (a1.shape,))
    # c = myarr[3000:length+(3000*mult)]
    # print("c.shape %s" % (c.shape,))

    incr = int(samples_per_second / echo_length)
    gap = length

    myarr[incr : gap + incr] += a1 >> 1
    myarr[incr * 2 : gap + (incr * 2)] += a1 >> 2
    myarr[incr * 3 : gap + (incr * 3)] += a1 >> 3
    myarr[incr * 4 : gap + (incr * 4)] += a1 >> 4

    if mydebug:
        print(f"SHAPE2: {myarr.shape}")

    sound2 = pg.sndarray.make_sound(myarr.astype(int16))

    return sound2
