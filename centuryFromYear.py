def centuryFromYear(year):
    century=0
    for year_num in range(year):
        if ( year_num%100==0 ):
            century += 1
    return century
