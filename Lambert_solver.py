"""
Global variables:
     AU_in_km:    Astronomical Unit in km
     muSUN:       Sun's gravitational parameter
     mu:          Primary's gravitational parameter
     deg2rad:     Degrees-to-radians conversion factor
     inv_mu:      inverse of mu
     sqrt_mu:     square root of mu

Classes:
     Vector3D:          3D vector object
     OrbitalElements:   Orbital Elements object
     dateObj:           Full date object

Functions:
    M2E:                  Converts from mean to eccentric anomaly by solving Kepler's
                          equation with Newton's method.
    QuarticRoot:          Iterative solver for Battin's quartic equation
                          x^4-P*x^3+Q*x-1=0, for the root closest to x=1.
    SingleImpulseDvOpt:   Solves the single-impulse time-free transfer.
    LambertAn:            Approximate analytical solver for Lambert's problem
    GlobalDVminEstimator: Computes a fast estimation of the global minimum
                          Delta-v, for a time range defined by a minimum departure
                          date and the synodic period.
    PorkChopAn:           Computes the pork-chop plot for given departure and arrival
                          orbital elements, a range of departure times [tdep_min,tdep_max],
                          and a range of times of flights [dt_min,dt_max], using the
                          approximate analytical solution implemented in function LambertAn.
"""



"""
Global variables:
     AU_in_km:    Astronomical Unit in km
     muSUN:       Sun's gravitational parameter
     mu:          Primary's gravitational parameter
     deg2rad:     Degrees-to-radians conversion factor
     inv_mu:      inverse of mu
     sqrt_mu:     square root of mu
"""

import math
import numpy as np

Au_in_km = 149597870.691
mu_sun = (2.959122082855911E-4) * (Au_in_km ** 3) / ((24 * 3600) ** 2)
mu = mu_sun
deg_2_rad = math.pi / 180
inverse_mu = 1 / mu
sqrt_mu = math.sqrt(mu)

print(Au_in_km, mu_sun, mu, deg_2_rad, inverse_mu, sqrt_mu)

#(I think I can just use numpy for this)
#class Vector3D:
    """
    Vector3D: 3D vector object
       Inputs (for constructor):
          x:    x coordinate
          y:    y coordinate
          z:    z coordinate
       Properties:
          x:    x coordinate
          y:    y coordinate
          z:    z coordinate
       Methods:
         dot(v):       Returns the dot product with v. If v is an scalar, output is
                       a Vector3D object. If v is a Vector3D, output is an scalar.
         cross(v):     Returns the cross product with v. Both v and the output
                       are Vector3D objects.
         add(v):       Returns the addition with v (scalar or Vector3D). The
                       output is a Vector3D object.
         substract(v): Returns the substraction with v (scalar or Vector3D).
                       The output is a Vector3D object.
         norm():       Returns the norm (scalar) of the Vector3D object.
         opposite():   Returns the opposite of the Vector3D object.
    """

"""
class Orbital_elements
class Date_obj

def mean_to_eccentric():
def quartic_root():
def single_impulse():
def lambert_solver():
def dv_estimator():
def pork_chop():
"""
