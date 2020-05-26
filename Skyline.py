#!/usr/bin/env python3
import matplotlib.pyplot as plt
import random

class Skyline:

    def __init__(self, arg1 = None, arg2 = None, arg3 = None):
        if arg1 == None:
            self.edificis = []
        elif type(arg1) == int:
            self.edificis = [(arg1, arg2), (arg3, 0)]
        else:
            print("Miau")
            for e in arg1:
                self = self.unio(Skyline(e[0], e[1], e[2]))
            print(self.edificis)

    def random(self, n, h, w, xmin, xmax):
        if n < 1:
            raise Exception
        if h < 0:
            raise Exception
        if w < 1:
            raise Exception
        if xmax <= xmin:
            raise Exception

        edificis = []

        for i in range(n):
            alt = random.randint(0,h)
            esq = ampl = xmax
            while esq + ampl > xmax:
                esq = random.randint(xmin, xmax)
                ampl = random.randint(1,min(w, xmax-xmin))
                dreta = esq + ampl                
            edificis += [(esq, alt, esq+w)]

        i=0
        print(len(edificis))
        for e in edificis:
            #print(i)
            if not self.edificis:
                self.edificis = [e]
            else:
                self = self.unir_edifici(e)
            i+=1

        print(len(self.edificis))
        return self


    def __mul__(self, other):
        if isinstance(other, self.__class__):
            print("Interseccio d'skylines")
            return self.interseccio(other)

        elif isinstance(other, int):
            print("Replicacio N vegades de l'skyline")
            return self.replica_skyline(other)

        else:
            return NotImplemented


    def __rmul__(self, other):
        return self*other


    def __add__(self, other):
        if isinstance(other, self.__class__):
            print("Unio d'skylines")
            return self.unio(other)

        elif isinstance(other, int):
            print("Desplaçament a la dreta de l’skyline N posicions")
            return self.desp_dreta(other)

        else:
            return NotImplemented


    def __radd__(self, other):
        return self+other


    def __sub__(self, other):
        if isinstance(other, int):
            print("Desplaçament a l’esquerra de l’skyline N posicions")
            return self.desp_esq(other)
        else:
            return NotImplemented


    def __neg__(self):
        print("Retorna l’skyline reflectit")
        return Skyline(2,2,7)


    def __str__(self):
        return str(self.edificis)


    def mostra(self):
        xs = []
        hs = []
        for i in range(len(self.edificis)-1):
            dif = self.edificis[i+1][0] - self.edificis[i][0]
            xs += [self.edificis[i][0]+k for k in range(dif)]
            hs += [self.edificis[i][1]] * dif
        
        plt.bar(xs, hs, width=1, align='edge', color=['red'])
        plt.show()
        plt.close()


    def unio(self, sky2):

        ed1 = self.edificis
        ed2 = sky2.edificis
        res = []

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

        print("Ed1: ", ed1)
        print("Ed2: ", ed2)

        while it1 != len(ed1) and it2 != len(ed2):
            (x1, h1) = ed1[it1]
            (x2, h2) = ed2[it2]

            if x1 == x2:
                res.append((x1, max(h1, h2)))
                ult_h1 = h1
                ult_h2 = h2
                it1 += 1
                it2 += 1

            elif x1 < x2:
                if h1 > ult_h1:
                    if h1 > ult_h2:
                        res.append((x1, h1))
                else:
                    if h1 > ult_h2:
                        res.append((x1,h1))
                    elif ult_h1 > ult_h2:
                        res.append((x1, ult_h2))
                ult_h1 = h1
                it1 += 1

            else:
                if h2 > ult_h2:
                    if h2 > ult_h1:
                        res.append((x2, h2))
                else:
                    if h2 > ult_h1:
                        res.append((x2,h2))
                    elif ult_h2 > ult_h1:
                        res.append((x2, ult_h1))
                ult_h2 = h2
                it2 += 1

        if it1 == len(ed1) and it2 != len(ed2):
            res += ed2[it2:]
        elif it2 == len(ed2) and it1 != len(ed1):
            res += ed1[it1:]

        res[-1] = ((max(ed1[-1][0], ed2[-1][0]), 0))

        print("Res: ", res)

        nou_sky = Skyline()
        nou_sky.edificis = res
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

        if xmin < xmax: #els skylines intersequen en algun punt
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
                            res.append((x1,h1))
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
                            res.append((x2,h2))
                    ult_h2 = h2
                    it2 += 1

        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky


    def replica_skyline(self, N):
        
        xmin = self.edificis[0][0]
        xmax = self.edificis[-1][0]
        mida = xmax - xmin
        res = []

        for i in range(0, N):
            for e in self.edificis:
                res.append((e[0]+mida*i, e[1]))

        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky


    def desp_dreta(self, N): #Es podria fer amb map?
        res = []
        for e in self.edificis:
            res.append((e[0]+N, e[1]))
        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky


    def desp_esq(self, N): #Es podria fer amb map?
        res = []
        for e in self.edificis:
            res.append((e[0]-N, e[1]))
        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky


    def area(self):
        area = 0
        for i in range(len(self.edificis)-1):
            area += (self.edificis[i+1][0] - self.edificis[i][0]) * self.edificis[i][1] 
        return area

    def alcada(self):
        return max([e[1] for e in self.edificis])


def main():
    #sk0 = Skyline()s
    sk2 = Skyline(1,2,3)
    sk0 = Skyline([(1, 2, 3), (3, 4, 6)])
    #sk1 = Skyline(1,2,3)
    # sk2 = Skyline(2,3,4)
    # sk3 = Skyline(2,1,6)
    # sk4 = Skyline(9,1,12)
    # sk5 = Skyline(-3,1,-2)
    # sk1 = sk1.unio(sk2)
    # sk1 = sk1.unio(sk3)
    # sk1 = sk1.unio(sk4)
    # sk1 = sk1.unio(sk5)
    #sk1 = sk0.interseccio(sk1)
    sk0.mostra()
    sk2.mostra()
    # print(sk1.area())
    # print(sk1.alcada())


if __name__ == "__main__":
    main()