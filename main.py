import webbrowser
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# Para sire
import pycurl
import urllib
import re
import io
import lxml
import getpass

import general, timetable, exam_calendar, tutorships

from student import tfg, global_evaluation, special_call, december_exams, group_assignment, practice, collaborating_students, compensation_evaluation, movilidad

import SIRE_info

# import Novell.Directory.Ldap

# import ldap
# import json






# id_user = ' '
# pw_user = ' '
      
      
STUDENT_TUTORSHIPS = map(chr, range(1))
    
    
# def conectar_ldap(user, password, update, context):
#     print("Intentando conectar al Usuario: "+user)
      
#     ldapHost = "ldap://ldap.uca.es"
#     LDAP_BASE_DN = "CN="+user+",dc=uca,dc=es"
#     LDAP_ATTRS = ["mail", "ou"]
#     ldap_filter = "tipodocumento=NIF"
    
#     loginDN = "CN="+user+",dc=uca,dc=es"
    
#     # ldapPort = 389
    
    
    
#     # ldapHost = "ldap://ldap.forumsys.com"
#     # LDAP_BASE_DN = "cn=read-only-admin,dc=example,dc=com"
#     # LDAP_ATTRS = ["ou"]
#     # ldap_filter = "(uid=%s)" % user
    
#     try:
#         # print("guay")
#         ldap_client = ldap.initialize(ldapHost)
#         ldap_client.set_option(ldap.OPT_PROTOCOL_VERSION,3)
#         # print("mola")
#         ldap_client.simple_bind_s(loginDN,password)
#         # ldap_client.simple_bind(user,password)
#         # print("del tiron")
#     except ldap.INVALID_CREDENTIALS:
#         print("Usuario o contraseña incorrectos")
#         ldap_client.unbind()
#         update.message.reply_text('Usuario o contraseña incorrectos')
#         return "ERROR"
#         # return json.dumps('Usuario o contraseña incorrectos')
#     except ldap.SERVER_DOWN:
#         print("La conexión con la UCA no se puede llevar a cabo en este momento")
#         update.message.reply_text('La conexión con la UCA no se puede llevar a cabo en este momento')
#         return "ERROR"
#         # return json.dumps('La conexión con la UCA no se puede llevar a cabo en este momento')
    
#     # user_info = json.dumps(ldap_client.search_s(LDAP_BASE_DN, ldap.SCOPE_SUBTREE, ldap_filter, LDAP_ATTRS))
    
#     user_info = ldap_client.search_s(LDAP_BASE_DN, ldap.SCOPE_BASE, ldap_filter, LDAP_ATTRS)
    
#     # print("Informacion de la LDAP   "+user_info)
    
#     # print(user_info)
#     # rol = user_info[0][1]["ou"]
#     # print(rol)
#     # print(rol[0])
    
#     rol = user_info[0][1]["ou"][0]
    
#     if(rol == b'Alumnos'):
#         print("Funciona")
#         return "Alumnos"
#     else:
#         print("ERROR")
#         return "MAL"
      
      
def input_id_user(update, context):
    
    if(general.flag_login == 0):
        general.flag_login = 1
        usuario = update.message.text.split(' y ')
        if(len(usuario) == 2):
        
            general.user_id = usuario[0] 
            general.user_pw = usuario[1] 
        
            if(usuario[0] == '1' or usuario[0] == '2' or usuario[0] == '3'):
                
                
                
                if(usuario[0] == '1'):
                    print('ESTUDIANTE')
                    update.message.reply_text('Escriba sobre que desea tener información en formato: Espacio-Dia-Mes-Año \n Por ejemplo: B02-11-05-2022')
                    return general.CONSULT_SIRE
                
                elif(usuario[0] == '2'):
                    print('PDI')
                    update.message.reply_text('Escriba sobre que desea tener información')
                    return general.CONSULT_SIRE
                
                elif(usuario[0] == '3'):
                    print('PAS')
                    update.message.reply_text('Escriba sobre que desea tener información')
                    return general.CONSULT_SIRE
            
            else:
                
                # rol = conectar_ldap(usuario[0],usuario[1], update, context)
                # if(rol == "Alumnos"):
                #     print('ESTUDIANTE')
                #     update.message.reply_text('Escriba sobre que desea tener información')
                #     return general.CONSULT_SIRE
                
                # else:
                    general.start_sire(update, context) 
        
        else:
            update.message.reply_text('Por favor, introduzca los datos de manera que se le explica en el mensaje')
            general.start_sire(update, context)
    else:
        update.message.reply_text('Ahora mismo no podemos conectarte, intentelo de nuevo mas tarde')
        return ConversationHandler.END
        
        
         
    # update.message.reply_text('Usuario: '+usuario[0]+' y  Contraseña: '+usuario[1]+'\n\n Escriba OK para continuar con la validación. \n\n Para poner de nuevo usuario y contraseña escriba otra cosa')
    
    # updater.private_key = usuario[0]
    # updater.private_key_password = usuario[1]
    
    # return general.SELECT_TYPE_USER
    
def desconexion_variable(update, context):
    general.flag_login = 0
    

def input_pw_user(update, context):
    
    # global pw_user
    
    updater.private_key_password = update.message.text
    
    print('Contrasenna: '+ updater.private_key_password +' ID USER = '+ updater.private_key )
   
    update.message.reply_text('Escriba OK para continuar con la validación. \n\n Para poner de nuevo usuario y contraseña escriba otra cosa')
    
    # return ConversationHandler.END
    return general.SELECT_TYPE_USER

def select_type_user(update, context):
    print('Usuario conectado: ' + updater.private_key)
    # print('Usuario de telegram: '+update.id)
    print('CHAT:')
    print(update.message.chat)
    print('USER:')
    # print(update.message.user)
    
    message = update.message.text.upper()
    
    if(message.find("OK") > -1):
        if(updater.private_key == '2'):
            print('HOLA')
            update.message.reply_text('Escriba sobre que desea tener información')
            return general.SELECTED_PDI
        else:
            print('ADIOS')
            update.message.reply_text('Escriba sobre que desea tener información')
            return general.SELECTED_STUDENT
    else:
        update.message.reply_text('Escriba de nuevo su usuario y contraseña')
        return general.INPUT_ID_USER
        

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
    
    
    # Alumnos Colaboradores
    
    dp.add_handler(CallbackQueryHandler(pattern='student_collaborating_students', callback=collaborating_students.student_collaborating_students))
    
    
    # Evaluacion por compensacion
    # dp.add_handler(CommandHandler('compensacion', evaluacion_compensacion.start_compensacion))
    dp.add_handler(CallbackQueryHandler(pattern='start_compensacion', callback=compensation_evaluation.start_compensacion))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_comnpensacion_no_habilitantes', callback=compensation_evaluation.start_compensacion_no_habilitantes))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_periodo', callback=compensation_evaluation.callback_compensacion_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_requisitos', callback=compensation_evaluation.callback_compensacion_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_req_especificos', callback=compensation_evaluation.callback_compensacion_req_especificos))
    
    # dp.add_handler(CallbackQueryHandler(pattern='student_spanish_compensacion_go_back', callback=compensation_evaluation.callback_compensacion_req_especificos))
    
    
    
    # Movilidad
    dp.add_handler(CallbackQueryHandler(pattern='inicio_movilidad', callback=movilidad.start_movilidad))
    dp.add_handler(CallbackQueryHandler(pattern='movilidad_otras_movilidades', callback=movilidad.movilidad_otras_movilidades))



    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='student_spanish_go_back', callback=menu_estudiante))
    
    # Tutorias
    dp.add_handler(CallbackQueryHandler(pattern='student_start_tutorships', callback=tutorships.student_start_tutorships))
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='student_spanish_go_back', callback=menu_estudiante))
    
    dp.add_handler(CallbackQueryHandler(pattern='student_menu_spanish_go_back', callback=second_menu_spanish))
    
    if(update.callback_query == None):

        update.message.reply_text(
            text = ' *Bienvenid@ al menu Estudiante*',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
                [InlineKeyboardButton(text='Horarios', callback_data='student_timetable'),InlineKeyboardButton(text='Calendarios de exámenes', callback_data='student_exam_calendar')],
                [InlineKeyboardButton(text='TFG/M', callback_data='inicio_tfg'), InlineKeyboardButton(text='Tutorías', callback_data='student_start_tutorships')],
                [InlineKeyboardButton(text='Evaluación global', callback_data='inicio_evaluacion_global'), InlineKeyboardButton(text='Llamamiento especial', callback_data='inicio_llamamiento_especial')],
                [InlineKeyboardButton(text='Convocatoria diciembre', callback_data='inicio_conv_diciembre'),InlineKeyboardButton(text='Asignación de grupos', callback_data='inicio_group_assignment')],
                [InlineKeyboardButton(text='Prácticas', callback_data='start_practice'), InlineKeyboardButton(text='Movilidad', callback_data='inicio_movilidad')],
                [InlineKeyboardButton(text='Alumnos colaboradores', callback_data='student_collaborating_students'), InlineKeyboardButton(text='Evaluación por compensación', callback_data='start_compensacion')],
                [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion/')],
                [InlineKeyboardButton(text='Volver', callback_data='student_menu_spanish_go_back')]
            ]),
            parse_mode='Markdown'
        )
    
    else: 
    
        query = update.callback_query
        query.answer()
        query.edit_message_text(
            text = ' *Bienvenid@ al menu Estudiante*',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
                [InlineKeyboardButton(text='Horarios', callback_data='student_timetable'),InlineKeyboardButton(text='Calendarios de exámenes', callback_data='student_exam_calendar')],
                [InlineKeyboardButton(text='TFG/M', callback_data='inicio_tfg'), InlineKeyboardButton(text='Tutorías', callback_data='student_start_tutorships')],
                [InlineKeyboardButton(text='Evaluación global', callback_data='inicio_evaluacion_global'), InlineKeyboardButton(text='Llamamiento especial', callback_data='inicio_llamamiento_especial')],
                [InlineKeyboardButton(text='Convocatoria diciembre', callback_data='inicio_conv_diciembre'),InlineKeyboardButton(text='Asignación de grupos', callback_data='inicio_group_assignment')],
                [InlineKeyboardButton(text='Prácticas', callback_data='start_practice'), InlineKeyboardButton(text='Movilidad', callback_data='inicio_movilidad')],
                [InlineKeyboardButton(text='Alumnos colaboradores', callback_data='student_collaborating_students'), InlineKeyboardButton(text='Evaluación por compensación', callback_data='start_compensacion')],
                [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion/')],
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
    
    # Tutorias
    dp.add_handler(CallbackQueryHandler(pattern='student_start_tutorships_english', callback=tutorships.student_start_tutorships_english))
    

    # Evaluación global
    dp.add_handler(CallbackQueryHandler(pattern='global_assessment_start_english', callback=global_evaluation.global_assessment_start_english))
    dp.add_handler(CallbackQueryHandler(pattern='global_assessment_periodo_english', callback=global_evaluation.callback_global_assessment_periodo_english))


    #Llamamiento Especial
    # dp.add_handler(CommandHandler('llamamiento_especial', llamamiento_especial.start_llamamiento_especial))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_llamamiento_especial', callback=special_call.start_llamamiento_especial))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_periodo', callback=special_call.callback_llamamiento_especial_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_requisitos', callback=special_call.callback_llamamiento_especial_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_examenes', callback=special_call.callback_llamamiento_especial_examenes))
    dp.add_handler(CallbackQueryHandler(pattern='llamamiento_especial_presentarmeSinFormulario', callback=special_call.callback_llamamiento_especial_presentarmeSinFormulario))

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
    
    
    # Alumnos Colaboradores
    
    dp.add_handler(CallbackQueryHandler(pattern='student_collaborating_students', callback=collaborating_students.student_collaborating_students))
    
    
    # Evaluacion por compensacion
    # dp.add_handler(CommandHandler('compensacion', evaluacion_compensacion.start_compensacion))
    dp.add_handler(CallbackQueryHandler(pattern='start_compensacion', callback=compensation_evaluation.start_compensacion))
    dp.add_handler(CallbackQueryHandler(pattern='inicio_comnpensacion_no_habilitantes', callback=compensation_evaluation.start_compensacion_no_habilitantes))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_periodo', callback=compensation_evaluation.callback_compensacion_periodo))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_requisitos', callback=compensation_evaluation.callback_compensacion_requisitos))
    dp.add_handler(CallbackQueryHandler(pattern='compensacion_req_especificos', callback=compensation_evaluation.callback_compensacion_req_especificos))
    
    # dp.add_handler(CallbackQueryHandler(pattern='student_spanish_compensacion_go_back', callback=compensation_evaluation.callback_compensacion_req_especificos))
    
    
    
    # Movilidad
    dp.add_handler(CallbackQueryHandler(pattern='inicio_movilidad', callback=movilidad.start_movilidad))
    dp.add_handler(CallbackQueryHandler(pattern='movilidad_otras_movilidades', callback=movilidad.movilidad_otras_movilidades))



    # Volver atras
    # dp.add_handler(CallbackQueryHandler(pattern='student_spanish_go_back', callback=menu_estudiante))
    
    
    
    # Volver atras
    dp.add_handler(CallbackQueryHandler(pattern='student_english_go_back', callback=student_menu_english))
    
    dp.add_handler(CallbackQueryHandler(pattern='student_menu_english_go_back', callback=second_menu_english))
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = ' *Welcome to the Student menu*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='ESI news', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Timetables', callback_data='student_timetable_english'),InlineKeyboardButton(text='Exams calendars', callback_data='student_exam_calendar_english')],
            [InlineKeyboardButton(text='TFG/M', callback_data='tfg_start_english'), InlineKeyboardButton(text='Tutorials', callback_data='student_start_tutorships_english')],
            [InlineKeyboardButton(text='Global assessment', callback_data='global_assessment_start_english'), InlineKeyboardButton(text='Special call', callback_data='inicio_llamamiento_especial')],
            [InlineKeyboardButton(text='December call', callback_data='inicio_conv_diciembre'),InlineKeyboardButton(text='Group assigment', callback_data='inicio_group_assignment')],
            [InlineKeyboardButton(text='Internships', callback_data='start_practice'), InlineKeyboardButton(text='Mobility', callback_data='inicio_movilidad')],
            [InlineKeyboardButton(text='Collaborating studing', callback_data='student_collaborating_students'), InlineKeyboardButton(text='Assesment by compensation', callback_data='start_compensacion')],
            [InlineKeyboardButton(text='ESI Academic Planning website', url='https://esingenieria.uca.es/ordenacion/')],
            [InlineKeyboardButton(text='Go back', callback_data='student_menu_english_go_back')]
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
        text = '*Bienvenid@ al menu PDI*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Horarios', callback_data='pdi_timetable'), InlineKeyboardButton(text='Calendarios de exámenes', callback_data='pdi_exam_calendar')],
            [InlineKeyboardButton(text='Calendario Académico', url='https://esingenieria.uca.es/wp-content/uploads/2021/05/Calendario-Academico-2021-22-ESI.pdf')],
            [InlineKeyboardButton(text='Formulario de incidencia docente', url='https://esingenieria.uca.es/ordenacion-pdi/'), InlineKeyboardButton(text='Horarios por áreas', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Guía para los programas docentes', url='https://esingenieria.uca.es/wp-content/uploads/2021/06/Indicaciones_Programas_Docentes_ESI%20_v2.pdf'), InlineKeyboardButton(text='Acceso a GOA', url='https://goa.uca.es/')],
            [InlineKeyboardButton(text='Acceso al Sistema de Información', url='https://sistemadeinformacion.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion/')],
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
        text = '*Welcome to the PDI menu*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='ESI news', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Timetables', callback_data='pdi_timetable_english'), InlineKeyboardButton(text='Exams calendars', callback_data='pdi_exam_calendar_english')],
            [InlineKeyboardButton(text='Academic Calendar', url='https://esingenieria.uca.es/wp-content/uploads/2021/05/Calendario-Academico-2021-22-ESI.pdf')],
            [InlineKeyboardButton(text='Teaching Incident Form', url='https://esingenieria.uca.es/ordenacion-pdi/'), InlineKeyboardButton(text='Timetables by areas', url='https://esingenieria.uca.es/ordenacion-pdi/')],
            [InlineKeyboardButton(text='Guide to teaching programmes', url='https://esingenieria.uca.es/wp-content/uploads/2021/06/Indicaciones_Programas_Docentes_ESI%20_v2.pdf'), InlineKeyboardButton(text='Access to GOA', url='https://goa.uca.es/')],
            [InlineKeyboardButton(text='Access to the Information System', url='https://sistemadeinformacion.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='ESI Academic Planning website', url='https://esingenieria.uca.es/ordenacion/')],
            [InlineKeyboardButton(text='Go back', callback_data='PDI_menu_english_go_back')]
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
    
    
    #Prueba
    dp.add_handler(CallbackQueryHandler(pattern='consulta_sire', callback=consulta_sire))

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Bienvenid@ al menu PAS*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Noticias ESI', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Horarios', callback_data='pas_timetable'), InlineKeyboardButton(text='Calendarios de exámenes', callback_data='pas_exam_calendar')],
            [InlineKeyboardButton(text='CAU de Infraestructuras', url='https://cau-infraestructuras.uca.es/cau/index.do')],
            [InlineKeyboardButton(text='CAU de Reparación', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M01'),InlineKeyboardButton(text='CAU de Climatización', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M07')],
            [InlineKeyboardButton(text='Directorio', url='https://directorio.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='Web Ordenación Académica ESI', url='https://esingenieria.uca.es/ordenacion/')],
            [InlineKeyboardButton(text='Consulta sire', callback_data='consulta_sire')],
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
    
    
    #Prueba
    dp.add_handler(CallbackQueryHandler(pattern='consulta_sire', callback=consulta_sire))

    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Welcome to the PAS menu*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='ESI news', url='https://esingenieria.uca.es/noticia/')],
            [InlineKeyboardButton(text='Timetables', callback_data='pas_timetable_english'), InlineKeyboardButton(text='Exams calendar', callback_data='pas_exam_calendar_english')],
            [InlineKeyboardButton(text='Infrastructure CAU', url='https://cau-infraestructuras.uca.es/cau/index.do')],
            [InlineKeyboardButton(text='Repairs CAU', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M01'),InlineKeyboardButton(text='Air conditioning CAU', url='https://cau-infraestructuras.uca.es/cau/grupoServicios.do?id=M07')],
            [InlineKeyboardButton(text='Directory', url='https://directorio.uca.es/'), InlineKeyboardButton(text='SIRE', url='https://sire.uca.es/')],
            [InlineKeyboardButton(text='ESI Academic Planning website', url='https://esingenieria.uca.es/ordenacion/')],
            [InlineKeyboardButton(text='Consulta sire', callback_data='consulta_sire')],
            [InlineKeyboardButton(text='Go back', callback_data='PAS_menu_english_go_back')]
        ]),
        parse_mode='Markdown'
    )


# Nuevo

def first_menu(update, context):
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_idiom_spanish', callback=second_menu_spanish))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_idiom_english', callback=second_menu_english))
    
    # print(update)
    # print(update.message.from_user.language_code)
    
    # if(update.message.from_user.language_code == "es"):
    if(update.callback_query == None):
        print(update.message.from_user.language_code)
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
        print(query.from_user.language_code)
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
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_student', callback=menu_estudiante))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_PDI', callback=menu_PDI))
    dp.add_handler(CallbackQueryHandler(pattern='selected_PAS', callback=menu_PAS))
    
    dp.add_handler(CallbackQueryHandler(pattern='selected_second_menu_go_back', callback=first_menu))
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = '*Seleccione que rol quiere consultar*',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Estudiante', callback_data='selected_student')],
            [InlineKeyboardButton(text='PDI', callback_data='selected_PDI')],
            [InlineKeyboardButton(text='PAS', callback_data='selected_PAS')],
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
            [InlineKeyboardButton(text='Go back', callback_data='selected_second_menu_go_back')]
        ]),
        parse_mode='Markdown'
    )  




def consulta_sire(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text('Para iniciar las consultas con sire escriba, /sire')
    
    
__LOGIN_URL__ = 'https://sire.uca.es/sire/login.do'
__PROCESA_LISTA_RESERVA_URL__ = 'https://sire.uca.es/sire/listadoSemanal.do'

class SIRESession():
    
    login = ""
    password=""
    logger = None
    iterate = False

    def __init__(self, login='', password= '', logger = None, iterate = False):
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.COOKIEFILE, "")
        self.curl.setopt(pycurl.FOLLOWLOCATION, 1)

        self.__page = io.BytesIO()
        self.__headers = io.BytesIO()
        self.curl.setopt(pycurl.WRITEHEADER, self.__headers)
        self.curl.setopt(pycurl.WRITEDATA, self.__page)

        self.curl.setopt(pycurl.URL, __LOGIN_URL__)
        self.curl.setopt(pycurl.POST, 1)

#         if not login:
# #            self.ulogin = input('SIRE - Identificador de usuario:')
#             self.login = input('SIRE - Identificador de correo:')
#         if not password:
#             self.password = getpass.getpass('Contraseña:')

        self.login = login
        self.password = password
        
        self.logger = logger
        self.iterate = iterate
        
        print(self.login +"y"+self.password)

        post_data = {'login': self.login, 'password': self.password}
        postfields = urllib.parse.urlencode(post_data)
        self.curl.setopt(pycurl.POSTFIELDS, postfields)

        self.curl.perform()
        try:
            headersBody = self.__headers.getvalue().decode('iso-8859-1')
            jsessionid = re.search('JSESSIONID=([\w\d]+)', headersBody).group(1)
            sid = re.search('SID=([\w\d]+)', headersBody).group(1)
#             if self.logger:
#                 self.logger.info('Acceso a SIRE realizado satisfactoriamente.')
#                 self.logger.info('SIRE: JSESSIONID=%s; SID=%s' %(jsessionid, sid))
#             else:
#                 print('Acceso a SIRE realizado satisfactoriamente.')
#                 print('SIRE: JSESSIONID=%s; SID=%s' %(jsessionid, sid))
#             self.cookieList = self.curl.getinfo(pycurl.INFO_COOKIELIST)
#             pageBody = self.__page.getvalue().decode('iso-8859-1')
#             cabecera = lxml.html.fromstring(pageBody.lstrip('\x00')).xpath('//div[@class="text-right"]/text()')
# #            cabecera = lxml.html.fromstring(pageBody.lstrip('\x00')).get_element_by_id('cabeceraPagina')
# #            self.responsableNombre = re.search('\t(\w[^\xa0]+)\s+\xa0', cabecera.text_content()).group(1).replace(" ","+")
#             self.responsableNombre = re.search('\t(\w[^\xa0]+)\s+\xa0', cabecera[-1]).group(1).replace(" ","+")
# #            self.responsable = self.ulogin.lstrip('u')
# #            self.responsable += "TRWAGMYFPDXBNJZSQVHLCKE"[int(self.responsable)%23]
        except:
            print("Fallo")
            # sys.stderr.write('Error en el acceso.\n')
            # sys.exit(1)

        if not self.iterate:
            del self.login, self.password
            
            
    def consulta_clase2(self, update, context):

        message = update.message.text.upper()

        if(message.find("SALIR") + message.find("DESCONECTAR") > -2):
            return general.desconexion(update, context)

        # print(update.message.text)
        
        consulta = update.message.text.split('-')
        
        #  B02-11-05-2022
        
        update.message.reply_text(
            text = '*Comprobando su eleccion: *\nClase:'+consulta[0]+' Dia:'+consulta[1]+' Mes:'+consulta[2]+' Año:'+consulta[3],
            parse_mode='Markdown'
        )
        
        # __init__(self,"490798721Y","c957619")
        
        url = "https://sire.uca.es/sire/listadoSemanal.do?centro=BPR&recurso="+consulta[0]+"&dia="+consulta[1]+"&mes="+consulta[2]+"&agno="+consulta[3]

            # webbrowser.open("https://sire.uca.es/sire/nuevaReserva.do?centro=ESI&recurso=10000971&motivo=TGRUP", new=2, autoraise=True)
        # webbrowser.open(url)
        # c = pycurl.Curl()
        # post_data = {'centro': 'BPR', 'recurso': consulta[0], 'dia': consulta[1], 'mes': consulta[2], 'agno': consulta[3]}
        # postfields = urllib.parse.urlencode(post_data)
        # self.curl.setopt(pycurl.POSTFIELDS, postfields)
        # self.curl.setopt(pycurl.URL, __PROCESA_LISTA_RESERVA_URL__+"?centro=BPR&recurso="+consulta[0]+"&dia="+consulta[1]+"&mes="+consulta[2]+"&agno="+consulta[3])
        
        # # self.__page.truncate(0)
        # # self.__headers.truncate(0)

        # # self.curl.perform()
        # pycurl.URL.perform()
        
        c = pycurl.Curl()
        c.setopt(pycurl.URL, __PROCESA_LISTA_RESERVA_URL__+"?centro=BPR&recurso="+consulta[0]+"&dia="+consulta[1]+"&mes="+consulta[2]+"&agno="+consulta[3])
        c.perform()
        
        # print(1)
        # self.curl.setopt(pycurl.URL, url)
        # print(2)
        # self.curl.perform()
        # print(3)
        # self.curl.close()
        
        update.message.reply_text(text = 'Escribe otra consulta o bien si desea finalizar la conexión SIRE escriba salir o desconectar')
    
    
    
    
def consulta_clase(update, context):

    patata=SIRESession("u49079821","c957619")
    # patata.__init__(update, context, "49079821Y","c957619")
    # patata = SIRE_info("49079821Y","c957619")
    patata.consulta_clase2(update,context)
    

    # message = update.message.text.upper()

    # if(message.find("SALIR") + message.find("DESCONECTAR") > -2):
    #     return general.desconexion(update, context)

    # # print(update.message.text)
    
    # consulta = update.message.text.split('-')
    
    # #  B02-11-05-2022
    
    # update.message.reply_text(
    #     text = '*Comprobando su eleccion: *\nClase:'+consulta[0]+' Dia:'+consulta[1]+' Mes:'+consulta[2]+' Año:'+consulta[3],
    #     parse_mode='Markdown'
    # )
    
    # # __init__("490798721Y","c957619")
    
    # url = "https://sire.uca.es/sire/listadoSemanal.do?centro=BPR&recurso="+consulta[0]+"&dia="+consulta[1]+"&mes="+consulta[2]+"&agno="+consulta[3]

        # webbrowser.open("https://sire.uca.es/sire/nuevaReserva.do?centro=ESI&recurso=10000971&motivo=TGRUP", new=2, autoraise=True)
    # webbrowser.open(url)
    
    
    # c = pycurl.Curl()
    # # c.setopt(pycurl.URL, __PROCESA_LISTA_RESERVA_URL__+"?centro=BPR&recurso="+consulta[0]+"&dia="+consulta[1]+"&mes="+consulta[2]+"&agno="+consulta[3])
    
    # # post_data = {'centro': 'BPR', 'recurso': consulta[0], 'dia': consulta[1], 'mes': consulta[2], 'agno': consulta[3]}
    # # postfields = urllib.parse.urlencode(post_data)
    # # c.setopt(pycurl.URL, __PROCESA_LISTA_RESERVA_URL__)
    # # c.setopt(pycurl.POSTFIELDS, postfields)
    
    
    # # c = pycurl.Curl()
    # # c.setopt(pycurl.URL, url)
    # c.perform()
    # c.close()
    
    # update.message.reply_text(text = 'Escribe otra consulta o bien si desea finalizar la conexión SIRE escriba salir o desconectar')





###########################################################################

if __name__ == '__main__':
    
    updater = Updater(token='2049537211:AAERyXIxQUMicwINmZqy1tAXai-G1EgJtKY', use_context=True)

    dp = updater.dispatcher
    
    # dp.add_handler(CommandHandler('iniciar', general.start_bot))
    
    # dp.add_handler(MessageHandler(Filters.regex('^pdi$'), menu_PDI))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('sire', general.start_sire),
        ],

        states={
            general.INPUT_ID_USER: [MessageHandler(Filters.text, input_id_user)], 
            general.CONSULT_SIRE: [MessageHandler(Filters.text, consulta_clase)]
        },

        fallbacks=[]
    ))
    
    
    # dp.add_handler(MessageHandler(Filters.regex(r'horarios|Horarios|HORARIOS|horario|Horario|HORARIO'), timetable.student_timetable))
    # dp.add_handler(MessageHandler(Filters.regex(r'exámenes|Exámenes|EXÁMENES|examenes|Examenes|EXAMENES'), exam_calendar.student_exam_calendar))
    
    # dp.add_handler(MessageHandler(Filters.regex(r'alumnos colaboradores|Alumnos colaboradores|ALUMNOS COLABORADORES'), collaborating_students.student_collaborating_students))
    # dp.add_handler(MessageHandler(Filters.regex(r'llamamiento especial|Llamamiento especial|LLAMAMIENTO ESPECIAL'), special_call.start_llamamiento_especial))
    # dp.add_handler(MessageHandler(Filters.regex(r'estudiante'), menu_estudiante))
    # dp.add_handler(MessageHandler(Filters.regex(r'PDI'), menu_PDI))
    # dp.add_handler(MessageHandler(Filters.regex(r'PAS'), menu_PAS))
    
    dp.add_handler(MessageHandler(Filters.text, first_menu))
    
    
    updater.start_polling()
    updater.idle()