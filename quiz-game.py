# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

#def question_one(questions):
    #for question in questions:
        #for key, value in question.items():
            #print(key, ":", value)
        #print("")

    #question = [question["prompt"] for question in questions]
    #print(question)

    #course = [dictionary["course"] for dictionary in list_of_dict]
    #price = [dictionary["price"] for dictionary in list_of_dict]

    
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for options in question["options"]:
            print(options)
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer.upper() == question["answer"]:
            print("Correct. Hooray!!")
            score += 1
            print(f"Score: {score}\n")
        else:
            print("Wrong. LOSER! The correct answer was", question["answer"])
            print(f"Score: {score}\n")
    
    print(f"Your final score is: {score} out of {len(questions)}")

    #x = questions[0]['prompt']
    #print(x)
    #for question in questions:
        #print(question.keys())
        #print(question.values())
        #print(question.items())

#prints first questions

#prints first questions options

#input for first question

#validates input

#compares input to answer
    #if correct shows second questions
    #if wrong display correct answer, goes to next questions
    #updates score if correct

#at end of game - show win message depending on score



run_quiz(questions)
