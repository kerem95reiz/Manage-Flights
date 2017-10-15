from CheckDifferences import CheckDifferences


class FindAndSendFlightWithProblem:

    def __init__(self):
        self.check_diff = CheckDifferences()
        self.table = self.check_diff.read_file()
        self.flights_list = self.check_diff.put_flights_into_objects(self.table)

    def flights_and_arrival_times(self):
        flight_no_and_arrival = []
        for flight in self.flights_list:
            flight_no_and_arrival.append((flight.flight_number.value, flight.arr_day.value + " "
                                          + flight.arr_ap_schedule.value + " " + flight.arr_time.value))
        return flight_no_and_arrival

    def are_different_flights_same_arrival(self, flight_1, flight_2):
        if (flight_1[0] != flight_2[0]) and (flight_1[1] == flight_2[1]):
            return True

    def filter_empty_lists_out(self, flights_list: list):
        at_least_two_flights = []
        for flight in flights_list:
            if flight.get_len_of_list() > 0:
                at_least_two_flights.append(flight)
        return at_least_two_flights

    def check_the_time_conflict(self):
        conflicting_groups = []
        flight_no_and_arrival = self.flights_and_arrival_times()
        for first_flight in flight_no_and_arrival:
            conf_fls = ConflictingFlights(first_flight[0])
            conflicting_groups.append(conf_fls)
            for compared_flight in flight_no_and_arrival:
                if self.are_different_flights_same_arrival(first_flight, compared_flight):
                    conf_fls.add_flight(compared_flight[0])
                    flight_no_and_arrival.remove(compared_flight)
        conflicting_groups = self.filter_empty_lists_out(conflicting_groups)
        return conflicting_groups


class ConflictingFlights:

    def __init__(self, id_of_flight: int):
        self.uid = id_of_flight
        self.group_of_the_flights = []

    def add_flight(self, flight_number):
        self.group_of_the_flights.append(flight_number)

    def get_group_of_flights(self):
        return self.group_of_the_flights

    def get_len_of_list(self):
        return self.group_of_the_flights.__len__()

    def get_self_uid(self):
        return self.uid

    def get_only_uids(self):
        uids = []
        for flight in self.group_of_the_flights:
            uids.append(flight.uid)
        return uids
