
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

# Ingles
    
def global_assessment_start_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'This is an evaluation format in which the student waives the method established in the subject record and takes a set of tests established by the teaching team of the subject. This method cannot be requested for the first sitting of the course',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='How and when can I apply for it?', callback_data='global_assessment_periodo_english')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )
    
def callback_global_assessment_periodo_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'It is requested to the person in charge of the subject by e-mail. The deadline is indicated in the following document',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Link to the document', url='https://esingenieria.uca.es/wp-content/uploads/2019/01/Evaluacionglobal.pdf')],
            [InlineKeyboardButton(text='Back', callback_data='global_assessment_start_english')]
        ])
    )