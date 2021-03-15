from flask import Flask, Markup
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime


app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Inicie sesión para acceder a esta página."
login_manager.refresh_view = "login"
login_manager.needs_refresh_message =(u"Nececita autenticarse nuevamente")
login_manager.needs_refresh_message_category = "info"

app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager.init_app(app)

class MedicUser_tbl(UserMixin, db.Model):
    __tablename__ = 'MedicUser_tbl'
    id = db.Column(db.Integer, primary_key=True)

    cedula_medic = db.Column(db.String(11), unique=True)
    firstname  = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(7))
    specialty = db.Column(db.String(20))
    exequatur = db.Column(db.String(15))
    photo_profile = db.Column(db.Text)
    email_address  = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(95))
    city = db.Column(db.String(70))
    address = db.Column(db.String(70))
    house_number = db.Column(db.String(70))
    telephone = db.Column(db.String(10))
    celphone = db.Column(db.String(10))
    facebook = db.Column(db.String(90))
    instagram = db.Column(db.String(90))
    twitter = db.Column(db.String(90))
    nivel_admin  = db.Column(db.String(50))
    created_user_account = db.Column(db.DateTime, default=datetime.now)
    
    # my_relation_login = db.relationship('Logindb')
    my_relation_medicenter = db.relationship('MediCenter_tbl')
    my_relation_patient = db.relationship('Pacient_tbl')
    my_relation_consult = db.relationship('Consult_tbl')
    my_relation_indications = db.relationship('Indications_tbl')
    my_relation_prescriptions = db.relationship('Prescription_tbl')
    

class Logindb_tbl(UserMixin, db.Model):
    __tablename__ = 'Logindb_tbl'

    id = db.Column(db.Integer, primary_key=True)
    hostname  = db.Column(db.String(100))
    my_ip = db.Column(db.String(100))
    my_ip_address = db.Column(db.String(100))
    get_user = db.Column(db.String(100))
    created_try_logged = db.Column(db.DateTime, default=datetime.now)


class MediCenter_tbl(UserMixin, db.Model):
    __tablename__ = 'MediCenter_tbl'

    id = db.Column(db.Integer, primary_key=True)

    name_med_center  = db.Column(db.String(50))
    med_center_icon = db.Column(db.Text)
    city = db.Column(db.String(70))
    address = db.Column(db.String(70))
    center_number = db.Column(db.String(70))
    telephone = db.Column(db.String(10))
    facebook = db.Column(db.String(90))
    instagram = db.Column(db.String(90))
    twitter = db.Column(db.String(90))
    web = db.Column(db.String(90))

    created_medicenter = db.Column(db.DateTime, default=datetime.now)
    my_med_user_id = db.Column(db.Integer, db.ForeignKey('MedicUser_tbl.id'))


class Pacient_tbl(UserMixin, db.Model):
    __tablename__ = 'Pacient_tbl'
    id = db.Column(db.Integer, primary_key=True)

    cedula_patient = db.Column(db.String(11), unique=True)
    firstname_patient  = db.Column(db.String(50))
    lastname_patient = db.Column(db.String(50))
    email_address  = db.Column(db.String(70))
    gender_patient = db.Column(db.String(7))
    security_medical_number  = db.Column(db.String(70))
    name_security_medical  = db.Column(db.String(70))
    birthday_patient = db.Column(db.DateTime)
    city = db.Column(db.String(70))
    address = db.Column(db.String(70))
    house_number = db.Column(db.String(70))
    telephone = db.Column(db.String(10))
    celphone = db.Column(db.String(10))

    created_pacient = db.Column(db.DateTime, default=datetime.now)
    my_med_center_id = db.Column(db.Integer, db.ForeignKey('MediCenter_tbl.id'))
    my_med_user_id = db.Column(db.Integer, db.ForeignKey('MedicUser_tbl.id'))


class Consult_tbl(UserMixin, db.Model):
    __tablename__ = 'Consult_tbl'

    id = db.Column(db.Integer, primary_key=True)

    systolic = db.Column(db.Integer)
    diastolic = db.Column(db.Integer)
    pulsations = db.Column(db.Integer)
    respiratory_rhythm = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    body_mass_index = db.Column(db.Integer)
    glycemic = db.Column(db.Integer)
    comment = db.Column(db.Text())   
      
    created_consult = db.Column(db.DateTime, default=datetime.now)

    my_med_center_id = db.Column(db.Integer, db.ForeignKey('MediCenter_tbl.id'))
    my_med_user_id = db.Column(db.Integer, db.ForeignKey('MedicUser_tbl.id'))
    my_pacient_id = db.Column(db.Integer, db.ForeignKey('Pacient_tbl.id'))


class Indications_tbl(UserMixin, db.Model):
    __tablename__ = 'Indications_tbl'
    id = db.Column(db.Integer, primary_key=True)
    indication_number = db.Column(db.String(30))

    indications_date = db.Column(db.DateTime)
    #--------------HEMATOLOGIA----------------------------
    hemograma = db.Column(db.Boolean)
    conteo_de_eosinofilos = db.Column(db.Boolean)
    conteo_de_plaquetas = db.Column(db.Boolean)
    conteo_de_reticulositos = db.Column(db.Boolean)
    in_de_hemolozoarios = db.Column(db.Boolean)
    inv_de_celulas_le = db.Column(db.Boolean)
    eritroretroalimentacion = db.Column(db.Boolean)
    #--------------ORINA----------------------------
    uroanalisis_completo = db.Column(db.Boolean)
    dosificacion_de_proteinas_24hs = db.Column(db.Boolean)
    dosificacion_de_creatina_24hs = db.Column(db.Boolean)
    acvanilmondelico_una = db.Column(db.Boolean)
    albumea = db.Column(db.Boolean)
    prueba_de_embarazo = db.Column(db.Boolean)
    diecisiete_ceto = db.Column(db.Boolean)
    diecisiete_oh = db.Column(db.Boolean)
    #--------------HECES----------------------------
    estudio_de_digestion = db.Column(db.Boolean)
    inv_de_hermintos_protozos = db.Column(db.Boolean)
    inv_de_sangre_oculta = db.Column(db.Boolean)
    inv_de_amebas_enheces_fecales = db.Column(db.Boolean)
    #--------------QUIMICA SANGUINEA----------------------------
    glicemia_basal = db.Column(db.Boolean)
    glicemiapp = db.Column(db.Boolean)
    curva_tolerancia_glucosa_hs = db.Column(db.Boolean)
    hb_glucosilada = db.Column(db.Boolean)
    bun = db.Column(db.Boolean)
    creatina = db.Column(db.Boolean)
    colesterol = db.Column(db.Boolean)
    colesterol_idl_ldl = db.Column(db.Boolean)
    trigliceridos_s = db.Column(db.Boolean)
    lipidos_totales = db.Column(db.Boolean)
    cloruros = db.Column(db.Boolean)
    sodio = db.Column(db.Boolean)
    co2 = db.Column(db.Boolean)
    calcio = db.Column(db.Boolean)
    fosforo_inorganico = db.Column(db.Boolean)
    magnecio = db.Column(db.Boolean)
    acido_urico = db.Column(db.Boolean)
    sgpt = db.Column(db.Boolean)
    sgot = db.Column(db.Boolean)
    fosfolosa_alcalina = db.Column(db.Boolean)
    gammaglutami_t_ggt = db.Column(db.Boolean)
    bilirrubina = db.Column(db.Boolean)
    proteinas_totales = db.Column(db.Boolean)
    fructo_camina = db.Column(db.Boolean)
    amilasa = db.Column(db.Boolean)
    laptosa = db.Column(db.Boolean)
    fosfato_acido_total = db.Column(db.Boolean)
    dosificacion_hierro_senico = db.Column(db.Boolean)
    amonio = db.Column(db.Boolean)
    ck_total = db.Column(db.Boolean)
    ck_mb = db.Column(db.Boolean)
    depuracion_creatinina_endogena = db.Column(db.Boolean)
    proteinas_oxina_24hr = db.Column(db.Boolean)
    creatininas_orina24hs = db.Column(db.Boolean)
    lilia = db.Column(db.Boolean)
    #--------------SEROLOGIA----------------------------
    antiestreptotilina_o_aso = db.Column(db.Boolean)
    factor_reumatoideo = db.Column(db.Boolean)
    anticuerpos_heterotico_monotest = db.Column(db.Boolean)
    proteina_c_reactiva = db.Column(db.Boolean)
    stretozyme = db.Column(db.Boolean)
    anti_dna = db.Column(db.Boolean)
    vdrl = db.Column(db.Boolean)
    fta_abs = db.Column(db.Boolean)
    anticuerpos_antinucleares_ana = db.Column(db.Boolean)
    anticuerpos_antimusculo_liso = db.Column(db.Boolean)
    tipificacion_sanguinea = db.Column(db.Boolean)
    test_coommlas_directo = db.Column(db.Boolean)
    test_control_indirecto = db.Column(db.Boolean)
    citoglobulinas = db.Column(db.Boolean)
    prueba_embarazo_suero = db.Column(db.Boolean)
    #--------------HORMONAS----------------------------
    t3 = db.Column(db.Boolean)
    t4 = db.Column(db.Boolean)
    tsh = db.Column(db.Boolean)
    t4_libre = db.Column(db.Boolean)
    #--------------MICELANEOS----------------------------
    espermalograma = db.Column(db.Boolean)
    anti_hiv = db.Column(db.Boolean)
    anti_hcv = db.Column(db.Boolean)
    antigeno_australiano_hbshb = db.Column(db.Boolean)
    hbs_ag = db.Column(db.Boolean)
    hbe_ag = db.Column(db.Boolean)
    anti_hav_iggigm = db.Column(db.Boolean)
    anti_hbe = db.Column(db.Boolean)
    anti_hbs = db.Column(db.Boolean)
    anti_hbc_core = db.Column(db.Boolean)
    alfa_feto_proteinas = db.Column(db.Boolean)
    clamidia = db.Column(db.Boolean)
    rubello_igl_igm = db.Column(db.Boolean)
    antiocodiolipinas = db.Column(db.Boolean)
    herpes_uno_dos = db.Column(db.Boolean)
    ameba_suero = db.Column(db.Boolean)
    cea = db.Column(db.Boolean)
    ca125 = db.Column(db.Boolean)
    ca15_3 = db.Column(db.Boolean)
    ca19_9 = db.Column(db.Boolean)
    toxoplasmosis_igg_igm = db.Column(db.Boolean)
    inmunoglubolinas_iga_ic_igm = db.Column(db.Boolean)
    ige = db.Column(db.Boolean)
    fenilina = db.Column(db.Boolean)
    hilicobacter_pylo = db.Column(db.Boolean)
    vit_b12 = db.Column(db.Boolean)
    ac_folico = db.Column(db.Boolean)
    psa = db.Column(db.Boolean)
    hemocultivo = db.Column(db.Boolean)
    urocultivo = db.Column(db.Boolean)
    coprocultivo = db.Column(db.Boolean)

    created_indications = db.Column(db.DateTime, default=datetime.now)
    my_med_center_id = db.Column(db.Integer, db.ForeignKey('MediCenter_tbl.id'))
    my_med_user_id = db.Column(db.Integer, db.ForeignKey('MedicUser_tbl.id'))
    my_pacient_id = db.Column(db.Integer, db.ForeignKey('Pacient_tbl.id'))


class Prescription_tbl(UserMixin, db.Model):
    __tablename__ = 'Prescription_tbl'

    id = db.Column(db.Integer, primary_key=True)
    prescription_number = db.Column(db.String(30))
    prescription_date = db.Column(db.DateTime)

    prescription_1  = db.Column(db.String(50))
    prescription_2  = db.Column(db.String(50))
    prescription_3  = db.Column(db.String(50))
    prescription_4  = db.Column(db.String(50))
    prescription_5  = db.Column(db.String(50))
    prescription_6  = db.Column(db.String(50))
    prescription_7  = db.Column(db.String(50))
    prescription_8  = db.Column(db.String(50))
    prescription_9  = db.Column(db.String(50))
    prescription_10  = db.Column(db.String(50))
    prescription_11  = db.Column(db.String(50))
    
    created_consult = db.Column(db.DateTime, default=datetime.now)
    my_med_center_id = db.Column(db.Integer, db.ForeignKey('MediCenter_tbl.id'))
    my_med_user_id = db.Column(db.Integer, db.ForeignKey('MedicUser_tbl.id'))
    my_pacient_id = db.Column(db.Integer, db.ForeignKey('Pacient_tbl.id'))
