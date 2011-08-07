#!/usr/bin/env python

"""
Find the average count of companies that have been allowed by the EPA to
pollute public water sources.
"""

from epa.pcs import PCS

# Go ahead and initialize a global PCS object.
GLOBAL_PCS = PCS()


def find_count(zip_code):
    """
    Find the number of facilities in a given ZIP Code that have a permit
    from the EPA that allows polluting public water sources.
    """
    data = GLOBAL_PCS.facility('location_zip_code', zip_code, count=300)
    if isinstance(data, str):
        # No facilities for the given ZIP Code.
        count = 0
    else:
        count = int(data['Count'])
    return count


def get_zip_codes(file_name):
    """
    Open a file containing a ZIP Code per line and return the ZIP Codes
    in a list.
    """
    with open(file_name) as f:
        zip_codes = f.readlines()
    return zip_codes


def total_count(file_name):
    """Get the total count of all facilities in the given ZIP Codes."""
    total_facilities = 0
    highest = {'count': 0, 'zip_code': None}
    zip_code_list = get_zip_codes('zip_codes_list.txt')
    for zip_code in zip_code_list:
        # Remove extraneous white-space.
        zip_code = zip_code.strip()
        current_amount = find_count(zip_code)
        total_facilities += current_amount
        if current_amount > highest['count']:
            highest['count'] = current_amount
            highest['zip_code'] = zip_code
    return total_facilities, highest


def main():
    print total_count('zip_codes_list.txt')
    # (2190, {'count': 178, 'zip_code': '32218'})


if __name__ == '__main__':
    main()
