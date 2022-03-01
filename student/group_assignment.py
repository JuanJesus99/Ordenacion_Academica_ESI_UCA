from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general



def start_group_assignment(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Enlaces a las web oficiales de la escuela',
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