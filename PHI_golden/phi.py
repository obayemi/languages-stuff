#!/usr/bin/env python3

"""
Simple Useless script to calculate the golden number
"""

import argparse

__author__ = 'obayemi'


def phi_rec(phi=2, rec=10, verbose=False):
    """adds rec recurtions to computing of phi from"""
    if verbose:
        print('%d: %f' % (rec, phi))
    return phi_rec(phi=(1.0 / float(phi)) + 1, rec=rec - 1, verbose=verbose) if rec > 0 else phi

parser = argparse.ArgumentParser(description='calculate Golden number')
parser.add_argument('iterations',
        nargs='?',
        type=int,
        default=10,
        help='number of iterations to compute PHI (default 10)')

parser.add_argument('start',
        nargs='?',
        type=float,
        default=2,
        help='value to start iterating from (default 2)')

parser.add_argument('--verbose', '-v',
        action='store_true',
        default=False,
        help='')

args = parser.parse_args()

print('Phi from %f after %d recursions: %f' %
        (args.start,
            args.iterations,
            phi_rec(args.start, args.iterations, args.verbose)))
