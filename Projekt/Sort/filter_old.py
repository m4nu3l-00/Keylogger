from reader import CsvReader


class Filter:
    def __init__(self, event_array):
        self.event_array = event_array

    def build_pairs(self):
        keys_pressed = []
        keys_released = []
        key_array = []
        for keys in self.event_array:
            if keys[2] is True:
                keys_pressed.append(keys)
            elif keys[2] is False:
                keys_released.append(keys)
        for key_released in keys_released:
            for key_pressed in keys_pressed:
                if key_pressed[0] == key_released[0]:
                    key_array.append([key_pressed[0], key_pressed[1], key_released[1]])
                    keys_pressed.remove(key_pressed)
                    break
        return key_array

    def calc_time_pressed(self, keys):
        neuron_array = []
        for i in range(len(keys)):
            time_pressed = float(keys[i][2]) - float(keys[i][1])
            if i == (len(keys) - 1):
                neuron_array.append([keys[i][0], time_pressed, None])
                break
            key_diff = float(keys[i+1][1]) - float(keys[i][2])
            neuron_array.append([keys[i][0], time_pressed, key_diff])

        return neuron_array

    def reformat(self, keys):
        translation_dict = {
            "KEY.space": "Space",
            "KEY.shift": "Shift",
            "KEY.alt_l": "Alt_l",
            "KEY.esc": "Esc",
            "KEY.tab": "Tab",
            "KEY.backspace": "Backspace",
            "KEY.f1": "F1",
            "KEY.f2": "F2",
            "KEY.f3": "F3",
            "KEY.f4": "F4",
            "KEY.f5": "F5",
            "KEY.f6": "F6",
            "KEY.f7": "F7",
            "KEY.f8": "F8",
            "KEY.f9": "F9",
            "KEY.f10": "F10",
            "KEY.f11": "F11",
            "KEY.f12": "F12",
            "\x06": "Strg F",
            "\x01": "Strg A"
        }
        for key in keys:
            if key[0] in translation_dict:
                key[0] = translation_dict.get(key[0])
            elif "'" in key[0]:
                key[0] = key[0].split("'")[1]
        return keys





filter = Filter(CsvReader.read_csv())
key_a = filter.build_pairs()
a =filter.calc_time_pressed(key_a)
b = filter.reformat(a)

