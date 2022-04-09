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

        self.size = Size.xs if (height <= 169) & (weight <= 55) else Size.s if (height <= 178) & (weight <= 65) else Size.m if (height <= 182) & (weight <= 75) else Size.l if (height <= 186) & (weight <= 85) else Size.xl if (height <= 190) & (weight <= 90) else Size.xxl if (height <= 194) & (weight <= 95) else Size.xxxl

#Replace inseam with waistwidth.
class Female_Pants:
    def __init__(self, hipwidth, waistbreadth):
        self.hipwidth = hipwidth
        self.waistbreadth = waistbreadth

        self.size = Size.xs if (hipwidth <= 85) & (waistbreadth <= 63)\
            else Size.s if (hipwidth <= 95) & (waistbreadth <= 71)\
            else Size.m if (hipwidth <= 101.5) & (waistbreadth <= 78.5)\
            else Size.l if (hipwidth <= 106) & (waistbreadth <= 86)\
            else Size.xl if (hipwidth <= 109) & (waistbreadth <= 91)\
            else Size.xxl if (hipwidth <= 117) & (waistbreadth <= 101)\
            else Size.xxxl