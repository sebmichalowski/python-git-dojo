from gittie_helper import GittieHelper


def main():
    x = GittieHelper()

    x.set_temperature(100)
    x.set_air_pollution(100)
    print(x.safety_calculator_test())


if __name__ == '__main__':
    main()
