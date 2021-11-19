h = float(input("Ingrese la hora inicial(solo la hora): "))#Se puede leer dos variables?
if h >= 0 and h <= 23:
    m = float(input("Ingrese los minutos iniciales: "))
    dh = float(input("Ingrese las horas de duración: "))
    dm = float(input("Ingrese los minutos de duración: "))
    mf = m + dm
    hf = h + dh
    if mf > 59:
        ma = (mf/60)
        mw = int(ma)
        mt = 60(mw) - mf
        if mf < 0:
            mt = -1 * mt
        hf = hf + int(ma)
    else:
        mt = mf
    print ("La hora final es: ",hf, "con ", mt, "min")
