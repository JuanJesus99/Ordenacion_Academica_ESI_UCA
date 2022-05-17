
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general

def student_exam_calendar(update, context):

    if(update.callback_query == None):

        update.message.reply_text(
            text = 'Calendario de exámenes por grado',
            reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
            ])
        )
            
    else:
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text = 'Calendario de exámenes por grado',
            reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                    [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
            ])
        )
            
      
def student_exam_calendar_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Exams calendars by degree',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Engineering Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Go back', callback_data='student_english_go_back')]
        ])
    )
        
def pdi_exam_calendar(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Calendario de exámenes por grado',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Volver', callback_data='PDI_spanish_go_back')]
        ])
    )
 
def pdi_exam_calendar_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Exams calendars by degree',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Engineering Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Go back', callback_data='PDI_english_go_back')]
        ])
    )
 
def pas_exam_calendar(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Calendario de exámenes por grado',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Volver', callback_data='PAS_spanish_go_back')]
        ])
    )
    
def pas_exam_calendar_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Exams calendars by degree',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://esingenieria.uca.es/docencia/grados/gia/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/docencia/grados/gididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://esingenieria.uca.es/docencia/grados/gie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://esingenieria.uca.es/docencia/grados/giei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://esingenieria.uca.es/docencia/grados/gii/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://esingenieria.uca.es/docencia/grados/gim/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://esingenieria.uca.es/docencia/grados/giti/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://esingenieria.uca.es/docencia/grados/giegiei/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://esingenieria.uca.es/docencia/grados/gimgie/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Engineering Industrial Design and Product Development Engineering', url='https://esingenieria.uca.es/docencia/grados/gimgididp/calendarios-y-convocatorias/')],
                [InlineKeyboardButton(text='Go back', callback_data='PAS_english_go_back')]
        ])
    )      