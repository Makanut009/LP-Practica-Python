#!/usr/bin/env python3
import matplotlib.pyplot as plt

class Skyline:
    def __init__(self, xmin = None, alt = None, xmax = None):
        if xmin == None:
            self.edificis = []
        else:
            self.edificis = [(xmin, alt, xmax)]

    # def __repr__(self):
    #     return self.__str__()

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

    def __str__(self):
        return str(self.edificis)
        
    def mostra(self):
        xs = []
        alts = []
        for e in self.edificis:
            xs += [i for i in range(e[0], e[2])]
            n = (e[2] - e[0])
            alts += [e[1]]*n
        
        plt.bar(xs, alts, width=1, align='edge', color=['red'])
        plt.show()
        plt.close()


    def unio(self, skyline):
        resultat = self
        for e in skyline.edificis:
            resultat = resultat.unir_edifici(e)
        return resultat

    def interseccio(self, skyline):
        resultat = self
        for e in skyline.edificis:
            resultat = resultat.intersecar_edifici(e)
        return resultat


    def unir_edifici(self, edifici):
        edificis = self.edificis
        nou_sky = Skyline()
        res = []

        xmin, alt, xmax = edifici[0], edifici[1], edifici[2]
        sky_xmin, sky_xmax = edificis[0][0], edificis[len(edificis)-1][2]

        if xmin < sky_xmin:
            print("Sobresurt per l'esquerra")
            if xmax < sky_xmin:
                res = [edifici] + [(xmax, 0, sky_xmin)]
            else:
                res = [(xmin, alt, sky_xmin)]

        for e in edificis: #VIGILAR QUÈ FEM AMB ELS =
            if alt > e[1]:
                if xmin < e[0]:
                    if xmax > e[0]:
                        if xmax < e[2]:
                            ed_nou = (e[0], alt, xmax)
                            ed_dret = (xmax, e[1], e[2])
                            res += [ed_nou, ed_dret]
                        else:
                            ed_nou = (e[0], alt, e[2])
                            res.append(ed_nou)
                    else:
                        res.append(e)

                elif xmin == e[0]:
                    if xmax >= e[2]:
                        ed_nou = (xmin, alt, e[2])
                        res += [ed_nou]
                    else:
                        ed_nou = (xmin, alt, xmax)
                        ed_dret = (xmax, e[1], e[2])
                        res += [ed_nou, ed_dret]

                else:
                    if xmin < e[2]:
                        if xmax > e[2]:
                            ed_esq = (e[0], e[1], xmin)
                            ed_nou = (xmin, alt, e[2])
                            res += [ed_esq, ed_nou]
                        else:
                            ed_esq = (e[0], e[1], xmin)
                            ed_nou = (xmin, alt, xmax)
                            ed_dret = (xmax, e[1], e[2])
                            res += [ed_esq, ed_nou, ed_dret]
                    else:
                        res.append(e)
            else:
                res.append(e)

        if xmax > sky_xmax:
            print("Sobresurt per la dreta")
            if xmin > sky_xmax:
                res += [(sky_xmax, 0, xmin)] + [edifici]
            else:
                res += [(sky_xmax, alt, xmax)]

        nou_sky.edificis = res
        return nou_sky


    def intersecar_edifici(self, edifici):
        nou_sky = Skyline()
        edificis = self.edificis
        res = []

        xmin, alt, xmax = edifici[0], edifici[1], edifici[2]

        esq = max(edificis[0][0], xmin)
        dreta = min(edificis[len(edificis)-1][2], xmax)

        if esq < dreta:
            for e in edificis:
                esq = max(e[0], xmin)
                dreta = min(e[2], xmax)
                res += [(esq, alt, dreta)] if alt <= e[1] else [(esq, e[1], dreta)]

        nou_sky.edificis = res
        return nou_sky


    def replica_skyline(self, N): #Es podria fer amb map?
        sky_nou = Skyline()
        edificis = self.edificis
        esq = edificis[0][0]
        dreta = edificis[len(edificis)-1][2]
        mida = dreta - esq

        for i in range(0, N):
            for e in edificis:
                sky_nou.edificis.append((e[0]+mida*i, e[1], e[2]+mida*i))
        return sky_nou


    def desp_dreta(self, N): #Es podria fer amb map?
        sky_nou = Skyline()
        for e in self.edificis:
            sky_nou.edificis.append((e[0]+N, e[1], e[2]+N))
        return sky_nou


    def desp_esq(self, N): #Es podria fer amb map?
        sky_nou = Skyline()
        for e in self.edificis:
            sky_nou.edificis.append((e[0]-N, e[1], e[2]-N))
        return sky_nou


    def area(self):
        return sum([(e[2]-e[0])*e[1] for e in self.edificis])

    def alcada(self):
        return max([e[1] for e in self.edificis])


def main():
    sk1 = Skyline(1, 2, 3)
    sk1 = sk1.unir_edifici((2,3,4))
    sk1 = sk1.unir_edifici((7,2,9))
    #sk1.mostra()
    #sk1-4
    sk1.mostra()
    print(sk1.area())
    print(sk1.alcada())
    

    # if isinstance(a, list):
    #     self.edificis = [a[0]]
    #     for e in range(1, len(a)):
    #         self.edificis += self.unir_edifici(e)


if __name__ == "__main__":
    main()