#You can change the responses based on your requirements or add new responses or delete non-essential responses...

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup","hiii","hey"):
        return "Hey! Welcome to Gogte Institute of Technology"
    if user_message in ("who are you", "who are you?"):
        return "Iam a Gitise_bot created by Chinmay and group!!"
    if user_message in ("can you help me","help"):
        return "yup how can i help you"
    if user_message in ("what are the courses offered?"):
        return "There are mainy 9 Undergraduate courses offered, they are 1.Computer Science & Engineering " \
               " 2.Information Science & Engineering 3.Mechanical Engineering " \
               "4.Electronics &  Communication Engineering 5.Electrical & Electronics Engineering " \
               "6.Civil Enginnering 7.Aeronautical Enginnering 8.B.Sc(Honors) 9.Architecture"
    if user_message in ("what is ise?"):
        return "ISE stands for Information Science and Engennering"
    if user_message in ("what is cse?"):
        return "CSE stands for Computer Science and Engennering"
    if user_message in ("what is the minimum qualification required?"):
        return "Passed in 2nd PUC / 12th Std / Equivalent Exam with English as one of the " \
               "Languages and obtained a Minimum of 45% of Marks in aggregate in Physics and " \
               "Mathematics along with Chemistry / Bio-Technology / Biology / Electronics /Computer. " \
               "(40% for SC, ST, Cat-1, 2A, 2B, 3A and 3B category candidates of Karnataka State)."
    if user_message in ("which is the highest salary package in ise?"):
        return "Highest Salary Package is 13.6 lpa"
    if user_message in ("what is the under graduate intake?"):
        return "intake is around 60"
    if user_message in ("what is fees for ise dept?"):
        return "78,000"

    return "I don't understand you!!"







