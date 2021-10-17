from my_tools import CreateTelegram2, GetDataDB, MakeDb, MakeAudio, MakeSqlite
from datetime import datetime
import sys

if __name__ == '__main__':
    # #* MY PERFORMANCE DB DATAFRAME
    # text_comvert = ''' los Nombrado JUAN RAMON MARTE DE LOS SANTOS, Cedula de Identidad y Electoral No. 402-1525977-7,FEDERICO MARTE MARTE, 
    # Cedula de Identidad y Electoral No. 107-0002699-9, dominicano, Cedula de Identidad Personal No. 402-1227247-6,Treinta Mil pesos dominicano, en efectivo y donde 
    # procedieron a marcharseb
    # '''
    # my_audio = MakeAudio(text_comvert,'audioName')
    # my_audio.saveAudio()
    
    # my_data_db = MakeDb()
    # my_data_db.connnect_to_SQLdb()
    # print(my_data_db)
    # my_data_sqlite = MakeSqlite()
    # my_data_sqlite.insert_data_in_dblite(('name_of_file_audio',datetime.now(), 'type_of_case'))
    # my_data_sqlite.get_consult_dblite()
    # my_data_sqlite.delete_consult_dblite()
    # start_time = time.time()
    #? ------------TELEGRAM BOT----------
    reduce_telebot = CreateTelegram2()
    #? ------------TELEGRAM BOT----------
    # print("--- %s seconds ---" % (time.time() - start_time))


    # import re
    # text_to_speech = '''Siendo  las 2332 horas del dia de 223-343434-3434-3434   CAL. C/O    DX. NUMERo la fecha, siendo        LAS hora y 
    # fecha mencionada'''.upper()

    # my_replace_text = {"\n":" ","\n\n":" ","\r":" ","\r\r":" ","\t":" ","\n\t":" ","-":"","RD$":"",
    #             "9-1-1":"NUEVE UNO UNO","CAL.":"CALIBRE","R/O":"RASO","C/O":"CABO","SGTO.":"SARGENTO","TTE.":"TENIENTE","CAP.":"CAPITÁN","MR.":"MAYOR",
    #             "1ER.":"PRIMER","2DO.":"SEGUNDO","COR.":"CORONEL","CNEL.":"CORONEL","GRAL.":"GENERAL",
    #             "DEPTO.":"DEPARTAMENTO","DPTO.":"DEPARTAMENTO","P.N.,":" ","P.N.":" ","PN.":" ","SR.":"SEÑOR","DR.":"DOCTOR","DRA.":"DOCTORA",
    #             "LIC.":"LICENCIADO","LICDO.":"LICENCIADO","LICDA.":"LICENCIADA","SRA.":"SEÑORA","SRA.":"SEÑORA",
    #             "DOM.":"DOMINICANO","DOM,":"DOMINICANO","R.D.":"REPÚBLICA DOMINICANA","D.N.":"DISTRITO NACIONAL",
    #             "AV.":"AVENIDA","S/N":"SIN NÚMERO","NO.":"NÚMERO","NUMERO":"NÚMERO","DX:":"DIAGNÓSTICO MÉDICO","DX,":"DIAGNÓSTICO MÉDICO",
    #             "DX.":"DIAGNÓSTICO MÉDICO","CED.":"CÉDULA","CED:":"CÉDULA","CEDULA":"CÉDULA",
    #             "MULTIPLE":"MÚLTIPLE","TRANSITO":"TRÁNSITO","TRAUMA":"TRÁUMA","COLISIONO":"COLISIONÓ",
    #             "MOTOR":"MOTÓR","PUBLICA":"PÚBLICA","MEDICO":"MÉDICO","PARASITO":"PARÁSITO"}
    
    # regex = re.sub("|".join(my_replace_text.keys()), lambda match: my_replace_text[match.string[match.start():match.end()]], text_to_speech)
    # print(sys.getsizeof(regex))
    # print(regex)

    # text_to_speech = str(text_to_speech).upper().replace('Siendo la fecha y hora mencionada,',' ').replace('  ',
    # ' ').replace('\t',' ').replace('\n\t',' ').replace('\n\n',' ').replace('\n',' ').replace('\r','').replace('9-1-1',
    # 'NUEVE UNO UNO').replace('\r','').replace('CAL.','CALIBRE').replace('C/O','CABO').replace('R/O','RASO').replace('CAP.','CAPITÁN').replace('MR.','MAYOR').replace('SGTO.','SARGENTO').replace('1ER.',
    # 'PRIMER').replace('2DO.','SEGUNDO').replace('TTE.','TENIENTE').replace('COR.','CORONEL').replace('CNEL.','CORONEL').replace('LIC.',
    # 'LICENCIADO').replace('LICDO.','LICENCIADO').replace('LICDA.','LICENCIADA').replace('DOM.','DOMINICANO').replace('DOM,','DOMINICANO').replace('AV.',
    # 'AVENIDA').replace('S/N','SIN NÚMERO').replace('DX,','DIAGNÓSTICO MÉDICO').replace('DX.','DIAGNÓSTICO MÉDICO').replace('DX.:','DIAGNÓSTICO MÉDICO').replace('DX:','DIAGNÓSTICO MÉDICO').replace('CED.',
    # 'CÉDULA').replace('CED:','CÉDULA').replace('CEDULA','CÉDULA').replace('NO.','NÚMERO').replace('DEPTO.','DEPARTAMENTO').replace('R.D.',
    # 'REPÚBLICA DOMINICANA').replace('D.N.','DISTRITO').replace('MULTIPLE','MÚLTIPLE').replace('-','').replace('TRANSITO',
    # 'TRÁNSITO').replace('TRAUMA','TRÁUMA').replace('COLISIONO','COLISIONÓ').replace('S/N','SIN NÚMERO').replace('RD$',' ').replace('MOTOR',
    # 'MOTÓR').replace('PUBLICA','PÚBLICA').replace('SR.','SEÑOR').replace('DR.','DOCTOR').replace('SRA.','SEÑORA').replace('DRA.','DOCTORA').replace('P.N.',' ').replace('P.N.,',
    # ' ').replace('PN.,',' ').replace('PARASITO','PARÁSITO')

    # print(sys.getsizeof(text_to_speech))
    # print(text_to_speech)


   


