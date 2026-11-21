from tkinter import *
from pygame import *
import sys, os
from datetime import datetime
from bulprint import print
import random as rd
from math import sqrt as sqroot
__doc__ = "print(help()) to show it"
__requirments__ = "pygame\ntkinter\nsys\nos\ndatetime\nrandom\nmath"
__python_version__ = "python::3.12,::3.13"
__version__ = "1.0.0"

def help():
    return """** game rocket help **
when run in state __main__:
- wait 0.5 sec
- click the button 'yes' in the upper left corner to start (or 'no' to exit)
- click '[direction] arrow button' on your keyboard to move to that direction (<-, ->, ^, [down arrow])
- you have the amount of life (shown in screen), if hit the meteor, lose 1

when imported:
- run startgame()
- ("... def startgame(echo:bool=True, execute:bool=False): ...")
@ can be updated
"""
def openfile():
    with open(__file__, 'r', encoding='utf-8') as f2coding:
        codefile = f2coding.read()
    return [codefile, __file__]
def startgame(file:bool=True, execute:bool=False):
    r = Tk()
    r.geometry('200x200')
    wpc = r.winfo_screenwidth()
    hpc = r.winfo_screenheight()
    r.overrideredirect(True)
    r.configure(bg='black')
    def sysexit():
        r.destroy()
        return
    def initpinit():
        init()
        r.destroy()
    Label(r, text='start?', font=('Arial', 35), bg='black', fg='yellow').grid(row=0, column=0, rowspan=2, columnspan=2)
    Button(r, text='Yes', font=('Arial', 30), bg='black', fg='lime', activebackground='white', activeforeground='black', command=initpinit).grid(row=2, column=1)
    Button(r, text='No', font=('Arial', 30), bg='black', fg='lime', activebackground='white', activeforeground='black', command=sysexit).grid(row=2, column=2)
    r.mainloop()
    fontword = font.SysFont('Arial', 20)
    if wpc > 1380:
        wpc = 1380
    if hpc > 1380:
        hpc = 1380
    explode = mixer.Sound("explosion.wav")
    usr = os.path.expanduser('~')
    s = display.set_mode((wpc - 100, hpc - 100))
    display.set_caption('rocket game')
    bg = image.load('nebula.png')
    s.blit(bg, (0, 0))
    icon = image.load('icon.ico')
    boom = image.load('broke.png')
    rocket = image.load('rocket.png')
    m = image.load('meteor.png')
    display.set_icon(icon)
    rx = (wpc - 100) / 2.5
    ry = (hpc - 100) / 2.5
    s.blit(rocket, (rx, ry))
    clock = time.Clock()
    ml = False
    mr = False
    mu = False
    md = False
    rfire = False
    mey = -100
    mex = rd.randint(0, wpc)
    mex2 = mex + 1
    mex3 = mex + 2
    mex4 = mex - 1
    mey2 = -100
    mey3 = -100
    mex5 = mex - 2
    mex6 = mex + 3
    mey4 = -100
    mex7 = mex + 4
    mex8 = mex - 3
    mex9 = mex - 4
    mey5 = -100
    mex10 = mex - 5
    mex11 = mex + 5
    mey6 = -100
    score = 0
    x1000 = False
    x10 = False
    x100 = False
    x10000 = False
    x10x = False
    errorlevel = False
    playmusic = False
    heart = 5
    listroi = list(range(0, wpc-100-40))
    while True:
        for events in event.get():
            if events.type == QUIT:
                return
            if events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    return
                if events.key == K_DOWN:
                    md = True
                if events.key == K_LEFT:
                    ml = True
                if events.key == K_RIGHT:
                    mr = True
                if events.key == K_UP:
                    mu = True
                if events.key == K_SPACE:
                    rfire = True
            if events.type == KEYUP:
                if events.key == K_DOWN:
                    md = False
                if events.key == K_LEFT:
                    ml = False
                if events.key == K_RIGHT:
                    mr = False
                if events.key == K_UP:
                    mu = False
                if events.key == K_SPACE:
                    rfire = False
        if score <= 200:
            meyc = 7
            rcc = 7
        elif score <= 500:
            rcc = 8
            meyc = 9
        else:
            rcc = 9
            meyc = 10.5
        if ml:
            rx -= rcc
        if mr:
            rx += rcc
        if mu:
            ry -= rcc
        if md:
            ry += rcc
        if ry < 0:
            ry = 0
        if ry > hpc - 100 - 160:
            ry = hpc - 100 - 160
        if rx < 0:
            rx = 0
        if rx > wpc - 100 - 93:
            rx = wpc - 100 - 93
        mey += meyc
        if len(listroi) == 0:
            listroi = list(range(0, wpc))
        if mey > hpc:
            mey = 0
            if mex != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex = rdc
            listroi.remove(rdc)
            if mex2 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex2 = rdc
            listroi.remove(rdc)
        if mey2 > hpc:
            mey2 = 0
            if mex3 != wpc + 100:
                score += 1
            if mex4 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex3 = rdc
            listroi.remove(rdc)
            rdc = rd.choice(listroi)
            mex4 = rdc
            listroi.remove(rdc)
        if mey3 > hpc:
            mey3 = 0
            if mex5 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex5 = rdc
            listroi.remove(rdc)
            if mex6 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex6 = rdc
            listroi.remove(rdc)
        if mey4 > hpc:
            mey4 = 0
            if mex7 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex7 = rdc
            listroi.remove(rdc)
            if mex8 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex8 = rdc
            listroi.remove(rdc)
        if mey5 > hpc:
            mey5 = 0
            if mex9 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex9 = rdc
            listroi.remove(rdc)
            if mex10 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex10 = rdc
            listroi.remove(rdc)
        if mey6 > hpc:
            mey6 = 0
            if mex11 != wpc + 100:
                score += 1
            rdc = rd.choice(listroi)
            mex11 = rdc
            listroi.remove(rdc)
        scoreword = fontword.render(f'Scores: {score}', True, (0, 255, 255))
        s.blit(bg, (0, 0))
        s.blit(m, (mex, mey))
        s.blit(m, (mex2, mey))
        if (mey == 7 * 50 and score > 20) or x1000:
            x1000 = True
        if (mey == 7 * 30 and score > 45) or x10:
            x10 = True
        if (mey == 7 * 40 and score > 80) or x100:
            x100 = True
        if (mey == 7 * 20 and score > 100) or x10000:
            x10000 = True
        if (mey == 7 * 10 and score > 150) or x10x:
            x10x = True

        if x10x:
            s.blit(m, (mex11, mey6))
            mey6 += meyc
        if x10:
            s.blit(m, (mex5, mey3))
            s.blit(m, (mex6, mey3))
            mey3 += meyc
        if x1000:
            s.blit(m, (mex3, mey2))
            s.blit(m, (mex4, mey2))
            mey2 += meyc
        if x100:
            s.blit(m, (mex7, mey4))
            s.blit(m, (mex8, mey4))
            mey4 += meyc
        if x10000:
            s.blit(m, (mex9, mey5))
            s.blit(m, (mex10, mey5))
            mey5 += meyc
        kc = sqroot((rx - mex) ** 2 + (ry - mey) ** 2)
        kc2 = sqroot((rx - mex2) ** 2 + (ry - mey) ** 2)
        kc3 = sqroot((rx - mex3) ** 2 + (ry - mey2) ** 2)
        kc4 = sqroot((rx - mex4) ** 2 + (ry - mey2) ** 2)
        kc5 = sqroot((rx - mex5) ** 2 + (ry - mey3) ** 2)
        kc6 = sqroot((rx - mex6) ** 2 + (ry - mey3) ** 2)
        kc7 = sqroot((rx - mex7) ** 2 + (ry - mey4) ** 2)
        kc8 = sqroot((rx - mex8) ** 2 + (ry - mey4) ** 2)
        kc9 = sqroot((rx - mex9) ** 2 + (ry - mey5) ** 2)
        kc10 = sqroot((rx - mex10) ** 2 + (ry - mey5) ** 2)
        kc11 = sqroot((rx - mex11) ** 2 + (ry - mey6) ** 2)
        if kc <= 160 / 2:
            heart -= 1
            mex = wpc + 100
        if kc2 <= 160 / 2:
            heart -= 1
            mex2 = wpc + 100
        if kc3 <= 160 / 2:
            heart -= 1
            mex3 = wpc + 100
        if kc4 <= 160 / 2:
            heart -= 1
            mex4 = wpc + 100
        if kc5 <= 160 / 2:
            heart -= 1
            mex5 = wpc + 100
        if kc6 <= 160 / 2:
            heart -= 1
            mex6 = wpc + 100
        if kc7 <= 160 / 2:
            heart -= 1
            mex7 = wpc + 100
        if kc8 <= 160 / 2:
            heart -= 1
            mex8 = wpc + 100
        if kc9 <= 160 / 2:
            heart -= 1
            mex9 = wpc + 100
        if kc10 <= 160 / 2:
            heart -= 1
            mex10 = wpc + 100
        if kc11 <= 160 / 2:
            heart -= 1
            mex11 = wpc + 100
        if heart <= 0 and not errorlevel:
            cantmove = (rx, ry, mex, mex2, mex3, mex4, mex5, mex6, mex7, mex8, mex9, mex10, mex11, mey, mey2, mey3, mey4, mey5, mey6)
            playmusic = True
            errorlevel = True
        if playmusic:
            def startgameagain(file, execute):
                r.destroy()
                startgame(file=file, execute=execute)
            r = Tk()
            r.withdraw()
            rtop = Toplevel(r)
            rtop.protocol("WM_DELETE_WINDOW", lambda: r.destroy())
            rtop.title("done")
            Label(rtop, text=f'scores: {score}', font=('Arial', 20)).grid(row=0, column=0, columnspan=2)
            Label(rtop, text='Do you want to try again?', font=('Arial', 20)).grid(row=1, column=0, columnspan=2)
            Button(rtop, text='Yes', font=('Arial', 20), bg='black', fg='white', activebackground='red', command=lambda:startgameagain(file, execute)).grid(row=2, column=0)
            Button(rtop, text='No', font=('Arial', 20), bg='black', fg='white', activebackground='red', command=sysexit).grid(row=2, column=1)
            explode.play()
            playmusic = False
        if errorlevel:
            s.blit(boom, (rx, ry))
            s.blit(rocket, (wpc + 500, 0))
            (rx, ry, mex, mex2, mex3, mex4, mex5, mex6, mex7, mex8, mex9, mex10, mex11, mey, mey2, mey3, mey4, mey5, mey6) = cantmove
            rtop.update()
            r.update()
        else:
            s.blit(rocket, (rx, ry))
            s.blit(scoreword, (0, 0))
        clock.tick(60)
        display.update()
if __name__ == '__main__':
    print('\n\n')
    print(f'starting... ({datetime.now().strftime("%Y/%m/%d-%H:%M:%S")}, {sys.executable})', time=0.5)
    startgame()