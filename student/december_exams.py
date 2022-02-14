
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general


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
        text = 'TÍTULOS DE GRADOS: \n\nPodrán solicitarla,  aquellos alumnos a los que reste para finalizar sus estudios 40 créditos o menos de la carga lectiva de la titulación o alternativamente, le resten un máximo de 3 asignaturas para terminar dichos estudios, aunque éstas en su conjunto superen los créditos indicados (incluido el TFG)'
                '\n\n\n\nTÍTULOS DE MÁSTER: \n\nPodrán solicitarla aquellos alumnos que le reste para finalizar 9 créditos o menos de la carga lectiva de la titulación (excluido el TFM)',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_conv_diciembre')]
        ])
    )
        
