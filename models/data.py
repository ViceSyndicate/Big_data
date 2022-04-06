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
