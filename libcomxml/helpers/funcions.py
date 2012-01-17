# -*- coding: utf-8 -*-

"""Helper functions for libComXml
"""

__all__ = ['codi_periode', 'codi_dh']


def codi_periode(tarifa, periode):
    """Retorna el codi OCSUM del periode segons
    http://172.26.0.42:2500/wiki/show/Codificacio_Periodes_OCSUM

    :param tarifa: codi ocsum de la tarifa
    :param periode: nom del periode en format Px on x = {1...6}
    """

    if tarifa in ('003', '011', '012', '013', '014', '015', '016'):
        return '6%s' % (periode[-1],)
    elif tarifa in ('001', '005'):
        return '10'
    elif tarifa in ('004', '006'):
        if periode == 'P1':
            return '01'
        elif periode == 'P2':
            return '03'


def codi_dh(tarifa, nlectures=6):
    """Retorna el codi ocsum de discriminació horaria

    :param tarifa: codi de la tarifa
    :param nlectures: nombre de lectures
    """

    if tarifa in ('001', '005'):
        return '1'
    elif tarifa in ('004', '006'):
        return '2'
    elif tarifa in ('012', '013', '014', '015', '016'):
        return '6'
    elif tarifa in ('003', '011'):
        if nlectures == 6:
            return '4' 
        else:
            return '3'
