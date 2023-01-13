from RandomNamesGenerator import RandomNamesGenerator as RNG
import copy
from datetime import datetime
from faker import Faker
from dateutil import relativedelta
from random import Random
import pandas
import calendar

RG = Random()

num_rows = 172
percentage_names = 40
dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
source_dir = "./CSV/"
target_dir = "./test-data/"
target_file = f"Depatures-{num_rows}-rows-{dt}"
fnames_source_file = "FirstNames-Popularity-fr.csv"
fnames_target_file = f"FirstNames-Popularity-fr-{dt}.csv"
fnames_drop_columns = ["Popularity"]

fnames_rename_columns = {'FirstName': 'Prénom', 'Gender': 'Sexe'}

fnames_sort_columns = ["Popularity"]
fnames_final_order = ["Prénom", "Sexe", "Popularity"]
fnames_columns_order = ["Popularity", "Sexe", "Prénom"]

lnames_source_file = "LastNames-Popularity-fr.csv"
lnames_target_file = f"LaststNames-Popularity-fr-{dt}.csv"
lnames_drop_columns = ["Popularity"]

lnames_rename_columns = {'patronyme': 'Patronym', 'LastNameCount': 'Popularity'}

lnames_sort_columns = ["Popularity"]
lnames_final_order = ["Patronym", "Popularity"]
lnames_columns_order = ["Popularity", "Patronym"]

roles = ["Stagiaire transformable",
         "Stagiaire non transformable",
         "Architecte Entreprise D *",
         "Architecte Entreprise M",
         "Architecte Entreprise P",
         "Architecte Entreprise S",
         "Architecte Solution B",
         "Architecte Solution D *",
         "Architecte Solution M",
         "Architecte Solution P",
         "Architecte Solution S",
         "Chef de Projet",
         "Consultant Application A",
         "Consultant Application B",
         "Consultant Application M",
         "Consultant Application S",
         "Consultant Indus Engagement",
         "Consultant Métier A",
         "Consultant Métier B",
         "Consultant Métier D",
         "Consultant Métier M",
         "Consultant Métier P",
         "Consultant Métier S",
         "Consultant Service Delivery",
         "Directeur d'Engagement",
         "Directeur d'Engagement D",
         "Ingénieur Logiciel A",
         "Ingénieur Logiciel B",
         "Ingénieur Logiciel M",
         "Ingénieur Logiciel S",
         "Manager Transfo SI M",
         "Manager Transfo SI P",
         "Manager Transfo SI S",
         "Manager Indus Engagement",
         "Responsable Projet",
         "Responsable Projet Senior",
         "Responsable Service Delivery",
         "Responsable Service Delivery Senior",
         "Enabling RH",
         "Enabling Finances",
         "Enabling Assistant(e)",
         "Enabling Assistant(e)",
         "RDQM",
         "RM",
         "SCM",
         "SCM *",
         "SGM",
         "Ingénieur commercial",
         "Ingénieur commercial confirmé",
         "Ingénieur commercial senior",
         "Responsable de compte",
         "Responsable commercial",
         "Responsable de compte confirmé",
         "Responsable commercial confirmé",
         "Directeur de compte",
         "Directeur de compte *",
         "Directeur commercial",
         "Directeur commercial *",
         "Infrastructure Services",
         "Apprenti",
         "Rôle indéfini",
         "Apprenti Commercial"]

service_lines = ["Management",
                 "Business et Digital transformation",
                 "Operation and product services",
                 "Digital technology and cloud",
                 "Move to Cloud",
                 "Data Value",
                 "Agile Center"]

situations_futures = ["Autres ESN",
                      "Client final",
                      "Services & Conseil",
                      "Editeurs",
                      "Mutation externe",
                      "Changement de métier / réorientation",
                      "Activité freelance"]

motifs_departs = ["Perspectives d'évolution",
                  "Projet Personnel",
                  "Intérêt des missions",
                  "Rémunération",
                  "Ambiance/Environnement de travail"]

sites = ["Tours",
         "Brest",
         "Lyon (Ivoire)",
         "Grenoble",
         "Nancy",
         "Aix",
         "Sophia",
         "Pau",
         "Rennes",
         "Montbonnot(Nov)",
         "Cesson(Spiréa)",
         "Pau (TS)",
         "Biot",
         "Aix-en-P.(Azur)"]

employment_situations = ["Création d'entreprise",
                        "Salarié dans le software",
                        "Micro Entreprenneur Software",
                        "Reconversion vers un nouveau metier",
                        "Parent au foyer",
                        "Industriel, artisan ou commerçant",
                        "Profession libérale",
                        "Cadre moyen ou supérieur",
                        "Salarié",
                        "Ouvrier",
                        "Personnel de services",
                        "Retraité",
                        "Sans activité professionnelle",
                        "En recherche d'emploi"]

padding_week_day = RG.randrange(2, 6)

FNG = RNG(source_dir, fnames_source_file) # RandomNamesGenerator for french first names

LNG = RNG(source_dir, lnames_source_file)

FirstNames_df = FNG.get_data()

FirstNames_percentage_rows = RNG.calculate_percentage_num_rows(FirstNames_df, percentage_names)

if FirstNames_percentage_rows < num_rows:
    num_rows = FirstNames_percentage_rows

LastNames_df = LNG.get_data()
LastNames_percentage_rows = RNG.calculate_percentage_num_rows(LastNames_df, percentage_names)

if LastNames_percentage_rows < num_rows:
    num_rows = LastNames_percentage_rows

FirstNames_df = RNG.prepare_data_frame(FNG, fnames_rename_columns, None, fnames_final_order, fnames_sort_columns, num_rows, percentage_names, False)

first_names = FirstNames_df.Prénom.values.tolist()
first_names_low = list()

for _ in first_names:
    first_names_low.append(str(_).capitalize())

LastNames_df = RNG.prepare_data_frame(LNG, lnames_rename_columns, None, lnames_final_order, lnames_sort_columns, num_rows, percentage_names, False)

last_names = LastNames_df.Patronym.values.tolist()
last_names_low = list()

for i in last_names:
    last_names_low.append(str(i).capitalize())

career_mgrs = list()
for _ in range(15):
    career_mgr_fn = first_names_low[RG.randint(1, len(first_names_low) -1)]
    career_mgr_ln = last_names_low[RG.randint(1, len(last_names_low) -1)]
    career_mgrs.append(career_mgr_fn + " " + career_mgr_ln)

FirstNames_df.insert(0, "Nom", first_names_low)
FirstNames_df.drop(columns="Popularity", inplace=True)

GGID = list()

f = Faker('fr_FR')

for _ in range(num_rows):
    GGID.append(f.unique.numerify(text='%#######'))

date_format = "%d-%m-%Y"
now = datetime.now()
creation = datetime.strptime("01-10-1967", date_format)
cap_dob = str(creation.strftime(date_format))
dummy_date = datetime.strptime("13-06-1991", date_format)

dobs = list()
ages = list()
start_dates = list()
service_years = list()
site_postes = list()
services_posts = list()
grades = list()
roles_posts = list()
notice_dates = list()
exit_dates = list()
assigned_career_mgrs = list()
exit_interviews = list()
RRH_interviews = list()
reasons_for_leaving_1 = list()
reasons_for_leaving_2 = list()
strengths = list()
areas_for_improvement = list()
future_employment_situations = list()
commentaires_RRH = list()

for i in range(num_rows):
    # Date of Birth
    dob = f.date_of_birth(None, 19, 65)
    dobs.append(dob)

    # Age
    now_dob = relativedelta.relativedelta(now, dob)
    age = now_dob.years
    ages.append(age)

    ## Get a random start date on a business day at least 19 years after dob and 31 days before today.
    employable_from = datetime.fromordinal(dob.toordinal() + 6570)
    employable_to = datetime.fromordinal(now.toordinal() - 31)
 
    start_date = f.date_between(employable_from, employable_to)   

    if start_date.weekday() > 4:
        start_date = datetime.fromordinal(start_date.toordinal() + padding_week_day).date()

    start_dates.append(start_date)

    now_start = relativedelta.relativedelta(now, start_date)
    years_service = now_start.years
    service_years.append(years_service)

    # Set the BU site of the employee
    site = sites[RG.randint(1, len(sites) - 1)]
    site_postes.append(site)

    # Set the Service Line of the employee
    service_post = service_lines[RG.randint(1, len(service_lines) - 1)]
    services_posts.append(service_post)

    # Set the grade of the employee
    random_grade = RG.randint(0, num_rows)
    
    if i == random_grade:
        years_service = years_service - 5

    if years_service >= 0 and years_service <= 5:
        grade = "A"
    
    if years_service > 5 and years_service <= 10:
        grade = "B"
    
    if years_service > 10 and years_service <= 15:
        grade  = "C"
    
    if years_service > 15 and years_service <= 20:
        grade = "D"
    
    if years_service > 20 and years_service <= 25:
        grade = "E"
    
    if years_service > 25:
        grade = "F"

    grades.append(grade)

    # Set the role of the employee
    role_post = roles[RG.randint(1, len(roles) - 1)]
    roles_posts.append(role_post)

    # Set Date notice given
    noticeable_date = datetime.strptime(f"01-01-{now.year}", "%d-%m-%Y")
    if start_date.toordinal() > noticeable_date.toordinal():
        noticeable_date = start_date

    notice_day = f.date_between(noticeable_date, now.today())
    notice_dates.append(notice_day)

    expected_exit_start = datetime.fromordinal(notice_day.toordinal() + 31)
    expected_exit_end = datetime.fromordinal(notice_day.toordinal() + 123)
    exit_day = f.date_between(expected_exit_start, expected_exit_end)

    if exit_day.weekday() > 4:
        exit_day = datetime.fromordinal(exit_day.toordinal() + padding_week_day).date()

    exit_dates.append(exit_day)

    assigned_career_manager = career_mgrs[RG.randint(1, len(career_mgrs) -1)]
    assigned_career_mgrs.append(assigned_career_manager)

    exit_interview_date = f.date_between(notice_day, datetime.fromordinal(exit_day.toordinal() -7))

    exit_interviews.append(exit_interview_date)

    RRH_interview_date = f.date_between(exit_interview_date, exit_day)

    RRH_interviews.append(RRH_interview_date)

    reason_leaving = motifs_departs[RG.randint(
        1, len(motifs_departs) - 1)]
    reasons_for_leaving_1.append(reason_leaving)

    reason_leaving = motifs_departs[RG.randint(
        1, len(motifs_departs) - 1)]
    reasons_for_leaving_2.append(reason_leaving)

    experiences_and_strengths = f.sentence(nb_words=7)

    strengths.append(experiences_and_strengths)

    improvement = f.sentence(nb_words=7)
    areas_for_improvement.append(improvement)

    empl_lst = employment_situations[:]
    if age <= 61:
        rm = "Retraité"
        empl_lst.remove("Retraité")
    
    if age >= 62:
        empl_lst.remove("Parent au foyer")

    future_employment = empl_lst[RG.randint(1, len(empl_lst) - 1)]
    future_employment_situations.append(future_employment)

    RRH_comment = f.paragraph(nb_sentences=2)

    commentaires_RRH.append(RRH_comment)



FirstNames_df.insert(0, 'GGID', GGID)
FirstNames_df.insert(4, "Date_de_naissance", dobs)
FirstNames_df.insert(5, "Age", ages)
FirstNames_df.insert(6, "Date_Embauche", start_dates)
FirstNames_df.insert(7, "Ancienneté", service_years)
FirstNames_df.insert(8, "Sites", site_postes)
FirstNames_df.insert(9, "Service_Line", services_posts)
FirstNames_df.insert(10, "Grade", grades)
FirstNames_df.insert(11, "Role", roles_posts)
FirstNames_df.insert(12, "Date_Démission_notification", notice_dates)
FirstNames_df.insert(13, "Date_de_départ_prévue", exit_dates)
FirstNames_df.insert(14, "Carrière_manager", assigned_career_mgrs)
FirstNames_df.insert(15, "Date_entretien_de_départ", exit_interviews)
FirstNames_df.insert(16, "RRH_entretien", RRH_interviews)
FirstNames_df.insert(17, "Motif_départ_1", reasons_for_leaving_1)
FirstNames_df.insert(18, "Motif_départ_2", reasons_for_leaving_2)
FirstNames_df.insert(19, 'Points_forts_expérience_parcours', strengths)
FirstNames_df.insert(20, "Axes_amélioration", areas_for_improvement)
FirstNames_df.insert(21, "Situation_future_entreprise_ou_autre", future_employment_situations)
FirstNames_df.insert(22, "Commentaire_RRH ", commentaires_RRH)

FirstNames_df.set_index('GGID')

RNG.write_to_csv(FirstNames_df, target_directory=target_dir, target_file=target_file)
RNG.write_to_xlsx(FirstNames_df, target_directory=target_dir,
                  target_file=target_file)

print(FirstNames_df.head())
