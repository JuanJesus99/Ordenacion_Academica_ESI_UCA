
import pycurl
import urllib
import re
import io
import lxml

from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, conversationhandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import general


__LOGIN_URL__ = 'https://sire.uca.es/sire/login.do'

class SIRESession():
    

    def __init__(self, update='', context='', login='', password= '', logger = None, iterate = False):
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

        post_data = {'login': self.login, 'password': self.password}
        postfields = urllib.urlencode(post_data)
        self.curl.setopt(pycurl.POSTFIELDS, postfields)

        self.curl.perform()
        try:
            headersBody = self.__headers.getvalue().decode('iso-8859-1')
            jsessionid = re.search('JSESSIONID=([\w\d]+)', headersBody).group(1)
            sid = re.search('SID=([\w\d]+)', headersBody).group(1)
            if self.logger:
                self.logger.info('Acceso a SIRE realizado satisfactoriamente.')
                self.logger.info('SIRE: JSESSIONID=%s; SID=%s' %(jsessionid, sid))
            else:
                print('Acceso a SIRE realizado satisfactoriamente.')
                print('SIRE: JSESSIONID=%s; SID=%s' %(jsessionid, sid))
            self.cookieList = self.curl.getinfo(pycurl.INFO_COOKIELIST)
            pageBody = self.__page.getvalue().decode('iso-8859-1')
            cabecera = lxml.html.fromstring(pageBody.lstrip('\x00')).xpath('//div[@class="text-right"]/text()')
#            cabecera = lxml.html.fromstring(pageBody.lstrip('\x00')).get_element_by_id('cabeceraPagina')
#            self.responsableNombre = re.search('\t(\w[^\xa0]+)\s+\xa0', cabecera.text_content()).group(1).replace(" ","+")
            self.responsableNombre = re.search('\t(\w[^\xa0]+)\s+\xa0', cabecera[-1]).group(1).replace(" ","+")
#            self.responsable = self.ulogin.lstrip('u')
#            self.responsable += "TRWAGMYFPDXBNJZSQVHLCKE"[int(self.responsable)%23]
        except:
            print("Fallo")
            # sys.stderr.write('Error en el acceso.\n')
            # sys.exit(1)

        if not self.iterate:
            del self.login, self.password
            
            
    def consulta_clase(self, update, context):

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
        self.setopt(pycurl.URL, url)
        self.perform()
        # c.close()
        
        update.message.reply_text(text = 'Escribe otra consulta o bien si desea finalizar la conexión SIRE escriba salir o desconectar')