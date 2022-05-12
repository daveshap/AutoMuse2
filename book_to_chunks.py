import textwrap
import os


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


if __name__ == '__main__':
    files = os.listdir('books/')
    for file in files:
        book = open_file('books/%s' % file)
        chunks = textwrap.wrap(book, 1500)
        print(file, len(chunks))
        count = 1
        for chunk in chunks:
            if count < 10:
                filename = file.replace('.txt','000%s.txt' % count)
            elif count < 100:
                filename = file.replace('.txt','00%s.txt' % count)
            elif count < 1000:
                filename = file.replace('.txt','0%s.txt' % count)
            save_file(chunk, 'chunks/%s' % filename)
            count += 1