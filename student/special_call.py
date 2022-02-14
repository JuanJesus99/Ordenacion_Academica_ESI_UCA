from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


import general

def start_llamamiento_especial(update, context):
    
    if(update.callback_query == None):
        update.message.reply_text(
            text = 'Es una fecha para examinarse de una asignatura que te coincide con otra en el calendario oficial',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='¿Cómo y cuándo puedo solicitarlo?', callback_data='llamamiento_especial_periodo')],
                [InlineKeyboardButton(text='¿Cuándo y cuáles serán los exámenes con llamamiento?', callback_data='llamamiento_especial_examenes')],
                [InlineKeyboardButton(text='¿Qué tengo que llevar al día del examen de llamamiento?', callback_data='llamamiento_especial_requisitos')],
                [InlineKeyboardButton(text='¿Puedo presentarme aunque no haya rellenado el formulario?', callback_data='llamamiento_especial_presentarmeSinFormulario')],
                [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
            ])
        )
    
    else:
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text = 'Es una fecha para examinarse de una asignatura que te coincide con otra en el calendario oficial',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='¿Cómo y cuándo puedo solicitarlo?', callback_data='llamamiento_especial_periodo')],
                [InlineKeyboardButton(text='¿Cuándo y cuáles serán los exámenes con llamamiento?', callback_data='llamamiento_especial_examenes')],
                [InlineKeyboardButton(text='¿Qué tengo que llevar al día del examen de llamamiento?', callback_data='llamamiento_especial_requisitos')],
                [InlineKeyboardButton(text='¿Puedo presentarme aunque no haya rellenado el formulario?', callback_data='llamamiento_especial_presentarmeSinFormulario')],
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
        text = 'Unos días después de que se cierre el plazo dado en el formulario, se publicará el calendario y alumnos incluidos. En cualquier caso, los días de llamamiento son después del último examen que aparece en el calendario.',
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
