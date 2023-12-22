
class Names:
    def __getitem__(self, item):
        return self.__getattribute__(item)
    def __setitem__(self, item, value):
        self.__setattr__(item, value)

WEATHER_UNITS = {'metric': '°C', 'imperial': '°F', 'standard': '°K'}

def approximate_size(size, flag_1024_or_1000=True, precision=1):
    UNITS = {1000: ['KB', 'MB', 'GB'], 1024: ['KiB', 'MiB', 'GiB']}
    mult = 1024 if flag_1024_or_1000 else 1000
    for unit in UNITS[mult]:
        size = size / mult
        if size < mult:
            if precision < 2:
                unit = unit[0] # truncate unit to just the first character
            return '{0:.{1}f} {2} '.format(size, precision, unit)