import turtle
import pandas


screen = turtle.Screen()
screen.title('Guess the States! U.S.A')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# This can be improved by opting out the state_x and state_y, and directly put it to set position
state = pandas.read_csv('50_states.csv')
state_states = state.state.to_list()
state_x = state.x.to_list()
state_y = state.y.to_list()

total_state = len(state_states)
score = 0

state_dict = {}
the_answers = []
missing_states = []

# Turning the data into a dict, with the states as keys and its coordinates as values
for i in range(len(state_states)):
    state_dict.update({state_states[i]: (state_x[i], state_y[i])})

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

for state in state_states:
    if state not in the_answers:
        missing_states.append(state)

dict_data = {
    'Missing States': missing_states,
    'Your answers': the_answers
}

new_dict = pandas.DataFrame.from_dict(dict_data, orient='index')
new_dict = new_dict.transpose()
new_dict.to_csv('Missing States')

screen.exitonclick()
