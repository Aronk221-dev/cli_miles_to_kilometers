import argparse


class Converter():
    MILE_IN_KILOMETER:float = 1.609344
    KILOMETER_IN_MILE:float = 0.6213711922
    
    def __init__(self, unit:str, value:float):
        self.unit = unit
        self.value = value

    def convert(self) -> float:
        if self.unit == "m":
            return self.value * self.MILE_IN_KILOMETER
        elif self.unit == "k":
            return self.value * self.KILOMETER_IN_MILE
        else:
            return 0.0

def main():
    parser = argparse.ArgumentParser(
        prog="Command Line - Miles to Kilometers"
    )
    parser.add_argument(
        "conversion_unit",
        type=str,
        help="m -> converts miles to kilometers\nkm -> converts kilometers to miles"
    )
    parser.add_argument(
        "conversion_value",
        type=float,
        help="The value you wish to convert"
    )
    args = parser.parse_args()
    
    unit:str = args.conversion_unit
    value:float = args.conversion_value
    
    converter = Converter(unit, value)
    result = converter.convert()
    
    if unit == "m":
        print(f"{value} mile(s) is {result} in kilometers.")
    elif unit == "k":
        print(f"{value} kilometer(s) is {result} in miles.")
    else:
        print("Could not convert. Try again.")

if __name__ == "__main__":
    main()