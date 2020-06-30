from scipy.interpolate import interp1d

def spline_velocidad(ts, vs):
    n = len(ts)
    ts_extra = []
    for i in range(n-1):
        ts_extra.append((ts[i] + ts[i + 1]) / 2)
    
    ts_extra = ts_extra + ts
    ts_extra.sort()
    
    spline = interp1d(ts, vs, 'cubic')
    
    vs_extra = spline(ts_extra)
    
    return ts_extra, vs_extra

