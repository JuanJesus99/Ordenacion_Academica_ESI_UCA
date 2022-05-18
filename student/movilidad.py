from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general


def start_movilidad(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'La Oficina de Movilidad brinda apoyo a los estudiantes que vienen a estudiar a la Escuela de Ingeniería, y promueve y apoya las oportunidades de movilidad de estudiantes y profesores',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Erasmus KA103', url='https://esingenieria.uca.es/internacional/movilidad/erasmus-ka103/')],
            [InlineKeyboardButton(text='Erasmus KA10', url='https://esingenieria.uca.es/internacional/movilidad/erasmus-ka107/')],
            [InlineKeyboardButton(text='Incoming', url='https://esingenieria.uca.es/internacional/movilidad/entrantes/')],
            [InlineKeyboardButton(text='SICUE', url='https://esingenieria.uca.es/internacional/movilidad/sicue/')],
            [InlineKeyboardButton(text='SICUE entrante', url='https://esingenieria.uca.es/internacional/movilidad/sicue-entrante/')],
            [InlineKeyboardButton(text='Otras movilidades', callback_data='movilidad_otras_movilidades')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
    
def mobility_start_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'The Mobility Office provides support to students coming to study at the School of Engineering, and promotes and supports student and faculty mobility opportunities',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Erasmus KA103', url='https://esingenieria.uca.es/internacional/movilidad/erasmus-ka103/')],
            [InlineKeyboardButton(text='Erasmus KA10', url='https://esingenieria.uca.es/internacional/movilidad/erasmus-ka107/')],
            [InlineKeyboardButton(text='Incoming', url='https://esingenieria.uca.es/internacional/movilidad/entrantes/')],
            [InlineKeyboardButton(text='SICUE', url='https://esingenieria.uca.es/internacional/movilidad/sicue/')],
            [InlineKeyboardButton(text='SICUE incoming', url='https://esingenieria.uca.es/internacional/movilidad/sicue-entrante/')],
            [InlineKeyboardButton(text='Other mobilities', callback_data='mobility_otras_movilidades_english')],
            [InlineKeyboardButton(text='Go back', callback_data='student_english_go_back')]
        ])
    )
    
def callback_movilidad_otras_movilidades(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Otras movilidades',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Beca Santander', url='https://esingenieria.uca.es/internacional/movilidad/beca-santander/')],
            [InlineKeyboardButton(text='PIMA', url='https://esingenieria.uca.es/internacional/movilidad/pima/')],
            [InlineKeyboardButton(text='UCA Internacional', url='https://esingenieria.uca.es/internacional/movilidad/uca-internacional/')],
            [InlineKeyboardButton(text='ERASMUS Prácticas', url='https://esingenieria.uca.es/internacional/movilidad/erasmus-practicas/')],
            [InlineKeyboardButton(text='Suplemento Europeo Título (SET)', url='https://esingenieria.uca.es/internacional/movilidad/set/')],
            [InlineKeyboardButton(text='Volver', callback_data='inicio_movilidad')]
        ])
    )
    
def callback_mobility_otras_movilidades_english(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Other mobilities',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Santander Scholarship', url='https://esingenieria.uca.es/internacional/movilidad/beca-santander/')],
            [InlineKeyboardButton(text='PIMA', url='https://esingenieria.uca.es/internacional/movilidad/pima/')],
            [InlineKeyboardButton(text='UCA Internacional', url='https://esingenieria.uca.es/internacional/movilidad/uca-internacional/')],
            [InlineKeyboardButton(text='ERASMUS internships', url='https://esingenieria.uca.es/internacional/movilidad/erasmus-practicas/')],
            [InlineKeyboardButton(text='European Diploma Supplement', url='https://esingenieria.uca.es/internacional/movilidad/set/')],
            [InlineKeyboardButton(text='Go back', callback_data='mobility_start_english')]
        ])
    )