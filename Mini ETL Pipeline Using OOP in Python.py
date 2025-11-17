class reader():
    def read(self):
        raise NotImplementedError

class FileIngestor(reader):
    def __init__(self, path):
        self.path = path
    
    def read(self):
        print(f"Reading : {self.path}")
        return f"Raw data from {self.path}"
    
class cleaner():
    def clean(self):
        raise NotImplementedError

class BasicCleaner(cleaner):
    def clean(self, data):
        print(f"Cleaner the data")
        return f"Cleaned data : {data}"

class Writer():
    def write(self):
        raise NotImplementedError

class FileWriter(Writer):
    def write(self, data):
        print(f"Writing the data")
        return f"written data: {data}"
    

class pipeline():
    def __init__(self, reader, cleaner, writer):
        self.reader = reader
        self.writer = writer
        self.cleaner = cleaner
    
    def run(self):
        raw_data = self.reader.read()
        cleaned = self.cleaner.clean(raw_data)
        written_data = self.writer.write(cleaned)


pipeline(FileIngestor("Data.csv"),
                    BasicCleaner(),
                    FileWriter()
).run()
