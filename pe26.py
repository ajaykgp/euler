#! /usr/bin/env python
# -*- coding - utf-8 -*-

"""This program converts a rational number
into its decimal representation.

A rational number is a number of the form p/q
where p and q are integers and q is not zero.
The decimal representation of a rational number
is either terminating or non-terminating but
repeating.

"""


def gcd(a, b):
    """Computes gcd of a, b
    using Euclid algorithm.

    """

    if not isinstance(a, int) or not isinstance(b, int):
        return None

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def decimal(p, q):
    """Computes the decimal representation
    of the rational number p/q. If the
    representation is non-terminating, then
    the recurring part is enclosed in parentheses.
    The result is returned as a string.

    """

    if not isinstance(p, int) or not isinstance(q, int):
        return ''

    if q == 0:
        return ''

    abs_p = abs(p)
    abs_q = abs(q)

    s = (p / abs_p) * (q / abs_q)
    g = gcd(abs_p, abs_q)

    p = abs_p / g
    q = abs_q / g

    rlist = []
    qlist = []

    quotient, remainder = divmod(p, q)
    qlist.append(quotient)
    rlist.append(remainder)

    if remainder == 0:
        return str(quotient)

    while remainder != 0:
        remainder *= 10
        quotient, remainder = divmod(remainder, q)
        qlist.append(quotient)

        if remainder in rlist:
            break
        else:
            rlist.append(remainder)

    qlist = map(str, qlist)

    if remainder:
        recur_index = rlist.index(remainder) + 1
        dstring = qlist[0] + '.' + ''.join(qlist[1:recur_index]) + \
            '(' + ''.join(qlist[recur_index:]) + ')'

        if s < 0:
            dstring = '-' + dstring
    else:
        dstring = qlist[0] + '.' + ''.join(qlist[1:])

        if s < 0:
            dstring = '-' + dstring

    return dstring


if __name__ == '__main__':
    p = raw_input('p: ')
    q = raw_input('q: ')

    try:
        p = int(p)
        q = int(q)

        if q == 0:
            raise ValueError

        print '%d/%d =' % (p, q), decimal(p, q)
    except ValueError:
        print 'invalid input'
