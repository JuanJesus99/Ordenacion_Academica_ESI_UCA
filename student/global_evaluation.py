
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general

def start_evaluacion_global(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Es un formato de evaluación en el que el estudiante renuncia al método establecido en la ficha de la asignatura y pasa a realizar un conjunto de pruebas establecidas por el equipo docente de la asignatura. Este método no se puede solicitar para la primera convocatoria de la asignatura.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='¿Cómo y cuándo puedo solicitarlo?', callback_data='evaluacion_global_periodo')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )


def callback_evaluacion_global_periodo(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Se solicita al responsable de la asignatura mediante correo electrónico. El plazo viene indicado en el siguiente documento',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Enlace al documento', url='https://esingenieria.uca.es/wp-content/uploads/2019/01/Evaluacionglobal.pdf')],
            [InlineKeyboardButton(text='Volver', callback_data='inicio_evaluacion_global')]
        ])
    )
    