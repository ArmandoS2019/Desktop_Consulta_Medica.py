from flask import render_template, request, flash, Markup, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_login import login_user, login_required, current_user, logout_user, fresh_login_required

from app import app, db
from app import login_manager
# ---------------DATABASE------------------
from app import MedicUser_tbl, MediCenter_tbl, Pacient_tbl, Consult_tbl, Prescription_tbl, Indications_tbl
# ---------------FORMS------------------
from app.forms import LoginForm, RegisterForm, MedicenterForm, PacientForm, ConsultForm, PrescriptionForm, IndicationForm
# --------------------------------------
import pymysql
pymysql.install_as_MySQLdb()


@login_manager.user_loader
def load_user(user_id):
    return MedicUser_tbl.query.get(int(user_id))

@app.before_request
def before_request():
    session.permanent = False
    app.permanent_session_lifetime = timedelta(minutes=1)


@app.errorhandler(404)
@login_required
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('404.html'), 500


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    # my_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    # get_user = getpass.getuser()
    # # -----------------------------------------------------------------------
    if current_user.is_authenticated:
        flash(Markup(f'{current_user.firstname} ya te encuentras en sesion.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
        return redirect(url_for('base'))

    if request.method == "POST" and form.validate_on_submit(): 

        # new_user_account = Logindb(hostname=str(hostname).upper().strip(),
        # my_ip=str(ip_address).upper().strip(),my_ip_address=str(ip_address).upper().strip(),get_user=str(get_user).upper().strip(),created_inf_logged=datetime.now())
        # db.session.add(new_user_account)
        # db.session.commit()

        email = MedicUser_tbl.query.filter_by(email_address=form.email_address.data).first()

        if not email or check_password_hash(email.password,form.password.data)==False:
            flash(Markup('Usuario o Contraseña incorrecto.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "danger")
            return redirect(url_for('login'))
        else:
            # session.permanent = form.admin_or_user.data
            login_user(email, remember=True)
            flash(Markup(f'Bienvenido {current_user.firstname}.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "warning")
            return redirect(url_for('base'))

    return render_template('public/login.html', form=form)


@app.route('/register', methods=['GET','POST'])
@login_required
def register():
    form = RegisterForm()
    medic_users = db.session.query(MedicUser_tbl).all()
    #TODO get data form medic register, next heritance JQUERY DATATABLE
    if request.method == "POST" and form.validate_on_submit(): 
        try:
            new_user_account = MedicUser_tbl(
            cedula_medic=form.cedula_medic.data,firstname=form.firstname.data,
            lastname=form.lastname.data,birthday=form.birthday.data,
            gender=form.gender.data,exequatur=form.exequatur.data,
            email_address=form.email_address.data,
            password=generate_password_hash(form.password.data),
            house_number=form.house_number.data,telephone=form.telephone.data,
            celphone=form.celphone.data,facebook=form.facebook.data,
            instagram=form.instagram.data,twitter=form.twitter.data,
            nivel_admin=form.nivel_admin.data,created_user_account=datetime.now())

            db.session.add(new_user_account)
            db.session.commit()
            flash(Markup('Registro exitoso.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
            return redirect(url_for('register'))
        except:
            flash(Markup('Cedula duplicada u otro error.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'),"danger")

    return render_template('admin/register.html', form=form, medic_users=medic_users)


@app.route('/mediccenter')
@app.route('/mediccenter', methods=['GET','POST'])
@login_required
def mediccenter():
    form_mcenter = MedicenterForm()

    medic_center = db.session.query(MediCenter_tbl).all()
    total_pacients = db.session.query(Pacient_tbl).count()
    center_count = db.session.query(MediCenter_tbl).count()

    if request.method == "POST" and form_mcenter.validate_on_submit(): 
        try:
            new_medic_center = MediCenter_tbl(
            name_med_center=str(form_mcenter.name_med_center.data).upper(),
            med_center_icon=form_mcenter.med_center_icon.data,
            city=str(form_mcenter.city.data).upper(),address=str(form_mcenter.address.data).upper(),
            center_number=form_mcenter.center_number.data,telephone=form_mcenter.telephone.data,
            facebook=form_mcenter.facebook.data,instagram=form_mcenter.instagram.data,
            twitter=form_mcenter.twitter.data,
            web=form_mcenter.web.data,created_medicenter=datetime.now())

            db.session.add(new_medic_center)
            db.session.commit()

            flash(Markup('Registro exitoso.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
            return redirect(url_for('mediccenter'))
        except:
            flash(Markup('Algun error al guardar los datos.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'),"danger")

    return render_template('for_user/mediccenter.html', form_mcenter=form_mcenter, 
                                               medic_center=medic_center,
                                               total_pacients=total_pacients,
                                               center_count=center_count)


@app.route('/pacient', methods=['GET','POST'])
@app.route('/pacient/<id>/center', methods=['GET','POST'])
@login_required
def pacient(id=None):

    form_pacient = PacientForm()

    medic_center = db.session.query(MediCenter_tbl).filter(MediCenter_tbl.id==id).first()
    pacients = db.session.query(Pacient_tbl).filter(Pacient_tbl.my_med_center_id==id).order_by(Pacient_tbl.created_pacient.desc()).all()
    pacient_count = db.session.query(Pacient_tbl).filter(Pacient_tbl.my_med_center_id==id).count()
    
    pacients_tbl = {'pacients':pacients,
                    'pacient_count':pacient_count,
                    'medic_center':medic_center}

    """TODO ESTUDIAR LA LOGICA, SI EL PACIENTE YA ESTA RESTRADO POR OTRO DOCTOR Y TIENE HISTORIAL, SOLICITAR
    PERMISO, LE LLEGA UNA NOTIFICACION, SI ESTE ACEPTA, ENTONCES AL SOLICITANTE SE LE DA PERMISO
    Y AGREGA HISTORIAL DEL PACIENTE, PERO DEJAR GUARDAR EL PERFIL, SI YA ESTA REGISTRADO Y ESTA EN OTRO PASA ESTO"""
    
    if request.method == "POST" and form_pacient.validate_on_submit(): 
        # try:
        add_new_pacient = Pacient_tbl(
        cedula_patient=str(form_pacient.cedula_patient.data).upper(),
        firstname_patient=str(form_pacient.firstname_patient.data).upper(),
        lastname_patient=str(form_pacient.lastname_patient.data).upper(),
        birthday_patient=str(form_pacient.birthday.data).upper(),
        gender_patient=form_pacient.gender_patient.data,
        address=form_pacient.address.data,
        city=form_pacient.city.data,
        house_number=form_pacient.house_number.data,
        name_security_medical=form_pacient.name_security_medical.data,
        security_medical_number=form_pacient.security_medical_number.data,
        celphone=form_pacient.celphone.data,
        telephone=form_pacient.telephone.data,
        email_address=form_pacient.email_address.data,
        my_med_center_id=id,
        created_pacient=datetime.now())

        db.session.add(add_new_pacient)
        db.session.commit()

        flash(Markup('Registro exitoso.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
        # return render_template('for_user/pacient.html', form_pacient=form_pacient, 
        #                                        pacients_tbl=pacients_tbl)
        return redirect(url_for('pacient', id=id))

        # # except:
        #     flash(Markup('Algun error al guardar los datos.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'),"danger")

    return render_template('for_user/pacient.html', form_pacient=form_pacient, 
                                               pacients_tbl=pacients_tbl)



@app.route('/evaluations')
@app.route('/evaluations/<id>', methods=['GET','POST'])
@login_required
def evaluations(id=None):
    form_consult = ConsultForm()
    form_prescription = PrescriptionForm()
    form_indication = IndicationForm()

    pacient = db.session.query(Pacient_tbl).filter(Pacient_tbl.id==id).first()
    consults_pacient_added = db.session.query(Consult_tbl).filter(Consult_tbl.my_pacient_id==id).order_by(Consult_tbl.created_consult.desc()).all()
    consults_prescriptions = db.session.query(Prescription_tbl).all()
    consult_pacient_count = db.session.query(Consult_tbl).filter(Consult_tbl.my_pacient_id==id).count()
    
    consults_tbl = {'pacient':pacient,
                    'consults_pacient_added':consults_pacient_added,
                    'consults_prescriptions':consults_prescriptions,
                    'consult_pacient_count':consult_pacient_count}
    """TODO ESTUDIAR LA LOGICA, SI EL PACIENTE YA ESTA RESTRADO POR OTRO DOCTOR Y TIENE HISTORIAL, SOLICITAR
    PERMISO, LE LLEGA UNA NOTIFICACION, SI ESTE ACEPTA, ENTONCES AL SOLICITANTE SE LE DA PERMISO
    Y AGREGA HISTORIAL DEL PACIENTE, PERO DEJAR GUARDAR EL PERFIL, SI YA ESTA REGISTRADO Y ESTA EN OTRO PASA ESTO"""
        
    if request.method == "POST" and form_consult.validate_on_submit(): 
        # try:
        add_new_med_consult = Consult_tbl(
        systolic=form_consult.systolic.data,
        diastolic=form_consult.diastolic.data,
        pulsations=form_consult.pulsations.data,
        respiratory_rhythm=form_consult.respiratory_rhythm.data,
        temperature=form_consult.temperature.data,
        height=form_consult.height.data,
        weight=form_consult.weight.data,
        body_mass_index=form_consult.systolic.data,
        glycemic=form_consult.systolic.data,
        comment=form_consult.systolic.data,
        my_pacient_id=id,
        created_consult=datetime.now())

        db.session.add(add_new_med_consult)
        db.session.commit()

        flash(Markup('Registro exitoso.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
        return redirect(url_for('evaluations', id=id))

        # except:
            # flash(Markup('Algun error al guardar los datos.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'),"danger")

    if request.method == "POST" and form_prescription.validate_on_submit(): 
        # try:

        add_new_receta = Prescription_tbl(
        prescription_number=f"0001-{ datetime.now().strftime('%Y') }",
        prescription_date=form_prescription.prescription_date.data,
        prescription_1=form_prescription.prescription_1.data,
        prescription_2=form_prescription.prescription_2.data,
        prescription_3=form_prescription.prescription_3.data,
        prescription_4=form_prescription.prescription_4.data,
        prescription_5=form_prescription.prescription_5.data,
        prescription_6=form_prescription.prescription_6.data,
        prescription_7=form_prescription.prescription_7.data,
        prescription_8=form_prescription.prescription_8.data,
        prescription_9=form_prescription.prescription_9.data,
        prescription_10=form_prescription.prescription_10.data,
        prescription_11=form_prescription.prescription_11.data,
        my_pacient_id=id,
        created_consult=datetime.now())
        
        db.session.add(add_new_receta)
        db.session.commit()

        flash(Markup('Registro exitoso.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
        # return render_template('for_user/pacient.html', form_pacient=form_pacient, 
        #                                        pacients_tbl=pacients_tbl)
        return redirect(url_for('evaluations', id=id))

    if request.method == "POST" and form_indication.validate_on_submit(): 
        # try:

        add_new_indication = Indications_tbl(
        indication_number=f"0001-{ datetime.now().strftime('%Y') }",
        indications_date=form_indication.indications_date.data,
        hemograma=form_indication.hemograma.data,
        conteo_de_eosinofilos=form_indication.conteo_de_eosinofilos.data,
        conteo_de_plaquetas=form_indication.conteo_de_plaquetas.data,
        conteo_de_reticulositos=form_indication.conteo_de_reticulositos.data,
        in_de_hemolozoarios=form_indication.in_de_hemolozoarios.data,
        inv_de_celulas_le=form_indication.inv_de_celulas_le.data,
        eritroretroalimentacion=form_indication.eritroretroalimentacion.data,

        my_pacient_id=id,
        created_consult=datetime.now())
        
        db.session.add(add_new_receta)
        db.session.commit()

        flash(Markup('Registro exitoso.  <a type="button" class="close" data-dismiss="alert" aria-label="close">&times;</a>'), "success")
        # return render_template('for_user/pacient.html', form_pacient=form_pacient, 
        #                                        pacients_tbl=pacients_tbl)
        return redirect(url_for('evaluations', id=id))


    return render_template('for_user/evaluations.html', form_consult=form_consult, 
                                                        form_prescription=form_prescription,
                                                        form_indication=form_indication,
                                                        consults_tbl=consults_tbl)




@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/test')
def test():
    return render_template('forms.html')

@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))





if __name__=='__main__':   
    db.create_all()
    app.run()

