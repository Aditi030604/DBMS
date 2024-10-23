from bottle import Bottle, template, request, redirect
import mysql.connector

app = Bottle()

# MySQL connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="aditi0306",  # Update with your MySQL password
        database="management"
    )

### ROUTES FOR VOLUNTEERS ###
@app.route('/volunteers')
def list_volunteers():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Volunteers")
    volunteers = cursor.fetchall()
    cursor.close()
    db.close()
    return template('volunteer_list', volunteers=volunteers, title='Volunteers')

@app.route('/register_volunteer', method=['GET', 'POST'])
def register_volunteer():
    if request.method == 'POST':
        name = request.forms.get('name')
        email = request.forms.get('email')
        phone = request.forms.get('phone')
        status = request.forms.get('status')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Volunteers (VName, VEmail, VPhoneNo, VStatus) VALUES (%s, %s, %s, %s)", 
                       (name, email, phone, status))
        db.commit()
        cursor.close()
        db.close()
        redirect('/volunteers')
    else:
        return template('volunteer_form', title='Register Volunteer')

### ROUTES FOR ORGANIZATIONS ###
@app.route('/organizations')
def list_organizations():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Organizations")
    organizations = cursor.fetchall()
    cursor.close()
    db.close()
    return template('organization_list', organizations=organizations, title='Organizations')

@app.route('/register_organization', method=['GET', 'POST'])
def register_organization():
    if request.method == 'POST':
        org_name = request.forms.get('org_name')
        poc_name = request.forms.get('poc_name')
        poc_email = request.forms.get('email')
        poc_phone = request.forms.get('phone')
        location = request.forms.get('location')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Organizations (OrganizationName, POCName, POCEmail, POCPhoneNo, Location) VALUES (%s, %s, %s, %s, %s)", 
                       (org_name, poc_name, poc_email, poc_phone, location))
        db.commit()
        cursor.close()
        db.close()
        redirect('/organizations')
    else:
        return template('organization_form', title='Register Organization')

### ROUTES FOR SKILLS ###
@app.route('/skills')
def list_skills():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Skills")
    skills = cursor.fetchall()
    cursor.close()
    db.close()
    return template('skill_list', skills=skills, title='Skills')

@app.route('/register_skill', method=['GET', 'POST'])
def register_skill():
    if request.method == 'POST':
        skill_name = request.forms.get('skill_name')
        skill_description = request.forms.get('skill_description')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Skills (SkillName, SkillDescription) VALUES (%s, %s)", 
                       (skill_name, skill_description))
        db.commit()
        cursor.close()
        db.close()
        redirect('/skills')
    else:
        return template('skill_form', title='Register Skill')

### ROUTES FOR RESOURCES ###
@app.route('/resources')
def list_resources():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Resources")
    resources = cursor.fetchall()
    cursor.close()
    db.close()
    return template('resource_list', resources=resources, title='Resources')

@app.route('/register_resource', method=['GET', 'POST'])
def register_resource():
    if request.method == 'POST':
        resource_name = request.forms.get('resource_name')
        resource_description = request.forms.get('resource_description')
        quantity = request.forms.get('quantity')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Resources (ResourceName, ResourceDescription, Quantity) VALUES (%s, %s, %s)", 
                       (resource_name, resource_description, quantity))
        db.commit()
        cursor.close()
        db.close()
        redirect('/resources')
    else:
        return template('resource_form', title='Register Resource')

### ROUTES FOR ASSIGNMENTS ###
@app.route('/assignments')
def list_assignments():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM VolunteerAssignments")
    assignments = cursor.fetchall()
    cursor.close()
    db.close()
    return template('assignment_list', assignments=assignments, title='Assignments')

@app.route('/register_assignment', method=['GET', 'POST'])
def register_assignment():
    if request.method == 'POST':
        assignment_date = request.forms.get('assignment_date')
        volunteer_id = request.forms.get('volunteer_id')
        organization_id = request.forms.get('organization_id')
        status = request.forms.get('status')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO VolunteerAssignments (AssignmentDate, VolunteerId, OrganizationId, Status) VALUES (%s, %s, %s, %s)", 
                       (assignment_date, volunteer_id, organization_id, status))
        db.commit()
        cursor.close()
        db.close()
        redirect('/assignments')
    else:
        return template('assignment_form', title='Register Assignment')

### ROUTES FOR DONATIONS ###
@app.route('/donations')
def list_donations():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Donations")
    donations = cursor.fetchall()
    cursor.close()
    db.close()
    return template('donation_list', donations=donations, title='Donations')

@app.route('/register_donation', method=['GET', 'POST'])
def register_donation():
    if request.method == 'POST':
        donation_date = request.forms.get('donation_date')
        volunteer_id = request.forms.get('volunteer_id')
        payment_type = request.forms.get('payment_type')
        amount = request.forms.get('amount')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Donations (DonationDate, VolunteerId, PaymentType, Amount) VALUES (%s, %s, %s, %s)", 
                       (donation_date, volunteer_id, payment_type, amount))
        db.commit()
        cursor.close()
        db.close()
        redirect('/donations')
    else:
        return template('donation_form', title='Register Donation')

### ROUTES FOR TRAINERS ###
@app.route('/trainers')
def list_trainers():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Trainers")
    trainers = cursor.fetchall()
    cursor.close()
    db.close()
    return template('trainer_list', trainers=trainers, title='Trainers')

@app.route('/register_trainer', method=['GET', 'POST'])
def register_trainer():
    if request.method == 'POST':
        trainer_name = request.forms.get('trainer_name')
        skill_expertise = request.forms.get('skill_expertise')
        contact_info = request.forms.get('contact_info')
        organization_id = request.forms.get('organization_id')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Trainers (TrainerName, SkillExpertise, ContactInfo, OrganizationId) VALUES (%s, %s, %s, %s)", 
                       (trainer_name, skill_expertise, contact_info, organization_id))
        db.commit()
        cursor.close()
        db.close()
        redirect('/trainers')
    else:
        return template('trainer_form', title='Register Trainer')

### ROUTES FOR SESSIONS ###
@app.route('/sessions')
def list_sessions():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM TrainingSessions")
    sessions = cursor.fetchall()
    cursor.close()
    db.close()
    return template('session_list', sessions=sessions, title='Sessions')

@app.route('/register_session', method=['GET', 'POST'])
def register_session():
    if request.method == 'POST':
        material_title = request.forms.get('material_title')
        trainer_id = request.forms.get('trainer_id')
        skill_id = request.forms.get('skill_id')
        session_date = request.forms.get('session_date')
        duration = request.forms.get('duration')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO TrainingSessions (MaterialTitle, TrainerId, SkillId, Date, Duration) VALUES (%s, %s, %s, %s, %s)", 
                       (material_title, trainer_id, skill_id, session_date, duration))
        db.commit()
        cursor.close()
        db.close()
        redirect('/sessions')
    else:
        return template('session_form', title='Register Session')

### ROUTES FOR MATERIALS ###
@app.route('/materials')
def list_materials():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM TrainingMaterials")
    materials = cursor.fetchall()
    cursor.close()
    db.close()
    return template('material_list', materials=materials, title='Materials')

@app.route('/register_material', method=['GET', 'POST'])
def register_material():
    if request.method == 'POST':
        material_title = request.forms.get('material_title')
        resource_link = request.forms.get('resource_link')

        # Insert into database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO TrainingMaterials (MaterialTitle, ResourceLink) VALUES (%s, %s)", 
                       (material_title, resource_link))
        db.commit()
        cursor.close()
        db.close()
        redirect('/materials')
    else:
        return template('material_form', title='Register Material')

@app.route('/')
def index():
    return template('index', title="Disaster Management System")

# Run the app
if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)