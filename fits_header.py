from astropy.io import fits
import astropy.units as u
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import glob, os
os.chdir("sandbox/220905/")
for file in glob.glob("[!_]*.fits"):
    with fits.open(file, mode='update') as hdul:
        hdr = hdul[0].header
        #if not 'CRVAL1' in hdr:
        print(file+' >> '+hdr['OBJNAME'])
        if 'RA' in hdr and 'DEC' in hdr and False:
            hdr['CRVAL1'] = (hdr['RA'], 'approx coord. in RA')
            hdr['CRVAL2'] = (hdr['DEC'], 'approx coord. in DEC')
        else:
            result_table = Simbad.query_object(hdr['OBJNAME'])
            if result_table:
                ra = result_table[0]['RA']
                dec = result_table[0]['RA']
                c = SkyCoord(ra+' '+dec, unit=(u.hourangle, u.deg))
                crval1, crval2 = c.to_string().split(' ')
                print('Coord ok : ', crval1, crval2)
                hdr['CRVAL1'] = (crval1, 'approx coord. in RA')
                hdr['CRVAL2'] = (crval2, 'approx coord. in DEC')
    print('---')


            