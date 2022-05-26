
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general

def student_timetable(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Horarios por grado',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://drive.google.com/file/d/10erEMmrPInT1dZtsKUO_oTGM4uJuuJ6p/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1R1hmjUpe4rvvDyMZIDyq9DJyzjaQip1D/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://drive.google.com/file/d/1LAPy94PVzCsAZAWeempjmR0XYjWndxfr/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1tN9gECQ3XhcF0ZbvjmC-fxeWBb1T_NqU/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://drive.google.com/file/d/1qdQzCfrnuM5b-Jcy5rrGZ8uYg-mA05f3/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://drive.google.com/file/d/1xAjcYsC7mRkx8dZ8k-vCA6a-7hcz_JBP/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://drive.google.com/file/d/1ZPI6ICyP97oOLuPE9rdwhLTy_r1kBHpB/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/17jjbGYBhNmAdGaYeS8Su33QYjcWavZ-8/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://drive.google.com/file/d/1bCwfIBbOsFCO6mcPsWipXac0an5CgA7H/view')],
            [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1XyDJl1W4wbi7EUi6ctmFmjUue8-Nqgoo/view')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
        
def student_timetable_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Timetables by degree',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://drive.google.com/file/d/10erEMmrPInT1dZtsKUO_oTGM4uJuuJ6p/view')],
            [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1R1hmjUpe4rvvDyMZIDyq9DJyzjaQip1D/view')],
            [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://drive.google.com/file/d/1LAPy94PVzCsAZAWeempjmR0XYjWndxfr/view')],
            [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://drive.google.com/file/d/1tN9gECQ3XhcF0ZbvjmC-fxeWBb1T_NqU/view')],
            [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://drive.google.com/file/d/1qdQzCfrnuM5b-Jcy5rrGZ8uYg-mA05f3/view')],
            [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://drive.google.com/file/d/1xAjcYsC7mRkx8dZ8k-vCA6a-7hcz_JBP/view')],
            [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://drive.google.com/file/d/1ZPI6ICyP97oOLuPE9rdwhLTy_r1kBHpB/view')],
            [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://drive.google.com/file/d/17jjbGYBhNmAdGaYeS8Su33QYjcWavZ-8/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://drive.google.com/file/d/1bCwfIBbOsFCO6mcPsWipXac0an5CgA7H/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Engineering Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1XyDJl1W4wbi7EUi6ctmFmjUue8-Nqgoo/view')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )      
        
def pdi_timetable(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Horarios por grado',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://drive.google.com/file/d/10erEMmrPInT1dZtsKUO_oTGM4uJuuJ6p/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1R1hmjUpe4rvvDyMZIDyq9DJyzjaQip1D/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://drive.google.com/file/d/1LAPy94PVzCsAZAWeempjmR0XYjWndxfr/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1tN9gECQ3XhcF0ZbvjmC-fxeWBb1T_NqU/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://drive.google.com/file/d/1qdQzCfrnuM5b-Jcy5rrGZ8uYg-mA05f3/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://drive.google.com/file/d/1xAjcYsC7mRkx8dZ8k-vCA6a-7hcz_JBP/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://drive.google.com/file/d/1ZPI6ICyP97oOLuPE9rdwhLTy_r1kBHpB/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/17jjbGYBhNmAdGaYeS8Su33QYjcWavZ-8/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://drive.google.com/file/d/1bCwfIBbOsFCO6mcPsWipXac0an5CgA7H/view')],
            [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1XyDJl1W4wbi7EUi6ctmFmjUue8-Nqgoo/view')],
            [InlineKeyboardButton(text='Volver', callback_data='PDI_spanish_go_back')]
        ])
    )

def pdi_timetable_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Timetables by degree',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://drive.google.com/file/d/10erEMmrPInT1dZtsKUO_oTGM4uJuuJ6p/view')],
            [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1R1hmjUpe4rvvDyMZIDyq9DJyzjaQip1D/view')],
            [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://drive.google.com/file/d/1LAPy94PVzCsAZAWeempjmR0XYjWndxfr/view')],
            [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://drive.google.com/file/d/1tN9gECQ3XhcF0ZbvjmC-fxeWBb1T_NqU/view')],
            [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://drive.google.com/file/d/1qdQzCfrnuM5b-Jcy5rrGZ8uYg-mA05f3/view')],
            [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://drive.google.com/file/d/1xAjcYsC7mRkx8dZ8k-vCA6a-7hcz_JBP/view')],
            [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://drive.google.com/file/d/1ZPI6ICyP97oOLuPE9rdwhLTy_r1kBHpB/view')],
            [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://drive.google.com/file/d/17jjbGYBhNmAdGaYeS8Su33QYjcWavZ-8/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://drive.google.com/file/d/1bCwfIBbOsFCO6mcPsWipXac0an5CgA7H/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Engineering Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1XyDJl1W4wbi7EUi6ctmFmjUue8-Nqgoo/view')],
            [InlineKeyboardButton(text='Back', callback_data='PDI_english_go_back')]
        ])
    )
       
def pas_timetable(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Horarios por grado',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://drive.google.com/file/d/10erEMmrPInT1dZtsKUO_oTGM4uJuuJ6p/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1R1hmjUpe4rvvDyMZIDyq9DJyzjaQip1D/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://drive.google.com/file/d/1LAPy94PVzCsAZAWeempjmR0XYjWndxfr/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1tN9gECQ3XhcF0ZbvjmC-fxeWBb1T_NqU/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://drive.google.com/file/d/1qdQzCfrnuM5b-Jcy5rrGZ8uYg-mA05f3/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://drive.google.com/file/d/1xAjcYsC7mRkx8dZ8k-vCA6a-7hcz_JBP/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://drive.google.com/file/d/1ZPI6ICyP97oOLuPE9rdwhLTy_r1kBHpB/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/17jjbGYBhNmAdGaYeS8Su33QYjcWavZ-8/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://drive.google.com/file/d/1bCwfIBbOsFCO6mcPsWipXac0an5CgA7H/view')],
            [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1XyDJl1W4wbi7EUi6ctmFmjUue8-Nqgoo/view')],
            [InlineKeyboardButton(text='Volver', callback_data='PAS_spanish_go_back')]
        ])
    )
    
def pas_timetable_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Timetables by degree',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://drive.google.com/file/d/10erEMmrPInT1dZtsKUO_oTGM4uJuuJ6p/view')],
            [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1R1hmjUpe4rvvDyMZIDyq9DJyzjaQip1D/view')],
            [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://drive.google.com/file/d/1LAPy94PVzCsAZAWeempjmR0XYjWndxfr/view')],
            [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://drive.google.com/file/d/1tN9gECQ3XhcF0ZbvjmC-fxeWBb1T_NqU/view')],
            [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://drive.google.com/file/d/1qdQzCfrnuM5b-Jcy5rrGZ8uYg-mA05f3/view')],
            [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://drive.google.com/file/d/1xAjcYsC7mRkx8dZ8k-vCA6a-7hcz_JBP/view')],
            [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://drive.google.com/file/d/1ZPI6ICyP97oOLuPE9rdwhLTy_r1kBHpB/view')],
            [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://drive.google.com/file/d/17jjbGYBhNmAdGaYeS8Su33QYjcWavZ-8/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://drive.google.com/file/d/1bCwfIBbOsFCO6mcPsWipXac0an5CgA7H/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Engineering Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1XyDJl1W4wbi7EUi6ctmFmjUue8-Nqgoo/view')],
            [InlineKeyboardButton(text='Back', callback_data='PAS_english_go_back')]
        ])
    )