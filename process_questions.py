import random
import os
from argparse import ArgumentParser

from util import www2fb, processed_text, clean_uri

parser = ArgumentParser(description="Joint Prediction")
parser.add_argument('--output', type=str, default='preprocess/processed_questions.txt')
parser.add_argument('--input', type=str, default='questions_only.txt')
args = parser.parse_args()

questions = []
with open(args.input, 'r') as f:
    for i, line in enumerate(f):
        questions.append(processed_text(line))

with open(args.output, 'w') as f:
    for line in questions:
        f.write("{}\n".format(line))
