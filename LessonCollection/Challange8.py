
from pprint import pprint

science_QnA = [
    { "category": "Science",
      "question": "What of these elments has the lowest Atomic Number?",
      "choices": {"A": "Nitrogen", "B": "Oxygen", "C": "Helium", "D": "Hydrogen"},
      "correct": "D",
    },
    { "category": "Science",
      "question": "The biological Class 'Aves'(Birds) includes all of the following EXCEPT..",
      "choices": {"A": "Pheasant", "B": "Penguin", "C": "Pangolin", "D": "Plover"},
      "correct": "C",
    },
    { "category": "Science",
      "question": "Which of the following is NOT a type of rock?",
      "choices": {"A": "Diatomic", "B": "Igneous", "C": "Metamorphic", "D": "Sedimentary"},
      "correct": "A",
    },
    { "category": "Science",
      "question": "How many nanoseconds are there in 1 second?",
      "choices": {"A": "1,000", "B": "1,000,000", "C": "1,000,000,000", "D": "1,000,000,000,000"},
      "correct": "C",
    },
    { "category": "Science",
      "question": "Which of these planets is closet to Earth?",
      "choices": {"A": "Mercury", "B": "Venus", "C": "Mars", "D": "Jupiter"},
      "correct": "B",
    },
    { "category": "Geography",
      "question": "Which of these countries is not in Africa?",
      "choices": {"A": "Cameroon", "B": "Oman", "C": "Sierra Leone", "D": "Chad"},
      "correct": "B",
    },
    { "category": "Geography",
      "question": "The largest of the Great Lakes is:",
      "choices": {"A": "Lake Michigan", "B": "Lake Ontario", "C": "Lake Huron", "D": "Lake Superior"},
      "correct": "D",
    },
    { "category": "Geography",
      "question": "The former name of Mt. Denali is:",
      "choices": {"A": "Mt. McKinley", "B": "Mt. Kilimanjaro", "C": "Mt. Fuji", "D": "Mt. Hood"},
      "correct": "Z",
    },
    { "category": "Geography",
      "question": "Which of these countries is a peninsula?",
      "choices": {"A": "Ecuador", "B": "Libya", "C": "Denmark", "D": "Mongolia"},
      "correct": "C",
    },
    { "category": "Geography",
      "question": "What is the longest river in the world?",
      "choices": {"A": "Nile River", "B": "Amazon River", "C": "Mississipi River", "D": "Yellow River"},
      "correct": "A",
    },
    { "category": "Movies",
      "question": "Which movie does not star Al Pacino?",
      "choices": {"A": "The Godfather", "B": "", "C": "Dog Day Afternoon", "D": "Goodfellas"},
      "correct": "D",
    },
    { "category": "Movies",
      "question": "In The Wizard of Oz, Dorothy's house lands on the Witch of the..",
      "choices": {"A": "North", "B": "South", "C": "East", "D": "West"},
      "correct": "C",
    },
]

# pprint(science_QnA)

for entry_dict in science_QnA:
    if entry_dict['category'] == "Movies":
        print(f"Question: {entry_dict['Question']}")

    for k,v in entry_dict['choices'].items():
        print(f"{k}, {v}")
