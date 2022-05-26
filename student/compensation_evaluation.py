from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general


def start_compensacion(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'La evaluación por compensación consiste en superar una asignatura, sin necesidad de realizar examen, siempre y cuando se cumplan los requisitos para ello',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Títulos habilitantes', callback_data='inicio_compensacion_habilitantes')],
            [InlineKeyboardButton(text='Títulos no habilitantes', callback_data='inicio_comnpensacion_no_habilitantes')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )

#  Habilitantes

def start_compensacion_habilitantes(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Títulos habilitantes',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Periodo de solicitud', callback_data='compensacion_habilitantes_periodo'), InlineKeyboardButton(text='Requisitos', callback_data='compensacion_habilitantes_requisitos')],
            [InlineKeyboardButton(text='CAU', url='https://cau-alumnos.uca.es/cau/servicio.do?id=O109')],
            [InlineKeyboardButton(text='Volver', callback_data='start_compensacion')]
        ])
    )

def callback_compensacion_habilitantes_periodo(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Primer Plazo: del 7 al 22 de enero. \nSegundo Plazo: del 7 al 22 de marzo. \nTercer Plazo: del 7 al 22 de julio. \nCuarto Plazo: del 22 de septiembre al 7 de octubre.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_compensacion_habilitantes')]
        ])
    )
    

def callback_compensacion_habilitantes_requisitos(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'a. Que se haya presentado a examen al menos en seis convocatorias.'
                '\nb. Que la nota media de las tres mejores calificaciones obtenidas en esas convocatorias sea, al menos, un 3,5. '
                '\nc. Que la nota media de las tres últimas convocatorias, hasta que se inicia este proceso de solicitud de aprobado por compensación, sea, al menos, un 1,5. ',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_compensacion_habilitantes')]
        ])
    )

# No habilitantes
def start_compensacion_no_habilitantes(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Títulos no habilitantes',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Periodo de solicitud', callback_data='compensacion_periodo'), InlineKeyboardButton(text='Requisitos', callback_data='compensacion_requisitos')],
            [InlineKeyboardButton(text='Requisitos específicos', callback_data='compensacion_req_especificos'),InlineKeyboardButton(text='CAU', url='https://cau-alumnos.uca.es/cau/servicio.do?id=O109')],
            [InlineKeyboardButton(text='Volver', callback_data='start_compensacion')]
        ])
    )

def callback_compensacion_periodo(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Primer Plazo: del 7 al 22 de enero. \nSegundo Plazo: del 7 al 22 de marzo. \nTercer Plazo: del 7 al 22 de julio. \nCuarto Plazo: del 22 de septiembre al 7 de octubre.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_comnpensacion_no_habilitantes')]
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
            [InlineKeyboardButton(text='Volver', callback_data='inicio_comnpensacion_no_habilitantes')]
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
            [InlineKeyboardButton(text='Volver', callback_data='inicio_comnpensacion_no_habilitantes')]
        ])
    )


#  Ingles

def compensation_evaluation_start_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'The assessment by compensation consists of passing a subject, without the need to take an exam, provided that the requirements for this are met',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Qualifying qualifications', callback_data='compensation_evaluation_qualifying_english')],
            [InlineKeyboardButton(text='Non qualifying qualifications', callback_data='compensation_evaluation_nonqualifying_english')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )


# Hablilitantes
def compensation_evaluation_qualifying_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Qualifying qualifications',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Application period', callback_data='compensation_evaluation_qualifying_periodo_english'), InlineKeyboardButton(text='Requirements', callback_data='compensation_evaluation_qualifying_requisitos_english')],
            [InlineKeyboardButton(text='CAU', url='https://cau-alumnos.uca.es/cau/servicio.do?id=O109')],
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_start_english')]
        ])
    )

def callback_compensation_evaluation_qualifying_periodo_english(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'First deadline: 7 to 22 January \nSecond deadline: 7 to 22 March \nThird deadline: 7 to 22 July \nFourth Deadline: from 22 September to 7 October',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_qualifying_english')]
        ])
    )


def callback_compensation_evaluation_qualifying_requisitos_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'a. You must have taken the exam at least six times. '
                '\nb. The average mark of the three best marks obtained in these examinations must be at least 3.5. '
                '\nc. That the average mark of the last three examinations, until this process of requesting a pass by compensation begins, is at least 1.5.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_qualifying_english')]
        ])
    )


#  No habilitantes

def compensation_evaluation_nonqualifying_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Non qualifying qualifications',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Application period', callback_data='compensation_evaluation_nonqualifying_periodo_english'), InlineKeyboardButton(text='Requirements', callback_data='compensation_evaluation_nonqualifying_requisitos_english')],
            [InlineKeyboardButton(text='Specific requirements', callback_data='compensation_evaluation_nonqualifying_especificos_english'),InlineKeyboardButton(text='CAU', url='https://cau-alumnos.uca.es/cau/servicio.do?id=O109')],
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_start_english')]
        ])
    )


    # query.edit_message_text(
    #     text = 'Non qualifying qualifications'
    #     reply_markup = InlineKeyboardMarkup([
    #         # [InlineKeyboardButton(text='Application period', callback_data='compensation_evaluation_nonqualifying_periodo_english'), InlineKeyboardButton(text='Requirements', callback_data='compensation_evaluation_nonqualifying_requisitos_english')],
    #         # [InlineKeyboardButton(text='Specific requirements', callback_data='compensation_evaluation_nonqualifying_requisitosespecificos_english'),InlineKeyboardButton(text='CAU', url='https://cau-alumnos.uca.es/cau/servicio.do?id=O109')],
    #         [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_start_english')]
    #     ])
    # )


def callback_compensation_evaluation_nonqualifying_periodo_english(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'First deadline: 7 to 22 January \nSecond deadline: 7 to 22 March \nThird deadline: 7 to 22 July \nFourth Deadline: from 22 September to 7 October',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_nonqualifying_english')]
        ])
    )


def callback_compensation_evaluation_nonqualifying_requisitos_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'DEGREE DEGREES (ALL requirements must be fulfilled)'
                '\n\n\t\t Undergraduate students must have passed at least 50% of the credits of their degree at the University of Cadiz.'
                '\n\n\t\t Students must have only one yearly or two semester subjects pending to finish their degree (this does not include the TFG, internships, rotations, practicum, on-boarding periods or similar).'
                '\n\n\n\nMASTER\'S DEGREES:'
                '\n\n\t\t The MASTER\'s student must have one subject pending in order to complete their Master\'s studies (which will be the subject of this application)',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_nonqualifying_english')]
        ])
    )

def callback_compensation_evaluation_nonqualifying_requisitos_especificos_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Fulfil all of the following requirements:'
                '\n\n\t\t 1. To have applied at least four times, in the last four years if it is a Bachelor\'s Degree, and in the last two years if it is a Master\'s Degree.'
                '\n\n\t\t 2. To have obtained a mark of at least 3.0 in the years referred to in section a.'
                '\n\n\t\t 3. The average mark of the two best marks obtained, in the courses referred to in section a, in the subject for which compensation is requested is 2.0'
                '\n\n\t\t 4. That the average mark of the student\'s transcript is:'
                '\n\t\t\t\t\t\t Master\'s degree: 7.5 (seven and a half)'
                '\n\t\t\t\t\t\t Bachelor\'s degrees in Arts and Humanities, Social and Legal Sciences and Health Sciences: 6.5 (six and a half) '
                '\n\t\t\t\t\t\t Bachelor\'s degrees in Science and Engineering or Architecture: 6 (six).'

                '\n\n\n2º. Undergraduate students who have obtained TWO grades equal to or higher than 4.0.'
                '\n\n\n3º. Students who are at least twice among the top 25% of those with the best marks in the February, June or September exams in academic years where the subject applied for has a performance rate of less than 25%',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='compensation_evaluation_nonqualifying_english')]
        ])
    )