# question_loader.py
# from .questions_Label import questions_Label
from .questions_CER import questions_CER
# from .questions_PRD import questions_PRD
# from .questions_Risk import questions_Risk
# from .questions_DesignValidation import questions_DesignValidation
# from .questions_Tracematrix import questions_Tracematrix


def questions():
    all_questions = []

    # modules = [questions_Label, questions_CER, questions_PRD, questions_Risk, questions_DesignValidation, questions_Tracematrix]
    modules = [questions_CER]  # Add other modules as needed
    for mod in modules:
        question_data = mod()
        if "Questions" in question_data:
            all_questions.extend(question_data["Questions"])

    return {"Questions": all_questions}

def priority():
    priority_list = ["Intended Use","Indication for Use","Contraindications","Claims","Warnings","Cautions","Date"]
    return priority_list
