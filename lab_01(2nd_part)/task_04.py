import os


class ReadInfo:
    """This class reads info for small large of text. Maximum 1000 symbols."""

    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    # setter for file name and control if this file exists or file name is a string
    @file_name.setter
    def file_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Given name is not a string.')
        if not os.path.isfile(name):
            raise FileNotFoundError()

        self.__file_name = name

    @file_name.getter
    def file_name(self):
        return self.__file_name

    # displaying the whole text
    def content_display(self):
        for line in open(self.file_name, 'r'):
            print(line, end='')

    # enumerating length of the data inside
    def file_length(self):
        length = 0
        for line in open(self.file_name, 'r'):
            if length > 1000:
                raise ValueError('Too much symbols.')
            length += len(line)
        return length
        # return sum(map(lambda: len(line), for line in open(self.file_name)))

    # enumerating number of words of the data inside
    def num_of_words(self):
        word_num = 0
        for line in open(self.file_name, 'r'):
            words = list(str.split(line))
            for word in words:
                if not word.isnumeric():
                    word_num += 1
        return word_num

    # enumerating lines of the data inside
    def num_of_lines(self):
        lines = [line.rstrip() for line in open(self.file_name)]
        return len(lines)

    # return the string from class ReadInfo
    def __str__(self):
        return f'Symbols: {self.file_length()} ' \
               f'Words: {self.num_of_words()} ' \
               f'Lines: {self.num_of_lines()}'


def main():
    file_name = input('enter file name:')
    reading = ReadInfo(file_name)
    print(reading)
    reading.content_display()


if __name__ == '__main__':
    main()
