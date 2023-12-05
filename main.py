import turtle
import pandas


screen = turtle.Screen()
screen.title('Guess the States! U.S.A')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv('50_states.csv')
total_state = len(states)
score = 0

state_dict = {row.state: (row.x, row.y) for index, row in states.iterrows()}
the_answers = []

run = True

while run:
    answer = screen.textinput(title='Guess the State', prompt=f'Name a State? {score}/{total_state}').title()
    if answer == 'Exit' or score == total_state:
        run = False

    if state_dict.get(answer):
        score += 1
        the_answers.append(answer)
        new = turtle.Turtle()
        new.hideturtle()
        new.penup()
        new.setposition(state_dict[answer])
        new.write(answer, align='left')

missing_states = [state for state in states.state if state not in the_answers]

dict_data = {
    'Missing States': missing_states,
    'Your answers': the_answers
}

new_dict = pandas.DataFrame.from_dict(dict_data, orient='index')
new_dict = new_dict.transpose()
new_dict.to_csv('Missing States')

screen.exitonclick()
