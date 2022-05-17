
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext.callbackcontext import CallbackContext

import general


def student_start_tutorships(update,context):
 
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Para ver las tutorías diríjase a la web',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Enlace a la web', url='https://tutorias.uca.es/tutorias/')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
    
def student_start_tutorships_english(update,context):
 
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'To see the tutorials go to the website',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Link to the websiteb', url='https://tutorias.uca.es/tutorias/')],
            [InlineKeyboardButton(text='Go back', callback_data='student_english_go_back')]
        ])
    )