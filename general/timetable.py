from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def student_timetable(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Horarios por grado',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://drive.google.com/file/d/1QFkcVDiwxaFc4ponNIkg5oQD3TbDyLUw/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/116TwrrCoYQxFdXN5hxhLpd-v49RSjQ8P/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://drive.google.com/file/d/1GzvC2tYPhPO7gva8NUpcYeku9XEmTnti/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1zCp42oCWuqC7BWInYBEGR3QhgjJsVt2f/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://drive.google.com/file/d/1vp1ngVlvRGyTYxp6W4775feD4k2ShEA8/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://drive.google.com/file/d/1f8APfJOsVOiLOwu8ywPLVow23W-n7tjN/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://drive.google.com/file/d/1GwAgLfJIppFJPrj6IheYVA9NZGOkM-HH/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1D3tu9QoN7ZMlXu2R_oOrz8QmcRanYX8c/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://drive.google.com/file/d/1Q6nnXPvR1_AID4X6dYrKlQ44QgCLtnUg/view')],
            [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1EKP8971ufwyvIRSH_t7LRSMQ9qIOZ23C/view')],
            [InlineKeyboardButton(text='Volver', callback_data='student_spanish_go_back')]
        ])
    )
        
def student_timetable_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Timetables by degree',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://drive.google.com/file/d/1QFkcVDiwxaFc4ponNIkg5oQD3TbDyLUw/view')],
            [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/116TwrrCoYQxFdXN5hxhLpd-v49RSjQ8P/view')],
            [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://drive.google.com/file/d/1GzvC2tYPhPO7gva8NUpcYeku9XEmTnti/view')],
            [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://drive.google.com/file/d/1zCp42oCWuqC7BWInYBEGR3QhgjJsVt2f/view')],
            [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://drive.google.com/file/d/1vp1ngVlvRGyTYxp6W4775feD4k2ShEA8/view')],
            [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://drive.google.com/file/d/1f8APfJOsVOiLOwu8ywPLVow23W-n7tjN/view')],
            [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://drive.google.com/file/d/1GwAgLfJIppFJPrj6IheYVA9NZGOkM-HH/view')],
            [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://drive.google.com/file/d/1D3tu9QoN7ZMlXu2R_oOrz8QmcRanYX8c/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://drive.google.com/file/d/1Q6nnXPvR1_AID4X6dYrKlQ44QgCLtnUg/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1EKP8971ufwyvIRSH_t7LRSMQ9qIOZ23C/view')],
            [InlineKeyboardButton(text='Back', callback_data='student_english_go_back')]
        ])
    )      
        
def pdi_timetable(update, context):

    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Horarios por grado',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://drive.google.com/file/d/1QFkcVDiwxaFc4ponNIkg5oQD3TbDyLUw/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/116TwrrCoYQxFdXN5hxhLpd-v49RSjQ8P/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://drive.google.com/file/d/1GzvC2tYPhPO7gva8NUpcYeku9XEmTnti/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1zCp42oCWuqC7BWInYBEGR3QhgjJsVt2f/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://drive.google.com/file/d/1vp1ngVlvRGyTYxp6W4775feD4k2ShEA8/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://drive.google.com/file/d/1f8APfJOsVOiLOwu8ywPLVow23W-n7tjN/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://drive.google.com/file/d/1GwAgLfJIppFJPrj6IheYVA9NZGOkM-HH/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1D3tu9QoN7ZMlXu2R_oOrz8QmcRanYX8c/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://drive.google.com/file/d/1Q6nnXPvR1_AID4X6dYrKlQ44QgCLtnUg/view')],
            [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1EKP8971ufwyvIRSH_t7LRSMQ9qIOZ23C/view')],
            [InlineKeyboardButton(text='Volver', callback_data='PDI_spanish_go_back')]
        ])
    )

def pdi_timetable_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Timetables by degree',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://drive.google.com/file/d/1QFkcVDiwxaFc4ponNIkg5oQD3TbDyLUw/view')],
            [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/116TwrrCoYQxFdXN5hxhLpd-v49RSjQ8P/view')],
            [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://drive.google.com/file/d/1GzvC2tYPhPO7gva8NUpcYeku9XEmTnti/view')],
            [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://drive.google.com/file/d/1zCp42oCWuqC7BWInYBEGR3QhgjJsVt2f/view')],
            [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://drive.google.com/file/d/1vp1ngVlvRGyTYxp6W4775feD4k2ShEA8/view')],
            [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://drive.google.com/file/d/1f8APfJOsVOiLOwu8ywPLVow23W-n7tjN/view')],
            [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://drive.google.com/file/d/1GwAgLfJIppFJPrj6IheYVA9NZGOkM-HH/view')],
            [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://drive.google.com/file/d/1D3tu9QoN7ZMlXu2R_oOrz8QmcRanYX8c/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://drive.google.com/file/d/1Q6nnXPvR1_AID4X6dYrKlQ44QgCLtnUg/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1EKP8971ufwyvIRSH_t7LRSMQ9qIOZ23C/view')],
            [InlineKeyboardButton(text='Back', callback_data='PDI_english_go_back')]
        ])
    )
       
def pas_timetable(update, context):
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Horarios por grado',
        reply_markup = InlineKeyboardMarkup([
           [InlineKeyboardButton(text='Grado en Ingeniería Aeroespacial', url='https://drive.google.com/file/d/1QFkcVDiwxaFc4ponNIkg5oQD3TbDyLUw/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/116TwrrCoYQxFdXN5hxhLpd-v49RSjQ8P/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Eléctrica', url='https://drive.google.com/file/d/1GzvC2tYPhPO7gva8NUpcYeku9XEmTnti/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1zCp42oCWuqC7BWInYBEGR3QhgjJsVt2f/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Informática', url='https://drive.google.com/file/d/1vp1ngVlvRGyTYxp6W4775feD4k2ShEA8/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería Mecánica', url='https://drive.google.com/file/d/1f8APfJOsVOiLOwu8ywPLVow23W-n7tjN/view')],
            [InlineKeyboardButton(text='Grado en Ingeniería en Tecnologías Industriales', url='https://drive.google.com/file/d/1GwAgLfJIppFJPrj6IheYVA9NZGOkM-HH/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial', url='https://drive.google.com/file/d/1D3tu9QoN7ZMlXu2R_oOrz8QmcRanYX8c/view')],
            [InlineKeyboardButton(text='Doble Grado en Ingeniería Mecánica e Ingeniería Eléctrica', url='https://drive.google.com/file/d/1Q6nnXPvR1_AID4X6dYrKlQ44QgCLtnUg/view')],
            [InlineKeyboardButton(text='Doble Grado de Ingeniería Mecánica e Ingeniería en Diseño Industrial y Desarrollo del Producto', url='https://drive.google.com/file/d/1EKP8971ufwyvIRSH_t7LRSMQ9qIOZ23C/view')],
            [InlineKeyboardButton(text='Volver', callback_data='PAS_spanish_go_back')]
        ])
    )
    
def pas_timetable_english(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text = 'Timetables by degree',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Degree in Aerospace Engineering', url='https://drive.google.com/file/d/1QFkcVDiwxaFc4ponNIkg5oQD3TbDyLUw/view')],
            [InlineKeyboardButton(text='Degree in Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/116TwrrCoYQxFdXN5hxhLpd-v49RSjQ8P/view')],
            [InlineKeyboardButton(text='Degree in Electrical Engineering', url='https://drive.google.com/file/d/1GzvC2tYPhPO7gva8NUpcYeku9XEmTnti/view')],
            [InlineKeyboardButton(text='Degree in Industrial Electronic Engineering', url='https://drive.google.com/file/d/1zCp42oCWuqC7BWInYBEGR3QhgjJsVt2f/view')],
            [InlineKeyboardButton(text='Degree in Computer Engineering', url='https://drive.google.com/file/d/1vp1ngVlvRGyTYxp6W4775feD4k2ShEA8/view')],
            [InlineKeyboardButton(text='Degree in Mechanical Engineering', url='https://drive.google.com/file/d/1f8APfJOsVOiLOwu8ywPLVow23W-n7tjN/view')],
            [InlineKeyboardButton(text='Degree in Industrial Technologies Engineering', url='https://drive.google.com/file/d/1GwAgLfJIppFJPrj6IheYVA9NZGOkM-HH/view')],
            [InlineKeyboardButton(text='Double Degree in Electrical Engineering and Industrial Electronic Engineering', url='https://drive.google.com/file/d/1D3tu9QoN7ZMlXu2R_oOrz8QmcRanYX8c/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Electrical Engineering', url='https://drive.google.com/file/d/1Q6nnXPvR1_AID4X6dYrKlQ44QgCLtnUg/view')],
            [InlineKeyboardButton(text='Double Degree in Mechanical Engineering and Industrial Design and Product Development Engineering', url='https://drive.google.com/file/d/1EKP8971ufwyvIRSH_t7LRSMQ9qIOZ23C/view')],
            [InlineKeyboardButton(text='Back', callback_data='PAS_english_go_back')]
        ])
    )