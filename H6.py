import json
import csv


def load_quiz(quiz_file):
    with open(quiz_file, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_results(user_name, score, results_file):
    results = {'name': user_name, 'score': score}
    with open(results_file, 'w') as file:
        json.dump([results], file)  # Save results as a list of dictionaries


def run_quiz(questions):
    score = 0
    for q in questions:
        print(q['question'])
        answer = input("Answer: ")
        if answer.lower() == q['answer'].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print()
    return score


def load_quiz(quiz_file):
    with open(quiz_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_results(user_name, score, results_file):
    with open(results_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'name': user_name, 'score': score})


def run_quiz(questions):
    score = 0
    for q in questions:
        print(q['question'])
        answer = input("Answer: ")
        if answer.lower() == q['answer'].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print()
    return score


def main():
    quiz_file = "C:\\Users\\shama\\Desktop\\Homework\\quiz.json"
    results_file = "C:\\Users\\shama\\Desktop\\Homework\\results.json"

    user_name = input("What's your name? ")
    question = load_quiz(quiz_file)

    if len(question) != 20:
        print("Error: The quiz must contain 20 questions.")
        return

    score = run_quiz(question)
    save_results(user_name, score, results_file)

    print(f"{user_name}, your final score is {score} out of {len(questions)}.")

    quiz_file = "quiz.csv"  # Path to the quiz CSV file
    results_file = "results.csv"  # Path to the results CSV file

    user_name = input("What's your name? ")
    questions = load_quiz(quiz_file)

    if len(questions) != 20:
        print("Error: The quiz must contain 20 questions.")
        return

    score = run_quiz(questions)
    save_results(user_name, score, results_file)

    print(f"{user_name}, your final score is {score} out of {len(questions)}.")

    quiz_file = "quiz.csv"  # Path to the quiz CSV file
    results_file = "results.csv"  # Path to the results CSV file

    user_name = input("What's your name? ")
    questions = load_quiz(quiz_file)

    if len(questions) != 20:
        print("Error: The quiz must contain 20 questions.")
        return

    score = run_quiz(questions)
    save_results(user_name, score, results_file)

    print(f"{user_name}, your final score is {score} out of {len(questions)}.")


if __name__ == "__main__":
    main()
