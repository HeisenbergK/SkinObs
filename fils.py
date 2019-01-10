def effwav(fil):
    names = ["u'", "g'", "r'", "i'", "z'"]
    wavls = [3543.0, 4770.0, 6231.0, 7625.0, 9134.0]
    if fil in names:
        return wavls[names.index(fil)]
    
def observatoryephem(obs):
    names = ['skinakas']
    lats = [35.2119]
    lons = [24.8992]
    heights = [1750.0]
    if obs in names:
        return [lats[names.index(obs)], lons[names.index(obs)], heights[names.index(obs)]]