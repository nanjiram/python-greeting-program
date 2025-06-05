def calculate_final_grade(labs_scores, midsem_score, final_score):
    if len(labs_scores) != 8:
        raise ValueError("There must be exactly 8 lab scores.")
    
    labs_avg = sum(labs_scores) / len(labs_scores)
    weighted_labs = labs_avg * 0.5
    weighted_exams = ((midsem_score + final_score) / 2) * 0.5
    total_score = weighted_labs + weighted_exams

    if total_score >= 90:
        grade = 'A'
    elif total_score >= 80:
        grade = 'B'
    elif total_score >= 70:
        grade = 'C'
    elif total_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return total_score, grade


def get_score_input(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    print("Enter 8 lab scores (0-100):")
    labs = [get_score_input(f"Lab {i+1} score: ") for i in range(8)]

    midsem = get_score_input("Enter Mid-semester exam score (0-100): ")
    final = get_score_input("Enter Final exam score (0-100): ")

    total, letter = calculate_final_grade(labs, midsem, final)

    print(f"\nFinal Score: {total:.2f}")
    print(f"Grade: {letter}")

