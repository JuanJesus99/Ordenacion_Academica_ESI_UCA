

from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


import main


# Updater sirve para saber las peticiones que va recibiendo el bot, todo lo que hace el usuario pasa por el updater

# INPUT_ID_USER = 0
# INPUT_PW_USER = 1
# SELECT_TYPE_USER = 2
# SELECTED_PDI = 3
# SELECTED_STUDENT = 4
# STUDENT_HORARIOS = 5
# STUDENT_TFG = 6
# STUDENT_EVALUACION_GLOBAL = 7
# STUDENT_LLAMAMIENTO_ESPECIAL = 8
# STUDENT_CONV_DICIEMBRE = 9
# STUDENT_ASIGNACION_GRUPOS = 10
# STUDENT_PRACTICAS = 11
# STUDENT_COMPENSACION = 12

# INPUT_ID_USER, INPUT_PW_USER, SELECT_TYPE_USER, SELECTED_STUDENT, SELECTED_PDI, SELECTED_PAS, STUDENT_TIMETABLE, STUDENT_EXAM_CALENDAR, STUDENT_TFG, STUDENT_TUTORSHIPS, STUDENT_GLOBAL_EVALUATION, STUDENT_SPECIAL_CALL, STUDENT_CONV_DICIEMBRE, STUDENT_GROUP_ASSIGNMENT, STUDENT_PRACTICAS_CURRICULARES,STUDENT_PRACTICAS_EXTRACURRICULARES, STUDENT_COMPENSACION, PDI_TIMETABLE, PDI_EXAM_CALENDAR, PAS_TIMETABLE, PAS_EXAM_CALENDAR = range(21)

INPUT_ID_USER, CONSULT_SIRE = range(2)

flag_login = 0
user_id = ''
user_pw = ''


def comienzo_bot(update, context):
    update.message.reply_text('Por favor para comenzar a utilizar el bot, escriba /iniciar')
    
def start_sire(update, context):
    if(flag_login):
        update.message.reply_text('Ahora mismo no podemos conectarte, intentelo de nuevo mas tarde')
        return ConversationHandler.END
    else:
        update.message.reply_text('Escriba su usuario y contraseña de la UCA de manera: USUARIO y CONSTRASEÑA.\n \t\tEjemplo: "u123321" y "c1123321"')
        return INPUT_ID_USER
    
def desconexion(update, context):
    main.desconexion_variable(update,context)
    update.message.reply_text('Conexión SIRE finalizada.')
    return ConversationHandler.END




# def student_go_back(update, context):
#     if(update.callback_query == None):
#         update.message.reply_text('Escriba sobre que desea tener información')
        
#     else:
#         query = update.callback_query
#         query.answer()
#         query.message.reply_text('Escriba sobre que desea tener información')
        
#     return SELECTED_STUDENT
    

# def pdi_go_back(update, context):
#     if(update.callback_query == None):
#         update.message.reply_text('Escriba sobre que desea tener información')
        
#     else:
#         query = update.callback_query
#         query.answer()
#         query.message.reply_text('Escriba sobre que desea tener información')
        
#     return SELECTED_PDI

# def pas_go_back(update, context):
#     if(update.callback_query == None):
#         update.message.reply_text('Escriba sobre que desea tener información')
        
#     else:
#         query = update.callback_query
#         query.answer()
#         query.message.reply_text('Escriba sobre que desea tener información')
        
#     return SELECTED_PAS

