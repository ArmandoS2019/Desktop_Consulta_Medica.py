
from app import db
# from app import Userdb, Directionsdb,Eventtype
#-------------------IMPORT TBL ------------------------------
from app import MedicUser_tbl
#-------------------IMPORT TBL ------------------------------
from flask_wtf import FlaskForm
from flask import flash, session
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash

from wtforms import StringField, PasswordField, RadioField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, Required, EqualTo, NumberRange, Regexp
from wtforms.validators import ValidationError
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.widgets import TextArea,Select
from wtforms.fields.html5 import EmailField, IntegerField, DateField, TimeField, TelField,URLField
from datetime import datetime

#------------------------------------------------------------
import pymysql
pymysql.install_as_MySQLdb()
#------------------------------------------------------------

# direction_list = db.session.query(Directionsdb.id,Directionsdb.name_dir).all()
# event_list = db.session.query(Eventtype.id,Eventtype.name_event).all()


def check_ced_registered(form, field):
    #TODO if field.data == current_user.cedula_medic:
        # flash("Ya te encuentras en sesion", "danger")
    user = MedicUser_tbl.query.filter_by(cedula_medic =field.data).first()
    if user:
        raise ValidationError('Cedula se encuentra registrada')

def check_mail_registered(form, field):
    # medic_users = db.session.query(MedicUser_tbl).all()
    mail_user = MedicUser_tbl.query.filter_by(email_address=field.data).first()
    if mail_user:
        raise ValidationError('Email se encuentra registrado')

def check_length_ced(form, field):
    if len(str(field.data)) != 11:
        raise ValidationError('Cedula debe contener 11 numeros')


class LoginForm(FlaskForm):
    email_address = EmailField('', validators=[InputRequired('Campo requerido')])
    password = PasswordField('', validators=[InputRequired('Campo requerido')])


class RegisterForm(FlaskForm):

    cedula_medic = StringField('Cedula |sin-',validators=[InputRequired('Campo requerido'),
                                              Regexp('\d{11}',message='Cedula erronea')])
    # cedula_medic = StringField('Cedula |sin-',validators=[InputRequired('Campo requerido'),
    #                                           Regexp('\d{11}',message='Cedula erronea'),
    #                                           check_ced_registered])
    
    firstname = StringField('Nombre',validators=[InputRequired('Campo requerido')])
    lastname = StringField('Apellido',validators=[InputRequired('Campo requerido')])
    birthday = DateField('Fecha Nacimiento',validators=[InputRequired('Campo requerido')])
    gender = RadioField('Sexo', choices=[('M','M'),('F','F')],validators=[InputRequired('Campo requerido')])

    email_address = EmailField('Email', validators=[InputRequired('Campo requerido')])
    # email_address = EmailField('Email', validators=[InputRequired('Campo requerido'),check_mail_registered])
    exequatur = StringField('Exequatur',validators=[InputRequired('Campo requerido')])
    password = PasswordField('Contraseña', validators=[InputRequired('Contraseña requerida'),EqualTo('confirm',message='Repetir contraseña')])
    confirm = PasswordField('Repetir contraseña')    
    #TODO: THIS WILL BE A DATABASE CITY
    city = [("",""),('La Romana','La Romana'),('Distrito Nacional','Distrito Nacional'),
                    ('Santiado d/l caballeros','Santiado d/l caballeros')]
    city = SelectField('Ciudad',choices=city, validators=[InputRequired('Campo requerido')])
    address = StringField('Direccion',validators=[InputRequired('Campo requerido')])
    house_number = StringField('',validators=[InputRequired('Campo requerido')])
    telephone = TelField('',validators=[InputRequired('Campo requerido')])
    celphone = StringField('',validators=[InputRequired('Campo requerido')])
    facebook = StringField('',validators=[InputRequired('Campo requerido')])
    instagram = StringField('',validators=[InputRequired('Campo requerido')])
    twitter = StringField('',validators=[InputRequired('Campo requerido')])
    
    nivel_admin = [("",""),('1','Basico'),('2','Medio'),
                    ('3','Administrador')]
    nivel_admin = SelectField('Nivel administrador',choices=nivel_admin, validators=[InputRequired('Campo requerido')])
    

class MedicenterForm(FlaskForm):
    name_med_center = StringField('Nombre del centro medico',validators=[InputRequired('Campo requerido')])

    city = [("",""),('La Romana','La Romana'),('Distrito Nacional','Distrito Nacional'),
                    ('Santiado d/l caballeros','Santiado d/l caballeros')]
    city = SelectField('Ciudad',choices=city, validators=[InputRequired('Campo requerido')])

    med_center_icon = FileField('Logo del centro')
    
    address = StringField('Direccion',validators=[InputRequired('Campo requerido')])
    center_number = StringField('Numero res.',validators=[InputRequired('Campo requerido')])
    telephone = TelField('Telefono',validators=[InputRequired('Campo requerido')])
    
    facebook = URLField('Facebook')
    instagram = URLField('Instagram')
    twitter = URLField('Twitter')
    web = URLField('Pagina Web')



class PacientForm(FlaskForm):

    cedula_patient = StringField('Cedula |sin-',validators=[InputRequired('Campo requerido'),
                                              Regexp('\d{11}',message='Cedula erronea')])
                                              
    firstname_patient = StringField('Nombre',validators=[InputRequired('Campo requerido')])
    lastname_patient = StringField('Apellido',validators=[InputRequired('Campo requerido')])
    birthday = DateField('Fecha Nacimiento',validators=[InputRequired('Campo requerido')])
    email_address = EmailField('Email', validators=[InputRequired('Campo requerido')])
    gender_patient = RadioField('Sexo', choices=[('M','M'),('F','F')],validators=[InputRequired('Campo requerido')])
    security_medical_number = StringField('Num. seguro.',validators=[InputRequired('Campo requerido')])

    name_security_medical = [("",""),('Senasa','Senasa'),('ARS Humano','ARS Humano'),
                    ('ARS Pali','ARS Pali')]
    name_security_medical = SelectField('Seguro',choices=name_security_medical, validators=[InputRequired('Campo requerido')])
    address = StringField('Direccion',validators=[InputRequired('Campo requerido')])

    #TODO: THIS WILL BE A DATABASE CITY
    city = [("",""),('La Romana','La Romana'),('Distrito Nacional','Distrito Nacional'),
                    ('Santiado d/l caballeros','Santiado d/l caballeros')]
    city = SelectField('Ciudad',choices=city, validators=[InputRequired('Campo requerido')])

    house_number = StringField('Numero res.',validators=[InputRequired('Campo requerido')])
    celphone = TelField('Celular',validators=[InputRequired('Campo requerido')])
    telephone = TelField('Telefono',validators=[InputRequired('Campo requerido')])
    
 
class ConsultForm(FlaskForm):

    systolic = IntegerField('Sistólica',validators=[InputRequired('Campo requerido')])
    diastolic = IntegerField('Diastólica',validators=[InputRequired('Campo requerido')])
    pulsations = IntegerField('Pulsaciones',validators=[InputRequired('Campo requerido')])
    respiratory_rhythm = IntegerField('Ritmo respiratorio',validators=[InputRequired('Campo requerido')])
    temperature = IntegerField('Temperatura',validators=[InputRequired('Campo requerido')])
    height = IntegerField('Altura',validators=[InputRequired('Campo requerido')])
    weight = IntegerField('Peso',validators=[InputRequired('Campo requerido')])
    body_mass_index = IntegerField('IMC',validators=[InputRequired('Campo requerido')])
    glycemic = IntegerField('Glicemia',validators=[InputRequired('Campo requerido')])
    comment = TextAreaField('', render_kw={"rows": 3, "cols": 11}, validators=[InputRequired('Campo requerido')])

    
 
class PrescriptionForm(FlaskForm):
    
    prescription_date = DateField('Fecha para la receta',validators=[InputRequired('Campo requerido')])
    prescription_1 = StringField('Llenar por orden cada prescripcion',validators=[InputRequired('Campo requerido')])
    prescription_2 = StringField('')
    prescription_3 = StringField('')
    prescription_4 = StringField('')
    prescription_5 = StringField('')
    prescription_6 = StringField('')
    prescription_7 = StringField('Orden 7 prescripcion')
    prescription_8 = StringField('')
    prescription_9 = StringField('')
    prescription_10 = StringField('')
    prescription_11 = StringField('')



class IndicationForm(FlaskForm):

    indications_date = DateField('',validators=[InputRequired('Campo requerido')])
    # #--------------HEMATOLOGIA----------------------------
    hemograma = BooleanField('')
    conteo_de_eosinofilos = BooleanField('')
    conteo_de_plaquetas = BooleanField('')
    conteo_de_reticulositos = BooleanField('')
    in_de_hemolozoarios = BooleanField('')
    inv_de_celulas_le = BooleanField('')
    eritroretroalimentacion = BooleanField('')
    # #--------------ORINA----------------------------
    uroanalisis_completo = BooleanField('')
    dosificacion_de_proteinas_24hs = BooleanField('')
    dosificacion_de_creatina_24hs = BooleanField('')
    acvanilmondelico_una = BooleanField('')
    albumea = BooleanField('')
    prueba_de_embarazo = BooleanField('')
    diecisiete_ceto = BooleanField('')
    diecisiete_oh = BooleanField('')
    # #--------------HECES----------------------------
    estudio_de_digestion = BooleanField('')
    inv_de_hermintos_protozos = BooleanField('')
    inv_de_sangre_oculta = BooleanField('')
    inv_de_amebas_enheces_fecales = BooleanField('')
    # #--------------QUIMICA SANGUINEA----------------------------
    glicemia_basal = BooleanField('')
    glicemiapp = BooleanField('')
    curva_tolerancia_glucosa_hs = BooleanField('')
    hb_glucosilada = BooleanField('')
    bun = BooleanField('')
    creatina = BooleanField('')
    colesterol = BooleanField('')
    colesterol_idl_ldl = BooleanField('')
    trigliceridos_s = BooleanField('')
    lipidos_totales = BooleanField('')
    cloruros = BooleanField('')
    sodio = BooleanField('')
    co2 = BooleanField('')
    calcio = BooleanField('')
    fosforo_inorganico = BooleanField('')
    magnecio = BooleanField('')
    acido_urico = BooleanField('')
    sgpt = BooleanField('')
    fosfolosa_alcalina = BooleanField('')
    gammaglutami_t_ggt = BooleanField('')
    bilirrubina = BooleanField('')
    proteinas_totales = BooleanField('')
    fructo_camina = BooleanField('')
    amilasa = BooleanField('')
    laptosa = BooleanField('')
    fosfato_acido_total = BooleanField('')
    dosificacion_hierro_senico = BooleanField('')
    amonio = BooleanField('')
    ck_total = BooleanField('')
    ck_mb = BooleanField('')
    depuracion_creatinina_endogena = BooleanField('')
    proteinas_oxina_24hr = BooleanField('')
    creatininas_orina24hs = BooleanField('')
    lilia = BooleanField('')
    # #--------------SEROLOGIA----------------------------
    antiestreptotilina_o_aso = BooleanField('')
    factor_reumatoideo = BooleanField('')
    anticuerpos_heterotico_monotest = BooleanField('')
    proteina_c_reactiva = BooleanField('')
    stretozyme = BooleanField('')
    anti_dna = BooleanField('')
    vdrl = BooleanField('')
    fta_abs = BooleanField('')
    anticuerpos_antinucleares_ana = BooleanField('')
    anticuerpos_antimusculo_liso = BooleanField('')
    tipificacion_sanguinea = BooleanField('')
    test_coommlas_directo = BooleanField('')
    test_control_indirecto = BooleanField('')
    citoglobulinas = BooleanField('')
    prueba_embarazo_suero = BooleanField('')
    # #--------------HORMONAS----------------------------
    t3 = BooleanField('')
    t4 = BooleanField('')
    tsh = BooleanField('')
    t4_libre = BooleanField('')
    # #--------------MICELANEOS----------------------------
    espermalograma = BooleanField('')
    anti_hiv = BooleanField('')
    anti_hcv = BooleanField('')
    antigeno_australiano_hbshb = BooleanField('')
    hbs_ag = BooleanField('')
    hbe_ag = BooleanField('')
    anti_hav_iggigm = BooleanField('')
    anti_hbe = BooleanField('')
    anti_hbs = BooleanField('')
    anti_hbc_core = BooleanField('')
    alfa_feto_proteinas = BooleanField('')
    clamidia = BooleanField('')
    rubello_igl_igm = BooleanField('')
    antiocodiolipinas = BooleanField('')
    herpes_uno_dos = BooleanField('')
    ameba_suero = BooleanField('')
    cea = BooleanField('')
    ca125 = BooleanField('')
    ca15_3 = BooleanField('')
    ca19_9 = BooleanField('')
    toxoplasmosis_igg_igm = BooleanField('')
    inmunoglubolinas_iga_ic_igm = BooleanField('')
    ige = BooleanField('')
    fenilina = BooleanField('')
    hilicobacter_pylo = BooleanField('')
    vit_b12 = BooleanField('')
    ac_folico = BooleanField('')
    psa = BooleanField('')
    hemocultivo = BooleanField('')
    urocultivo = BooleanField('')
    coprocultivo = BooleanField('')

