import csv


class CsvReader:

    @staticmethod
    def read_csv():
        with open('keylogger.csv') as csv_file:
            event_array = []
            reader = csv.reader(csv_file, delimiter=',')
            for csv_data in reader:
                data[1] = float(data[1])
                csv_data[2] = csv_data[2] == 'True'
                event_array.append(csv_data)
            return event_array
