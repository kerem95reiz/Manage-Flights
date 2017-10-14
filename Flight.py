class Flight:

    def __init__(self, flight_details: list):
        self.flight_number = flight_details[0]
        self.day_of_origin = flight_details[1]
        self.dep_ap_schedule = flight_details[2]
        self.dep_day = flight_details[3]
        self.dep_time = flight_details[4]
        self.arr_ap_schedule = flight_details[5]
        self.arr_day = flight_details[6]
        self.arr_time = flight_details[7]
        self.arr_day_schedule = flight_details[8]
        self.ac_version = flight_details[9]

    def get_flight_number(self):
        return self.flight_number

    def get_day_of_origin(self):
        return self.day_of_origin

    def get_dep_ap_schedule(self):
        return self.dep_ap_schedule

    def get_dep_day(self):
        return self.dep_day

    def get_dep_time(self):
        return self.dep_time

    def get_arr_ap_schedule(self):
        return self.arr_ap_schedule

    def get_arr_day(self):
        return self.arr_day

    def get_arr_time(self):
        return self.arr_time

    def get_arr_day_schedule(self):
        return self.arr_day_schedule

    def get_ac_version(self):
        return self.ac_version
