def effwav(fil):
    names = ["u'", "g'", "r'", "i'", "z'"]
    wavls = [3543.0, 4770.0, 6231.0, 7625.0, 9134.0]
    if fil in names:
        return wavls[names.index(fil)]
    
def observatoryephem(obs):
    names = ['skinakas', 'roque', 'helmos']
    lats = [35.2119, 28.7606, 37.9844, 37.9719] # north
    lons = [24.8992, -17.8816, 22.1961, 22.6186] # east
    heights = [1750.0, 2326.0, 2340.0, 930.0] # meters
    if obs in names:
        return [lats[names.index(obs)], lons[names.index(obs)], heights[names.index(obs)]]