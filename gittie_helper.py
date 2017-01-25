class GittieHelper():

    def __init__(self):

        """
        Initialize attributes with default value
        """
        self.temperature_degree = 0
        self.humidity_value = 0
        self.air_pollution_level = 50
        self.day_number = 1

    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree:
        """
        try:
            temperature_degree = float(temperature_degree)
            self.temperature_degree = temperature_degree
        except:
            ValueError('Give us integer please')

    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:
        """
        try:
            humidity_value = float(humidity_value)
            self.humidity_value = humidity_value
        except:
            ValueError('Give us integer please')

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        if (int(air_pollution_level) > 0) and (int(air_pollution_level) < 121):
            self.air_pollution_level = air_pollution_level

    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        if (int(day_number) < 366) and (int(day_number) > 0):
            self.day_number = int(day_number)

    def get_value(self):
        """
        Method should calculate if exiting home is safe for gittie
        """
        pass
