from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer_checker', methods=['GET', 'POST'])
def answer_checker():
    result = ""
    if request.method == 'POST':
        equation = request.form['equation']
        try:
            parts = equation.split('=')
            if len(parts) != 2:
                result = "Invalid format. Please enter in the format 'a + b = c'."
            else:
                left_side = parts[0].strip()
                user_answer = int(parts[1].strip())
                correct_answer = eval(left_side)

                if user_answer == correct_answer:
                    result = "Correct!"
                else:
                    result = f"Wrong. The correct answer is {correct_answer}"
        except (ValueError, SyntaxError, NameError):
            result = "Invalid input. Please enter a valid equation."

    return render_template('answer_checker.html', result=result)

@app.route('/memory_bank', methods=['GET', 'POST'])
def memory_bank():
    if 'problems' not in memory_bank.__dict__:
        memory_bank.problems = []
    MAX_PROBLEMS = 4
    result = ""
    if request.method == 'POST':
        if 'problem' in request.form:
            problem = request.form['problem']
            try:
                parts = problem.split('=')
                if len(parts) != 2:
                    result = "Invalid format. Please enter in the format 'a + b = c'."
                else:
                    if len(memory_bank.problems) < MAX_PROBLEMS:
                        memory_bank.problems.append(problem)
                        result = "Problem stored successfully!"
                    else:
                        result = "Memory Bank is full. Only 4 problems can be stored."
            except (ValueError, SyntaxError, NameError):
                result = "Invalid input. Please enter a valid problem."
        elif 'reset' in request.form:
            memory_bank.problems = []
            result = "Memory Bank has been reset."
        elif 'start' in request.form:
            return redirect(url_for('solve_problems'))

    return render_template('memory_bank.html', result=result, problems=memory_bank.problems)

@app.route('/solve_problems', methods=['GET', 'POST'])
def solve_problems():
    if 'problems' not in memory_bank.__dict__:
        memory_bank.problems = []
    result = ""
    problem_index = str(request.args.get('problem_index', '0'))
    if isinstance(problem_index, str) and problem_index.isdigit():
        problem_index = int(problem_index)
    else:
        problem_index = 0
    current_problem = None
    if isinstance(problem_index, str) and problem_index.isdigit():
        problem_index = int(problem_index)
    else:
        problem_index = 0

    if request.method == 'POST':
        user_answer = request.form.get('user_answer')
        problem_index = str(request.form.get('problem_index', '0'))
        if problem_index.isdigit():
            problem_index = int(problem_index)
        else:
            problem_index = 0
        if user_answer is not None and problem_index < len(memory_bank.problems):
            try:
                parts = memory_bank.problems[problem_index].split('=')
                left_side = parts[0].strip()
                correct_answer = eval(left_side)
                if int(user_answer) == correct_answer:
                    result = "Correct!"
                else:
                    result = f"Wrong. The correct answer is {correct_answer}"
            except (ValueError, SyntaxError, NameError):
                result = "Invalid input. Please enter a valid answer."

            problem_index += 1
            if problem_index >= len(memory_bank.problems):
                return redirect(url_for('memory_bank'))
        else:
            problem_index = 0

    if len(memory_bank.problems) > problem_index:
        current_problem = memory_bank.problems[problem_index]

    return render_template('solve_problems.html', current_problem=current_problem, result=result, problem_index=problem_index if current_problem else 0)

if __name__ == '__main__':
    app.run(debug=True)
