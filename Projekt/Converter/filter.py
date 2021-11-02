class Filter:
    def __init__(self, event_array):
        self.event_array = event_array
        self.converted = False

    def __build_pairs(self):
        keys_pressed = []
        keys_released = []
        key_array = []
        for keys in self.event_array:
            if keys[2] is True:
                keys_pressed.append(keys)
            elif keys[2] is False:
                keys_released.append(keys)
        for key_pressed in keys_pressed:
            for key_released in keys_released:
                if key_pressed[0] == key_released[0]:
                    key_array.append([key_pressed[0], key_pressed[1], key_released[1]])
                    keys_released.remove(key_released)
                    break
        self.event_array = key_array

    def __calc_time_pressed(self):
        time_array = []
        for i in range(len(self.event_array)):
            time_pressed = self.event_array[i][2] - self.event_array[i][1]
            if i == (len(self.event_array) - 1):
                time_array.append([self.event_array[i][0], time_pressed, None])
                break
            key_diff = self.event_array[i+1][1] - self.event_array[i][2]
            time_array.append([self.event_array[i][0], time_pressed, key_diff])

        self.event_array = time_array

    def __reformat(self):
        translation_dict = {
            "\x06": "STRG F",
            "\x01": "STRG A"
        }
        for key in self.event_array:
            key[0] = key[0].replace('KEY.', '')
            if key[0] in translation_dict:
                key[0] = translation_dict.get(key[0])
            elif "'" in key[0]:
                key[0] = key[0].split("'")[1]

    def filter_data(self):
        if not self.converted:
            self.__build_pairs()
            self.__calc_time_pressed()
            self.__reformat()
        return self.event_array
