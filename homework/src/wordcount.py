
#Ejemplo del caso de uso:
# python3 -m homework data/input data/output
import sys

from homework.src._internals.count_words import count_words
from homework.src._internals.parse_args import parse_args
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts


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


