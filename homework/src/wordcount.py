
#Ejemplo del caso de uso:
# python3 -m homework data/input data/output
import argparse
import os
import sys


def prepocess_lines(lines):
    return[line.lower().strip() for line in lines]
   

def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words


def count_words(words):
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def write_word_counts(output_folder, word_counts):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, "wordcount.tsv")

    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in word_counts.items():
            f.write(f"{word}\t{count}\n")



def parse_args():

    parser = argparse.ArgumentParser(description="Count words in files.")

    parser.add_argument(
        "input",
        type=str,
        help="Path to the input folder containing files to process",
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder for results",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output

def read_all_lines(input_folder):

    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines    

def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    prepocess_lines = prepocess_lines(lines)
    words = split_into_words(prepocess_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)





    # Aquí iría el código para contar palabras en los archivos de input_folder
    # y guardar los resultados en output_folder

    #print(f"Input folder: {input_folder}")
    #print(f"Output folder: {output_folder}")


