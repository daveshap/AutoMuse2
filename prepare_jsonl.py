import os
import json


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def get_next_chunk(filepath, name):
    numbers = filepath.replace('.txt','').replace(name,'')
    number = int(numbers) + 1
    if number < 10:
        filename = '%s000%s.txt' % (name, number)
    elif number < 100:
        filename = '%s00%s.txt' % (name, number)
    elif number < 1000:
        filename = '%s0%s.txt' % (name, number)
    return open_file('chunks/%s' % filename)


if __name__ == '__main__':
    books = os.listdir('books/')
    data = list()
    for book in books:
        name = book.replace('.txt', '')
        summaries = [i for i in os.listdir('summaries/') if name in i]
        outline = open_file('outlines/%s' % book)
        summary_chunk = ''
        for summary in summaries:
            summary_chunk = summary_chunk + ' ' + open_file('summaries/%s' % summary)  # accumulate the summaries so far
            last_chunk = open_file('chunks/%s' % summary)  # get the chunk equal to the currently summarized one
            next_chunk = get_next_chunk(summary, name)
            prompt = open_file('prompt_full.txt').replace('<<OUTLINE>>', outline).replace('<<SUMMARY>>', summary_chunk).replace('<<CHUNK>>', last_chunk)
            print(summary, len(prompt) + len(next_chunk))
            info = {'prompt': prompt, 'completion': ' ' + next_chunk}
            save_file(prompt, 'prompts/%s' % summary)
            save_file(next_chunk, 'completions/%s' % summary)
            data.append(info)
    with open('novel.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')