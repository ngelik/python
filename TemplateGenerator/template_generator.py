import  sys


class TemplateGenerator(object):
    def __init__(self, settings):
        self._settings = settings

    def _save_to_file(self, data_list):
        if self._settings.file_template is None:
            out_file_name = 'out_' + self._settings.in_file_name
            print ("Saving in single file: {0} ...".format(out_file_name))
            self._save(out_file_name, ''.join(data_list))
        else:
            print("Saving in following files:")
            for i in range(self._settings.file_start_counter, self._settings.count - self._settings.start_count + 1):
                file_name = self._replace(self._settings.file_template, str(i))
                print("In {0}".format(file_name))
                self._save(file_name, data_list[i - self._settings.file_start_counter])

    def _make_data(self, data):
        out_text = []
        for i in range(self._settings.start_count, self._settings.count + 1):
            out_text.append(self._replace(data, str(i)))
        print "Replaced {0} times".format(self._settings.count - self._settings.start_count + 1)
        return out_text

    def _show_settings(self):
        print(vars(self._settings))

    def _replace(self, data, value):
        return data.replace(self._settings.template, str(value))

    def _save(self, file_name, data):
        with open(file_name, "w") as my_file:
            my_file.write(data)

    def _load_file_to_str(self, file_name):
        with open(file_name, "r") as my_file:
            in_text = my_file.read()
        print ("Loaded from file: " + in_text)
        return in_text

    def run(self):
        self._show_settings()
        data_list = self._make_data(self._load_file_to_str(self._settings.in_file_name))
        self._save_to_file(data_list)