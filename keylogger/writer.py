import csv


def write_csv(event_array: list) -> None:
    """
    Writes Data from the Array into a csv- Files.
    Structure of the File ist: Key, Time, Event
    :param event_array: Format of the List (String: Key, int: Time, bool: Event)
    Event=0 -> press; Event=1 ->release
    """
    with open('keylogger.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(event_array)
