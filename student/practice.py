

from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general


# Practicas Curriculares

def start_practicas_curriculares(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Las prácticas curriculares son actividades académicas integrantes del plan de estudio que se desarrollan en empresas externas o en la propia universidad, el proyecto formativo está definido por cada titulación. Pueden ser obligatorias u optativas.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='¿Cuál es la duración mínima/máxima?', callback_data='practicas_curriculares_duracion')],
            [InlineKeyboardButton(text='¿Tienen algún coste y/o alguna retribución para el estudiante?', callback_data='practicas_curriculares_retribucion')],
            [InlineKeyboardButton(text='¿Existe alguna ayuda económica o de algún tipo?', callback_data='practicas_curriculares_ayuda_economica')],
            [InlineKeyboardButton(text='¿Debo hacerlas en la misma localidad que estudio?', callback_data='practicas_curriculares_localidad')],
            [InlineKeyboardButton(text='¿Puedo hacer más de una práctica curricular?', callback_data='practicas_curriculares_numero')],
            [InlineKeyboardButton(text='¿Dónde debo inscribirme para realizar prácticas curriculares?', callback_data='practicas_curriculares_periodo')],
            [InlineKeyboardButton(text='¿En qué se diferencian por tanto de las prácticas extracurriculares?', callback_data='practicas_curriculares_diferencias')],
            [InlineKeyboardButton(text='¿Puedo convalidar unas prácticas extracurriculares por las curriculares?', callback_data='practicas_curriculares_convalidar')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
        


def callback_practicas_curriculares_duracion(update, context):
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Cada plan de estudios define la duración de las prácticas, por lo general oscilan entre 6 y 12 semanas.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )
        


def callback_practicas_curriculares_retribucion(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'No tienen coste para la empresa, cada empresa/entidad decide si son retribuidas o no, prácticamente no tienen retribución económica. Para el estudiante sí tiene coste, al igual que si fuera una asignatura, pagarás los créditos equivalentes que tengan tus prácticas.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )
        


def callback_practicas_curriculares_ayuda_economica(update, context):
    
   
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'El Vicerrectorado de Estudiantes y Empleo convoca cada curso académico unas ayudas al transporte para estudiantes de prácticas curriculares. Os dejamos el enlace directo dónde la publicarán (cuando salgan).',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Portal', url='https://atencionalumnado.uca.es/becas-practicas-curriculares/')],
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])   
    )


def callback_practicas_curriculares_localidad(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'No necesariamente. Simplemente necesitas que la empresa/entidad en la que quieras hacer las prácticas tenga Convenio con la Universidad de Cádiz (en caso de que no lo tenga, podrás proponerle a la empresa que lo haga. Es un trámite relativamente sencillo y que suele durar en cerrarse 1 mes).',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )
        


def callback_practicas_curriculares_numero(update, context):
     
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Los estudiantes deben cumplimentar una serie de créditos definidos en cada plan de estudio, éstos se pueden dividir en una o varias asignaturas de prácticas. Por lo general cada grado tiene una sola asignatura de práctica curricular.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )
        


def callback_practicas_curriculares_periodo(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Los estudiantes no tienen que inscribirse en ninguna plataforma, simplemente matricularos de la “asignatura” prácticas. La selección de estudiante-empresa la realizan los centros, los estudiantes seleccionados recibirán un mail con la dirección de la plataforma de gestión de prácticas curriculares http//practicas.uca.es donde validarán el documento de aceptación de prácticas.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )
        

def callback_practicas_curriculares_convalidar(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Mientras las prácticas se ajusten a los requisitos (trabajo relacionado con el plan de estudios del grado y duración –en horas- mínima requerida) que se pide en cada facultad/centro, se podrá solicitar dicha convalidación. Este proceso se tramitará en cada centro por las personas que formen la comisión de convalidaciones.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )
    
def callback_practicas_curriculares_diferencias(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Las prácticas extracurriculares tienen exactamente el mismo fin que las curriculares, pero con las principales diferencias de:'
                '\n\nCurriculares: Tienen coste para el estudiante, la duración depende de lo que venga en el Plan de Estudios del grado y oscilará entre las 6-12 semanas (sin opción a prórroga), sin opción a que sean remuneradas y sí están incluidas en el Plan de Estudios.'
                '\n\nExtracurriculares: No tienen coste para el estudiante, la duración depende de lo que oferte la empresa y será como máximo de 6 meses (prorrogables 3 meses más), con posibilidad para que sean remuneradas y no están incluidas en el Plan de Estudios (por lo que tendrían que convalidarse, siempre que esta opción sea posible y las prácticas se ajuste a los requisitos del Centro/Facultad).',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_curriculares')]
        ])
    )







# Practicas Extracurriculares

def start_practicas_extracurriculares(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Las prácticas extracurriculares, son aquéllas que los estudiantes podrán realizar con carácter voluntario durante su periodo de formación y que, aun teniendo los mismos fines que las prácticas curriculares, no forman parte del correspondiente plan de estudios. No obstante, serán contempladas en el suplemento europeo al título (SET) conforme determine la normativa vigente',
        reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(text='¿Cuál es la duración mínima/máxima?', callback_data='practicas_extracurriculares_duracion')],
                [InlineKeyboardButton(text='¿Tienen algún coste y/o alguna retribución para el estudiante?', callback_data='practicas_extracurriculares_retribucion')],
                [InlineKeyboardButton(text='¿Existe alguna ayuda económica o de algún tipo?', callback_data='practicas_extracurriculares_ayuda_economica')],
                [InlineKeyboardButton(text='¿Qué es la beca PRAEM de la Junta de Andalucía?', callback_data='practicas_extracurriculares_beca')],
                [InlineKeyboardButton(text='¿Cómo/dónde puedo encontrar prácticas de este tipo?', callback_data='practicas_extracurriculares_encontrar')],
                [InlineKeyboardButton(text='¿Debo hacerlas en la misma localidad que estudio?', callback_data='practicas_extracurriculares_localidad')],
                [InlineKeyboardButton(text='¿Puedo convalidar unas prácticas extracurriculares por las curriculares?', callback_data='practicas_extracurriculares_convalidar')],
                [InlineKeyboardButton(text='¿Puedo hacer más de una práctica extracurricular?', callback_data='practicas_extracurriculares_numero')],
                [InlineKeyboardButton(text='¿En qué se diferencian por tanto de las prácticas curriculares?', callback_data='practicas_extracurriculares_diferencias')],
                [InlineKeyboardButton(text='¿Cuáles son los requisitos que debo cumplir para poder hacer prácticas extracurriculares?', callback_data='practicas_extracurriculares_requisitos')],
                [InlineKeyboardButton(text='¿Existe algún plazo para solicitarlas?', callback_data='practicas_extracurriculares_periodo')],
                [InlineKeyboardButton(text='¿Tienes derecho a vacaciones mientras realizas las prácticas?', callback_data='practicas_extracurriculares_vacaciones')],
                [InlineKeyboardButton(text='¿Debo recuperar los días que asisto a exámenes? ¿Y tutorías?', callback_data='practicas_extracurriculares_recuperar_dias')],
                [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
        


def callback_practicas_extracurriculares_duracion(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'No hay un mínimo definido, el máximo son 6 meses por curso académico, con la posibilidad extraordinaria de ampliar mediante prórroga por otros 3 meses más',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )
        


def callback_practicas_extracurriculares_retribucion(update, context):
     
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Depende del programa, por lo general son del plan propio y sí tienen un coste para la empresa/entidad por mes/estudiante. No hay obligación de retribución mínima para las ofertas, aunque en general sí tienen retribución.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )
        

def callback_practicas_extracurriculares_ayuda_economica(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Algunos programas de prácticas extracurriculares tienen financiación (PRAEM, becas Santander, ONCE, Univergem, etc.) o en el caso de las becas de formación (prácticas extracurriculares en la propia universidad) que normalmente tienen retribución económica.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_beca(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Es un programa financiado por la Junta de Andalucía y gestionado por la UCA cuyo objetivo es el fomento de la inserción laboral a través de las prácticas en empresas de los estudiantes universitarios. Tiene una dotación económica de 180€/mes que abona la universidad, aparte, la empresa está obligada a abonar un mínimo de otros 180€/mes al estudiante',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )
        


def callback_practicas_extracurriculares_encontrar(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Esta modalidad de prácticas se gestionan a través de la plataforma Ícaro, donde deben estar inscritos los demandantes de prácticas extracurriculares. En dicho portal puede consultar la oferta diaria de prácticas extracurriculares',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Portal', url='https://icaro.ual.es/')],
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_localidad(update, context):
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'No necesariamente. Simplemente necesitas que la empresa/entidad en la que quieras hacer las prácticas esté registrada en la plataforma Ícaro y a través de ella oferte unas prácticas (previo Convenio con la Universidad de Cádiz. En caso de que no lo tenga, podrás proponerle a la empresa que lo haga. Es un trámite relativamente sencillo y que suele durar en cerrarse 1 mes).',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_numero(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Sí, siempre que no se superen los 6 meses por curso académico. El requisito imprescindible para poder realizar prácticas extracurriculares es permanecer matriculado en la universidad de algún crédito.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_requisitos(update, context):
    
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Para solicitar las prácticas debes estar matriculado durante el curso de realización de las prácticas en una titulación oficial,  tener superado, al menos, el 50% de los créditos de la titulación que cursa y tener su inscripción correcta en el portal de prácticas ICARO.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_periodo(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'No. Las empresas pueden realizar sus ofertas durante todo el año, si bien la gestión de las mismas estará sujeta a las necesidades de organización de la unidad de prácticas. El plazo para la inscripción en las mismas será el establecido para cada oferta a través de ICARO.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_vacaciones(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'No se contemplan las vacaciones durante el desarrollo de las prácticas. Normalmente estarás sujeto a los días festivos que haya contemplados en la empresa y/o en la localidad a la que pertenezca la misma.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )


def callback_practicas_extracurriculares_recuperar_dias(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'La asistencia a exámenes parciales y finales, justificadas, no serán días que debas recuperar. Al igual con las tutorías académicas.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )
    
def callback_practicas_extracurriculares_convalidar(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Mientras las prácticas se ajusten a los requisitos (trabajo relacionado con el plan de estudios del grado y duración –en horas- mínima requerida) que se pide en cada facultad/centro, se podrá solicitar dicha convalidación. Este proceso se tramitará en cada centro por las personas que formen la comisión de convalidaciones.',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )
    
def callback_practicas_extracurriculares_diferencias(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text( 
        text = 'Las prácticas extracurriculares tienen exactamente el mismo fin que las curriculares, pero con las principales diferencias de:'
                '\n\nCurriculares: Tienen coste para el estudiante, la duración depende de lo que venga en el Plan de Estudios del grado y oscilará entre las 6-12 semanas (sin opción a prórroga), sin opción a que sean remuneradas y sí están incluidas en el Plan de Estudios.'
                '\n\nExtracurriculares: No tienen coste para el estudiante, la duración depende de lo que oferte la empresa y será como máximo de 6 meses (prorrogables 3 meses más), con posibilidad para que sean remuneradas y no están incluidas en el Plan de Estudios (por lo que tendrían que convalidarse, siempre que esta opción sea posible y las prácticas se ajuste a los requisitos del Centro/Facultad).',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Volver', callback_data='inicio_practicas_extracurriculares')]
        ])
    )