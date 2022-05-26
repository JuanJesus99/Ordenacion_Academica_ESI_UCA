from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


import general

def start_llamamiento_especial(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Es una fecha para examinarse de una asignatura que te coincide con otra en el calendario oficial',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='¿Cómo y cuándo puedo solicitarlo?', callback_data='llamamiento_especial_periodo')],
            [InlineKeyboardButton(text='¿Cuándo y cuáles serán los exámenes con llamamiento?', callback_data='llamamiento_especial_examenes')],
            [InlineKeyboardButton(text='¿Qué tengo que llevar al día del examen de llamamiento?', callback_data='llamamiento_especial_requisitos')],
            [InlineKeyboardButton(text='¿Puedo presentarme aunque no haya rellenado el formulario?', callback_data='llamamiento_especial_presentarmeSinFormulario')],
            [InlineKeyboardButton(text='Salgo en la lista pero al final, he decidido hacer únicamente el examen de la convocatoria ordinaria, ¿puedo?', callback_data='llamamiento_especial_ordinaria')],
            [InlineKeyboardButton(text='¿Puedo presentarme al llamamiento si no me coincide con otro examen?', callback_data='llamamiento_especial_sino_coincide')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )


def callback_llamamiento_especial_periodo(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Un tiempo después de que se publique el calendario de exámenes, recibirás un TAVIRA (a tu correo oficial) para rellenar un formulario. En el formulario tendrás que marcar todas las asignaturas que te coincidan y que te quieras presentar',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_llamamiento_especial')]
        ])
    )


def callback_llamamiento_especial_examenes(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Unos días después de que se cierre el plazo dado en el formulario, se publicará el calendario y alumnos incluidos. En cualquier caso, los días de llamamiento son después del último examen que aparece en el calendario',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_llamamiento_especial')]
        ])
    )



def callback_llamamiento_especial_requisitos(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Obligatoriamente el justificante firmado de haberte presentado al otro examen que te coincidía.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_llamamiento_especial')]
        ])
    )


def callback_llamamiento_especial_presentarmeSinFormulario(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'No es lo recomendado pero si te coincide con otro examen, sí puedes presentarte si vas con el justificante firmado.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_llamamiento_especial')]
        ])
    )


def callback_llamamiento_especial_ordinaria(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Sí',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_llamamiento_especial')]
        ])
    )

def callback_llamamiento_especial_sino_coincide(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'No',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_llamamiento_especial')]
        ])
    )


# Ingles
   
def special_call_start_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'It is a date for examining a subject that coincides with another in the official calendar',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='How and when can I apply?', callback_data='special_call_periodo_english')],
            [InlineKeyboardButton(text='When and which exams will be called?', callback_data='special_call_examenes_english')],
            [InlineKeyboardButton(text='What do I have to bring with me on the day of the exam?', callback_data='special_call_requisitos_english')],
            [InlineKeyboardButton(text='Can I sit the exam even if I have not filled in the form?', callback_data='special_call_presentarmeSinFormulario_english')],
            [InlineKeyboardButton(text='I am on the list but in the end, I have decided to take only the exam for the ordinary exam, can I do it?', callback_data='special_call_ordinaria_english')],
            [InlineKeyboardButton(text='Can I sit the call if it does not coincide with another exam?', callback_data='special_call_sino_coincide_english')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )


def callback_special_call_periodo_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Some time after the exam calendar is published, you will receive a TAVIRA (to your official mail) to fill in a form. In the form you will have to mark all the subjects that coincide with yours and that you want to take',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='special_call_start_english')]
        ])
    )

def callback_special_call_examenes_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'A few days after the deadline given on the form, the calendar and the students included will be published. In any case, the call days are after the last exam that appears in the calendar.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='special_call_start_english')]
        ])
    )
        

def callback_special_call_requisitos_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'You must bring the signed proof of having taken the other exam that coincided with your exam',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='special_call_start_english')]
        ])
    )


def callback_special_call_presentarmeSinFormulario_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'It is not recommended, but if it coincides with another exam, you can sit it if you bring the signed receipt',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='special_call_start_english')]
        ])
    )

def callback_special_call_ordinaria_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Yes',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='special_call_start_english')]
        ])
    )

def callback_special_call_sino_coincide_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'No',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Back', callback_data='special_call_start_english')]
        ])
    )