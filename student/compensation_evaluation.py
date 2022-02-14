from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general


def start_compensacion(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'La evaluación por compensación consiste en superar una asignatura, sin necesidad de realizar examen, siempre y cuando se cumplan los requisitos para ello',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Periodo de solicitud', callback_data='compensacion_periodo'), InlineKeyboardButton(text='Requisitos', callback_data='compensacion_requisitos')],
            [InlineKeyboardButton(text='Requisitos específicos', callback_data='compensacion_req_especificos'),InlineKeyboardButton(text='CAU', url='https://cau-alumnos.uca.es/cau/servicio.do?id=O109')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )

def callback_compensacion_periodo(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Primer Plazo: del 7 al 22 de enero. \nSegundo Plazo: del 7 al 22 de marzo. \nTercer Plazo: del 7 al 22 de julio. \nCuarto Plazo: del 22 de septiembre al 7 de octubre.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_compensacion')]
        ])
    )
    

def callback_compensacion_requisitos(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'TÍTULOS DE GRADOS (deberán cumplirse TODOS los requisitos):'
                '\n\n\t\t El alumno de Grado deberá haber aprobado en la Universidad de Cádiz al menos el 50% de los créditos de su titulación.'
                '\n\n\t\t Deberá tener pendiente para terminar su Grado solo una asignatura anual o dos semestrales (en ese cómputo no se cuentan ni el TFG, ni las  prácticas, ni el rotatorio, ni el prácticum, ni periodos de embarque o similares).'
                '\n\n\n\nTÍTULOS DE MÁSTER:'
                '\n\n\t\t El alumno de MÁSTER deberá tener pendiente para terminar sus estudios de Máster una asignatura (que será la asignatura objeto de esta solicitud)',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_compensacion')]
        ])
    )
   


def callback_compensacion_req_especificos(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '1º. Cumplir todos los requisitos siguientes:'
                '\n\n\t\t 1. Que se haya presentado al menos cuatro veces, en los cuatro últimos cursos si es un Grado, y en los dos últimos cursos si se trata de estudios de Máster.'
                '\n\n\t\t 2. Que haya obtenido una nota de al menos un 3,0 en los años referidos en el apartado a).'
                '\n\n\t\t 3. Que la nota media de las dos mejores calificaciones obtenidas, en los cursos referidos en el apartado a), en la asignatura cuya compensación se solicita sea de un 2,0'
                '\n\n\t\t 4. Que la nota media de su expediente sea:'
                '\n\t\t\t\t\t\t  Máster: 7,5 (siete y medio)'
                '\n\t\t\t\t\t\t  Grados rama de Artes y humanidades, Ciencias Sociales y Jurídicas y Ciencias de la Salud: 6,5 (seis y medio) '
                '\n\t\t\t\t\t\t  Grados ramas de Ciencias e Ingeniería o Arquitectura: 6 (seis)'

                '\n\n\n2º. Alumnos de GRADO que hayan obtenido DOS calificaciones iguales o superiores a un 4,0'
                '\n\n\n3º. Alumnado que se sitúe al menos dos veces entre el 25% de los mejores calificados en las convocatorias de febrero, junio o septiembre en cursos académicos donde la asignatura solicitada tenga una tasa de rendimiento inferior al 25%',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_compensacion')]
        ])
    )

