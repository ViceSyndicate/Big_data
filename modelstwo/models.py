class Size:
    xs = "XSMALL"
    s = "SMALL"
    m = "MEDIUM"
    l = "LARGE"
    xl = "XLARGE"
    xxl = "XXLARGE"
    xxxl = "XXXLARGE"


class Male_Shirt_Chest:
    def __init__(self, weight, height, chestcircumference):
        self.weight = weight
        self.height = height
        self.chestcircumference = chestcircumference

        # self.chestbreadth = args.chestbreadth
        # self.waistbreadth = args.waistbreadth
        # self.hipbreadth = args.hipbreadth

        self.size = Size.xs if (height <= 169) & (weight <= 55) & (chestcircumference <= 90) \
            else Size.s if (height <= 178) & (weight <= 65) & (chestcircumference <= 96)  \
            else Size.m if (height <= 182) & (weight <= 75) & (chestcircumference <= 101)  \
            else Size.l if (height <= 186) & (weight <= 85) & (chestcircumference <= 106)  \
            else Size.xl if (height <= 190) & (weight <= 90) & (chestcircumference <= 111)  \
            else Size.xxl if (height <= 194) & (weight <= 95) & (chestcircumference <= 117)  \
            else Size.xxxl
