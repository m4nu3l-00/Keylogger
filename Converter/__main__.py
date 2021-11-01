import sys
import csv
from filter import Filter


def main(argv) -> None:
    try:
        in_path = argv[0]
        out_path = argv[1]

        #read csv
        in_data = []
        with open(in_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for data in reader:
                data[1] = float(data[1])
                data[2] = data[2] == 'True'
                in_data.append(data)

        #convert_data
        data_filter = Filter(in_data)
        out_data = data_filter.filter_data()

        #write_csv
        with open(out_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(out_data)

        print("Conversion successfull!")

    except Exception as e:
        print("Error: Please enter valid paths with valid csv files.")
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
