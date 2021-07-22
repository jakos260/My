#-*- coding: utf_8 -*-

# Przewidywanie wzrostu sprzedazy
import numpy as np
from scipy.linalg import lstsq

year = np.array([2010.000000, 2010.083333, 2010.166667, 2010.250000,
    2010.333333, 2010.416667, 2010.500000, 2010.583333,
    2010.666667, 2010.750000, 2010.833333, 2010.916667,
    2011.000000, 2011.083333, 2011.166667, 2011.250000,
    2011.333333, 2011.416667, 2011.500000, 2011.583333,
    2011.666667, 2011.750000, 2011.833333, 2011.916667,
    2012.000000, 2012.083333, 2012.166667, 2012.250000,
    2012.333333, 2012.416667, 2012.500000, 2012.583333,
    2012.666667, 2012.750000, 2012.833333, 2012.916667,
    2013.000000, 2013.083333, 2013.166667, 2013.250000,
    2013.333333, 2013.416667, 2013.500000, 2013.583333,
    2013.666667, 2013.750000, 2013.833333, 2013.916667,
    2014.000000, 2014.083333, 2014.166667, 2014.250000,
    2014.333333, 2014.416667, 2014.500000, 2014.583333,
    2014.666667, 2014.750000, 2014.833333, 2014.916667,
    2015.000000, 2015.083333, 2015.166667, 2015.250000,
    2015.333333, 2015.416667, 2015.500000, 2015.583333,
    2015.666667, 2015.750000, 2015.833333, 2015.916667,
    2016.000000, 2016.083333, 2016.166667, 2016.250000,
    2016.333333, 2016.416667, 2016.500000, 2016.583333,
    2016.666667, 2016.750000, 2016.833333, 2016.916667,
    2017.000000, 2017.083333, 2017.166667, 2017.250000,
    2017.333333, 2017.416667, 2017.500000, 2017.583333,
    2017.666667, 2017.750000, 2017.833333, 2017.916667])
sale = np.array([10.500000, 11.900000, 13.400000, 12.700000, 13.900000,
    14.000000, 13.500000, 14.500000, 14.300000, 14.900000,
    16.900000, 17.400000, 11.900000, 12.600000, 13.500000,
    13.600000, 14.600000, 14.400000, 15.700000, 14.000000,
    15.500000, 15.800000, 16.500000, 20.100000, 13.200000,
    14.400000, 16.100000, 14.900000, 15.700000, 15.300000,
    16.800000, 15.700000, 16.800000, 16.300000, 18.700000,
    19.700000, 14.600000, 15.400000, 16.200000, 17.800000, 
    17.800000, 16.100000, 17.400000, 17.000000, 17.200000,
    17.900000, 20.500000, 22.500000, 15.100000, 17.400000,
    17.200000, 17.800000, 18.600000, 18.900000, 18.300000,
    17.900000, 19.200000, 18.800000, 20.400000, 23.000000,
    16.500000, 17.900000, 19.600000, 20.200000, 19.100000,
    19.700000, 19.700000, 20.500000, 20.300000, 20.300000, 
    22.400000, 23.800000, 18.900000, 19.500000, 19.800000,
    19.700000, 20.800000, 21.100000, 21.000000, 21.000000,
    20.600000, 21.400000, 23.700000, 24.600000, 20.000000,
    20.800000, 22.100000, 20.900000, 21.500000, 22.100000,
    22.600000, 22.700000, 21.900000, 22.900000, 24.000000,
    26.600000])

M = year[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,sale)

print "a =", model[1]
print "b =", model[0]
