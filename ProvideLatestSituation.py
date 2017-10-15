from CheckDifferences import CheckDifferences
from FindAndSendFlightWithProblem import FindAndSendFlightWithProblem as fsf
import json


class ProvideLatestSituation:

    def __init__(self):
        find_problem = fsf()
        self.check_diff = CheckDifferences()
        self.list_of_flights = self._gather_flights()
        self.list_of_conflicting_flights = find_problem.check_the_time_conflict()

    def _gather_flights(self):
        table = self.check_diff.read_file()
        list_of_flights = self.check_diff.put_flights_into_objects(table)
        return list_of_flights

    def is_there_problem(self):
        after_emergency_listed_flights = []
        if self.list_of_conflicting_flights.__len__() > 0:
            for flight in self.list_of_conflicting_flights:
                after_emergency_listed_flights.append(flight.uid)

            for ok_flight in self.list_of_flights:
                if ok_flight.get_flight_number().value not in after_emergency_listed_flights:
                    after_emergency_listed_flights.append(ok_flight.get_flight_number().value)
        return after_emergency_listed_flights

    def get_all_flights_ordered(self, ordered_ids):
        list_of_flights_ordered_after_emergency = []
        for sorted_flight_id in ordered_ids:
            for unsorted_flight in self.list_of_flights:
                temp_flight = unsorted_flight
                if sorted_flight_id == temp_flight.get_flight_number().value:
                    list_of_flights_ordered_after_emergency.append(temp_flight)
        return list_of_flights_ordered_after_emergency

    def conflicting_uids(self):
        uids = []
        for flight in self.list_of_conflicting_flights:
            uids.append(flight.uid)
        return uids

    def jsonify_flights(self, flights: list):
        jsonified_flights = {}
        flights_json = self._generate_flights_to_jsonify(flights)
        jsonified_flights['flights'] = flights_json
        jsonified_flights = json.dumps(jsonified_flights)
        return jsonified_flights

    def _get_flight_status(self, flight):
        conflicting_flights = self.conflicting_uids()
        if flight.get_flight_number().value in conflicting_flights:
            status = 'emergency'
        else:
            status = 'normal'
        return status

    def _generate_flights_to_jsonify(self, flights):
        flights_json = []
        for flight in flights:
            status = self._get_flight_status(flight)
            data_flight = {'flight_number': flight.get_flight_number().value,
                           'day_of_origin': flight.get_day_of_origin().value,
                           'dep_ap_schedule': flight.get_dep_ap_schedule().value,
                           'dep_day': flight.get_dep_day().value,
                           'dep_time': flight.get_dep_time().value,
                           'arr_ap_schedule': flight.get_arr_ap_schedule().value,
                           'arr_day': flight.get_arr_day().value,
                           'arr_time': flight.get_arr_time().value,
                           'arr_day_schedule': flight.get_arr_day_schedule().value,
                           'ac_schedule': flight.get_ac_version().value}
            to_make_json_flight = {'situation': status,
                                   'flight': data_flight}
            flights_json.append(to_make_json_flight)
        return flights_json

    # only with this method, the whole class can be used practically
    def provide_lat_sit(self):
        list_of_problematic_flights = self.is_there_problem()
        ordered_list_flights = self.get_all_flights_ordered(list_of_problematic_flights)
        jsonified = self.jsonify_flights(ordered_list_flights)
        return jsonified



