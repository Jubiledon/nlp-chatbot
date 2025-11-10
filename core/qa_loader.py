import csv

def load_qa_dataset(filepath):
    questions, answers = [], []
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f) 
        for row in reader:
            if len(row) >= 3:
                questions.append(row[1].lower())
                answers.append(row[2])
    return questions, answers
