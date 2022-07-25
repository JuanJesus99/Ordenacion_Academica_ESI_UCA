from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def student_exam_calendar(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Calendario de exámenes por grado',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIA.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIDIDP.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIE.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEI.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGII.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIM.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGITI.pdf')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEGIEI.pdf')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIE.pdf')],
                [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIDIDP.pdf')],
                [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )          
      
def student_exam_calendar_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Exams calendars by degree',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIA.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIDIDP.pdf')],
                [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIE.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEI.pdf')],
                [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGII.pdf')],
                [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIM.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGITI.pdf')],
                [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEGIEI.pdf')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIE.pdf')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIDIDP.pdf')],
                [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )
        
def pdi_exam_calendar(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Calendario de exámenes por grado',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIA.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIDIDP.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIE.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEI.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGII.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIM.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGITI.pdf')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEGIEI.pdf')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIE.pdf')],
                [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIDIDP.pdf')],
                [InlineKeyboardButton(text='Volver', callback_data='PDI_spanish_go_back')]
        ])
    )
 
def pdi_exam_calendar_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Exams calendars by degree',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIA.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIDIDP.pdf')],
                [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIE.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEI.pdf')],
                [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGII.pdf')],
                [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIM.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGITI.pdf')],
                [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEGIEI.pdf')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIE.pdf')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIDIDP.pdf')],
                [InlineKeyboardButton(text='Back', callback_data='PDI_english_go_back')]
        ])
    )
 
def pas_exam_calendar(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Calendario de exámenes por grado',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIA.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIDIDP.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIE.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEI.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGII.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIM.pdf')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGITI.pdf')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEGIEI.pdf')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIE.pdf')],
                [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIDIDP.pdf')],
                [InlineKeyboardButton(text='Volver', callback_data='PAS_spanish_go_back')]
        ])
    )
    
def pas_exam_calendar_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Exams calendars by degree',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIA.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIDIDP.pdf')],
                [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIE.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEI.pdf')],
                [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGII.pdf')],
                [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIM.pdf')],
                [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGITI.pdf')],
                [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIEGIEI.pdf')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIE.pdf')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/wp-content/uploads/2022/05/CalendarioGIMGIDIDP.pdf')],
                [InlineKeyboardButton(text='Back', callback_data='PAS_english_go_back')]
        ])
    )      