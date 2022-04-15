class DataWriterFactory:
    class _DataWriter:
        def __init__(self, file_name):
            self.file = open(file_name, "w")

        def write(self, data):
            self.file.write(str(data))

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()

    def __init__(self, path, file_name, extension):
        self.written_files = 0
        self.path = path
        self.file_name = file_name
        self.extension = extension

    def write_new(self, data):
        self._DataWriter(f'{self.path}/{self.file_name}_{self.written_files}.{self.extension}').write(data)
        self.written_files += 1
