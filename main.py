import webbrowser
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from general import timetable, exam_calendar
from student import tfg, global_evaluation, special_call, december_exams, group_assignment, practice, collaborating_students, compensation_evaluation, movilidad

# Menus

def first_menu(update, context):
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_idiom_spanish', callback=second_menu_spanish))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_idiom_english', callback=second_menu_english))
    
    if(update.callback_query == None):
        if(update.message.from_user.language_code == "es"):
            update.message.reply_text(
                text = '*Bienvenid@ al bot de Ordenación Académica de la ESI - UCA* \nSeleccione una opción',
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Español', callback_data='selected_idiom_spanish')],
                    [InlineKeyboardButton(text='Inglés', callback_data='selected_idiom_english')]
                ]),
                parse_mode='Markdown'
            )
        else:
            update.message.reply_text(
                text = '*Welcome to the ESI-UCA Academic Planning Bot* \nSelect an option',
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Spanish', callback_data='selected_idiom_spanish')],
                    [InlineKeyboardButton(text='English', callback_data='selected_idiom_english')]
                ]),
                parse_mode='Markdown'
            )
            
    else:
        query = update.callback_query
        query.answer()
        if(query.from_user.language_code == "es"):
            query.edit_message_text(
                text = '*Bienvenid@ al bot de Ordenación Académica de la ESI - UCA* \nSeleccione una opción',
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Español', callback_data='selected_idiom_spanish')],
                    [InlineKeyboardButton(text='Inglés', callback_data='selected_idiom_english')]
                ]),
                parse_mode='Markdown'
            )
        else:
            query = update.callback_query
            query.answer()
            query.edit_message_text(
                text = '*Welcome to the ESI-UCA Academic Planning Bot* \nSelect an option',
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Spanish', callback_data='selected_idiom_spanish')], 
                    [InlineKeyboardButton(text='English', callback_data='selected_idiom_english')]
                ]),
                parse_mode='Markdown'
            )

def second_menu_spanish(update, context):
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_student_spanish', callback=menu_estudiante))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_PDI_spanish', callback=menu_PDI))
    dp.add_handler(CallbackQueryHandler(pattern='selected_PAS_spanish', callback=menu_PAS))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_second_menu_go_back', callback=first_menu))
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Seleccione que rol quiere consultar*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Estudiante', callback_data='selected_student_spanish')],
            [InlineKeyboardButton(text='PDI', callback_data='selected_PDI_spanish')],
            [InlineKeyboardButton(text='PAS', callback_data='selected_PAS_spanish')],
            [InlineKeyboardButton(text='Volver', callback_data='selected_second_menu_go_back')]
        ]),
        parse_mode='Markdown'
    )  
    
def second_menu_english(update, context):
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_student_english', callback=student_menu_english))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_PDI_english', callback=PDI_menu_english))
    dp.add_handler(CallbackQueryHandler(pattern='selected_PAS_english', callback=PAS_menu_english))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_second_menu_go_back', callback=first_menu))
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Select which role you want to consult*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Student', callback_data='selected_student_english')],
            [InlineKeyboardButton(text='PDI', callback_data='selected_PDI_english')],
            [InlineKeyboardButton(text='PAS', callback_data='selected_PAS_english')],
            [InlineKeyboardButton(text='Back', callback_data='selected_second_menu_go_back')]
        ]),
        parse_mode='Markdown'
    )  


# STUDENT
def menu_estudiante(update, context):
    
    # Horarios
    # dp.add_handler(CommandHandler('horarios', horarios.start_horarios))
    dp.add_handler(CallbackQueryHandler(pattern='student_timetable', callback=timetable.student_timetable))
    
    
    # Calendario de examenes
    dp.add_handler(CallbackQueryHandler(pattern='student_exam_calendar', callback=exam_calendar.student_exam_calendar))
    
    
    # TFG
    # dp.add_handler(CommandHandler('tfg', tfg.start_tfg))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_tfg', callback=tfg.start_tfg))
    dp.add_handler(CallbackQueryHandler(pattern='tfg_reglamento', callback=tfg.callback_tfg_reglamento))
    dp.add_handler(CallbackQueryHandler(pattern='tfg_fechas_reuniones', callback=tfg.callback_tfg_fechas_reuniones))
    dp.add_handler(CallbackQueryHandler(pattern='tfg_periodos_defensa', callback=tfg.callback_tfg_periodo_defensa))
    
    # Documentos TFG
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_reglamento', callback=tfg.get_tfg_reglamento))
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_portada_externa', callback=tfg.get_tfg_portada_externa))
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_primera_interna', callback=tfg.get_tfg_primera_interna))
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_segunda_interna', callback=tfg.get_tfg_segunda_interna))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/01', callback=tfg.get_TFG01))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/02', callback=tfg.get_TFG02))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/03', callback=tfg.get_TFG03))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/04', callback=tfg.get_TFG04))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/05', callback=tfg.get_TFG05))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/06', callback=tfg.get_TFG06))
    
    

    # Evaluación global
    # dp.add_handler(CommandHandler('evaluacion_global', evaluacion_global.start_evaluacion_global))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_evaluacion_global', callback=global_evaluation.start_evaluacion_global))
    dp.add_handler(CallbackQueryHandler(pattern='evaluacion_global_periodo', callback=global_evaluation.callback_evaluacion_global_periodo))


    #Llamamiento Especial
    # dp.add_handler(CommandHandler('llamamiento_especial', llamamiento_especial.start_llamamiento_especial))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_llamamiento_especial', callback=special_call.start_llamamiento_especial))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_periodo', callback=special_call.callback_llamamiento_especial_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_requisitos', callback=special_call.callback_llamamiento_especial_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_examenes', callback=special_call.callback_llamamiento_especial_examenes))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_presentarmeSinFormulario', callback=special_call.callback_llamamiento_especial_presentarmeSinFormulario))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_ordinaria', callback=special_call.callback_llamamiento_especial_ordinaria))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_sino_coincide', callback=special_call.callback_llamamiento_especial_sino_coincide))

    # Convocatoria Diciembre
    # dp.add_handler(CommandHandler('convocatoria_diciembre', convocatoria_diciembre.start_conv_diciembre))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_conv_diciembre', callback=december_exams.start_conv_diciembre))
    dp.add_handler(CallbackQueryHandler(pattern='conv_diciembre_periodo', callback=december_exams.callback_conv_diciembre_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='conv_diciembre_requisitos', callback=december_exams.callback_conv_diciembre_requisitos))


    # Asignacion de grupos
    # dp.add_handler(CommandHandler('asignacion_grupos', asignacion_grupos.start_asignacion_grupos))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_group_assignment', callback=group_assignment.start_group_assignment))
    
    
    # Practicas
    # dp.add_handler(CallbackQueryHandler(pattern='practicas_convalidar', callback=practice.callback_practicas_convalidar))
    # dp.add_handler(CallbackQueryHandler(pattern='practicas_diferencias', callback=practice.callback_practicas_diferencias))
    
    dp.add_handler(CallbackQueryHandler(pattern='start_practice', callback=practice.start_practicas))
      
    # Practicas curriculares
    # dp.add_handler(CommandHandler('practicas_curriculares', practicas.start_practicas_curriculares))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_practicas_curriculares', callback=practice.start_practicas_curriculares))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_duracion', callback=practice.callback_practicas_curriculares_duracion))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_retribucion', callback=practice.callback_practicas_curriculares_retribucion))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_ayuda_economica', callback=practice.callback_practicas_curriculares_ayuda_economica))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_localidad', callback=practice.callback_practicas_curriculares_localidad))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_numero', callback=practice.callback_practicas_curriculares_numero))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_periodo', callback=practice.callback_practicas_curriculares_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_convalidar', callback=practice.callback_practicas_curriculares_convalidar))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_curriculares_diferencias', callback=practice.callback_practicas_curriculares_diferencias))
      
    # Practicas extracurriculares
    # dp.add_handler(CommandHandler('practicas_extracurriculares', practicas.start_practicas_extracurriculares))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_practicas_extracurriculares', callback=practice.start_practicas_extracurriculares))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_duracion', callback=practice.callback_practicas_extracurriculares_duracion))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_retribucion', callback=practice.callback_practicas_extracurriculares_retribucion))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_ayuda_economica', callback=practice.callback_practicas_extracurriculares_ayuda_economica))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_beca', callback=practice.callback_practicas_extracurriculares_beca))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_encontrar', callback=practice.callback_practicas_extracurriculares_encontrar))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_localidad', callback=practice.callback_practicas_extracurriculares_localidad))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_numero', callback=practice.callback_practicas_extracurriculares_numero))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_requisitos', callback=practice.callback_practicas_extracurriculares_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_periodo', callback=practice.callback_practicas_extracurriculares_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_vacaciones', callback=practice.callback_practicas_extracurriculares_vacaciones))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_recuperar_dias', callback=practice.callback_practicas_extracurriculares_recuperar_dias))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_convalidar', callback=practice.callback_practicas_extracurriculares_convalidar))
    dp.add_handler(CallbackQueryHandler(pattern='practicas_extracurriculares_diferencias', callback=practice.callback_practicas_extracurriculares_diferencias))
    
    
    # Movilidad
    dp.add_handler(CallbackQueryHandler(pattern='inicio_movilidad', callback=movilidad.start_movilidad))
    dp.add_handler(CallbackQueryHandler(pattern='movilidad_otras_movilidades', callback=movilidad.callback_movilidad_otras_movilidades))
    
    
    # Alumnos Colaboradores
    dp.add_handler(CallbackQueryHandler(pattern='student_collaborating_students', callback=collaborating_students.student_collaborating_students))
    
    
    # Evaluacion por compensacion
    dp.add_handler(CallbackQueryHandler(pattern='start_compensacion', callback=compensation_evaluation.start_compensacion))

    dp.add_handler(CallbackQueryHandler(pattern='inicio_compensacion_habilitantes', callback=compensation_evaluation.start_compensacion_habilitantes))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_habilitantes_periodo', callback=compensation_evaluation.callback_compensacion_habilitantes_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_habilitantes_requisitos', callback=compensation_evaluation.callback_compensacion_habilitantes_requisitos))

    dp.add_handler(CallbackQueryHandler(pattern='inicio_comnpensacion_no_habilitantes', callback=compensation_evaluation.start_compensacion_no_habilitantes))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_periodo', callback=compensation_evaluation.callback_compensacion_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_requisitos', callback=compensation_evaluation.callback_compensacion_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_req_especificos', callback=compensation_evaluation.callback_compensacion_req_especificos))
    
    # dp.add_handler(CallbackQueryHandler(pattern='student_spanish_compensacion_go_back', callback=compensation_evaluation.callback_compensacion_req_especificos))
    
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='student_spanish_go_back', callback=menu_estudiante))
    
    dp.add_handler(CallbackQueryHandler(pattern='student_menu_spanish_go_back', callback=second_menu_spanish))
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = ' *Menú Estudiante*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Horarios', callback_data='student_timetable'),InlineKeyboardButton(text='Calendarios de exámenes', callback_data='student_exam_calendar')],
            [InlineKeyboardButton(text='TFG/M', callback_data='inicio_tfg'), InlineKeyboardButton(text='Tutorías', url='https://tutorias.uca.es/tutorias/')],
            [InlineKeyboardButton(text='Evaluación global', callback_data='inicio_evaluacion_global'), InlineKeyboardButton(text='Llamamiento especial', callback_data='inicio_llamamiento_especial')],
            [InlineKeyboardButton(text='Convocatoria diciembre', callback_data='inicio_conv_diciembre'),InlineKeyboardButton(text='Asignación de grupos', callback_data='inicio_group_assignment')],
            [InlineKeyboardButton(text='Prácticas', callback_data='start_practice'), InlineKeyboardButton(text='Movilidad', callback_data='inicio_movilidad')],
            [InlineKeyboardButton(text='Alumnos colaboradores', callback_data='student_collaborating_students'), InlineKeyboardButton(text='Evaluación por compensación', callback_data='start_compensacion')],
            [InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/'), InlineKeyboardButton(text='Expediente académico', url='https://portalservicios.uca.es/ServiciosApp/')],
            [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion-estudiantes/')],
            [InlineKeyboardButton(text='Volver', callback_data='student_menu_spanish_go_back')]
        ]),
        parse_mode='Markdown'
    )

def student_menu_english(update, context):
     # Horarios
    dp.add_handler(CallbackQueryHandler(pattern='student_timetable_english', callback=timetable.student_timetable_english))
    
    # Calendario de examenes
    dp.add_handler(CallbackQueryHandler(pattern='student_exam_calendar_english', callback=exam_calendar.student_exam_calendar_english))
    
    # TFG
    dp.add_handler(CallbackQueryHandler(pattern='tfg_start_english', callback=tfg.tfg_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='tfg_reglamento_english', callback=tfg.callback_tfg_reglamento_english))
    dp.add_handler(CallbackQueryHandler(pattern='tfg_fechas_reuniones_english', callback=tfg.callback_tfg_fechas_reuniones_english))
    dp.add_handler(CallbackQueryHandler(pattern='tfg_periodos_defensa_english', callback=tfg.callback_tfg_periodo_defensa_english))
    
    # Documentos TFG
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_reglamento', callback=tfg.get_tfg_reglamento))
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_portada_externa', callback=tfg.get_tfg_portada_externa))
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_primera_interna', callback=tfg.get_tfg_primera_interna))
    dp.add_handler(CallbackQueryHandler(pattern='get_tfg_segunda_interna', callback=tfg.get_tfg_segunda_interna))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/01', callback=tfg.get_TFG01))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/02', callback=tfg.get_TFG02))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/03', callback=tfg.get_TFG03))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/04', callback=tfg.get_TFG04))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/05', callback=tfg.get_TFG05))
    dp.add_handler(CallbackQueryHandler(pattern='get_TFG/06', callback=tfg.get_TFG06))
    

    # Evaluación global
    dp.add_handler(CallbackQueryHandler(pattern='global_assessment_start_english', callback=global_evaluation.global_assessment_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='global_assessment_periodo_english', callback=global_evaluation.callback_global_assessment_periodo_english))


    #Llamamiento Especial
    dp.add_handler(CallbackQueryHandler(pattern='special_call_start_english', callback=special_call.special_call_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='special_call_periodo_english', callback=special_call.callback_special_call_periodo_english))
    dp.add_handler(CallbackQueryHandler(pattern='special_call_examenes_english', callback=special_call.callback_special_call_examenes_english))
    dp.add_handler(CallbackQueryHandler(pattern='special_call_requisitos_english', callback=special_call.callback_special_call_requisitos_english))
    dp.add_handler(CallbackQueryHandler(pattern='special_call_presentarmeSinFormulario_english', callback=special_call.callback_special_call_presentarmeSinFormulario_english))
    dp.add_handler(CallbackQueryHandler(pattern='special_call_ordinaria_english', callback=special_call.callback_special_call_ordinaria_english))
    dp.add_handler(CallbackQueryHandler(pattern='special_call_sino_coincide_english', callback=special_call.callback_special_call_sino_coincide_english))

    # Convocatoria Diciembre
    dp.add_handler(CallbackQueryHandler(pattern='december_call_start_english', callback=december_exams.december_call_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='december_call_periodo_english', callback=december_exams.callback_december_call_periodo_english))
    dp.add_handler(CallbackQueryHandler(pattern='december_call_requisitos_english', callback=december_exams.callback_december_call_requisitos_english))


    # Asignacion de grupos
    dp.add_handler(CallbackQueryHandler(pattern='group_assignment_start_english', callback=group_assignment.group_assignment_start_english))
    
    
    # Practicas
    dp.add_handler(CallbackQueryHandler(pattern='practice_start_english', callback=practice.practice_start_english))
      
    # Practicas curriculares
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_start_english', callback=practice.practice_curriculares_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_duracion', callback=practice.callback_practice_curriculares_duracion))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_retribucion', callback=practice.callback_practice_curriculares_retribucion))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_ayuda_economica', callback=practice.callback_practice_curriculares_ayuda_economica))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_localidad', callback=practice.callback_practice_curriculares_localidad))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_numero', callback=practice.callback_practice_curriculares_numero))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_periodo', callback=practice.callback_practice_curriculares_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_convalidar', callback=practice.callback_practice_curriculares_convalidar))
    dp.add_handler(CallbackQueryHandler(pattern='practice_curriculares_diferencias', callback=practice.callback_practice_curriculares_diferencias))
      
    # Practicas extracurriculares
    # dp.add_handler(CommandHandler('practicas_extracurriculares', practicas.start_practicas_extracurriculares))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_start_english', callback=practice.practice_extracurriculares_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_duracion', callback=practice.callback_practice_extracurriculares_duracion))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_retribucion', callback=practice.callback_practice_extracurriculares_retribucion))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_ayuda_economica', callback=practice.callback_practice_extracurriculares_ayuda_economica))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_beca', callback=practice.callback_practice_extracurriculares_beca))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_encontrar', callback=practice.callback_practice_extracurriculares_encontrar))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_localidad', callback=practice.callback_practice_extracurriculares_localidad))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_numero', callback=practice.callback_practice_extracurriculares_numero))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_requisitos', callback=practice.callback_practice_extracurriculares_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_periodo', callback=practice.callback_practice_extracurriculares_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_vacaciones', callback=practice.callback_practice_extracurriculares_vacaciones))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_recuperar_dias', callback=practice.callback_practice_extracurriculares_recuperar_dias))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_convalidar', callback=practice.callback_practice_extracurriculares_convalidar))
    dp.add_handler(CallbackQueryHandler(pattern='practice_extracurriculares_diferencias', callback=practice.callback_practice_extracurriculares_diferencias))
    
    
    
    # Movilidad
    dp.add_handler(CallbackQueryHandler(pattern='mobility_start_english', callback=movilidad.mobility_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='mobility_otras_movilidades_english', callback=movilidad.callback_mobility_otras_movilidades_english))
    

    # Alumnos Colaboradores
    dp.add_handler(CallbackQueryHandler(pattern='collaborating_students_start_english', callback=collaborating_students.collaborating_students_start_english))
    
    
    # Evaluacion por compensacion
    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_start_english', callback=compensation_evaluation.compensation_evaluation_start_english))

    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_qualifying_english', callback=compensation_evaluation.compensation_evaluation_qualifying_english))
    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_qualifying_periodo_english', callback=compensation_evaluation.callback_compensation_evaluation_qualifying_periodo_english))
    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_qualifying_requisitos_english', callback=compensation_evaluation.callback_compensation_evaluation_qualifying_requisitos_english))

    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_nonqualifying_english', callback=compensation_evaluation.compensation_evaluation_nonqualifying_english))
    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_nonqualifying_periodo_english', callback=compensation_evaluation.callback_compensation_evaluation_nonqualifying_periodo_english))
    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_nonqualifying_requisitos_english', callback=compensation_evaluation.callback_compensation_evaluation_nonqualifying_requisitos_english))
    dp.add_handler(CallbackQueryHandler(pattern='compensation_evaluation_nonqualifying_especificos_english', callback=compensation_evaluation.callback_compensation_evaluation_nonqualifying_requisitos_especificos_english))
    
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='student_english_go_back', callback=student_menu_english))
    dp.add_handler(CallbackQueryHandler(pattern='student_menu_english_go_back', callback=second_menu_english))
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = ' *Student menu*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='ESI news', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Timetables', callback_data='student_timetable_english'),InlineKeyboardButton(text='Exam calendar', callback_data='student_exam_calendar_english')],
            [InlineKeyboardButton(text='TFG/M', callback_data='tfg_start_english'), InlineKeyboardButton(text='Tutorials', url='https://tutorias.uca.es/tutorias/')],
            [InlineKeyboardButton(text='Global assessment', callback_data='global_assessment_start_english'), InlineKeyboardButton(text='Special call', callback_data='special_call_start_english')],
            [InlineKeyboardButton(text='December exams', callback_data='december_call_start_english'),InlineKeyboardButton(text='Group assignment', callback_data='group_assignment_start_english')],
            [InlineKeyboardButton(text='Internships', callback_data='practice_start_english'), InlineKeyboardButton(text='Mobility', callback_data='mobility_start_english')],
            [InlineKeyboardButton(text='Collaborating students', callback_data='collaborating_students_start_english'), InlineKeyboardButton(text='Assessment by compensation', callback_data='compensation_evaluation_start_english')],
            [InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/'), InlineKeyboardButton(text='Academic records', url='https://portalservicios.uca.es/ServiciosApp/')],
            [InlineKeyboardButton(text='ESI Academic Planning website', url='https://esingenieria.uca.es/ordenacion-estudiantes/')],
            [InlineKeyboardButton(text='Back', callback_data='student_menu_english_go_back')]
        ]),
        parse_mode='Markdown'
    )

# PDI
def menu_PDI(update, context):
    
    # Horarios
    dp.add_handler(CallbackQueryHandler(pattern='pdi_timetable', callback=timetable.pdi_timetable))
    
    # Calendario de exámenes
    dp.add_handler(CallbackQueryHandler(pattern='pdi_exam_calendar', callback=exam_calendar.pdi_exam_calendar))
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='PDI_spanish_go_back', callback=menu_PDI))
    
    dp.add_handler(CallbackQueryHandler(pattern='PDI_menu_spanish_go_back', callback=second_menu_spanish))
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Menú PDI*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Horarios', callback_data='pdi_timetable'), InlineKeyboardButton(text='Calendarios de exámenes', callback_data='pdi_exam_calendar')],
            [InlineKeyboardButton(text='Calendario Académico', url='https://esingenieria.uca.es/wp-content/uploads/2021/05/Calendario-Academico-2021-22-ESI.pdf')],
            [InlineKeyboardButton(text='Formulario de incidencia docente', url='https://esingenieria.uca.es/ordenacion-pdi/'), InlineKeyboardButton(text='Horarios por áreas', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Guía para los programas docentes', url='https://esingenieria.uca.es/wp-content/uploads/2021/06/Indicaciones_Programas_Docentes_ESI%20_v2.pdf'), InlineKeyboardButton(text='Acceso a GOA', url='https://goa.uca.es/')],
            [InlineKeyboardButton(text='Acceso al Sistema de Información', url='https://sistemadeinformacion.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Volver', callback_data='PDI_menu_spanish_go_back')]
        ]),
        parse_mode='Markdown'
    )
    
def PDI_menu_english(update, context):
     # Horarios
    dp.add_handler(CallbackQueryHandler(pattern='pdi_timetable_english', callback=timetable.pdi_timetable_english))
    
    # Calendario de exámenes
    dp.add_handler(CallbackQueryHandler(pattern='pdi_exam_calendar_english', callback=exam_calendar.pdi_exam_calendar_english))
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='PDI_english_go_back', callback=PDI_menu_english))
    
    dp.add_handler(CallbackQueryHandler(pattern='PDI_menu_english_go_back', callback=second_menu_english))
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*PDI menu*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='ESI news', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Timetables', callback_data='pdi_timetable_english'), InlineKeyboardButton(text='Exam calendar', callback_data='pdi_exam_calendar_english')],
            [InlineKeyboardButton(text='Academic Calendar', url='https://esingenieria.uca.es/wp-content/uploads/2021/05/Calendario-Academico-2021-22-ESI.pdf')],
            [InlineKeyboardButton(text='Teacher  Incident Form', url='https://esingenieria.uca.es/ordenacion-pdi/'), InlineKeyboardButton(text='Timetables by areas', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Guide to teaching programmes', url='https://esingenieria.uca.es/wp-content/uploads/2021/06/Indicaciones_Programas_Docentes_ESI%20_v2.pdf'), InlineKeyboardButton(text='Access to GOA', url='https://goa.uca.es/')],
            [InlineKeyboardButton(text='Access to the Information System', url='https://sistemadeinformacion.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='ESI Academic Planning website', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Back', callback_data='PDI_menu_english_go_back')]
        ]),
        parse_mode='Markdown'
    )



# PAS
def menu_PAS(update, context):
    
    # Horarios
    dp.add_handler(CallbackQueryHandler(pattern='pas_timetable', callback=timetable.pas_timetable))
    
    # Calendario de exámenes
    dp.add_handler(CallbackQueryHandler(pattern='pas_exam_calendar', callback=exam_calendar.pas_exam_calendar))
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='PAS_spanish_go_back', callback=menu_PAS))
    
    dp.add_handler(CallbackQueryHandler(pattern='PAS_menu_spanish_go_back', callback=second_menu_spanish))
    

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Menú PAS*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Horarios', callback_data='pas_timetable'), InlineKeyboardButton(text='Calendarios de exámenes', callback_data='pas_exam_calendar')],
            [InlineKeyboardButton(text='CAU de Infraestructuras', url='https://cau-infraestructuras.uca.es/cau/index.do')],
            [InlineKeyboardButton(text='CAU de Reparación', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M01'),InlineKeyboardButton(text='CAU de Climatización', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M07')],
            [InlineKeyboardButton(text='Directorio', url='https://directorio.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Volver', callback_data='PAS_menu_spanish_go_back')]
        ]),
        parse_mode='Markdown'
    )

    
def PAS_menu_english(update, context):
    
    # Horarios
    dp.add_handler(CallbackQueryHandler(pattern='pas_timetable_english', callback=timetable.pas_timetable_english))
    
    # Calendario de exámenes
    dp.add_handler(CallbackQueryHandler(pattern='pas_exam_calendar_english', callback=exam_calendar.pas_exam_calendar_english))
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='PAS_english_go_back', callback=PAS_menu_english))
    
    dp.add_handler(CallbackQueryHandler(pattern='PAS_menu_english_go_back', callback=second_menu_english))
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*PAS menu*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='ESI news', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Timetables', callback_data='pas_timetable_english'), InlineKeyboardButton(text='Exam calendar', callback_data='pas_exam_calendar_english')],
            [InlineKeyboardButton(text='Infrastructure CAU', url='https://cau-infraestructuras.uca.es/cau/index.do')],
            [InlineKeyboardButton(text='Repairs CAU', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M01'),InlineKeyboardButton(text='Air conditioning CAU', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M07')],
            [InlineKeyboardButton(text='Directory', url='https://directorio.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='ESI Academic Planning website', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Back', callback_data='PAS_menu_english_go_back')]
        ]),
        parse_mode='Markdown'
    )


###########################################################################

if __name__ == '__main__':
    
    updater = Updater(token='2049537211:AAERyXIxQUMicwINmZqy1tAXai-G1EgJtKY', use_context=True)

    dp = updater.dispatcher
    
    # dp.add_handler(MessageHandler(Filters.text, first_menu))
    
    dp.add_handler(CommandHandler('start', first_menu))
    
    updater.start_polling()
    updater.idle()