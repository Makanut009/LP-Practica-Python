import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class Skyline:

    def __init__(self, *args):
        """Inicialitza l'skyline de diferent manera segons el nombre de paràmetres"""

        if not args:
            self.edificis = []

        # Creació composta
        elif len(args) == 1:
            skylines = []
            for e in args[0]:
                skylines += [Skyline(e[0], e[1], e[2])]
            self.edificis = (unio_rec(skylines)).edificis  # Unió recursiva d'edificis

        # Creació simple
        elif len(args) == 3:
            self.edificis = [(args[0], args[1]), (args[2], 0)]

        # Creació aleatòria
        elif len(args) == 5:
            self.random(args[0], args[1], args[2], args[3], args[4])

        else:
            raise Exception("Nombre de paràmetres incorrectes per crear l'skyline")

    def __mul__(self, other):
        """Definició de l'operació '*' per als skylines"""
        if isinstance(other, self.__class__):   # Dos skylines -> Intersecció
            return self.interseccio(other)
        elif isinstance(other, int):
            return self.replica_skyline(other)  # Skyline i enter -> Replicació
        else:
            return NotImplemented

    def __rmul__(self, other):  # Definim també l'operació '*' per la dreta
        return self*other

    def __add__(self, other):
        """Definició de l'operació '+' per als skylines"""
        if isinstance(other, self.__class__):  # Dos skylines -> Unió
            return self.unio(other)
        elif isinstance(other, int):    # Skyline i enter -> Desplaçament dreta
            return self.desp_dreta(other)
        else:
            return NotImplemented

    def __radd__(self, other):  # Definim també l'operació '+' per la dreta
        return self+other

    def __sub__(self, other):
        """Definició de l'operació '-' per als skylines"""
        if isinstance(other, int):  # Skyline i enter -> Desplaçament esquerra
            return self.desp_esq(other)
        else:
            return NotImplemented

    def __neg__(self):
        """Negació d'skylines"""
        if not self.edificis:
            return Skyline()

        esq, dreta = self.edificis[0][0], self.edificis[-1][0]
        xs = [-e[0]+esq+dreta for e in reversed(self.edificis)]
        hs = [e[1] for e in reversed(self.edificis[:-1])] + [0]

        sk = Skyline()
        sk.edificis = list(zip(xs, hs))
        return sk

    def __str__(self):
        """Mètode per imprimir els edificis de l'skyline per terminal"""
        return str(self.edificis)

    def random(self, n, h, w, xmin, xmax):
        """Genera un skyline a partir d'n edificis generats aleatòriament"""
        if n < 1 or h < 0 or w < 1 or xmax <= xmin:
            raise Exception("Paràmetres per a la generació aleatòria incorrectes")
        # Ús d'un generador aleatori
        skylines = [next(rg(h, w, xmin, xmax)) for _ in range(n)]
        # Unió recursiva d'edificis
        self.edificis = (unio_rec(skylines)).edificis

    def mostra(self):
        """Genera i mostra la figura de l'skyline"""
        xs = []
        hs = []
        ws = []
        if self.edificis:
            e1 = self.edificis[0]
            for i in range(1, len(self.edificis)):
                e2 = self.edificis[i]
                if e1[1] > 0:
                    xs.append(e1[0])
                    hs.append(e1[1])
                    ws.append(e2[0] - e1[0])
                e1 = e2

        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.bar(xs, hs, width=ws, align='edge', color=['red'])
        plt.show()
        plt.close()

    def unio(self, sky2):
        """Computa la unió de dos skylines"""

        ed1 = self.edificis
        ed2 = sky2.edificis
        res = []

        if not ed1 or not ed2:  # Si alguns dels skylines és buit
            nou_sky = Skyline()
            nou_sky.edificis = ed2 if not ed1 else ed1
            return nou_sky

        it1 = it2 = 0
        ult_h1 = ult_h2 = 0  # Darrera alçada llegida de cada skyline

        while it1 != len(ed1) and it2 != len(ed2):
            (x1, h1) = ed1[it1]
            (x2, h2) = ed2[it2]

            if x1 == x2:  # Si els dos edificis tenen la mateixa x
                if max(h1, h2) != max(ult_h1, ult_h2):
                    # Afegim l'edifici si l'skyline no tenia ja aquesta alçada
                    res.append((x1, max(h1, h2)))
                ult_h1 = h1
                ult_h2 = h2
                it1 += 1
                it2 += 1

            elif x1 < x2:  # Si l'ed1 és a l'esquerra de l'ed2
                if h1 > ult_h2:
                    res.append((x1, h1))        # Afegim l'edifici si és més alt
                elif ult_h1 > ult_h2:
                    res.append((x1, ult_h2))    # Baixem només fins a ult_h2
                ult_h1 = h1
                it1 += 1

            else:  # Si l'ed2 és a l'esquerra de l'ed1
                if h2 > ult_h1:
                    res.append((x2, h2))        # Afegim l'edifici si és més alt
                elif ult_h2 > ult_h1:
                    res.append((x2, ult_h1))    # Baixem només fins a ult_h1
                ult_h2 = h2
                it2 += 1

        # Afegim edificis restants
        if it1 == len(ed1) and it2 != len(ed2):
            res += ed2[it2:]
        elif it2 == len(ed2) and it1 != len(ed1):
            res += ed1[it1:]

        res[-1] = ((max(ed1[-1][0], ed2[-1][0]), 0))  # Gestió del darrer edifici

        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky

    def interseccio(self, sky2):
        """Computa la intersecció de dos skylines"""

        ed1 = self.edificis
        ed2 = sky2.edificis
        res = []

        if not ed1 or not ed2:
            return Skyline()

        max_xmin = max(ed1[0][0], ed2[0][0])
        min_xmax = min(ed1[-1][0], ed2[-1][0])

        if max_xmin >= min_xmax:  # Els skylines no intersequen
            return Skyline()

        it1 = it2 = 0
        ult_h1 = ult_h2 = 0  # Darrera alçada llegida de cada skyline

        while it1 != len(ed1) and it2 != len(ed2):
            (x1, h1) = ed1[it1]
            (x2, h2) = ed2[it2]

            if x1 == x2:  # Si els dos edificis tenen la mateixa x
                res.append((x1, min(h1, h2)))
                ult_h1 = h1
                ult_h2 = h2
                it1 += 1
                it2 += 1

            elif x1 < x2:  # Si l'ed1 és a l'esquerra de l'ed2
                if h1 <= ult_h2:
                    res.append((x1, h1))        # Afegim l'edifici si és més baix
                elif ult_h1 < ult_h2:
                    res.append((x1, ult_h2))    # Pugem només fins a ult_h2
                it1 += 1
                ult_h1 = h1

            else:  # Si l'ed2 és a l'esquerra de l'ed1
                if h2 < ult_h1:
                    res.append((x2, h2))        # Afegim l'edifici si és més baix
                elif ult_h2 < ult_h1:
                    res.append((x2, ult_h1))    # Pugem només fins a ult_h1
                it2 += 1
                ult_h2 = h2

        nou_sky = Skyline()
        nou_sky.edificis = res
        return nou_sky

    def replica_skyline(self, N):
        """Replica l'skyline N vegades"""
        if N < 0:
            raise Exception("No es pot replicar un skyline un nombre negatiu de vegades")
        if N == 0:
            return Skyline()

        if not self.edificis:
            return Skyline()

        xmin = self.edificis[0][0]
        xmax = self.edificis[-1][0]
        mida = xmax - xmin

        res = [(e[0]+mida*i, e[1]) for i in range(1, N) for e in self.edificis]

        nou_sky = Skyline()
        nou_sky.edificis = self.edificis + res
        return nou_sky

    def desp_dreta(self, N):
        """Desplaça l'skyline N posicions cap a la dreta"""
        nou_sky = Skyline()
        nou_sky.edificis = list(map(lambda e: (e[0]+N, e[1]), self.edificis))
        return nou_sky

    def desp_esq(self, N):
        """Desplaça l'skyline N posicions cap a l'esquerra"""
        nou_sky = Skyline()
        nou_sky.edificis = list(map(lambda e: (e[0]-N, e[1]), self.edificis))
        return nou_sky

    def area(self):
        """Calcula l'àrea de l'skyline"""
        area = 0
        eds = self.edificis
        for i in range(len(eds)-1):
            area += (eds[i+1][0] - eds[i][0]) * eds[i][1]
        return area

    def alcada(self):
        """Calcula l'alçada màxima de l'skyline"""
        return max([e[1] for e in self.edificis])


# FUNCIONS AUXILIARS

def rg(h, w, xmin, xmax):
    """Generador aleatori d'skylines"""
    while True:
        alt = random.randint(0, h)
        esq = ampl = xmax
        while esq + ampl > xmax:
            esq = random.randint(xmin, xmax)
            ampl = random.randint(1, min(w, xmax-xmin))
            dreta = esq + ampl
        yield Skyline(esq, alt, esq+w)


def unio_rec(skylines):
    """Uneix la llista d'skylines recursivament"""
    if len(skylines) == 1:  # Cas base 1: un sol skyline
        return skylines[0]

    if len(skylines) == 2:  # Cas base 2: dos skylines
        return skylines[0].unio(skylines[1])

    sk1 = unio_rec(skylines[:len(skylines)//2])
    sk2 = unio_rec(skylines[len(skylines)//2:])
    return sk1.unio(sk2)


if __name__ == "__main__":
    main()
