from my_tools import CreateTelegram2, GetDataDB, MakeDb, MakeAudio, MakeSqlite, ReplaceText


if __name__ == '__main__':
    # #* MY PERFORMANCE DB DATAFRAME
    # text_comvert = ''' los Nombrado JUAN RAMON MARTE DE LOS SANTOS, Cedula de Identidad y Electoral No. 402-1525977-7,FEDERICO MARTE MARTE, 
    # Cedula de Identidad y Electoral No. 107-0002699-9, dominicano, Cedula de Identidad Personal No. 402-1227247-6,Treinta Mil pesos dominicano, en efectivo y donde 
    # procedieron a marcharseb
    # '''
    # my_audio = MakeAudio(text_comvert,'audioName')
    # my_audio.saveAudio()


    
    my_data_db = MakeDb()
    my_data_db.connnect_to_SQLdb()

    # my_data_sqlite = MakeSqlite()
    # # my_data_sqlite.insert_data_in_dblite(('name_of_file_audio','datetime.now()', 'type_of_case'))
    # data = my_data_sqlite.get_consult_dblite()
    # my_data = [x for x in data]
    # print(my_data[1])
    # my_data_sqlite.delete_consult_dblite()
    
    #? ------------TELEGRAM BOT----------
    #reduce_telebot = CreateTelegram2()
    #? ------------TELEGRAM BOT----------
    

   



   


