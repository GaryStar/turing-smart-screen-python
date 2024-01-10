
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


from ctypes import *

class GUID(Structure):
    _fields_ = [("Data1", c_ulong),
                ("Data2", c_ushort),
                ("Data3", c_ushort),
                ("Data4", c_byte * 8)]

    def __init__(self, name=None):
        if name is not None:
            oledll.ole32.CLSIDFromString(str(name), byref(self))

    def __unicode__(self):
        p = c_wchar_p()
        oledll.ole32.StringFromCLSID(byref(self), byref(p))
        result = p.value
        oledll.ole32.CoTaskMemFree(p)
        return result
    __str__ = __unicode__

