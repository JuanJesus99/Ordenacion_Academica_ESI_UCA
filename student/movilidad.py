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
    
def movilidad_otras_movilidades(update, context):
    
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