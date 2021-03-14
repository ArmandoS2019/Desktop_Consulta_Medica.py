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
    hemograma = db.Column(db.Boolean, default=False, nullable=False)
    conteo_de_eosinofilos = db.Column(db.Boolean, default=False, nullable=False)
    conteo_de_plaquetas = db.Column(db.Boolean, default=False, nullable=False)
    conteo_de_reticulositos = db.Column(db.Boolean, default=False, nullable=False)
    in_de_hemolozoarios = db.Column(db.Boolean, default=False, nullable=False)
    inv_de_celulas_le = db.Column(db.Boolean, default=False, nullable=False)
    eritroretroalimentacion = db.Column(db.Boolean, default=False, nullable=False)
    #--------------ORINA----------------------------
    uroanalisis_completo = db.Column(db.Boolean, default=False, nullable=False)
    dosificacion_de_proteinas_24hs = db.Column(db.Boolean, default=False, nullable=False)
    dosificacion_de_creatina_24hs = db.Column(db.Boolean, default=False, nullable=False)
    acvanilmondelico_una = db.Column(db.Boolean, default=False, nullable=False)
    albumea = db.Column(db.Boolean, default=False, nullable=False)
    prueba_de_embarazo = db.Column(db.Boolean, default=False, nullable=False)
    diecisiete_ceto = db.Column(db.Boolean, default=False, nullable=False)
    diecisiete_oh = db.Column(db.Boolean, default=False, nullable=False)
    #--------------HECES----------------------------
    estudio_de_digestion = db.Column(db.Boolean, default=False, nullable=False)
    inv_de_hermintos_protozos = db.Column(db.Boolean, default=False, nullable=False)
    inv_de_sangre_oculta = db.Column(db.Boolean, default=False, nullable=False)
    inv_de_amebas_enheces_fecales = db.Column(db.Boolean, default=False, nullable=False)
    #--------------QUIMICA SANGUINEA----------------------------
    glicemia_basal = db.Column(db.Boolean, default=False, nullable=False)
    glicemiapp = db.Column(db.Boolean, default=False, nullable=False)
    curva_tolerancia_glucosa_hs = db.Column(db.Boolean, default=False, nullable=False)
    hb_glucosilada = db.Column(db.Boolean, default=False, nullable=False)
    bun = db.Column(db.Boolean, default=False, nullable=False)
    creatina = db.Column(db.Boolean, default=False, nullable=False)
    colesterol = db.Column(db.Boolean, default=False, nullable=False)
    colesterol_idl_ldl = db.Column(db.Boolean, default=False, nullable=False)
    trigliceridos_s = db.Column(db.Boolean, default=False, nullable=False)
    lipidos_totales = db.Column(db.Boolean, default=False, nullable=False)
    cloruros = db.Column(db.Boolean, default=False, nullable=False)
    sodio = db.Column(db.Boolean, default=False, nullable=False)
    co2 = db.Column(db.Boolean, default=False, nullable=False)
    calcio = db.Column(db.Boolean, default=False, nullable=False)
    fosforo_inorganico = db.Column(db.Boolean, default=False, nullable=False)
    magnecio = db.Column(db.Boolean, default=False, nullable=False)
    acido_urico = db.Column(db.Boolean, default=False, nullable=False)
    sgpt = db.Column(db.Boolean, default=False, nullable=False)
    sgot = db.Column(db.Boolean, default=False, nullable=False)
    fosfolosa_alcalina = db.Column(db.Boolean, default=False, nullable=False)
    gammaglutami_t_ggt = db.Column(db.Boolean, default=False, nullable=False)
    bilirrubina = db.Column(db.Boolean, default=False, nullable=False)
    proteinas_totales = db.Column(db.Boolean, default=False, nullable=False)
    fructo_camina = db.Column(db.Boolean, default=False, nullable=False)
    amilasa = db.Column(db.Boolean, default=False, nullable=False)
    laptosa = db.Column(db.Boolean, default=False, nullable=False)
    fosfato_acido_total = db.Column(db.Boolean, default=False, nullable=False)
    dosificacion_hierro_senico = db.Column(db.Boolean, default=False, nullable=False)
    amonio = db.Column(db.Boolean, default=False, nullable=False)
    ck_total = db.Column(db.Boolean, default=False, nullable=False)
    ck_mb = db.Column(db.Boolean, default=False, nullable=False)
    depuracion_creatinina_endogena = db.Column(db.Boolean, default=False, nullable=False)
    proteinas_oxina_24hr = db.Column(db.Boolean, default=False, nullable=False)
    creatininas_orina24hs = db.Column(db.Boolean, default=False, nullable=False)
    lilia = db.Column(db.Boolean, default=False, nullable=False)
    #--------------SEROLOGIA----------------------------
    antiestreptotilina_o_aso = db.Column(db.Boolean, default=False, nullable=False)
    factor_reumatoideo = db.Column(db.Boolean, default=False, nullable=False)
    anticuerpos_heterotico_monotest = db.Column(db.Boolean, default=False, nullable=False)
    proteina_c_reactiva = db.Column(db.Boolean, default=False, nullable=False)
    stretozyme = db.Column(db.Boolean, default=False, nullable=False)
    anti_dna = db.Column(db.Boolean, default=False, nullable=False)
    vdrl = db.Column(db.Boolean, default=False, nullable=False)
    fta_abs = db.Column(db.Boolean, default=False, nullable=False)
    anticuerpos_antinucleares_ana = db.Column(db.Boolean, default=False, nullable=False)
    anticuerpos_antimusculo_liso = db.Column(db.Boolean, default=False, nullable=False)
    tipificacion_sanguinea = db.Column(db.Boolean, default=False, nullable=False)
    test_coommlas_directo = db.Column(db.Boolean, default=False, nullable=False)
    test_control_indirecto = db.Column(db.Boolean, default=False, nullable=False)
    citoglobulinas = db.Column(db.Boolean, default=False, nullable=False)
    prueba_embarazo_suero = db.Column(db.Boolean, default=False, nullable=False)
    #--------------HORMONAS----------------------------
    t3 = db.Column(db.Boolean, default=False, nullable=False)
    t4 = db.Column(db.Boolean, default=False, nullable=False)
    tsh = db.Column(db.Boolean, default=False, nullable=False)
    t4_libre = db.Column(db.Boolean, default=False, nullable=False)
    #--------------MICELANEOS----------------------------
    espermalograma = db.Column(db.Boolean, default=False, nullable=False)
    anti_hiv = db.Column(db.Boolean, default=False, nullable=False)
    anti_hcv = db.Column(db.Boolean, default=False, nullable=False)
    antigeno_australiano_hbshb = db.Column(db.Boolean, default=False, nullable=False)
    hbs_ag = db.Column(db.Boolean, default=False, nullable=False)
    hbe_ag = db.Column(db.Boolean, default=False, nullable=False)
    anti_hav_iggigm = db.Column(db.Boolean, default=False, nullable=False)
    anti_hbe = db.Column(db.Boolean, default=False, nullable=False)
    anti_hbs = db.Column(db.Boolean, default=False, nullable=False)
    anti_hbc_core = db.Column(db.Boolean, default=False, nullable=False)
    alfa_feto_proteinas = db.Column(db.Boolean, default=False, nullable=False)
    clamidia = db.Column(db.Boolean, default=False, nullable=False)
    rubello_igl_igm = db.Column(db.Boolean, default=False, nullable=False)
    antiocodiolipinas = db.Column(db.Boolean, default=False, nullable=False)
    herpes_uno_dos = db.Column(db.Boolean, default=False, nullable=False)
    ameba_suero = db.Column(db.Boolean, default=False, nullable=False)
    cea = db.Column(db.Boolean, default=False, nullable=False)
    ca125 = db.Column(db.Boolean, default=False, nullable=False)
    ca15_3 = db.Column(db.Boolean, default=False, nullable=False)
    ca19_9 = db.Column(db.Boolean, default=False, nullable=False)
    toxoplasmosis_igg_igm = db.Column(db.Boolean, default=False, nullable=False)
    inmunoglubolinas_iga_ic_igm = db.Column(db.Boolean, default=False, nullable=False)
    ige = db.Column(db.Boolean, default=False, nullable=False)
    fenilina = db.Column(db.Boolean, default=False, nullable=False)
    hilicobacter_pylo = db.Column(db.Boolean, default=False, nullable=False)
    vit_b12 = db.Column(db.Boolean, default=False, nullable=False)
    ac_folico = db.Column(db.Boolean, default=False, nullable=False)
    psa = db.Column(db.Boolean, default=False, nullable=False)
    hemocultivo = db.Column(db.Boolean, default=False, nullable=False)
    urocultivo = db.Column(db.Boolean, default=False, nullable=False)
    coprocultivo = db.Column(db.Boolean, default=False, nullable=False)

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
