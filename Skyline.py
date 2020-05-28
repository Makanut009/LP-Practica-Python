import matplotlib.pyplot as plt
import random
import time


class Skyline:

    def __init__(self, *args):

        if not args:
            self.edificis = []

        # Creació composta
        elif len(args) == 1:
            skylines = []
            for e in args[0]:
                skylines += [Skyline(e[0], e[1], e[2])]
            self.edificis = (unio_rec(skylines)).edificis

        # Creació normal
        elif len(args) == 3:
            self.edificis = [(args[0], args[1]), (args[2], 0)]

        # Creació aleatòria
        elif len(args) == 5:
            self.random(args[0], args[1], args[2], args[3], args[4])

        else:
            print("Nombre de paràmetres incorrectes per crear l'skyline")
            raise Exception

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.interseccio(other)
        elif isinstance(other, int):
            return self.replica_skyline(other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self*other

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.unio(other)
        elif isinstance(other, int):
            return self.desp_dreta(other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self+other

    def __sub__(self, other):
        if isinstance(other, int):
            return self.desp_esq(other)
        else:
            return NotImplemented

    def __neg__(self):
        esq, dreta = self.edificis[0][0], self.edificis[-1][0]
        xs = [-e[0]+esq+dreta for e in self.edificis]
        xs.reverse()
        hs = [0] + [e[1] for e in self.edificis[:-1]]
        hs.reverse()

        sk = Skyline()
        sk.edificis = list(zip(xs, hs))
        return sk

    def __str__(self):
        return str(self.edificis)


    def random(self, n, h, w, xmin, xmax):
        if n < 1 or h < 0 or w < 1 or xmax <= xmin:
            raise Exception
        
        skylines = [next(rg(h, w, xmin, xmax)) for _ in range(n)]

        self.edificis = (unio_rec(skylines)).edificis

    def mostra(self):
        xs = []
        hs = []
        ws = []
        e1 = self.edificis[0]
        for i in range(1, len(self.edificis)):
            e2 = self.edificis[i]
            if e1[1] > 0:
                xs.append(e1[0])
                hs.append(e1[1])
                ws.append(e2[0] - e1[0])
            e1 = e2

        plt.bar(xs, hs, width=ws, align='edge', color=['red'])
        plt.show()
        plt.close()

    def unio(self, sky2):

        ed1 = self.edificis.copy()
        ed2 = sky2.edificis

        if not ed1:
            nou_sky = Skyline()
            nou_sky.edificis = ed2
            return nou_sky

        if not ed2:
            nou_sky = Skyline()
            nou_sky.edificis = ed1
            return nou_sky

        it1 = it2 = 0
        ult_h1 = ult_h2 = 0
        (x1, h1) = ed1[it1]
        (x2, h2) = ed2[it2]

        while it1 != len(ed1) and it2 != len(ed2):

            if x1 == x2:
                ed1[it1] = (x1, max(h1, h2))
                ult_h1 = h1
                ult_h2 = h2
                it1 += 1
                it2 += 1
                if it1 != len(ed1):
                    (x1, h1) = ed1[it1]
                if it2 != len(ed2):
                    (x2, h2) = ed2[it2]

            elif x1 < x2:
                if h1 > ult_h1:
                    if h1 < ult_h2:
                        del ed1[it1]
                    else:
                        it1 += 1

                else:
                    if h1 < ult_h2:
                        if ult_h1 > ult_h2:
                            ed1[it1] = (x1, ult_h2)
                            it1 += 1
                        else:
                            del ed1[it1]
                    else:
                        it1 += 1

                ult_h1 = h1
                if it1 != len(ed1):
                    (x1, h1) = ed1[it1]

            else:
                if h2 > ult_h2:
                    if h2 > ult_h1:
                        ed1.insert(it1, (x2, h2))
                        it1 += 1

                else:
                    if h2 < ult_h1:
                        if ult_h2 > ult_h1:
                            ed1.insert(it1, (x2, ult_h1))
                            it1 += 1
                    else:
                        ed1.insert(it1, (x2, h2))
                        it1 += 1

                it2 += 1
                ult_h2 = h2
                if it2 != len(ed2):
                    (x2, h2) = ed2[it2]

        if it1 == len(ed1) and it2 != len(ed2):
            ed1 += ed2[it2:]

        nou_sky = Skyline()
        nou_sky.edificis = ed1
        return nou_sky

    def interseccio(self, sky2):

        ed1 = self.edificis
        ed2 = sky2.edificis

        if not ed1 or not ed2:
            return Skyline()

        it1 = it2 = 0
        ult_h1 = ult_h2 = 0
        res = []

        xmin = max(ed1[0][0], ed2[0][0])
        xmax = min(ed1[-1][0], ed2[-1][0])

        if xmin < xmax:  # els skylines intersequen en algun punt
            while it1 != len(ed1) and it2 != len(ed2):
                (x1, h1) = ed1[it1]
                (x2, h2) = ed2[it2]

                if x1 == x2:
                    res.append((x1, min(h1, h2)))
                    ult_h1 = h1
                    ult_h2 = h2
                    it1 += 1
                    it2 += 1

                elif x1 < x2:
                    if h1 > ult_h1:
                        if h1 < ult_h2:
                            res.append((x1, h1))
                    else:
                        if h1 < ult_h2:
                            res.append((x1, h1))
                    ult_h1 = h1
                    it1 += 1

                else:
                    if h2 > ult_h2:
                        if h2 < ult_h1:
                            res.append((x2, h2))
                        else:
                            res.append((x2, ult_h1))
                    else:
                        if h2 < ult_h1:
                            res.append((x2, h2))
                    ult_h2 = h2
                    it2 += 1

        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky

    def replica_skyline(self, N):
        xmin = self.edificis[0][0]
        xmax = self.edificis[-1][0]
        mida = xmax - xmin

        res = [(e[0]+mida*i, e[1]) for i in range(1, N) for e in self.edificis]

        nou_sky = Skyline()
        nou_sky.edificis = self.edificis + res
        return nou_sky

    def desp_dreta(self, N):
        nou_sky = Skyline()
        nou_sky.edificis = list(map(lambda e: (e[0]+N, e[1]), self.edificis))
        return nou_sky

    def desp_esq(self, N):
        nou_sky = Skyline()
        nou_sky.edificis = list(map(lambda e: (e[0]-N, e[1]), self.edificis))
        return nou_sky

    def area(self):
        area = 0
        eds = self.edificis
        for i in range(len(eds)-1):
            area += (eds[i+1][0] - eds[i][0]) * eds[i][1]
        return area

    def alcada(self):
        return max([e[1] for e in self.edificis])


def rg(h, w, xmin, xmax):
    while True:
        alt = random.randint(0, h)
        esq = ampl = xmax
        while esq + ampl > xmax:
            esq = random.randint(xmin, xmax)
            ampl = random.randint(1, min(w, xmax-xmin))
            dreta = esq + ampl
        yield Skyline(esq, alt, esq+w)


def unio_rec(skylines):
    if len(skylines) == 1:
        return skylines[0]

    if len(skylines) == 2:
        return skylines[0].unio(skylines[1])

    sk1 = unio_rec(skylines[:len(skylines)//2])
    sk2 = unio_rec(skylines[len(skylines)//2:])
    return sk1.unio(sk2)


def main():
    #sk1 = Skyline()
    #sk2 = Skyline(1, 2, 3)
    #sk3 = Skyline([(0, 3, 1), (1, 1, 2), (3, 3, 4)])
    #sk4 = Skyline(10000, 20, 3, 1, 10000)
    #sk5 = Skyline(5, 10, 3, 0, 100)
    start1 = time.time()
    sk4 = Skyline(100000, 20, 3, 1, 10000)
    end1 = time.time()
    sk4.mostra()
    print(end1 - start1)


if __name__ == "__main__":
    main()
