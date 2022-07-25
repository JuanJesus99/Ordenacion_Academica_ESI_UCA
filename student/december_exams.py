from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start_conv_diciembre(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Es una convocatoria extraordinaria que se realiza en el mes de diciembre',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Periodo de solicitud', callback_data='conv_diciembre_periodo')],
            [InlineKeyboardButton(text='Requisitos', callback_data='conv_diciembre_requisitos'),InlineKeyboardButton(text='CAU', url='https://cau-admpr.uca.es/cau/servicio.do?id=U027')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
   
def callback_conv_diciembre_periodo(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'El plazo para solicitar el derecho a examen en la convocatoria de diciembre es la primera quincena de noviembre',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_conv_diciembre')]
        ])
    )
    
def callback_conv_diciembre_requisitos(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'TÍTULOS DE GRADOS: \n\nPodrán solicitarla, aquellos alumnos a los que reste para finalizar sus estudios 40 créditos o menos de la carga lectiva de la titulación o alternativamente, le resten un máximo de 3 asignaturas para terminar dichos estudios, aunque éstas en su conjunto superen los créditos indicados (incluido el TFG)'
                '\n\n\n\nTÍTULOS DE MÁSTER: \n\nPodrán solicitarla aquellos alumnos que le reste para finalizar 9 créditos o menos de la carga lectiva de la titulación (excluido el TFM)',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_conv_diciembre')]
        ])
    )

# Ingles

def december_call_start_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'This is an extraordinary call for applications in December',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Application period', callback_data='december_call_periodo_english')],
            [InlineKeyboardButton(text='Requirements', callback_data='december_call_requisitos_english'),InlineKeyboardButton(text='CAU', url='https://cau-admpr.uca.es/cau/servicio.do?id=U027')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )

def callback_december_call_periodo_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'The deadline to apply for the right to sit the exam in December is the first fortnight of November',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='december_call_start_english')]
        ])
    )
    
def callback_december_call_requisitos_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'BACHELOR`S DEGREES: \n\nStudents who have 40 or less credits left to finish their studies or, alternatively, have a maximum of 3 subjects left to finish their studies, even if these together exceed the indicated credits (including the TFG), may apply for the right to take the exam'
                '\n\n\n\nMASTER`S DEGREES: \n\nStudents who have 9 credits or less of the course load of the degree (excluding the TFM) may apply for it',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='december_call_start_english')]
        ])
    )