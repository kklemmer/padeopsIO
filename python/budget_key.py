class bidict(dict):
    """
    Bi-directional dictionary, courtesy of: 
    https://stackoverflow.com/questions/3318625/how-to-implement-an-efficient-bidirectional-hash-table

    Used to look up a mapping and inverse mapping (not necessarily unique) between key parings. 
    """
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value,[]).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value,[]).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key],[]).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)


def get_key(): 
    """
    Returns a bidirectional has table between colloquial string values for budget terms and 
    a tuple-look up ordered (budget #, term #) as defined in e.g. budget_time_avg.F90. 
    """
    key = {  # BUDGET 0 TERMS: (1st and second order averages, scalars excluded)
        'ubar': (0, 1), 
        'vbar': (0, 2), 
        'wbar': (0, 3), 
        'uu': (0, 4), 
        'uv': (0, 5), 
        'uw': (0, 6), 
        'vv': (0, 7), 
        'vw': (0, 8), 
        'ww': (0, 9), 
        'pbar': (0, 10), 
        'tau11': (0, 11), 
        'tau12': (0, 12), 
        'tau13': (0, 13), 
        'tau22': (0, 14), 
        'tau23': (0, 15), 
        'tau33': (0, 16), 
        'pu': (0, 17), 
        'pv': (0, 18), 
        'pw': (0, 19), 
        'uk': (0, 20), 
        'vk': (0, 21), 
        'wk': (0, 22), 
        'ujtau1j': (0, 23), 
        'ujtau2j': (0, 24), 
        'ujtau3j': (0, 25), 
        'Tbar': (0, 26), 
        'uT': (0, 27), 
        'vT': (0, 28), 
        'wT': (0, 29), 
        'TT': (0, 30), 
        # BUDGET 1 TERMS: (momentum)
        'DuDt': (1, 1),  # x-advection
        'dpdx': (1, 2),  # x-pressure gradient
        'xSGS': (1, 3),  # x-sub grid stresses
        'xAD': (1, 4),   # x-Actuator disk
        'DvDt': (1, 5),  
        'dpdy': (1, 6), 
        'ySGS': (1, 7), 
        'DwDt': (1, 8), 
        'dpdz': (1, 9), 
        'zSGS': (1, 10),
        'xCor': (1, 11), # x-coriolis
        'xGeo': (1, 12), # x-geostrophic pressure grad. 
        'yCor': (1, 13), 
        'yGeo': (1, 14), 
        'yAD': (1, 15), 
        # BUDGET 2 TERMS: (MKE)  TODO - improve the naming keys
        'MKE_TKE_loss': (2, 1), 
        'MKE_adv': (2, 2), 
        'MKE_tau_transport': (2, 3), 
        'MKE_p_transport': (2, 4), 
        'MKE_SGS_transport': (2, 5), 
        'MKE_dissipation': (2, 6), 
        'MKE_AD': (2, 7), 
        'MKE_geostrophic': (2, 8), 
        'MKE_coriolis': (2, 9),
        # BUDGET 3 TERMS: (TKE)
        'TKE_shear_production': (3, 1), 
        'TKE_turb_transport': (3, 2), 
        'TKE_p_strain': (3, 3), 
        'TKE_p_transport': (3, 4), 
        'TKE_SGS_transport': (3, 5), 
        'TKE_dissipation': (3, 6), 
        'TKE_buoyancy': (3, 7), 
        'TKE_coriolis': (3, 8), 
        'TKE_AD': (3, 9)
        # BUDGET 4 TERMS: TODO
        }
    
    return bidict(key)
