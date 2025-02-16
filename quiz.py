
questions = [
    {"question": "What is the capital city of India?",
     "options": ["A: Delhi", "B: Kolkata", "C: Mumbai", "D: Bangalore"],
     "answer": "A"},
    {"question": "What is the capital city of Pakistan?",
     "options": ["A: Lahore", "B: Karachi", "C: Multan", "D: Islamabad"],
     "answer": "D"},
    {"question": "What is the capital city of China?",
     "options": ["A: Beijing", "B: Shanghai", "C: Chengdu", "D: Shenzhen"],
     "answer": "A"},
    {"question": "What is the capital city of Nepal?",
     "options": ["A: Kathmandu", "B: Pharaoh", "C: Dharan", "D: Lalitpur"],
     "answer": "A"},
    {"question": "What is the capital city of Japan?",
     "options": ["A: Kobe", "B: Tokyo", "C: Hiroshima", "D: Osaka"],
     "answer": "B"},
    {"question": "What is the capital city of Bhutan?",
     "options": ["A: Jakar", "B: Punakha", "C: Thimphu", "D: Kobe"],
     "answer": "C"},
    {"question": "What is the capital city of Srilanka?",
     "options": ["A: Chennai", "B: Colombo", "C : Shanghai", "D : Kochi"],
     "answer": "B"
     },
    {"question": "What is the capital city of Bangladesh?",
     "options": ["A : Bogra", "B: Kishoreganj", "C: Narsingdi", "D: Dhaka"],
     "answer": "D"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Validate input
    while answer not in ['A', 'B', 'C', 'D']:
        print("Invalid option! Please choose A, B, C, or D.")
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

print(f"Your final score is {score}/{len(questions)}.")
