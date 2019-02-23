# From https://rosettacode.org/wiki/Validate_International_Securities_Identification_Number#Python
# For valid ISIN number

def check_isin(a):
    if len(a) != 12 or not all(c.isalpha() for c in a[:2]) or not all(c.isalnum() for c in a[2:]):
        return False
    s = "".join(str(int(c, 36)) for c in a)
    return 0 == (sum(sum(divmod(2 * (ord(c) - 48), 10)) for c in s[-2::-2]) +
                 sum(ord(c) - 48 for c in s[::-2])) % 10