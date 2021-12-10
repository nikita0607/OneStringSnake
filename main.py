import pygame
from random import randint as rnd

(lambda parts, win, apple, *_: (
    [(lambda: (
        [exit() for i in pygame.event.get() if i.type == pygame.QUIT],

        (lambda keys, set: [(globals().__setitem__("direction", i[1]), set.remove(None)) for i in [(pygame.K_UP, 0, 2),
                                                                          (pygame.K_DOWN, 2, 0),
                                                                          (pygame.K_RIGHT, 1, 3),
                                                                          (pygame.K_LEFT, 3, 1), ] if
                       (keys[i[0]] and len(set) and globals()["direction"] != i[2])])(pygame.key.get_pressed(), [None]),

        (lambda: (win.fill((0, 0, 0)),
                  [pygame.draw.rect(win, (255, 255, 255), (part["x"], part["y"], 16, 16)) for part in parts],
                  ))(),

        pygame.draw.rect(win, (210, 180, 180), (apple["x"], apple["y"], 16, 16)),
        pygame.display.update(),

        [(parts[i].__setitem__("x", parts[i-1]["x"]), parts[i].__setitem__("y", parts[i-1]["y"]))
         for i in range(len(parts)-1, 0, -1)],

        parts[0].__setitem__("y", parts[0]["y"]-20*(not (globals()["direction"]))),
        parts[0].__setitem__("y", parts[0]["y"]+20*(not (globals()["direction"]-2))),
        parts[0].__setitem__("x", parts[0]["x"]+20*(not (globals()["direction"]-1))),
        parts[0].__setitem__("x", parts[0]["x"]-20*(not (globals()["direction"]-3))),

        parts[0].__setitem__("x", 2) if parts[0]["x"] == 1002 else None,
        parts[0].__setitem__("x", 982) if parts[0]["x"] == -18 else None,
        parts[0].__setitem__("y", 2) if parts[0]["y"] == 502 else None,
        parts[0].__setitem__("y", 482) if parts[0]["y"] == -18 else None,

        (apple.__setitem__("x", -80), apple.__setitem__("y", -80), apple.__setitem__("time", 10),
         parts.append({"x": -80, "y": -80})) if (parts[0]["x"] == apple["x"] and parts[0]["y"] == apple["y"]) else None,

        print(parts),

        (lambda res: (print(f"You lose! Your score: {len(parts)}"), exit()) if len(res) else None)
        ((lambda set: [(i, set.remove(None))[0] for i in range(1, len(parts)) if (parts[0]["x"] == parts[i]["x"] and
                                                           parts[0]["y"] == parts[i]["y"] and len(set))])([None])),

        apple.__setitem__("time", apple["time"]-1) if apple["time"] > 0 else None,
        (apple.__setitem__("x", rnd(1, 40)*20+2), apple.__setitem__("y", rnd(1, 20)*20+2), apple.__setitem__("time", -1))
        if apple["time"] == 0 else None,

        pygame.time.delay(100)
        ))()
     for i in range(1, 10000000000000)]

))([{"x": 22, "y": 22}], pygame.display.set_mode((1000, 500)), {"x": rnd(1, 40)*20+2, "y": rnd(1, 20)*20+2, "time": -1},
   globals().__setitem__("direction", 1))