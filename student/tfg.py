from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general

def start_tfg(update, context):
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Es el trabajo que hay que realizar pa terminar la carrera',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Reglamento de TFG/M y modelos', callback_data='tfg_reglamento')],
            [InlineKeyboardButton(text='Calendario de fechas', url='https://esingenieria.uca.es/wp-content/uploads/2021/09/Calendario-TFGM-de-la-Escuela-Superior-de-Ingenieria-de-la-Universidad-de-Cadiz.pdf')],
            [InlineKeyboardButton(text='Fechas reuniones ordinarias comisión de TFG/M', callback_data='tfg_fechas_reuniones')],
            [InlineKeyboardButton(text='Períodos de defensa aprobados por la comisión', callback_data='tfg_periodos_defensa')],
            [InlineKeyboardButton(text='Enlace a la página web de la escuela', url='https://esingenieria.uca.es/docencia/tfg-m/')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
        
        
def send_document(filename, chat):
    
    chat.send_document(
        document=open(filename,'rb')
    )
    
        
def callback_tfg_reglamento(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
            text = '¿Que documento quiere?',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Reglamento de Trabajos de Fin de Grado y Máster', callback_data='get_tfg_reglamento')],
                [InlineKeyboardButton(text='Portada externa', callback_data='get_tfg_portada_externa'),InlineKeyboardButton(text='Primera interna', callback_data='get_tfg_primera_interna'),InlineKeyboardButton(text='Segunda interna', callback_data='get_tfg_segunda_interna')],
                [InlineKeyboardButton(text='TFG/M-01: Propuesta de TFG/M', callback_data='get_TFG/01'),InlineKeyboardButton(text='TFG/M-02: Solicitud de asignación de TFG/M', callback_data='get_TFG/02')],
                [InlineKeyboardButton(text='TFG/M-03: Solicitud depresentación en otro idioma del TFG/M', callback_data='get_TFG/03'), InlineKeyboardButton(text='TFG/M-04: Autorización del director de TFG/M', callback_data='get_TFG/04')],
                [InlineKeyboardButton(text='TFG/M-05: Difsión pública del TFG/M', callback_data='get_TFG/05'), InlineKeyboardButton(text='TFG/M-06: Renuncia al nombramiento como miembro de tribunal de TFG/M', callback_data='get_TFG/06')],
                [InlineKeyboardButton(text='Volver', callback_data='inicio_tfg')]
            ])
        )
   


def get_tfg_reglamento(update, context):
    filename = 'files/Reglamento-TFGM-ESI.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)

def get_tfg_portada_externa(update, context):
    filename = 'files/Portada-externa.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
    
def get_tfg_primera_interna(update, context):
    filename = 'files/Primera-interna.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
    
def get_tfg_segunda_interna(update, context):
    filename = 'files/Segunda-interna.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
    


def get_TFG01(update, context):
    filename = 'files/TFG-M01.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
        
def get_TFG02(update, context):
    
    filename = 'files/TFG-M02.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
        
def get_TFG03(update, context):
    
    filename = 'files/TFG-M03.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
    
def get_TFG04(update, context):
    filename = 'files/TFG-M04.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
    
def get_TFG05(update, context):
    filename = 'files/TFG-M05.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)
    
def get_TFG06(update, context):
    filename = 'files/TFG-M06.pdf'
    
    if(update.callback_query == None):
        chat = update.message.chat
            
    else: 
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        
    send_document(filename, chat)    


def callback_tfg_fechas_reuniones(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'CURSO 2021/2022\n'
        ' Miércoles 6 de octubre, 12:00\n Miércoles 10 de noviembre, 12:00\n Jueves 2 de diciembre, 12:00\n Miércoles 12 de enero, 12:00\n' 
        ' Jueves 3 de febrero , 12:00\n Miércoles 16 de marzo, 12:00\n Lunes 18 de abril, 12:00\n Miércoles 11 de mayo, 12:00\n' 
        ' Miércoles 15 de junio, 12:00\n Miércoles 6 de julio, 12:00\n Miércoles 7 de septiembre, 12:00\n',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_tfg')]
        ])
    )
        


def callback_tfg_periodo_defensa(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
            text = 'CURSO 2021/2022\n'
                ' 18 al 22 de octubre de 2021\n 22 al 26 de noviembre de 2021\n 14 al 17 de diciembre de 2021\n 24 al 27 de enero de 2022\n' 
                ' 15 al 25 de febrero de 2022\n 28 de marzo al 1 de abril de 2022\n 26 de abril al 3 de mayo de 2022\n 23 al 27 de mayo de 2022\n' 
                ' 27 de junio al 1 de julio de 2022\n 18 al 22 de julio de 2022\n 19 al 30 de septiembre de 2022\n',
                reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Volver', callback_data='inicio_tfg')]
            ])
        )    