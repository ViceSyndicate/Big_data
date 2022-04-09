class Size:
    xs = "XSMALL"
    s = "SMALL"
    m = "MEDIUM"
    l = "LARGE"
    xl = "XLARGE"
    xxl = "XXLARGE"
    xxxl = "XXXLARGE"


class Male_Shirt:
    def __init__(self, weight, height, *args):
        self.weight = weight
        self.height = height

        #self.chestbreadth = args.chestbreadth
        #self.waistbreadth = args.waistbreadth
        #self.hipbreadth = args.hipbreadth

        self.size = Size.xs if (height <= 169) & (weight <= 55) \
            else Size.s if (height <= 178) & (weight <= 65) \
            else Size.m if (height <= 182) & (weight <= 75) \
            else Size.l if (height <= 186) & (weight <= 85) \
            else Size.xl if (height <= 190) & (weight <= 90) \
            else Size.xxl if (height <= 194) & (weight <= 95) \
            else Size.xxxl

#Replace inseam with waistwidth.
class Female_Pants:
    def __init__(self, hipcircumference, waistcircumference):
        self.hipwidth = hipcircumference
        self.waistbreadth = waistcircumference

        self.size = Size.xs if (hipcircumference <= 85) & (waistcircumference <= 63)\
            else Size.s if (hipcircumference <= 95) & (waistcircumference <= 71)\
            else Size.m if (hipcircumference <= 101.5) & (waistcircumference <= 78.5)\
            else Size.l if (hipcircumference <= 106) & (waistcircumference <= 86)\
            else Size.xl if (hipcircumference <= 109) & (waistcircumference <= 91)\
            else Size.xxl if (hipcircumference <= 117) & (waistcircumference <= 101)\
            else Size.xxxl


class Male_Pants:
    def __init__(self, hipcircumference, waistcircumference):
        self.hipwidth = hipcircumference
        self.waistbreadth = waistcircumference

        self.size = Size.xs if (hipcircumference <= 87) & (waistcircumference <= 66)\
            else Size.s if (hipcircumference <= 92) & (waistcircumference <= 74)\
            else Size.m if (hipcircumference <= 96) & (waistcircumference <= 80.5)\
            else Size.l if (hipcircumference <= 100.5) & (waistcircumference <= 85.5)\
            else Size.xl if (hipcircumference <= 106.5) & (waistcircumference <= 94)\
            else Size.xxl if (hipcircumference <= 111) & (waistcircumference <= 102)\
            else Size.xxxl