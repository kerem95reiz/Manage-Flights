import xlrd as excel
from Flight import Flight


class CheckDifferences:

    def __init__(self):
        self.previous_list = []

    def read_file(self):
        flight_table = excel.open_workbook('./source/DEMO_FLIGHTPLAN.xlsx')

        sheet = flight_table.sheets().__getitem__(0)
        number_of_cols = sheet.row_values(0).__len__()
        number_of_rows = sheet.col_values(0).__len__()

        table = []
        for x in range(number_of_rows):
            table.append([])
            for y in range(number_of_cols):
                table[x].append(sheet.cell(x, y))
        return table

    def put_flights_into_objects(self, table: list):
        flights = []
        table = table[1:]
        for x in range(table.__len__()):
            curr_element = table[x]
            details = [
                curr_element[1],
                curr_element[3],
                curr_element[4],
                curr_element[5],
                curr_element[6],
                curr_element[7],
                curr_element[8],
                curr_element[9],
                curr_element[10],
                curr_element[15]
            ]
            flights.append(Flight(details))
        return flights

    def are_two_flight_lists_different(self, current_list):
        # Depending on, if there is a change that is not a problem,
        #   then, send it as a problem
        # otherwise do not do anything

        for x in range(current_list.__len__()):
            if self.flights_are_different(current_list[x], self.previous_list[x]):
                return True

        return False

    def flights_are_different(self, flight_1: Flight, flight_2: Flight):

        if (not (
            flight_1.get_ac_version() == flight_2.get_ac_version() and
            flight_1.get_arr_ap_schedule() == flight_2.get_arr_ap_schedule() and
            flight_1.get_arr_day() == flight_2.get_arr_day() and
            flight_1.get_arr_day_schedule() == flight_2.get_arr_day_schedule() and
            flight_1.get_flight_number() == flight_2.get_flight_number() and
            flight_1.get_day_of_origin() == flight_2.get_day_of_origin() and
            flight_1.get_dep_ap_schedule() == flight_2.get_dep_ap_schedule() and
            flight_1.get_dep_day() == flight_2.get_dep_day() and
            flight_1.get_dep_time() == flight_2.get_dep_time() and
            flight_1.get_arr_time() == flight_2.get_arr_time()
        )):
            return True

    def are_two_situations_different(self):
        files = self.read_file()
        flights = self.put_flights_into_objects(files)
        is_different = self.are_two_flight_lists_different(flights)
        return is_different
