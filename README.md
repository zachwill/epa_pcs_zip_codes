EPA PCS
=======

Polluters Per ZIP Code
----------------------

Today, I decided to take the [top 25 most populated cities in the United
States](http://en.wikipedia.org/wiki/List_of_United_States_cities_by_population)
and find the 531 individual ZIP Codes that make up those cities (minus the
ZIP Codes that are only used for PO Boxes -- the [Python script for doing
this is up on Github, too](https://github.com/zachwill/usps_zipcodes)).

Then, I used Code for America's [Python `epa`
module](https://github.com/codeforamerica/epa_python) to look-up the
total number of facilities with EPA permits to pollute public water
sources -- along with the ZIP Code that contained the most facilities.


Installation
------------

Want to be able to run the same queries I was able to? It's pretty easy,
just make sure you have `pip` installed on your computer, and run the
following command.

    $ sudo pip install epa

Or you can use the `requirements.txt` file I've included in the repo.

    $ sudo pip install -r requirements.txt


What were the results?
----------------------

### Total ###

**2190** facilites have been permits to pollute public water sources.

You can run the `epa_pcs_zip_codes.py` script to verify this, but it will
take a couple minutes -- and put a strain on the EPA's servers. But, if
you're unsure of the number I've presented, you can go ahead and run the
script for yourself.

    $ python epa_pcs_zip_codes.py


### Highest Count ###

The Jacksonville, Florida ZIP Code of 32218 has **178** facilities that have
been granted EPA permits to pollute public water sources -- some of the
records date back to the 1970s.

```python
    >>> # How can I verify that?
    ... from epa.pcs import PCS

    >>> data = PCS().facility('location_zip_code', '32218', count=200)
    >>> data['Count']
    178
```

### Average ###

The average number of facilities per ZIP Code turns out to be **a little
more then 4**.

```python
    >>> from __future__ import division
    >>> 2190 / 531
    4.124293785310734
```
