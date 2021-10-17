
import pyttsx3
import pyodbc

import sqlite3
from sqlite3 import Error
from datetime import datetime

import pandas as pd
import os
import time
import re
# from telegram.ext.messagehandler import MessageHandler
# from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageFilter, Filters
# from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
# import telegram

# import logging

# from threading import Thread

from telethon import TelegramClient, events, Button
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

class MakeDb:
    def __init__(self):
        self.DRIVER = "ODBC Driver 17 for SQL Server"
        self.SERVER = '10.200.10.46'
        self.DATABASE = 'ULTICABINET'
        self.UID = 'InspectoriaBI'
        self.PWD = 'G2UudQz7pFxbUTJR'
        # self.connnect_to_SQLdb()

        
    def connnect_to_SQLdb(self):
        try:
            conn = pyodbc.connect(f"""DRIVER={self.DRIVER};
                                    SERVER={self.SERVER};
                                    DATABASE={self.DATABASE};
                                    UID={self.UID};
                                    PWD={self.PWD}""")

            self.cursor = conn.cursor()
            print(repr('Successful get CONN to SQL SERVER'))
        except Exception as e:
            print(repr(f"Error to get CONN to SQL SERVER-> {e}"))

        try:
            sql_query = "SELECT * FROM NotasInformativasPN ORDER BY Fecha DESC"
            self.df1 = pd.read_sql(sql_query, conn)
            self.df_db = pd.DataFrame(self.df1).sort_values(by=['Expediente'], ascending=True).tail(11)
            print(repr('Successful df to SQL SERVER'))

            # TODO pending to SEARCH ONLY 2 FIELDS caption and text to convert FOR BETTER PERFORMANCE
        except Exception as e:
            print(f'Error get query PANDAS to SQL SERVER-> {e}')
            pass
        else:
            return self.df_db

    def view_all_tables(self):
        for row in self.cursor.tables():
            print(row.table_name)
            # print(cursor.description)


class MakeSqlite():

    def __init__(self, tuple_of_data=None):
        
        self.tuple_of_data = tuple_of_data

        self.conn = self.get_the_connection()
        # self.insert_data_in_dblite()
        # self.get_consult_dblite()
                
    def get_the_connection(self):
        try:
            connection = sqlite3.connect('save_id_and_verify.db', check_same_thread=False)
            cursor = connection.cursor()
            create_table_query = """CREATE TABLE IF NOT EXISTS tbl_notes
            ([id] INTEGER PRIMARY KEY, [notes_id] TEXT NOT NULL,[current_date] TEXT,[tipo_hecho] TEXT)"""
            cursor.execute(create_table_query)
            print(repr('Successful connection SQLite'))
        except Error as e:
            print(f'Error while connecting to SQlite: {e}')
        return connection
            
    def insert_data_in_dblite(self,tuple_of_data):
        sql = '''INSERT INTO tbl_notes(notes_id,current_date,tipo_hecho)
                VALUES(?,?,?)'''
        cursor = self.conn
        cursor.execute(sql, tuple_of_data)
        self.conn.commit()
        print(repr('Successful insert data to SQLite'))

    def get_consult_dblite(self):
        #THIS LAMBDA IS FOR GET CLEAR LIST OF DATA FETCHALL
        self.conn.row_factory = lambda cursor, row: row[0]
        data_consult = self.conn.execute("SELECT notes_id FROM tbl_notes ORDER BY current_date").fetchall()
        print(repr(data_consult))
        print(repr('Successful view QUERY data to SQLite'))
 
        # print(repr(data_consult))
        return data_consult

    def delete_consult_dblite(self):
        #THIS LAMBDA IS FOR GET CLEAR LIST OF DATA FETCHALL
        self.conn.row_factory = lambda cursor, row: row[0]
        data_consult = self.conn.execute('''DELETE FROM tbl_notes 
                                            WHERE id = 11;)''')

        print(repr('Successful delete before 511 row SQLite'))
        # self.conn.commit()
        # print(repr(data_consult))
        return data_consult


class MakeAudio:
    """ 1 - WE NEED THREE VARIALBLES 
            voice_id, 
            text_to_speech, 
            name_of_audiofile
    """

    def __init__(self, hour_of_case, date_of_case, text_to_speech, name_of_audiofile):

        espanish_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
        english_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 165)
        self.engine.setProperty("volume",9)
        self.voices = self.engine.getProperty('voices') 
        self.engine.setProperty("voice", espanish_voice_id)

                                                                     # Siendo la fecha y hora mencionada,
        # self.text_to_speech = str(f"SIENDO LAS {hour_of_case} HORAS DEL DÍA {date_of_case}, {text_to_speech}").upper().replace('Siendo la fecha y hora mencionada,',' ').replace('  ',
        # ' ').replace('\t',' ').replace('\n\t',' ').replace('\n\n',' ').replace('\n',' ').replace('\r','').replace('9-1-1',
        # 'NUEVE UNO UNO').replace('\r','').replace('CAL.','CALIBRE').replace('C/O','CABO').replace('R/O','RASO').replace('CAP.','CAPITÁN').replace('MR.','MAYOR').replace('SGTO.','SARGENTO').replace('1ER.',
        # 'PRIMER').replace('2DO.','SEGUNDO').replace('TTE.','TENIENTE').replace('COR.','CORONEL').replace('CNEL.','CORONEL').replace('LIC.',
        # 'LICENCIADO').replace('LICDO.','LICENCIADO').replace('LICDA.','LICENCIADA').replace('DOM.','DOMINICANO').replace('DOM,','DOMINICANO').replace('AV.',
        # 'AVENIDA').replace('S/N','SIN NÚMERO').replace('DX,','DIAGNÓSTICO MÉDICO').replace('DX.:','DIAGNÓSTICO MÉDICO').replace('DX:','DIAGNÓSTICO MÉDICO').replace('CED.',
        # 'CÉDULA').replace('CED:','CÉDULA').replace('CEDULA','CÉDULA').replace('NO.','NÚMERO').replace('DEPTO.','DEPARTAMENTO').replace('R.D.',
        # 'REPÚBLICA DOMINICANA').replace('D.N.','DISTRITO').replace('MULTIPLE','MÚLTIPLE').replace('-','').replace('TRANSITO',
        # 'TRÁNSITO').replace('TRAUMA','TRÁUMA').replace('COLISIONO','COLISIONÓ').replace('S/N','SIN NÚMERO').replace('RD$',' ').replace('MOTOR',
        # 'MOTÓR').replace('PUBLICA','PÚBLICA').replace('SR.','SEÑOR').replace('DR.','DOCTOR').replace('SRA.','SEÑORA').replace('DRA.','DOCTORA').replace('P.N.',' ').replace('P.N.,',
        # ' ').replace('PN.,',' ').replace('PARASITO','PARÁSITO')
        replaces = {"siendo las hora y fecha mencionada": " ",
                "las":" LAS",
                "!":"."}
                
        self.text_to_speech = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], text_to_speech, re.IGNORECASE)

        self.name_of_audio = f'{str(name_of_audiofile)}.ogg'
      
    def saveAudio(self):
        self.engine.save_to_file(self.text_to_speech, f"my_audios/{self.name_of_audio}")
        self.engine.runAndWait()

    def soundAudio(self):
        self.engine.say(self.text_to_speech)
        self.engine.runAndWait()
        # self.engine.stop()
    
    def check_my_inf_voices(self):
        for voice in self.voices:
            print(f"{voice}")
            # print(voice.id)


class GetDataDB(MakeSqlite, MakeDb):

    def __init__(self):

        MakeSqlite.__init__(self)
        MakeDb.__init__(self)

        self.df_db = self.connnect_to_SQLdb()
        self.my_list_of_id = self.get_consult_dblite()
        #self.delete_consult_dblite()
        #! THINK CAN MAKE BETTER WITH DATAFRAME
        # print(repr(self.df_db['Resumen del Hecho']))
        # self.df_db['Resumen del Hecho'].replace({"Siendo":'Funciola'}, regex=True)
        # print(repr(self.my_list_of_id))

        self.get_data_from_db()


    def get_data_from_db(self):
        try:

            # name_of_file_audio = ''
            # startTime = time.time()
            # print(time.ctime())
            for row in self.df_db.iloc:  
                if row[9] != None:
                # if row[4] == 'PERDIDAS HUMANAS':

                    name_of_file_audio, body_text_of_audio, hour_of_case, date_of_case = row[0],row[9],row[6],row[5]   #I

                    if name_of_file_audio not in self.my_list_of_id:
                        print("LOOK FOR THIS ID ",name_of_file_audio)
                        #THIS save audio
                        my_audio = MakeAudio(hour_of_case,date_of_case,body_text_of_audio, name_of_file_audio)
                        my_audio.saveAudio()

                        self.insert_data_in_dblite((name_of_file_audio,datetime.now(), 'type_of_case'))
                        # os.unlink(f'my_audios/{name_of_file_audio}.ogg')
                        # name_of_file_audio = name_of_file_audio
                    else:
                        pass
                        # if name_of_file_audio:
                        #     os.unlink(f'my_audios/{name_of_file_audio}')
                        # pass
            # time.sleep(2)

            # endTime = time.time()
            # elapsedTime = endTime - startTime
        except Exception as e:
            print(f'Error GetDataDB no attribute iloc:-> {e}')
            pass
        # print("Elapsed Time = %s" % elapsedTime)


class CreateTelegram2(MakeSqlite, MakeDb):

    def __init__(self):

        MakeSqlite.__init__(self)
        MakeDb.__init__(self)
        # link_auth = 'https://my.telegram.org/auth'
        # api_id = 8934265 #? FLOTA INSPECTORIA
        # api_hash = '8905f539615f4b58f9e7708d013d292b' #? FLOTA INSPECTORIA
        api_id = 8284769
        api_hash = 'd300c8b90caebfe786bf66703cefdf81'
        # bot_token = '2020198865:AAFFyifB9p998OciU7Zl0Sh1VDfHdo-4UTA'    
        phone = '18293871165'
        # username = 'ArM- S'
        # channel_invite_link = 'https://t.me/joinchat/GDPs3Jfw3mE0NTMx'
        # Handle all callback queries and check data inside the handler

        # client = TelegramClient('anon', api_id, api_hash)
        client = TelegramClient('login.session', api_id, api_hash).start(phone=phone)
        # list all sessions
        print(client.session.list_sessions())
        try:
            # client.start()
            
            # print(client.is_user_authorized())
            async def main():
                # Getting information about yourself
                me = await client.get_me()

                # print(me.stringify())
                # # You can print all the dialogs/conversations that you are part of:
                # async for dialog in client.iter_dialogs():
                #     print(dialog.name, 'has ID', dialog.id)
                #? TEST FLOTA
                # await client.log_out()
         
                while True:
                    try:
                        save_audio_and_return_name_file = GetDataDB()
                        # pass
                    except Exception as e:
                        print(repr(f"Error dentro botsave audio getdata{e}"))
                        pass
                    
                    for file_audio in os.listdir('my_audios'):
                        # FOR FILE IN MY FOLDER FILES IF NOT .OGG REMOVE FILE
                        if file_audio[-4:] == '.ogg':
                            #FLOTA_INSPECTORIA_ID = -606469599
                            GRUPO_INSPECTORIA_SE_ID = -1001450279157
                            await client.send_file(GRUPO_INSPECTORIA_SE_ID, 
                                f'my_audios/{file_audio}', 
                                thumb='logopn.jpg',
                                voice_note=True,
                                caption=f'P.N. {file_audio[:11]}',
                                audio=True) # P
                            os.unlink(f'my_audios/{file_audio}')
                        else:
                            os.unlink(f'my_audios/{file_audio}')
        finally:
            client.disconnect()
        with client:
            client.loop.run_until_complete(main())
            
        
