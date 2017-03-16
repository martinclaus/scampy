# SCAMPY - SCAlable ocean Model written in PYthon

SCAMPY is an ocean model written in Python that is designed to run on
platforms ranging from consumer laptops to large computing clusters. The idea
of using python is to have fast development cycles while accepting possible
performance issues. However, most of the number crunching will be performed via
[numpy](http://www.numpy.org) and distributed computing will be managed via the
[global arrays toolkit](http://hpc.pnl.gov/globalarrays/) if available. This
will ensure that most things which are critical for performance are done
natively in C/C++ with as little overhead as possible.

Actually, SCAMPY will be a modelling frame-work rather than a model. It will
provide a rather simple API for you to quickly develop your own models. It
will provide a basic set of operators, such as interpolation operators for
staggered grids.
