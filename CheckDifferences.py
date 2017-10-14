import xlrd as excel
from Flight import Flight
from xlrd.sheet import Sheet


class CheckDifferences:

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

    def parse_read_data(self, table: list):

        flights = []
        table = table[1:]
        for x in range(table.__len__()):
            curr_element = table[x]
            details =[
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
        #print(flights)

        return flights

    def save_it(self):

        pass

    def compare_two_situation(self):
        # Depending on, if there is a change that is not a problem,
        #   then, send it as a problem
        # otherwise do not do anything

        pass



