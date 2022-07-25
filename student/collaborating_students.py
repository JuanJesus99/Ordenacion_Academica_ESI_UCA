from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def student_collaborating_students(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Mediante la figura de alumno colaborador se trata de estimular la participación de los alumnos en actividades propias de los departamentos facilitando su iniciación a las tareas investigadoras. También hacer posible que puedan participar en funciones de docencia; sin que en ningún momento pueda entenderse que es el alumno colaborador el que imparte las clases regladas teóricas y prácticas, cometido que corresponde exclusivamente al profesor',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Reglamento', url='https://secretariageneral.uca.es/docs/Unidades/normativa/alumnos/969.pdf')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
        
def collaborating_students_start_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'By means of the collaborating student, the aim is to stimulate the participation of students in departmental activities, facilitating their initiation to research tasks. It also makes it possible for them to participate in teaching functions, without it ever being understood that the collaborating student is the one who teaches the regulated theoretical and practical classes, a task that corresponds exclusively to the lecturer',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Regulations', url='https://secretariageneral.uca.es/docs/Unidades/normativa/alumnos/969.pdf')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )