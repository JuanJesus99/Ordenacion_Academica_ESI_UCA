
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general

def student_collaborating_students(update, context):
   
   if(update.callback_query == None):
        update.message.reply_text(
            text = 'Mediante la figura de alumno colaborador se trata de estimular la participación de los alumnos en actividades propias de los departamentos facilitando su iniciación a las tareas investigadoras. También hacer posible que puedan participar en funciones de docencia; sin que en ningún momento pueda entenderse que es el alumno colaborador el que imparte las clases regladas teóricas y prácticas, cometido que corresponde exclusivamente al profesor',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Reglamento', url='https://secretariageneral.uca.es/docs/Unidades/normativa/alumnos/969.pdf')],
                [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
            ])
        )
        
   else:
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text = 'Mediante la figura de alumno colaborador se trata de estimular la participación de los alumnos en actividades propias de los departamentos facilitando su iniciación a las tareas investigadoras. También hacer posible que puedan participar en funciones de docencia; sin que en ningún momento pueda entenderse que es el alumno colaborador el que imparte las clases regladas teóricas y prácticas, cometido que corresponde exclusivamente al profesor',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Reglamento', url='https://secretariageneral.uca.es/docs/Unidades/normativa/alumnos/969.pdf')],
                [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
            ])
        )