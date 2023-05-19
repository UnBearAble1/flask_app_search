# Import Flask and dependencies
from flask import Flask, render_template, flash, request, redirect, url_for
from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField
import uuid as uuid
import os

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Add Databse for articles
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///articles.db"

# Set up secret Key for CRSF
app.config['SECRET_KEY'] = "testing testing"

# initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create Article Model
class Articles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	content = db.Column(db.Text)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	slug = db.Column(db.String(100))

# Create Article submission form
class ArticleForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	content = StringField("Content", validators=[DataRequired()], widget=TextArea())
	slug = StringField("Slug", validators=[DataRequired()])
	submit = SubmitField("Submit")


	# Create a string
	def __repr__(self):
		return '<Name %r>' %self.name



# # Create Article submission Route
# @app.route('/article/add', methods=['GET', 'POST'])
# def add_article():
# 	form = ArticleForm()
# 	return render_template("add_article.html",
# 			form=form)

# Create Article submission Route
@app.route('/article/add', methods=['GET', 'POST'])
def add_article():
	form = ArticleForm()

	if form.validate_on_submit():
		article = Articles(
			# define the variables based on the data submitted in the form
			title=form.title.data, 
			content=form.content.data, 
			slug=form.slug.data)
		# Clear the submission form
		form.title.data = ''
		form.content.data = ''
		form.slug.data = ''

		# Add article data to the article database
		db.session.add(article)
		db.session.commit()

		# Return Message
		flash("Article Submitted Successfully")
	
	# Redirect to the webpage
	return render_template ("add_article.html",
			 form=form)

# Pass things into the Navbar
@app.context_processor
def base():
	form = SearchForm()
	return dict(form=form)

# Create Search Function
@app.route('/search', methods=["POST"])
def search():
	form = SearchForm()
	posts = Posts.query
	if form.validate_on_submit():
		# Get data from submitted form
		post.searched = form.searched.data
		# Query the Database
		posts = posts.filter(Posts.content.like('%' + post.searched + '%'))
		posts = posts.order_by(Posts.title).all()

		return render_template("search.html",
		 form=form,
		 searched = post.searched,
		 posts = posts)
	
# Create a search form
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Define what to do when a user goes to the index route
@app.route("/")
def Home():
    return render_template("Home.html")

# Define which html page to render a user goes to the each route
@app.route("/Conditions")
def Conditions():
    return render_template("Conditions.html")

@app.route("/Armor_and_Weapons")
def Armor_and_Weapons():
    return render_template("Armor_and_Weapons.html")

@app.route("/Actions")
def Actions():
    return render_template("Actions.html")

@app.route("/Other_Rules")
def Other_Rules():
    return render_template("Other_Rules.html")

@app.route("/Creating_Abilities")
def Creating_Abilities():
    return render_template("Creating_Abilities.html")

@app.route("/Core_Game_Rules")
def Core_Game_Rules():
    return render_template("Core_Game_Rules.html")

@app.route("/Character_Creation")
def Character_Creation():
    return render_template("Character_Creation.html")

@app.route("/persistent-damage")
def persistent_damage():
	return render_template("persistent-damage.html")

@app.route("/frightened")
def frightened():
	return render_template("frightened.html")

@app.route("/dazzled")
def dazzled():
	return render_template("dazzled.html")

@app.route("/controlled")
def controlled():
	return render_template("controlled.html")

@app.route("/undetected")
def undetected():
	return render_template("undetected.html")

@app.route("/enfeebled")
def enfeebled():
	return render_template("enfeebled.html")

@app.route("/clumsy")
def clumsy():
	return render_template("clumsy.html")

@app.route("/petrified")
def petrified():
	return render_template("petrified.html")

@app.route("/paralyzed")
def paralyzed():
	return render_template("paralyzed.html")

@app.route("/grabbed")
def grabbed():
	return render_template("grabbed.html")

@app.route("/unconscious")
def unconscious():
	return render_template("unconscious.html")

@app.route("/quickened")
def quickened():
	return render_template("quickened.html")

@app.route("/blinded")
def blinded():
	return render_template("blinded.html")

@app.route("/deafened")
def deafened():
	return render_template("deafened.html")

@app.route("/concealed")
def concealed():
	return render_template("concealed.html")

@app.route("/wounded")
def wounded():
	return render_template("wounded.html")

@app.route("/stupefied")
def stupefied():
	return render_template("stupefied.html")

@app.route("/invisible")
def invisible():
	return render_template("invisible.html")

@app.route("/fascinated")
def fascinated():
	return render_template("fascinated.html")

@app.route("/unnoticed")
def unnoticed():
	return render_template("unnoticed.html")

@app.route("/fleeing")
def fleeing():
	return render_template("fleeing.html")

@app.route("/immobilized")
def immobilized():
	return render_template("immobilized.html")

@app.route("/sickened")
def sickened():
	return render_template("sickened.html")

@app.route("/observed")
def observed():
	return render_template("observed.html")

@app.route("/confused")
def confused():
	return render_template("confused.html")

@app.route("/prone")
def prone():
	return render_template("prone.html")

@app.route("/encumbered")
def encumbered():
	return render_template("encumbered.html")

@app.route("/doomed")
def doomed():
	return render_template("doomed.html")

@app.route("/slowed")
def slowed():
	return render_template("slowed.html")

@app.route("/restrained")
def restrained():
	return render_template("restrained.html")

@app.route("/fatigued")
def fatigued():
	return render_template("fatigued.html")

@app.route("/drained")
def drained():
	return render_template("drained.html")

@app.route("/hidden")
def hidden():
	return render_template("hidden.html")

@app.route("/broken")
def broken():
	return render_template("broken.html")

@app.route("/stunned")
def stunned():
	return render_template("stunned.html")

@app.route("/aid")
def aid():
	return render_template("aid.html")

@app.route("/drop-prone")
def drop_prone():
	return render_template("drop-prone.html")

@app.route("/maneuver-in-flight")
def maneuver_in_flight():
	return render_template("maneuver-in-flight.html")

@app.route("/escape")
def escape():
	return render_template("escape.html")

@app.route("/avert-gaze")
def avert_gaze():
	return render_template("avert-gaze.html")

@app.route("/ready")
def ready():
	return render_template("ready.html")

@app.route("/sense-motive")
def sense_motive():
	return render_template("sense-motive.html")

@app.route("/fly")
def fly():
	return render_template("fly.html")

@app.route("/point-out")
def point_out():
	return render_template("point-out.html")

@app.route("/mount")
def mount():
	return render_template("mount.html")

@app.route("/tumble-through")
def tumble_through():
	return render_template("tumble-through.html")

@app.route("/stand")
def stand():
	return render_template("stand.html")

@app.route("/take-cover")
def take_cover():
	return render_template("take-cover.html")

@app.route("/strike")
def strike():
	return render_template("strike.html")

@app.route("/delay")
def delay():
	return render_template("delay.html")

@app.route("/crawl")
def crawl():
	return render_template("crawl.html")

@app.route("/recall-knowledge")
def recall_knowledge():
	return render_template("recall-knowledge.html")

@app.route("/dismiss")
def dismiss():
	return render_template("dismiss.html")

@app.route("/burrow")
def burrow():
	return render_template("burrow.html")

@app.route("/seek")
def seek():
	return render_template("seek.html")

@app.route("/step")
def step():
	return render_template("step.html")

@app.route("/interact")
def interact():
	return render_template("interact.html")

@app.route("/leap")
def leap():
	return render_template("leap.html")

@app.route("/balance")
def balance():
	return render_template("balance.html")

@app.route("/squeeze")
def squeeze():
	return render_template("squeeze.html")

@app.route("/grab-an-edge")
def grab_an_edge():
	return render_template("grab-an-edge.html")

@app.route("/decipher-writing")
def decipher_writing():
	return render_template("decipher-writing.html")

@app.route("/arrest-a-fall")
def arrest_a_fall():
	return render_template("arrest-a-fall.html")

@app.route("/release")
def release():
	return render_template("release.html")

@app.route("/stride")
def stride():
	return render_template("stride.html")

@app.route("/raise-a-shield")
def raise_a_shield():
	return render_template("raise-a-shield.html")

@app.route("/acrobatics-dex")
def acrobatics_dex():
	return render_template("acrobatics-dex.html")

@app.route("/climb")
def climb():
	return render_template("climb.html")

@app.route("/force-open")
def force_open():
	return render_template("force-open.html")

@app.route("/high-jump")
def high_jump():
	return render_template("high-jump.html")

@app.route("/long-jump")
def long_jump():
	return render_template("long-jump.html")

@app.route("/identify-alchemy")
def identify_alchemy():
	return render_template("identify-alchemy.html")

@app.route("/crafting-int")
def crafting_int():
	return render_template("crafting-int.html")

@app.route("/manipulate")
def manipulate():
	return render_template("manipulate.html")

@app.route("/auditory")
def auditory():
	return render_template("auditory.html")

@app.route("/linguistic")
def linguistic():
	return render_template("linguistic.html")

@app.route("/concentrate")
def concentrate():
	return render_template("concentrate.html")

@app.route("/visual")
def visual():
	return render_template("visual.html")

@app.route("/secret")
def secret():
	return render_template("secret.html")

@app.route("/exploration")
def exploration():
	return render_template("exploration.html")

@app.route("/impersonate")
def impersonate():
	return render_template("impersonate.html")

@app.route("/mental")
def mental():
	return render_template("mental.html")

@app.route("/create-a-diversion")
def create_a_diversion():
	return render_template("create-a-diversion.html")

@app.route("/lie")
def lie():
	return render_template("lie.html")

@app.route("/feint")
def feint():
	return render_template("feint.html")

@app.route("/request")
def request():
	return render_template("request.html")

@app.route("/disposition-and-attitude")
def disposition_and_attitude():
	return render_template("disposition-and-attitude.html")

@app.route("/emotion")
def emotion():
	return render_template("emotion.html")

@app.route("/coerce")
def coerce():
	return render_template("coerce.html")

@app.route("/fear")
def fear():
	return render_template("fear.html")

@app.route("/demoralize")
def demoralize():
	return render_template("demoralize.html")

@app.route("/lore-int")
def lore_int():
	return render_template("lore-int.html")

@app.route("/long-term-rest")
def long_term_rest():
	return render_template("long-term-rest.html")

@app.route("/earn-income")
def earn_income():
	return render_template("earn-income.html")

@app.route("/gather-information")
def gather_information():
	return render_template("gather-information.html")

@app.route("/treat-poison")
def treat_poison():
	return render_template("treat-poison.html")

@app.route("/treat-disease")
def treat_disease():
	return render_template("treat-disease.html")

@app.route("/command-an-animal")
def command_an_animal():
	return render_template("command-an-animal.html")

@app.route("/nature-wis")
def nature_wis():
	return render_template("nature-wis.html")

@app.route("/occultism-int")
def occultism_int():
	return render_template("occultism-int.html")

@app.route("/move")
def move():
	return render_template("move.html")

@app.route("/performance-chr")
def performance_chr():
	return render_template("performance-chr.html")

@app.route("/religion-wis")
def religion_wis():
	return render_template("religion-wis.html")

@app.route("/subsist")
def subsist():
	return render_template("subsist.html")

@app.route("/create-forgery")
def create_forgery():
	return render_template("create-forgery.html")

@app.route("/society-int")
def society_int():
	return render_template("society-int.html")

@app.route("/conceal-an-object")
def conceal_an_object():
	return render_template("conceal-an-object.html")

@app.route("/hide")
def hide():
	return render_template("hide.html")

@app.route("/sneak")
def sneak():
	return render_template("sneak.html")

@app.route("/stealth-dex")
def stealth_dex():
	return render_template("stealth-dex.html")

@app.route("/cover")
def cover():
	return render_template("cover.html")

@app.route("/sense-direction")
def sense_direction():
	return render_template("sense-direction.html")

@app.route("/cover-tracks")
def cover_tracks():
	return render_template("cover-tracks.html")

@app.route("/survival-wis")
def survival_wis():
	return render_template("survival-wis.html")

@app.route("/track")
def track():
	return render_template("track.html")

@app.route("/palm-an-object")
def palm_an_object():
	return render_template("palm-an-object.html")

@app.route("/steal")
def steal():
	return render_template("steal.html")

@app.route("/pick-a-lock")
def pick_a_lock():
	return render_template("pick-a-lock.html")

@app.route("/thievery-dex")
def thievery_dex():
	return render_template("thievery-dex.html")

@app.route("/difficult-terrain")
def difficult_terrain():
	return render_template("difficult-terrain.html")

@app.route("/environmental-damage")
def environmental_damage():
	return render_template("environmental-damage.html")

@app.route("/temperature")
def temperature():
	return render_template("temperature.html")

@app.route("/cursed")
def cursed():
	return render_template("cursed.html")

@app.route("/destiny")
def destiny():
	return render_template("destiny.html")

@app.route("/divine-curse")
def divine_curse():
	return render_template("divine-curse.html")

@app.route("/dread")
def dread():
	return render_template("dread.html")

@app.route("/delusions")
def delusions():
	return render_template("delusions.html")

@app.route("/clueless")
def clueless():
	return render_template("clueless.html")

@app.route("/charitable")
def charitable():
	return render_template("charitable.html")

@app.route("/drug-addiction")
def drug_addiction():
	return render_template("drug-addiction.html")

@app.route("/easily-overstimulated")
def easily_overstimulated():
	return render_template("easily-overstimulated.html")

@app.route("/callous")
def callous():
	return render_template("callous.html")

@app.route("/bad-temper")
def bad_temper():
	return render_template("bad-temper.html")

@app.route("/code-of-honor")
def code_of_honor():
	return render_template("code-of-honor.html")

@app.route("/disciples-of-faith")
def disciples_of_faith():
	return render_template("disciples-of-faith.html")

@app.route("/bloodlust")
def bloodlust():
	return render_template("bloodlust.html")

@app.route("/amnesia")
def amnesia():
	return render_template("amnesia.html")

@app.route("/easy-to-read")
def easy_to_read():
	return render_template("easy-to-read.html")

@app.route("/curious")
def curious():
	return render_template("curious.html")

@app.route("/dyslexia")
def dyslexia():
	return render_template("dyslexia.html")

@app.route("/compulsive-behavior")
def compulsive_behavior():
	return render_template("compulsive-behavior.html")

@app.route("/cowardice")
def cowardice():
	return render_template("cowardice.html")

@app.route("/enemies")
def enemies():
	return render_template("enemies.html")

@app.route("/flashbacks")
def flashbacks():
	return render_template("flashbacks.html")

@app.route("/frightens-animals")
def frightens_animals():
	return render_template("frightens-animals.html")

@app.route("/gluttony")
def gluttony():
	return render_template("gluttony.html")

@app.route("/greed")
def greed():
	return render_template("greed.html")

@app.route("/gullibility")
def gullibility():
	return render_template("gullibility.html")

@app.route("/honesty")
def honesty():
	return render_template("honesty.html")

@app.route("/impulsiveness")
def impulsiveness():
	return render_template("impulsiveness.html")

@app.route("/resting")
def resting():
	return render_template("resting.html")

@app.route("/insomniac")
def insomniac():
	return render_template("insomniac.html")

@app.route("/jealousy")
def jealousy():
	return render_template("jealousy.html")

@app.route("/kleptomania")
def kleptomania():
	return render_template("kleptomania.html")

@app.route("/lecherousness")
def lecherousness():
	return render_template("lecherousness.html")

@app.route("/loner")
def loner():
	return render_template("loner.html")

@app.route("/magic-susceptibility")
def magic_susceptibility():
	return render_template("magic-susceptibility.html")

@app.route("/miserliness")
def miserliness():
	return render_template("miserliness.html")

@app.route("/no-sense-of-humor")
def no_sense_of_humor():
	return render_template("no-sense-of-humor.html")

@app.route("/no-sense-of-smelltaste")
def no_sense_of_smelltaste():
	return render_template("no-sense-of-smelltaste.html")

@app.route("/nocturnal")
def nocturnal():
	return render_template("nocturnal.html")

@app.route("/non-iconographic")
def non_iconographic():
	return render_template("non-iconographic.html")

@app.route("/obsession")
def obsession():
	return render_template("obsession.html")

@app.route("/odious-personal-habit")
def odious_personal_habit():
	return render_template("odious-personal-habit.html")

@app.route("/on-the-edge")
def on_the_edge():
	return render_template("on-the-edge.html")

@app.route("/deafness")
def deafness():
	return render_template("deafness.html")

@app.route("/motion-sickness")
def motion_sickness():
	return render_template("motion-sickness.html")

@app.route("/chronic-pain")
def chronic_pain():
	return render_template("chronic-pain.html")

@app.route("/fragile")
def fragile():
	return render_template("fragile.html")

@app.route("/farsighted")
def farsighted():
	return render_template("farsighted.html")

@app.route("/one-arm")
def one_arm():
	return render_template("one-arm.html")

@app.route("/bad-back")
def bad_back():
	return render_template("bad-back.html")

@app.route("/leg-disability")
def leg_disability():
	return render_template("leg-disability.html")

@app.route("/physically-off-putting")
def physically_off_putting():
	return render_template("physically-off-putting.html")

@app.route("/alcoholism")
def alcoholism():
	return render_template("alcoholism.html")

@app.route("/numb")
def numb():
	return render_template("numb.html")

@app.route("/natural-climate-cold")
def natural_climate_cold():
	return render_template("natural-climate-cold.html")

@app.route("/mute")
def mute():
	return render_template("mute.html")

@app.route("/hemophilia")
def hemophilia():
	return render_template("hemophilia.html")

@app.route("/klutz")
def klutz():
	return render_template("klutz.html")

@app.route("/low-pain-threshold")
def low_pain_threshold():
	return render_template("low-pain-threshold.html")

@app.route("/dependency")
def dependency():
	return render_template("dependency.html")

@app.route("/cannot-speak")
def cannot_speak():
	return render_template("cannot-speak.html")

@app.route("/hard-of-hearing")
def hard_of_hearing():
	return render_template("hard-of-hearing.html")

@app.route("/extra-sleep")
def extra_sleep():
	return render_template("extra-sleep.html")

@app.route("/fat")
def fat():
	return render_template("fat.html")

@app.route("/bad-grip")
def bad_grip():
	return render_template("bad-grip.html")

@app.route("/light-sleeper")
def light_sleeper():
	return render_template("light-sleeper.html")

@app.route("/blindness")
def blindness():
	return render_template("blindness.html")

@app.route("/neurological-disorder")
def neurological_disorder():
	return render_template("neurological-disorder.html")

@app.route("/one-eye")
def one_eye():
	return render_template("one-eye.html")

@app.route("/natural-climate-hot")
def natural_climate_hot():
	return render_template("natural-climate-hot.html")

@app.route("/nearsighted")
def nearsighted():
	return render_template("nearsighted.html")

@app.route("/depressed")
def depressed():
	return render_template("depressed.html")

@app.route("/guilt-complex")
def guilt_complex():
	return render_template("guilt-complex.html")

@app.route("/mood-swings")
def mood_swings():
	return render_template("mood-swings.html")

@app.route("/pacifism")
def pacifism():
	return render_template("pacifism.html")

@app.route("/paranoia")
def paranoia():
	return render_template("paranoia.html")

@app.route("/phantom-voices")
def phantom_voices():
	return render_template("phantom-voices.html")

@app.route("/phobias")
def phobias():
	return render_template("phobias.html")

@app.route("/post-combat-shakes")
def post_combat_shakes():
	return render_template("post-combat-shakes.html")

@app.route("/pyromania")
def pyromania():
	return render_template("pyromania.html")

@app.route("/restricted-diet")
def restricted_diet():
	return render_template("restricted-diet.html")

@app.route("/restricted-vision")
def restricted_vision():
	return render_template("restricted-vision.html")

@app.route("/resistance")
def resistance():
	return render_template("resistance.html")

@app.route("/weakness")
def weakness():
	return render_template("weakness.html")

@app.route("/revulsion")
def revulsion():
	return render_template("revulsion.html")

@app.route("/sadism")
def sadism():
	return render_template("sadism.html")

@app.route("/secret-3536570")
def secret_3536570():
	return render_template("secret-3536570.html")

@app.route("/selfless")
def selfless():
	return render_template("selfless.html")

@app.route("/sense-of-duty")
def sense_of_duty():
	return render_template("sense-of-duty.html")

@app.route("/short-attention-span")
def short_attention_span():
	return render_template("short-attention-span.html")

@app.route("/short-life-span")
def short_life_span():
	return render_template("short-life-span.html")

@app.route("/shyness")
def shyness():
	return render_template("shyness.html")

@app.route("/sleepwalker")
def sleepwalker():
	return render_template("sleepwalker.html")

@app.route("/sleepy")
def sleepy():
	return render_template("sleepy.html")

@app.route("/slow-healer")
def slow_healer():
	return render_template("slow-healer.html")

@app.route("/social-stigma")
def social_stigma():
	return render_template("social-stigma.html")

@app.route("/split-personality")
def split_personality():
	return render_template("split-personality.html")

@app.route("/stubbornness")
def stubbornness():
	return render_template("stubbornness.html")

@app.route("/stuttering")
def stuttering():
	return render_template("stuttering.html")

@app.route("/supersensitive")
def supersensitive():
	return render_template("supersensitive.html")

@app.route("/susceptible")
def susceptible():
	return render_template("susceptible.html")

@app.route("/trademark")
def trademark():
	return render_template("trademark.html")

@app.route("/trickster")
def trickster():
	return render_template("trickster.html")

@app.route("/truthfulness")
def truthfulness():
	return render_template("truthfulness.html")

@app.route("/uncontrollable-appetite")
def uncontrollable_appetite():
	return render_template("uncontrollable-appetite.html")

@app.route("/unhealing")
def unhealing():
	return render_template("unhealing.html")

@app.route("/unluckiness")
def unluckiness():
	return render_template("unluckiness.html")

@app.route("/vow")
def vow():
	return render_template("vow.html")

@app.route("/vulnerability")
def vulnerability():
	return render_template("vulnerability.html")

@app.route("/weakness-4510561")
def weakness_4510561():
	return render_template("weakness-4510561.html")

@app.route("/workaholic")
def workaholic():
	return render_template("workaholic.html")

@app.route("/vengeful-hatred")
def vengeful_hatred():
	return render_template("vengeful-hatred.html")

@app.route("/striking-retribution")
def striking_retribution():
	return render_template("striking-retribution.html")

@app.route("/tomb-watchers-glare")
def tomb_watchers_glare():
	return render_template("tomb-watchers-glare.html")

@app.route("/ghost-touch")
def ghost_touch():
	return render_template("ghost-touch.html")

@app.route("/incorporeal")
def incorporeal():
	return render_template("incorporeal.html")

@app.route("/harmlessly-cute")
def harmlessly_cute():
	return render_template("harmlessly-cute.html")

@app.route("/impersenator")
def impersenator():
	return render_template("impersenator.html")

@app.route("/elude-trouble")
def elude_trouble():
	return render_template("elude-trouble.html")

@app.route("/kneecap")
def kneecap():
	return render_template("kneecap.html")

@app.route("/recognize-ambush")
def recognize_ambush():
	return render_template("recognize-ambush.html")

@app.route("/scamper")
def scamper():
	return render_template("scamper.html")

@app.route("/skittering-scuttle")
def skittering_scuttle():
	return render_template("skittering-scuttle.html")

@app.route("/vengeance")
def vengeance():
	return render_template("vengeance.html")

@app.route("/incredible-ferocity")
def incredible_ferocity():
	return render_template("incredible-ferocity.html")

@app.route("/rampaging-ferocity")
def rampaging_ferocity():
	return render_template("rampaging-ferocity.html")

@app.route("/undying-ferocity")
def undying_ferocity():
	return render_template("undying-ferocity.html")

@app.route("/rapid-instincts")
def rapid_instincts():
	return render_template("rapid-instincts.html")

@app.route("/twitchy")
def twitchy():
	return render_template("twitchy.html")

@app.route("/threatening-approach")
def threatening_approach():
	return render_template("threatening-approach.html")

@app.route("/predators-growl")
def predators_growl():
	return render_template("predators-growl.html")

@app.route("/ancestral-performer")
def ancestral_performer():
	return render_template("ancestral-performer.html")

@app.route("/ancestral-ties")
def ancestral_ties():
	return render_template("ancestral-ties.html")

@app.route("/ancestral-warden")
def ancestral_warden():
	return render_template("ancestral-warden.html")

@app.route("/palpable-enmity")
def palpable_enmity():
	return render_template("palpable-enmity.html")

@app.route("/skilled-surge")
def skilled_surge():
	return render_template("skilled-surge.html")

@app.route("/iron-born")
def iron_born():
	return render_template("iron-born.html")

@app.route("/ageless-patience")
def ageless_patience():
	return render_template("ageless-patience.html")

@app.route("/scavengers-search")
def scavengers_search():
	return render_template("scavengers-search.html")

@app.route("/shapechangers-intuition")
def shapechangers_intuition():
	return render_template("shapechangers-intuition.html")

@app.route("/watchful")
def watchful():
	return render_template("watchful.html")

@app.route("/defiance-unto-death")
def defiance_unto_death():
	return render_template("defiance-unto-death.html")

@app.route("/ancestral-suspicion")
def ancestral_suspicion():
	return render_template("ancestral-suspicion.html")

@app.route("/doughtiness")
def doughtiness():
	return render_template("doughtiness.html")

@app.route("/irrepressible")
def irrepressible():
	return render_template("irrepressible.html")

@app.route("/stone-face")
def stone_face():
	return render_template("stone-face.html")

@app.route("/unwavering-mein")
def unwavering_mein():
	return render_template("unwavering-mein.html")

@app.route("/verve")
def verve():
	return render_template("verve.html")

@app.route("/willful-and-proud")
def willful_and_proud():
	return render_template("willful-and-proud.html")

@app.route("/ceaseless-shadows")
def ceaseless_shadows():
	return render_template("ceaseless-shadows.html")

@app.route("/war-marcher")
def war_marcher():
	return render_template("war-marcher.html")

@app.route("/keep-up-appearances")
def keep_up_appearances():
	return render_template("keep-up-appearances.html")

@app.route("/easily-dismissed")
def easily_dismissed():
	return render_template("easily-dismissed.html")

@app.route("/aerolist")
def aerolist():
	return render_template("aerolist.html")

@app.route("/skittering-sneak")
def skittering_sneak():
	return render_template("skittering-sneak.html")

@app.route("/sense-allies")
def sense_allies():
	return render_template("sense-allies.html")

@app.route("/fox-trick")
def fox_trick():
	return render_template("fox-trick.html")

@app.route("/protective-surge")
def protective_surge():
	return render_template("protective-surge.html")

@app.route("/defiant-yell")
def defiant_yell():
	return render_template("defiant-yell.html")

@app.route("/intuitive-cooperation")
def intuitive_cooperation():
	return render_template("intuitive-cooperation.html")

@app.route("/drag-down")
def drag_down():
	return render_template("drag-down.html")

@app.route("/palegic-aptitude")
def palegic_aptitude():
	return render_template("palegic-aptitude.html")

@app.route("/riptide")
def riptide():
	return render_template("riptide.html")

@app.route("/cliff-hanger")
def cliff_hanger():
	return render_template("cliff-hanger.html")

@app.route("/quick-hands")
def quick_hands():
	return render_template("quick-hands.html")

@app.route("/expert-drill-sergeant")
def expert_drill_sergeant():
	return render_template("expert-drill-sergeant.html")

@app.route("/graceful-guidance")
def graceful_guidance():
	return render_template("graceful-guidance.html")

@app.route("/wary-of-enchantment")
def wary_of_enchantment():
	return render_template("wary-of-enchantment.html")

@app.route("/hustle")
def hustle():
	return render_template("hustle.html")

@app.route("/eye-for-treasure")
def eye_for_treasure():
	return render_template("eye-for-treasure.html")

@app.route("/junk-tinker")
def junk_tinker():
	return render_template("junk-tinker.html")

@app.route("/reinforcement")
def reinforcement():
	return render_template("reinforcement.html")

@app.route("/tinkering-fingers")
def tinkering_fingers():
	return render_template("tinkering-fingers.html")

@app.route("/courteous-comeback")
def courteous_comeback():
	return render_template("courteous-comeback.html")

@app.route("/elemental-adept")
def elemental_adept():
	return render_template("elemental-adept.html")

@app.route("/scalding-spit")
def scalding_spit():
	return render_template("scalding-spit.html")

@app.route("/cautious-crawler")
def cautious_crawler():
	return render_template("cautious-crawler.html")

@app.route("/hustler")
def hustler():
	return render_template("hustler.html")

@app.route("/pack-rat")
def pack_rat():
	return render_template("pack-rat.html")

@app.route("/warren-navigator")
def warren_navigator():
	return render_template("warren-navigator.html")

@app.route("/avoid-notice")
def avoid_notice():
	return render_template("avoid-notice.html")

@app.route("/agile")
def agile():
	return render_template("agile.html")

@app.route("/attached")
def attached():
	return render_template("attached.html")

@app.route("/backstabber")
def backstabber():
	return render_template("backstabber.html")

@app.route("/backswing")
def backswing():
	return render_template("backswing.html")

@app.route("/brutal")
def brutal():
	return render_template("brutal.html")

@app.route("/climbing")
def climbing():
	return render_template("climbing.html")

@app.route("/concealable")
def concealable():
	return render_template("concealable.html")

@app.route("/deadly")
def deadly():
	return render_template("deadly.html")

@app.route("/disarm-weapon-trait")
def disarm_weapon_trait():
	return render_template("disarm-weapon-trait.html")

@app.route("/fatal")
def fatal():
	return render_template("fatal.html")

@app.route("/finesse")
def finesse():
	return render_template("finesse.html")

@app.route("/forceful")
def forceful():
	return render_template("forceful.html")

@app.route("/free-hand")
def free_hand():
	return render_template("free-hand.html")

@app.route("/grapple-weapon-trait")
def grapple_weapon_trait():
	return render_template("grapple-weapon-trait.html")

@app.route("/hampering")
def hampering():
	return render_template("hampering.html")

@app.route("/jousting")
def jousting():
	return render_template("jousting.html")

@app.route("/modular")
def modular():
	return render_template("modular.html")

@app.route("/nonlethal")
def nonlethal():
	return render_template("nonlethal.html")

@app.route("/parry")
def parry():
	return render_template("parry.html")

@app.route("/propulsive")
def propulsive():
	return render_template("propulsive.html")

@app.route("/range")
def range():
	return render_template("range.html")

@app.route("/ranged-trip")
def ranged_trip():
	return render_template("ranged-trip.html")

@app.route("/reach")
def reach():
	return render_template("reach.html")

@app.route("/reload")
def reload():
	return render_template("reload.html")

@app.route("/repeating")
def repeating():
	return render_template("repeating.html")

@app.route("/shove-3653080")
def shove_3653080():
	return render_template("shove-3653080.html")

@app.route("/sweep")
def sweep():
	return render_template("sweep.html")

@app.route("/tethered")
def tethered():
	return render_template("tethered.html")

@app.route("/thrown")
def thrown():
	return render_template("thrown.html")

@app.route("/trip-weapon-trait")
def trip_weapon_trait():
	return render_template("trip-weapon-trait.html")

@app.route("/twin")
def twin():
	return render_template("twin.html")

@app.route("/two-hand")
def two_hand():
	return render_template("two-hand.html")

@app.route("/unarmed")
def unarmed():
	return render_template("unarmed.html")

@app.route("/versatile")
def versatile():
	return render_template("versatile.html")

@app.route("/volley")
def volley():
	return render_template("volley.html")

@app.route("/disarm-resist")
def disarm_resist():
	return render_template("disarm-resist.html")

@app.route("/improvisational-defender")
def improvisational_defender():
	return render_template("improvisational-defender.html")

@app.route("/razzle-dazzle")
def razzle_dazzle():
	return render_template("razzle-dazzle.html")

@app.route("/returning-throw")
def returning_throw():
	return render_template("returning-throw.html")

@app.route("/shoulder-slam")
def shoulder_slam():
	return render_template("shoulder-slam.html")

@app.route("/agonizing-rebuke")
def agonizing_rebuke():
	return render_template("agonizing-rebuke.html")

@app.route("/cultural-specialty")
def cultural_specialty():
	return render_template("cultural-specialty.html")

@app.route("/dynamic-linguistics")
def dynamic_linguistics():
	return render_template("dynamic-linguistics.html")

@app.route("/extraplanar-study")
def extraplanar_study():
	return render_template("extraplanar-study.html")

@app.route("/seer")
def seer():
	return render_template("seer.html")

@app.route("/know-your-own")
def know_your_own():
	return render_template("know-your-own.html")

@app.route("/adroit-manipulation")
def adroit_manipulation():
	return render_template("adroit-manipulation.html")

@app.route("/no-evidence")
def no_evidence():
	return render_template("no-evidence.html")

@app.route("/silent-step")
def silent_step():
	return render_template("silent-step.html")

@app.route("/super-sneaky")
def super_sneaky():
	return render_template("super-sneaky.html")

@app.route("/very-sneaky")
def very_sneaky():
	return render_template("very-sneaky.html")

@app.route("/adapted-cantrip")
def adapted_cantrip():
	return render_template("adapted-cantrip.html")

@app.route("/feed-on-pain")
def feed_on_pain():
	return render_template("feed-on-pain.html")

@app.route("/intuitive-illusions")
def intuitive_illusions():
	return render_template("intuitive-illusions.html")

@app.route("/magic-rider")
def magic_rider():
	return render_template("magic-rider.html")

@app.route("/star-orb")
def star_orb():
	return render_template("star-orb.html")

@app.route("/sheltering-slab")
def sheltering_slab():
	return render_template("sheltering-slab.html")

@app.route("/stonecunning")
def stonecunning():
	return render_template("stonecunning.html")

@app.route("/loud-singer")
def loud_singer():
	return render_template("loud-singer.html")

@app.route("/mask-of-fear")
def mask_of_fear():
	return render_template("mask-of-fear.html")

@app.route("/mask-of-pain")
def mask_of_pain():
	return render_template("mask-of-pain.html")

@app.route("/mask-of-rejection")
def mask_of_rejection():
	return render_template("mask-of-rejection.html")

@app.route("/clan-protector")
def clan_protector():
	return render_template("clan-protector.html")

@app.route("/clans-edge")
def clans_edge():
	return render_template("clans-edge.html")

@app.route("/protective-sheath")
def protective_sheath():
	return render_template("protective-sheath.html")

@app.route("/titan-slinger")
def titan_slinger():
	return render_template("titan-slinger.html")

@app.route("/steady-on-stone")
def steady_on_stone():
	return render_template("steady-on-stone.html")

@app.route("/environmental-climber")
def environmental_climber():
	return render_template("environmental-climber.html")

@app.route("/superior-environmental-climber")
def superior_environmental_climber():
	return render_template("superior-environmental-climber.html")

@app.route("/cobble-dancer")
def cobble_dancer():
	return render_template("cobble-dancer.html")

@app.route("/environment-craft")
def environment_craft():
	return render_template("environment-craft.html")

@app.route("/natural-scout")
def natural_scout():
	return render_template("natural-scout.html")

@app.route("/swift-stalker")
def swift_stalker():
	return render_template("swift-stalker.html")

@app.route("/terrain-runner")
def terrain_runner():
	return render_template("terrain-runner.html")

@app.route("/terrain-stalker")
def terrain_stalker():
	return render_template("terrain-stalker.html")

@app.route("/wintertouched")
def wintertouched():
	return render_template("wintertouched.html")

@app.route("/uncanny-agility")
def uncanny_agility():
	return render_template("uncanny-agility.html")

@app.route("/animal-class-elocutionist")
def animal_class_elocutionist():
	return render_template("animal-class-elocutionist.html")

@app.route("/true-animal-elocutionist")
def true_animal_elocutionist():
	return render_template("true-animal-elocutionist.html")

@app.route("/unsettling-to-animals")
def unsettling_to_animals():
	return render_template("unsettling-to-animals.html")

@app.route("/airy-step")
def airy_step():
	return render_template("airy-step.html")

@app.route("/blazing-aura")
def blazing_aura():
	return render_template("blazing-aura.html")

@app.route("/continuous-assault")
def continuous_assault():
	return render_template("continuous-assault.html")

@app.route("/energy-blessed")
def energy_blessed():
	return render_template("energy-blessed.html")

@app.route("/harness-shroud")
def harness_shroud():
	return render_template("harness-shroud.html")

@app.route("/shroud-cloud")
def shroud_cloud():
	return render_template("shroud-cloud.html")

@app.route("/heat-wave")
def heat_wave():
	return render_template("heat-wave.html")

@app.route("/hydraulic-deflection")
def hydraulic_deflection():
	return render_template("hydraulic-deflection.html")

@app.route("/elemental-maneuvers")
def elemental_maneuvers():
	return render_template("elemental-maneuvers.html")

@app.route("/improved-elemental-bulwark")
def improved_elemental_bulwark():
	return render_template("improved-elemental-bulwark.html")

@app.route("/mist-strider")
def mist_strider():
	return render_template("mist-strider.html")

@app.route("/radiance")
def radiance():
	return render_template("radiance.html")

@app.route("/tetraelemental-assault")
def tetraelemental_assault():
	return render_template("tetraelemental-assault.html")

@app.route("/cloak-of-poison")
def cloak_of_poison():
	return render_template("cloak-of-poison.html")

@app.route("/graceful-step")
def graceful_step():
	return render_template("graceful-step.html")

@app.route("/hopping-stride")
def hopping_stride():
	return render_template("hopping-stride.html")

@app.route("/light-step")
def light_step():
	return render_template("light-step.html")

@app.route("/lower-their-guard")
def lower_their_guard():
	return render_template("lower-their-guard.html")

@app.route("/invigorating-fear")
def invigorating_fear():
	return render_template("invigorating-fear.html")

@app.route("/expert-dynamic-skill")
def expert_dynamic_skill():
	return render_template("expert-dynamic-skill.html")

@app.route("/true-dynamic-skill")
def true_dynamic_skill():
	return render_template("true-dynamic-skill.html")

@app.route("/universal-dynamic-skill")
def universal_dynamic_skill():
	return render_template("universal-dynamic-skill.html")

@app.route("/eclectic-obsession")
def eclectic_obsession():
	return render_template("eclectic-obsession.html")

@app.route("/incredible-improvisation")
def incredible_improvisation():
	return render_template("incredible-improvisation.html")

@app.route("/guiding-luck")
def guiding_luck():
	return render_template("guiding-luck.html")

@app.route("/harbingers-hex")
def harbingers_hex():
	return render_template("harbingers-hex.html")

@app.route("/jinxed")
def jinxed():
	return render_template("jinxed.html")

@app.route("/lucky-defense")
def lucky_defense():
	return render_template("lucky-defense.html")

@app.route("/quick-curse")
def quick_curse():
	return render_template("quick-curse.html")

@app.route("/superstition")
def superstition():
	return render_template("superstition.html")

@app.route("/jinx-glutton")
def jinx_glutton():
	return render_template("jinx-glutton.html")

@app.route("/lucky-break")
def lucky_break():
	return render_template("lucky-break.html")

@app.route("/sense-for-trouble")
def sense_for_trouble():
	return render_template("sense-for-trouble.html")

@app.route("/shared-luck-8064152")
def shared_luck_8064152():
	return render_template("shared-luck-8064152.html")

@app.route("/tradition-bane")
def tradition_bane():
	return render_template("tradition-bane.html")

@app.route("/kneel-for-no-man-or-god")
def kneel_for_no_man_or_god():
	return render_template("kneel-for-no-man-or-god.html")

@app.route("/magic-resistance")
def magic_resistance():
	return render_template("magic-resistance.html")

@app.route("/speak-with-plants")
def speak_with_plants():
	return render_template("speak-with-plants.html")

@app.route("/counteracting")
def counteracting():
	return render_template("counteracting.html")

@app.route("/purge-sins")
def purge_sins():
	return render_template("purge-sins.html")

@app.route("/bright-fletchling")
def bright_fletchling():
	return render_template("bright-fletchling.html")

@app.route("/earth-sense")
def earth_sense():
	return render_template("earth-sense.html")

@app.route("/search1")
def search1():
	return render_template("search1.html")

@app.route("/spirit-soother")
def spirit_soother():
	return render_template("spirit-soother.html")

@app.route("/extinguish-light")
def extinguish_light():
	return render_template("extinguish-light.html")

@app.route("/hefting-shadow")
def hefting_shadow():
	return render_template("hefting-shadow.html")

@app.route("/sculpt-shadows")
def sculpt_shadows():
	return render_template("sculpt-shadows.html")

@app.route("/shadow-blending")
def shadow_blending():
	return render_template("shadow-blending.html")

@app.route("/fortuitous-shift")
def fortuitous_shift():
	return render_template("fortuitous-shift.html")

@app.route("/life-leap")
def life_leap():
	return render_template("life-leap.html")

@app.route("/basic-innate-spell")
def basic_innate_spell():
	return render_template("basic-innate-spell.html")

@app.route("/energized-font")
def energized_font():
	return render_template("energized-font.html")

@app.route("/innate-cantrip")
def innate_cantrip():
	return render_template("innate-cantrip.html")

@app.route("/fey-touched")
def fey_touched():
	return render_template("fey-touched.html")

@app.route("/life-giving-magic")
def life_giving_magic():
	return render_template("life-giving-magic.html")

@app.route("/expert-innate-spell")
def expert_innate_spell():
	return render_template("expert-innate-spell.html")

@app.route("/otherworldly-acumen")
def otherworldly_acumen():
	return render_template("otherworldly-acumen.html")

@app.route("/charred-remains")
def charred_remains():
	return render_template("charred-remains.html")

@app.route("/steam-spell")
def steam_spell():
	return render_template("steam-spell.html")

@app.route("/twist-healing")
def twist_healing():
	return render_template("twist-healing.html")

@app.route("/echoes-in-stone")
def echoes_in_stone():
	return render_template("echoes-in-stone.html")

@app.route("/treacherous-earth")
def treacherous_earth():
	return render_template("treacherous-earth.html")

@app.route("/long-lived")
def long_lived():
	return render_template("long-lived.html")

@app.route("/hybrid-form")
def hybrid_form():
	return render_template("hybrid-form.html")

@app.route("/myriad-forms")
def myriad_forms():
	return render_template("myriad-forms.html")

@app.route("/quick-shape")
def quick_shape():
	return render_template("quick-shape.html")

@app.route("/ankle-bite")
def ankle_bite():
	return render_template("ankle-bite.html")

@app.route("/fang-sharpener")
def fang_sharpener():
	return render_template("fang-sharpener.html")

@app.route("/bloodletting-fangs")
def bloodletting_fangs():
	return render_template("bloodletting-fangs.html")

@app.route("/envenom-fangs")
def envenom_fangs():
	return render_template("envenom-fangs.html")

@app.route("/gnaw")
def gnaw():
	return render_template("gnaw.html")

@app.route("/hungry")
def hungry():
	return render_template("hungry.html")

@app.route("/sawtooth")
def sawtooth():
	return render_template("sawtooth.html")

@app.route("/sharp-fangs")
def sharp_fangs():
	return render_template("sharp-fangs.html")

@app.route("/swinging-bite")
def swinging_bite():
	return render_template("swinging-bite.html")

@app.route("/taste-blood")
def taste_blood():
	return render_template("taste-blood.html")

@app.route("/cheek-pouches")
def cheek_pouches():
	return render_template("cheek-pouches.html")

@app.route("/big-mouth")
def big_mouth():
	return render_template("big-mouth.html")

@app.route("/quick-stow")
def quick_stow():
	return render_template("quick-stow.html")

@app.route("/daywalker")
def daywalker():
	return render_template("daywalker.html")

@app.route("/defy-death")
def defy_death():
	return render_template("defy-death.html")

@app.route("/focused-cat-nap")
def focused_cat_nap():
	return render_template("focused-cat-nap.html")

@app.route("/healers-halo")
def healers_halo():
	return render_template("healers-halo.html")

@app.route("/ten-lives")
def ten_lives():
	return render_template("ten-lives.html")

@app.route("/springing-leaper")
def springing_leaper():
	return render_template("springing-leaper.html")

@app.route("/fleet-footed")
def fleet_footed():
	return render_template("fleet-footed.html")

@app.route("/lotus-style")
def lotus_style():
	return render_template("lotus-style.html")

@app.route("/warren-digger")
def warren_digger():
	return render_template("warren-digger.html")

@app.route("/bioluminescent")
def bioluminescent():
	return render_template("bioluminescent.html")

@app.route("/keen-eyes")
def keen_eyes():
	return render_template("keen-eyes.html")

@app.route("/cindersoul")
def cindersoul():
	return render_template("cindersoul.html")

@app.route("/cleansing-blood")
def cleansing_blood():
	return render_template("cleansing-blood.html")

@app.route("/duskwalker")
def duskwalker():
	return render_template("duskwalker.html")

@app.route("/emberkin")
def emberkin():
	return render_template("emberkin.html")

@app.route("/graveborn")
def graveborn():
	return render_template("graveborn.html")

@app.route("/inoculating-blood")
def inoculating_blood():
	return render_template("inoculating-blood.html")

@app.route("/intercorporate")
def intercorporate():
	return render_template("intercorporate.html")

@app.route("/necromantic-physiology")
def necromantic_physiology():
	return render_template("necromantic-physiology.html")

@app.route("/powerful-guts")
def powerful_guts():
	return render_template("powerful-guts.html")

@app.route("/resist-sleep")
def resist_sleep():
	return render_template("resist-sleep.html")

@app.route("/rooted")
def rooted():
	return render_template("rooted.html")

@app.route("/scar-thick-skin")
def scar_thick_skin():
	return render_template("scar-thick-skin.html")

@app.route("/steady-guts")
def steady_guts():
	return render_template("steady-guts.html")

@app.route("/steelskin")
def steelskin():
	return render_template("steelskin.html")

@app.route("/stormtossed")
def stormtossed():
	return render_template("stormtossed.html")

@app.route("/unfettered")
def unfettered():
	return render_template("unfettered.html")

@app.route("/vigorous-health")
def vigorous_health():
	return render_template("vigorous-health.html")

@app.route("/vivacious")
def vivacious():
	return render_template("vivacious.html")

@app.route("/well-groomed")
def well_groomed():
	return render_template("well-groomed.html")

@app.route("/wind-tempered")
def wind_tempered():
	return render_template("wind-tempered.html")

@app.route("/seedpod")
def seedpod():
	return render_template("seedpod.html")

@app.route("/thorned-seedpod")
def thorned_seedpod():
	return render_template("thorned-seedpod.html")

@app.route("/hear-the-heartbeat")
def hear_the_heartbeat():
	return render_template("hear-the-heartbeat.html")

@app.route("/lifesense")
def lifesense():
	return render_template("lifesense.html")

@app.route("/low-light-vision")
def low_light_vision():
	return render_template("low-light-vision.html")

@app.route("/plague-sense")
def plague_sense():
	return render_template("plague-sense.html")

@app.route("/tactile-oceaner")
def tactile_oceaner():
	return render_template("tactile-oceaner.html")

@app.route("/uncanny-awareness")
def uncanny_awareness():
	return render_template("uncanny-awareness.html")

@app.route("/step-lively")
def step_lively():
	return render_template("step-lively.html")

@app.route("/shinstabber")
def shinstabber():
	return render_template("shinstabber.html")

@app.route("/toppling-dance")
def toppling_dance():
	return render_template("toppling-dance.html")

@app.route("/tough-tumbler")
def tough_tumbler():
	return render_template("tough-tumbler.html")

@app.route("/mist-child")
def mist_child():
	return render_template("mist-child.html")

@app.route("/veil-skin")
def veil_skin():
	return render_template("veil-skin.html")

@app.route("/spines")
def spines():
	return render_template("spines.html")

@app.route("/toxic-spines")
def toxic_spines():
	return render_template("toxic-spines.html")

@app.route("/spore-cloud")
def spore_cloud():
	return render_template("spore-cloud.html")

@app.route("/eerie-compression")
def eerie_compression():
	return render_template("eerie-compression.html")

@app.route("/flexible")
def flexible():
	return render_template("flexible.html")

@app.route("/lightless-litheness")
def lightless_litheness():
	return render_template("lightless-litheness.html")

@app.route("/smushy")
def smushy():
	return render_template("smushy.html")

@app.route("/drowning-and-suffocation")
def drowning_and_suffocation():
	return render_template("drowning-and-suffocation.html")

@app.route("/internal-respirator")
def internal_respirator():
	return render_template("internal-respirator.html")

@app.route("/irongut")
def irongut():
	return render_template("irongut.html")

@app.route("/starvation-and-thirst")
def starvation_and_thirst():
	return render_template("starvation-and-thirst.html")

@app.route("/parthenogenic")
def parthenogenic():
	return render_template("parthenogenic.html")

@app.route("/root-feeder")
def root_feeder():
	return render_template("root-feeder.html")

@app.route("/dust-soul")
def dust_soul():
	return render_template("dust-soul.html")

@app.route("/long-marcher")
def long_marcher():
	return render_template("long-marcher.html")

@app.route("/tongue-disarm")
def tongue_disarm():
	return render_template("tongue-disarm.html")

@app.route("/control-fall")
def control_fall():
	return render_template("control-fall.html")

@app.route("/true-breakfall")
def true_breakfall():
	return render_template("true-breakfall.html")

@app.route("/dangle")
def dangle():
	return render_template("dangle.html")

@app.route("/hard-appendage")
def hard_appendage():
	return render_template("hard-appendage.html")

@app.route("/larcenous-appendage")
def larcenous_appendage():
	return render_template("larcenous-appendage.html")

@app.route("/shed-appendage")
def shed_appendage():
	return render_template("shed-appendage.html")

@app.route("/mischievous-appendage")
def mischievous_appendage():
	return render_template("mischievous-appendage.html")

@app.route("/soaring-flight")
def soaring_flight():
	return render_template("soaring-flight.html")

@app.route("/limited-flight")
def limited_flight():
	return render_template("limited-flight.html")

@app.route("/glide")
def glide():
	return render_template("glide.html")

@app.route("/wing-cloak")
def wing_cloak():
	return render_template("wing-cloak.html")

@app.route("/aquatic-combat")
def aquatic_combat():
	return render_template("aquatic-combat.html")

@app.route("/aquatic-camouflage")
def aquatic_camouflage():
	return render_template("aquatic-camouflage.html")

@app.route("/deep-diver")
def deep_diver():
	return render_template("deep-diver.html")

@app.route("/perfect-dive")
def perfect_dive():
	return render_template("perfect-dive.html")

@app.route("/perfect-lungs")
def perfect_lungs():
	return render_template("perfect-lungs.html")

@app.route("/water-diver")
def water_diver():
	return render_template("water-diver.html")

@app.route("/water-piercer")
def water_piercer():
	return render_template("water-piercer.html")

@app.route("/brine-born")
def brine_born():
	return render_template("brine-born.html")

@app.route("/venomous")
def venomous():
	return render_template("venomous.html")

@app.route("/fae-killer")
def fae_killer():
	return render_template("fae-killer.html")

@app.route("/lycanthrope-killer")
def lycanthrope_killer():
	return render_template("lycanthrope-killer.html")

@app.route("/spiteful-rake")
def spiteful_rake():
	return render_template("spiteful-rake.html")

@app.route("/natural-climbing")
def natural_climbing():
	return render_template("natural-climbing.html")

@app.route("/alter-resistance")
def alter_resistance():
	return render_template("alter-resistance.html")

@app.route("/freeze-it")
def freeze_it():
	return render_template("freeze-it.html")

@app.route("/slip-the-grasp")
def slip_the_grasp():
	return render_template("slip-the-grasp.html")

@app.route("/sickening-counter")
def sickening_counter():
	return render_template("sickening-counter.html")

@app.route("/quadro")
def quadro():
	return render_template("quadro.html")

@app.route("/preemptive-configuration")
def preemptive_configuration():
	return render_template("preemptive-configuration.html")

@app.route("/roll-with-it")
def roll_with_it():
	return render_template("roll-with-it.html")

@app.route("/chameleon")
def chameleon():
	return render_template("chameleon.html")

@app.route("/ferocious-beasts")
def ferocious_beasts():
	return render_template("ferocious-beasts.html")

@app.route("/natural-climber")
def natural_climber():
	return render_template("natural-climber.html")

@app.route("/allys-shelter")
def allys_shelter():
	return render_template("allys-shelter.html")

@app.route("/cooperative-nature")
def cooperative_nature():
	return render_template("cooperative-nature.html")

@app.route("/cooperative-soul")
def cooperative_soul():
	return render_template("cooperative-soul.html")

@app.route("/group-aid")
def group_aid():
	return render_template("group-aid.html")

@app.route("/ghost-strike")
def ghost_strike():
	return render_template("ghost-strike.html")

@app.route("/extreme-shared-luck")
def extreme_shared_luck():
	return render_template("extreme-shared-luck.html")

@app.route("/light-adjustment")
def light_adjustment():
	return render_template("light-adjustment.html")

@app.route("/heartened-vivacity")
def heartened_vivacity():
	return render_template("heartened-vivacity.html")

@app.route("/hard-to-fool")
def hard_to_fool():
	return render_template("hard-to-fool.html")

@app.route("/finest-trick")
def finest_trick():
	return render_template("finest-trick.html")

@app.route("/distracting-shadows")
def distracting_shadows():
	return render_template("distracting-shadows.html")

@app.route("/appendage-spin")
def appendage_spin():
	return render_template("appendage-spin.html")

@app.route("/steady-balance")
def steady_balance():
	return render_template("steady-balance.html")

@app.route("/nimble-crawl")
def nimble_crawl():
	return render_template("nimble-crawl.html")

@app.route("/masterful-crawl")
def masterful_crawl():
	return render_template("masterful-crawl.html")

@app.route("/contortionist")
def contortionist():
	return render_template("contortionist.html")

@app.route("/cat-fall")
def cat_fall():
	return render_template("cat-fall.html")

@app.route("/masterful-cat-fall")
def masterful_cat_fall():
	return render_template("masterful-cat-fall.html")

@app.route("/legendary-catfall")
def legendary_catfall():
	return render_template("legendary-catfall.html")

@app.route("/aerobatic-mastery")
def aerobatic_mastery():
	return render_template("aerobatic-mastery.html")

@app.route("/acrobatic-performer")
def acrobatic_performer():
	return render_template("acrobatic-performer.html")

@app.route("/prone-fighter")
def prone_fighter():
	return render_template("prone-fighter.html")

@app.route("/quick-squeeze")
def quick_squeeze():
	return render_template("quick-squeeze.html")

@app.route("/legendary-squeeze")
def legendary_squeeze():
	return render_template("legendary-squeeze.html")

@app.route("/kip-up")
def kip_up():
	return render_template("kip-up.html")

@app.route("/shake-it-up")
def shake_it_up():
	return render_template("shake-it-up.html")

@app.route("/acrobat-dedication")
def acrobat_dedication():
	return render_template("acrobat-dedication.html")

@app.route("/tumble-behind")
def tumble_behind():
	return render_template("tumble-behind.html")

@app.route("/travel-domain-travelers-transit")
def travel_domain_travelers_transit():
	return render_template("travel-domain-travelers-transit.html")

@app.route("/impressive-landing")
def impressive_landing():
	return render_template("impressive-landing.html")

@app.route("/graceful-landing")
def graceful_landing():
	return render_template("graceful-landing.html")

@app.route("/water-step")
def water_step():
	return render_template("water-step.html")

@app.route("/cloud-walk")
def cloud_walk():
	return render_template("cloud-walk.html")

@app.route("/implausible-infiltration")
def implausible_infiltration():
	return render_template("implausible-infiltration.html")

@app.route("/travel-domain-agile-feet")
def travel_domain_agile_feet():
	return render_template("travel-domain-agile-feet.html")

@app.route("/freedom-domain-unimpeded-stride")
def freedom_domain_unimpeded_stride():
	return render_template("freedom-domain-unimpeded-stride.html")

@app.route("/freedom-domain-word-of-freedom")
def freedom_domain_word_of_freedom():
	return render_template("freedom-domain-word-of-freedom.html")

@app.route("/dodging-roll")
def dodging_roll():
	return render_template("dodging-roll.html")

@app.route("/tumbling-strike")
def tumbling_strike():
	return render_template("tumbling-strike.html")

@app.route("/acrobatic-dodge")
def acrobatic_dodge():
	return render_template("acrobatic-dodge.html")

@app.route("/defensive-roll")
def defensive_roll():
	return render_template("defensive-roll.html")

@app.route("/graceful-leaper")
def graceful_leaper():
	return render_template("graceful-leaper.html")

@app.route("/dancing-leaf")
def dancing_leaf():
	return render_template("dancing-leaf.html")

@app.route("/additive")
def additive():
	return render_template("additive.html")

@app.route("/exploitive-bomb")
def exploitive_bomb():
	return render_template("exploitive-bomb.html")

@app.route("/astonishing-explosive")
def astonishing_explosive():
	return render_template("astonishing-explosive.html")

@app.route("/perpetual-bomber")
def perpetual_bomber():
	return render_template("perpetual-bomber.html")

@app.route("/splash")
def splash():
	return render_template("splash.html")

@app.route("/demolition-charge")
def demolition_charge():
	return render_template("demolition-charge.html")

@app.route("/greater-bomb-discovery")
def greater_bomb_discovery():
	return render_template("greater-bomb-discovery.html")

@app.route("/bomb-making-prodigy")
def bomb_making_prodigy():
	return render_template("bomb-making-prodigy.html")

@app.route("/directional-bomb")
def directional_bomb():
	return render_template("directional-bomb.html")

@app.route("/mega-bomb")
def mega_bomb():
	return render_template("mega-bomb.html")

@app.route("/perfect-debilitation")
def perfect_debilitation():
	return render_template("perfect-debilitation.html")

@app.route("/quick-bomber")
def quick_bomber():
	return render_template("quick-bomber.html")

@app.route("/smoke-bomb")
def smoke_bomb():
	return render_template("smoke-bomb.html")

@app.route("/sticky-bomb")
def sticky_bomb():
	return render_template("sticky-bomb.html")

@app.route("/true-debilitating-bomb")
def true_debilitating_bomb():
	return render_template("true-debilitating-bomb.html")

@app.route("/greater-debilitating-bomb")
def greater_debilitating_bomb():
	return render_template("greater-debilitating-bomb.html")

@app.route("/uncanny-bombs")
def uncanny_bombs():
	return render_template("uncanny-bombs.html")

@app.route("/golem-grafter")
def golem_grafter():
	return render_template("golem-grafter.html")

@app.route("/accursed-fist")
def accursed_fist():
	return render_template("accursed-fist.html")

@app.route("/iron-lung")
def iron_lung():
	return render_template("iron-lung.html")

@app.route("/legs-of-stone")
def legs_of_stone():
	return render_template("legs-of-stone.html")

@app.route("/quicken-heartbeat")
def quicken_heartbeat():
	return render_template("quicken-heartbeat.html")

@app.route("/healing-bomb")
def healing_bomb():
	return render_template("healing-bomb.html")

@app.route("/greater-merciful-elixir")
def greater_merciful_elixir():
	return render_template("greater-merciful-elixir.html")

@app.route("/surgical-prodigy")
def surgical_prodigy():
	return render_template("surgical-prodigy.html")

@app.route("/supreme-surgical-prodigy")
def supreme_surgical_prodigy():
	return render_template("supreme-surgical-prodigy.html")

@app.route("/alchemical-alacrity")
def alchemical_alacrity():
	return render_template("alchemical-alacrity.html")

@app.route("/efficient-alchemy")
def efficient_alchemy():
	return render_template("efficient-alchemy.html")

@app.route("/enduring-alchemy")
def enduring_alchemy():
	return render_template("enduring-alchemy.html")

@app.route("/unstable-concoction")
def unstable_concoction():
	return render_template("unstable-concoction.html")

@app.route("/feral-mutagen")
def feral_mutagen():
	return render_template("feral-mutagen.html")

@app.route("/mutagen-prodigy")
def mutagen_prodigy():
	return render_template("mutagen-prodigy.html")

@app.route("/perpetual-mutagenist")
def perpetual_mutagenist():
	return render_template("perpetual-mutagenist.html")

@app.route("/shaped-contaminant")
def shaped_contaminant():
	return render_template("shaped-contaminant.html")

@app.route("/improved-poison-weapon")
def improved_poison_weapon():
	return render_template("improved-poison-weapon.html")

@app.route("/deadly-weapon-poison")
def deadly_weapon_poison():
	return render_template("deadly-weapon-poison.html")

@app.route("/poison-coat")
def poison_coat():
	return render_template("poison-coat.html")

@app.route("/poisoners-twist")
def poisoners_twist():
	return render_template("poisoners-twist.html")

@app.route("/perpetual-toxicologist")
def perpetual_toxicologist():
	return render_template("perpetual-toxicologist.html")

@app.route("/toxicology-prodigy")
def toxicology_prodigy():
	return render_template("toxicology-prodigy.html")

@app.route("/toxicological-discovery")
def toxicological_discovery():
	return render_template("toxicological-discovery.html")

@app.route("/eternal-elixir")
def eternal_elixir():
	return render_template("eternal-elixir.html")

@app.route("/crystal-keeper")
def crystal_keeper():
	return render_template("crystal-keeper.html")

@app.route("/strange-script")
def strange_script():
	return render_template("strange-script.html")

@app.route("/unravel-mysteries")
def unravel_mysteries():
	return render_template("unravel-mysteries.html")

@app.route("/assured-identification")
def assured_identification():
	return render_template("assured-identification.html")

@app.route("/quick-identify")
def quick_identify():
	return render_template("quick-identify.html")

@app.route("/recognize-spell")
def recognize_spell():
	return render_template("recognize-spell.html")

@app.route("/quick-recognition")
def quick_recognition():
	return render_template("quick-recognition.html")

@app.route("/spellmaster")
def spellmaster():
	return render_template("spellmaster.html")

@app.route("/loaner-spell")
def loaner_spell():
	return render_template("loaner-spell.html")

@app.route("/timeless-body")
def timeless_body():
	return render_template("timeless-body.html")

@app.route("/bardic-lore")
def bardic_lore():
	return render_template("bardic-lore.html")

@app.route("/assured-knowledge")
def assured_knowledge():
	return render_template("assured-knowledge.html")

@app.route("/automatic-knowledge")
def automatic_knowledge():
	return render_template("automatic-knowledge.html")

@app.route("/bestiary-scholar")
def bestiary_scholar():
	return render_template("bestiary-scholar.html")

@app.route("/combat-assessment")
def combat_assessment():
	return render_template("combat-assessment.html")

@app.route("/diverse-recognition")
def diverse_recognition():
	return render_template("diverse-recognition.html")

@app.route("/dubious-knowledge")
def dubious_knowledge():
	return render_template("dubious-knowledge.html")

@app.route("/enigmas-knowledge")
def enigmas_knowledge():
	return render_template("enigmas-knowledge.html")

@app.route("/innate-magic-intuition")
def innate_magic_intuition():
	return render_template("innate-magic-intuition.html")

@app.route("/masterful-obfuscation")
def masterful_obfuscation():
	return render_template("masterful-obfuscation.html")

@app.route("/knowledge-domain-scholarly-recollection")
def knowledge_domain_scholarly_recollection():
	return render_template("knowledge-domain-scholarly-recollection.html")

@app.route("/knowledge-domain-know-the-enemy")
def knowledge_domain_know_the_enemy():
	return render_template("knowledge-domain-know-the-enemy.html")

@app.route("/mastermind")
def mastermind():
	return render_template("mastermind.html")

@app.route("/clever-gambit")
def clever_gambit():
	return render_template("clever-gambit.html")

@app.route("/reason-rapidly")
def reason_rapidly():
	return render_template("reason-rapidly.html")

@app.route("/recognize-threat")
def recognize_threat():
	return render_template("recognize-threat.html")

@app.route("/recollect-studies")
def recollect_studies():
	return render_template("recollect-studies.html")

@app.route("/remember-your-training")
def remember_your_training():
	return render_template("remember-your-training.html")

@app.route("/storytelling")
def storytelling():
	return render_template("storytelling.html")

@app.route("/storytelling-recollection")
def storytelling_recollection():
	return render_template("storytelling-recollection.html")

@app.route("/storytelling-lessons")
def storytelling_lessons():
	return render_template("storytelling-lessons.html")

@app.route("/thorough-reports")
def thorough_reports():
	return render_template("thorough-reports.html")

@app.route("/discerning-strike")
def discerning_strike():
	return render_template("discerning-strike.html")

@app.route("/thorough-research")
def thorough_research():
	return render_template("thorough-research.html")

@app.route("/just-the-facts")
def just_the_facts():
	return render_template("just-the-facts.html")

@app.route("/know-what-you-know")
def know_what_you_know():
	return render_template("know-what-you-know.html")

@app.route("/cheat-death")
def cheat_death():
	return render_template("cheat-death.html")

@app.route("/spellmasters-resilience")
def spellmasters_resilience():
	return render_template("spellmasters-resilience.html")

@app.route("/spellmasters-tenacity")
def spellmasters_tenacity():
	return render_template("spellmasters-tenacity.html")

@app.route("/trick-magic-item")
def trick_magic_item():
	return render_template("trick-magic-item.html")

@app.route("/scroll-trickster")
def scroll_trickster():
	return render_template("scroll-trickster.html")

@app.route("/foolproof-instructions")
def foolproof_instructions():
	return render_template("foolproof-instructions.html")

@app.route("/scroll-cache")
def scroll_cache():
	return render_template("scroll-cache.html")

@app.route("/skim-scroll")
def skim_scroll():
	return render_template("skim-scroll.html")

@app.route("/hunters-luck")
def hunters_luck():
	return render_template("hunters-luck.html")

@app.route("/draconic-bloodline-dragon-claws")
def draconic_bloodline_dragon_claws():
	return render_template("draconic-bloodline-dragon-claws.html")

@app.route("/draconic-bloodline-dragon-breath")
def draconic_bloodline_dragon_breath():
	return render_template("draconic-bloodline-dragon-breath.html")

@app.route("/draconic-bloodline-dragon-wings")
def draconic_bloodline_dragon_wings():
	return render_template("draconic-bloodline-dragon-wings.html")

@app.route("/fey-bloodline-genies-veil")
def fey_bloodline_genies_veil():
	return render_template("fey-bloodline-genies-veil.html")

@app.route("/fey-bloodline-hearts-desire")
def fey_bloodline_hearts_desire():
	return render_template("fey-bloodline-hearts-desire.html")

@app.route("/fey-bloodline-wish-twisted-form")
def fey_bloodline_wish_twisted_form():
	return render_template("fey-bloodline-wish-twisted-form.html")

@app.route("/imperial-bloodline-extend-spell")
def imperial_bloodline_extend_spell():
	return render_template("imperial-bloodline-extend-spell.html")

@app.route("/imperial-bloodline-arcane-countermeasures")
def imperial_bloodline_arcane_countermeasures():
	return render_template("imperial-bloodline-arcane-countermeasures.html")

@app.route("/imperial-bloodline-ancestral-memories")
def imperial_bloodline_ancestral_memories():
	return render_template("imperial-bloodline-ancestral-memories.html")

@app.route("/change-domain-adapt-self")
def change_domain_adapt_self():
	return render_template("change-domain-adapt-self.html")

@app.route("/change-domain-adaptive-ablation")
def change_domain_adaptive_ablation():
	return render_template("change-domain-adaptive-ablation.html")

@app.route("/glyph-domain-ghostly-transcription")
def glyph_domain_ghostly_transcription():
	return render_template("glyph-domain-ghostly-transcription.html")

@app.route("/glyph-domain-redact")
def glyph_domain_redact():
	return render_template("glyph-domain-redact.html")

@app.route("/magic-domain-magics-vessel")
def magic_domain_magics_vessel():
	return render_template("magic-domain-magics-vessel.html")

@app.route("/time-domain-delay-consequence")
def time_domain_delay_consequence():
	return render_template("time-domain-delay-consequence.html")

@app.route("/time-domain-stasis")
def time_domain_stasis():
	return render_template("time-domain-stasis.html")

@app.route("/wyrmkin-domain-draconic-barrage")
def wyrmkin_domain_draconic_barrage():
	return render_template("wyrmkin-domain-draconic-barrage.html")

@app.route("/wyrmkin-domain-roar-of-the-wyrm")
def wyrmkin_domain_roar_of_the_wyrm():
	return render_template("wyrmkin-domain-roar-of-the-wyrm.html")

@app.route("/dragon-disciple")
def dragon_disciple():
	return render_template("dragon-disciple.html")

@app.route("/claws-of-the-dragon")
def claws_of_the_dragon():
	return render_template("claws-of-the-dragon.html")

@app.route("/draconic-scent")
def draconic_scent():
	return render_template("draconic-scent.html")

@app.route("/scales-of-the-dragon")
def scales_of_the_dragon():
	return render_template("scales-of-the-dragon.html")

@app.route("/crystal-keeper-focus")
def crystal_keeper_focus():
	return render_template("crystal-keeper-focus.html")

@app.route("/glyph-expert")
def glyph_expert():
	return render_template("glyph-expert.html")

@app.route("/unified-theory")
def unified_theory():
	return render_template("unified-theory.html")

@app.route("/spellmasters-ward")
def spellmasters_ward():
	return render_template("spellmasters-ward.html")

@app.route("/augment-summoning")
def augment_summoning():
	return render_template("augment-summoning.html")

@app.route("/call-of-the-grave")
def call_of_the_grave():
	return render_template("call-of-the-grave.html")

@app.route("/charming-words")
def charming_words():
	return render_template("charming-words.html")

@app.route("/dimensional-steps")
def dimensional_steps():
	return render_template("dimensional-steps.html")

@app.route("/diviners-sight")
def diviners_sight():
	return render_template("diviners-sight.html")

@app.route("/dread-aura")
def dread_aura():
	return render_template("dread-aura.html")

@app.route("/protective-ward")
def protective_ward():
	return render_template("protective-ward.html")

@app.route("/energy-absorption")
def energy_absorption():
	return render_template("energy-absorption.html")

@app.route("/hand-of-the-apprentice")
def hand_of_the_apprentice():
	return render_template("hand-of-the-apprentice.html")

@app.route("/warped-terrain")
def warped_terrain():
	return render_template("warped-terrain.html")

@app.route("/physical-boost")
def physical_boost():
	return render_template("physical-boost.html")

@app.route("/shifting-form")
def shifting_form():
	return render_template("shifting-form.html")

@app.route("/universal-versatility")
def universal_versatility():
	return render_template("universal-versatility.html")

@app.route("/vigilant-eye")
def vigilant_eye():
	return render_template("vigilant-eye.html")

@app.route("/magic-sense")
def magic_sense():
	return render_template("magic-sense.html")

@app.route("/combat-climber")
def combat_climber():
	return render_template("combat-climber.html")

@app.route("/impossible-climber")
def impossible_climber():
	return render_template("impossible-climber.html")

@app.route("/follow-the-expert")
def follow_the_expert():
	return render_template("follow-the-expert.html")

@app.route("/lead-climber")
def lead_climber():
	return render_template("lead-climber.html")

@app.route("/quick-climber")
def quick_climber():
	return render_template("quick-climber.html")

@app.route("/rapid-mantel")
def rapid_mantel():
	return render_template("rapid-mantel.html")

@app.route("/wall-jump")
def wall_jump():
	return render_template("wall-jump.html")

@app.route("/titan-wrestler")
def titan_wrestler():
	return render_template("titan-wrestler.html")

@app.route("/might-domain-enduring-might")
def might_domain_enduring_might():
	return render_template("might-domain-enduring-might.html")

@app.route("/might-domain-athletic-rush")
def might_domain_athletic_rush():
	return render_template("might-domain-athletic-rush.html")

@app.route("/cloud-jump")
def cloud_jump():
	return render_template("cloud-jump.html")

@app.route("/powerful-leap")
def powerful_leap():
	return render_template("powerful-leap.html")

@app.route("/quick-jump")
def quick_jump():
	return render_template("quick-jump.html")

@app.route("/forced-entry")
def forced_entry():
	return render_template("forced-entry.html")

@app.route("/adrenaline-rush")
def adrenaline_rush():
	return render_template("adrenaline-rush.html")

@app.route("/bashing-charge")
def bashing_charge():
	return render_template("bashing-charge.html")

@app.route("/hefty-hauler")
def hefty_hauler():
	return render_template("hefty-hauler.html")

@app.route("/incredible-movement")
def incredible_movement():
	return render_template("incredible-movement.html")

@app.route("/water-sprint")
def water_sprint():
	return render_template("water-sprint.html")

@app.route("/wall-run")
def wall_run():
	return render_template("wall-run.html")

@app.route("/breath-control")
def breath_control():
	return render_template("breath-control.html")

@app.route("/impossible-swimmer")
def impossible_swimmer():
	return render_template("impossible-swimmer.html")

@app.route("/quick-swim")
def quick_swim():
	return render_template("quick-swim.html")

@app.route("/underwater-marauder")
def underwater_marauder():
	return render_template("underwater-marauder.html")

@app.route("/pick-up-the-pace")
def pick_up_the_pace():
	return render_template("pick-up-the-pace.html")

@app.route("/caravan-leader")
def caravan_leader():
	return render_template("caravan-leader.html")

@app.route("/friendly-toss")
def friendly_toss():
	return render_template("friendly-toss.html")

@app.route("/sticky-poison")
def sticky_poison():
	return render_template("sticky-poison.html")

@app.route("/alchemical-crafter-efficiency")
def alchemical_crafter_efficiency():
	return render_template("alchemical-crafter-efficiency.html")

@app.route("/tweak-appearances")
def tweak_appearances():
	return render_template("tweak-appearances.html")

@app.route("/bless-tonic")
def bless_tonic():
	return render_template("bless-tonic.html")

@app.route("/bless-toxin")
def bless_toxin():
	return render_template("bless-toxin.html")

@app.route("/rapid-affixture")
def rapid_affixture():
	return render_template("rapid-affixture.html")

@app.route("/seasoned")
def seasoned():
	return render_template("seasoned.html")

@app.route("/specialty-crafting")
def specialty_crafting():
	return render_template("specialty-crafting.html")

@app.route("/impeccable-crafting")
def impeccable_crafting():
	return render_template("impeccable-crafting.html")

@app.route("/creation-domain-artistic-flourish")
def creation_domain_artistic_flourish():
	return render_template("creation-domain-artistic-flourish.html")

@app.route("/creation-domain-splash-of-art")
def creation_domain_splash_of_art():
	return render_template("creation-domain-splash-of-art.html")

@app.route("/indulgence-domain-overstuff")
def indulgence_domain_overstuff():
	return render_template("indulgence-domain-overstuff.html")

@app.route("/indulgence-domain-take-its-course")
def indulgence_domain_take_its_course():
	return render_template("indulgence-domain-take-its-course.html")

@app.route("/reverse-engineering")
def reverse_engineering():
	return render_template("reverse-engineering.html")

@app.route("/alchemical-savant")
def alchemical_savant():
	return render_template("alchemical-savant.html")

@app.route("/stone-blood")
def stone_blood():
	return render_template("stone-blood.html")

@app.route("/fortified-flesh")
def fortified_flesh():
	return render_template("fortified-flesh.html")

@app.route("/improvised-crafting")
def improvised_crafting():
	return render_template("improvised-crafting.html")

@app.route("/shoddy")
def shoddy():
	return render_template("shoddy.html")

@app.route("/quick-repair")
def quick_repair():
	return render_template("quick-repair.html")

@app.route("/craft-facsimile")
def craft_facsimile():
	return render_template("craft-facsimile.html")

@app.route("/scrounger")
def scrounger():
	return render_template("scrounger.html")

@app.route("/high-quality-scrounging")
def high_quality_scrounging():
	return render_template("high-quality-scrounging.html")

@app.route("/signifier-mask")
def signifier_mask():
	return render_template("signifier-mask.html")

@app.route("/masked-casting")
def masked_casting():
	return render_template("masked-casting.html")

@app.route("/signifiers-sight")
def signifiers_sight():
	return render_template("signifiers-sight.html")

@app.route("/expert-disassembler")
def expert_disassembler():
	return render_template("expert-disassembler.html")

@app.route("/giant-snare")
def giant_snare():
	return render_template("giant-snare.html")

@app.route("/quick-snares")
def quick_snares():
	return render_template("quick-snares.html")

@app.route("/lightning-snares")
def lightning_snares():
	return render_template("lightning-snares.html")

@app.route("/remote-trigger")
def remote_trigger():
	return render_template("remote-trigger.html")

@app.route("/snare-hopping")
def snare_hopping():
	return render_template("snare-hopping.html")

@app.route("/surprise-snare")
def surprise_snare():
	return render_template("surprise-snare.html")

@app.route("/ubiquitous-snares")
def ubiquitous_snares():
	return render_template("ubiquitous-snares.html")

@app.route("/impossible-snares")
def impossible_snares():
	return render_template("impossible-snares.html")

@app.route("/improvised-repair")
def improvised_repair():
	return render_template("improvised-repair.html")

@app.route("/bargain-hunter")
def bargain_hunter():
	return render_template("bargain-hunter.html")

@app.route("/dandy")
def dandy():
	return render_template("dandy.html")

@app.route("/hobnobber")
def hobnobber():
	return render_template("hobnobber.html")

@app.route("/entourage")
def entourage():
	return render_template("entourage.html")

@app.route("/mesmerizing-gaze")
def mesmerizing_gaze():
	return render_template("mesmerizing-gaze.html")

@app.route("/command-attention")
def command_attention():
	return render_template("command-attention.html")

@app.route("/vigilante")
def vigilante():
	return render_template("vigilante.html")

@app.route("/lion-blade-spy")
def lion_blade_spy():
	return render_template("lion-blade-spy.html")

@app.route("/subjective-truth")
def subjective_truth():
	return render_template("subjective-truth.html")

@app.route("/sow-rumor")
def sow_rumor():
	return render_template("sow-rumor.html")

@app.route("/quick-disguise")
def quick_disguise():
	return render_template("quick-disguise.html")

@app.route("/discreet-inquiry")
def discreet_inquiry():
	return render_template("discreet-inquiry.html")

@app.route("/hidden-magic")
def hidden_magic():
	return render_template("hidden-magic.html")

@app.route("/confabulator")
def confabulator():
	return render_template("confabulator.html")

@app.route("/slippery-secrets")
def slippery_secrets():
	return render_template("slippery-secrets.html")

@app.route("/fabricated-connections")
def fabricated_connections():
	return render_template("fabricated-connections.html")

@app.route("/charlatan")
def charlatan():
	return render_template("charlatan.html")

@app.route("/quick-change")
def quick_change():
	return render_template("quick-change.html")

@app.route("/convincing-illusion")
def convincing_illusion():
	return render_template("convincing-illusion.html")

@app.route("/flicker")
def flicker():
	return render_template("flicker.html")

@app.route("/lengthy-diversion")
def lengthy_diversion():
	return render_template("lengthy-diversion.html")

@app.route("/trickery-domain-sudden-shift")
def trickery_domain_sudden_shift():
	return render_template("trickery-domain-sudden-shift.html")

@app.route("/reactive-distraction")
def reactive_distraction():
	return render_template("reactive-distraction.html")

@app.route("/reveal-machinations")
def reveal_machinations():
	return render_template("reveal-machinations.html")

@app.route("/lie-to-me")
def lie_to_me():
	return render_template("lie-to-me.html")

@app.route("/distracting-flattery")
def distracting_flattery():
	return render_template("distracting-flattery.html")

@app.route("/backup-disguise")
def backup_disguise():
	return render_template("backup-disguise.html")

@app.route("/charming-liar")
def charming_liar():
	return render_template("charming-liar.html")

@app.route("/analyze-idiolect")
def analyze_idiolect():
	return render_template("analyze-idiolect.html")

@app.route("/spys-countermeasures")
def spys_countermeasures():
	return render_template("spys-countermeasures.html")

@app.route("/blank-slate")
def blank_slate():
	return render_template("blank-slate.html")

@app.route("/many-guises")
def many_guises():
	return render_template("many-guises.html")

@app.route("/double-speak")
def double_speak():
	return render_template("double-speak.html")

@app.route("/trickery-domain-tricksters-twin")
def trickery_domain_tricksters_twin():
	return render_template("trickery-domain-tricksters-twin.html")

@app.route("/bravos-determination")
def bravos_determination():
	return render_template("bravos-determination.html")

@app.route("/secret-speech")
def secret_speech():
	return render_template("secret-speech.html")

@app.route("/family-domain-soothing-words")
def family_domain_soothing_words():
	return render_template("family-domain-soothing-words.html")

@app.route("/family-domain-unity")
def family_domain_unity():
	return render_template("family-domain-unity.html")

@app.route("/passion-domain-captivating-adoration")
def passion_domain_captivating_adoration():
	return render_template("passion-domain-captivating-adoration.html")

@app.route("/passion-domain-charming-touch")
def passion_domain_charming_touch():
	return render_template("passion-domain-charming-touch.html")

@app.route("/bon-mot")
def bon_mot():
	return render_template("bon-mot.html")

@app.route("/evangelize")
def evangelize():
	return render_template("evangelize.html")

@app.route("/pointed-question")
def pointed_question():
	return render_template("pointed-question.html")

@app.route("/glad-hand")
def glad_hand():
	return render_template("glad-hand.html")

@app.route("/group-impression")
def group_impression():
	return render_template("group-impression.html")

@app.route("/legendary-negotiation")
def legendary_negotiation():
	return render_template("legendary-negotiation.html")

@app.route("/shameless-request")
def shameless_request():
	return render_template("shameless-request.html")

@app.route("/tense-negotiator")
def tense_negotiator():
	return render_template("tense-negotiator.html")

@app.route("/all-in-my-head")
def all_in_my_head():
	return render_template("all-in-my-head.html")

@app.route("/no-cause-for-alarm")
def no_cause_for_alarm():
	return render_template("no-cause-for-alarm.html")

@app.route("/one-for-all")
def one_for_all():
	return render_template("one-for-all.html")

@app.route("/ringmasters-introduction")
def ringmasters_introduction():
	return render_template("ringmasters-introduction.html")

@app.route("/diplomacy-feats")
def diplomacy_feats():
	return render_template("diplomacy-feats.html")

@app.route("/diehard")
def diehard():
	return render_template("diehard.html")

@app.route("/necromantic-resistance")
def necromantic_resistance():
	return render_template("necromantic-resistance.html")

@app.route("/necromantic-resilience")
def necromantic_resilience():
	return render_template("necromantic-resilience.html")

@app.route("/toughness")
def toughness():
	return render_template("toughness.html")

@app.route("/acquired-tolerance")
def acquired_tolerance():
	return render_template("acquired-tolerance.html")

@app.route("/divine-health")
def divine_health():
	return render_template("divine-health.html")

@app.route("/inner-strength")
def inner_strength():
	return render_template("inner-strength.html")

@app.route("/resist-poison")
def resist_poison():
	return render_template("resist-poison.html")

@app.route("/swift-river")
def swift_river():
	return render_template("swift-river.html")

@app.route("/ardent-nature")
def ardent_nature():
	return render_template("ardent-nature.html")

@app.route("/aura-of-courage")
def aura_of_courage():
	return render_template("aura-of-courage.html")

@app.route("/bravery")
def bravery():
	return render_template("bravery.html")

@app.route("/cognitive-loophole")
def cognitive_loophole():
	return render_template("cognitive-loophole.html")

@app.route("/conceited-mindset")
def conceited_mindset():
	return render_template("conceited-mindset.html")

@app.route("/determination")
def determination():
	return render_template("determination.html")

@app.route("/enlightened-presence")
def enlightened_presence():
	return render_template("enlightened-presence.html")

@app.route("/pure-clarity")
def pure_clarity():
	return render_template("pure-clarity.html")

@app.route("/projected-clarity")
def projected_clarity():
	return render_template("projected-clarity.html")

@app.route("/resounding-bravery")
def resounding_bravery():
	return render_template("resounding-bravery.html")

@app.route("/shake-it-off")
def shake_it_off():
	return render_template("shake-it-off.html")

@app.route("/unshakeable-idealism")
def unshakeable_idealism():
	return render_template("unshakeable-idealism.html")

@app.route("/ward-mind")
def ward_mind():
	return render_template("ward-mind.html")

@app.route("/immutable-body")
def immutable_body():
	return render_template("immutable-body.html")

@app.route("/group-coercion")
def group_coercion():
	return render_template("group-coercion.html")

@app.route("/lasting-coercion")
def lasting_coercion():
	return render_template("lasting-coercion.html")

@app.route("/quick-coercion")
def quick_coercion():
	return render_template("quick-coercion.html")

@app.route("/antagonize")
def antagonize():
	return render_template("antagonize.html")

@app.route("/deimatic-display")
def deimatic_display():
	return render_template("deimatic-display.html")

@app.route("/intimidating-glare")
def intimidating_glare():
	return render_template("intimidating-glare.html")

@app.route("/scare-to-death")
def scare_to_death():
	return render_template("scare-to-death.html")

@app.route("/terrified-retreat")
def terrified_retreat():
	return render_template("terrified-retreat.html")

@app.route("/terrifying-howl")
def terrifying_howl():
	return render_template("terrifying-howl.html")

@app.route("/terrifying-resistance")
def terrifying_resistance():
	return render_template("terrifying-resistance.html")

@app.route("/youre-next")
def youre_next():
	return render_template("youre-next.html")

@app.route("/nightmares-domain-shared-nightmare")
def nightmares_domain_shared_nightmare():
	return render_template("nightmares-domain-shared-nightmare.html")

@app.route("/nightmares-domain-waking-nightmare")
def nightmares_domain_waking_nightmare():
	return render_template("nightmares-domain-waking-nightmare.html")

@app.route("/tyranny-domain-touch-of-obedience")
def tyranny_domain_touch_of_obedience():
	return render_template("tyranny-domain-touch-of-obedience.html")

@app.route("/aura-of-despair")
def aura_of_despair():
	return render_template("aura-of-despair.html")

@app.route("/decry-thief")
def decry_thief():
	return render_template("decry-thief.html")

@app.route("/walk-the-plank")
def walk_the_plank():
	return render_template("walk-the-plank.html")

@app.route("/watch-your-back")
def watch_your_back():
	return render_template("watch-your-back.html")

@app.route("/battle-cry")
def battle_cry():
	return render_template("battle-cry.html")

@app.route("/medical-researcher")
def medical_researcher():
	return render_template("medical-researcher.html")

@app.route("/forensic-acumen")
def forensic_acumen():
	return render_template("forensic-acumen.html")

@app.route("/ward-medic")
def ward_medic():
	return render_template("ward-medic.html")

@app.route("/rapid-response")
def rapid_response():
	return render_template("rapid-response.html")

@app.route("/advanced-medicine")
def advanced_medicine():
	return render_template("advanced-medicine.html")

@app.route("/legendary-medic")
def legendary_medic():
	return render_template("legendary-medic.html")

@app.route("/treat-condition")
def treat_condition():
	return render_template("treat-condition.html")

@app.route("/doctors-visitation")
def doctors_visitation():
	return render_template("doctors-visitation.html")

@app.route("/mortal-healing")
def mortal_healing():
	return render_template("mortal-healing.html")

@app.route("/paragon-battle-medicine")
def paragon_battle_medicine():
	return render_template("paragon-battle-medicine.html")

@app.route("/resuscitate")
def resuscitate():
	return render_template("resuscitate.html")

@app.route("/innoculation")
def innoculation():
	return render_template("innoculation.html")

@app.route("/robust-recovery")
def robust_recovery():
	return render_template("robust-recovery.html")

@app.route("/doctors-visitation-9859353")
def doctors_visitation_9859353():
	return render_template("doctors-visitation-9859353.html")

@app.route("/holistic-care")
def holistic_care():
	return render_template("holistic-care.html")

@app.route("/emergency-medical-assistance")
def emergency_medical_assistance():
	return render_template("emergency-medical-assistance.html")

@app.route("/keep-it-together")
def keep_it_together():
	return render_template("keep-it-together.html")

@app.route("/feather-step")
def feather_step():
	return render_template("feather-step.html")

@app.route("/consult-the-spirits")
def consult_the_spirits():
	return render_template("consult-the-spirits.html")

@app.route("/animal-trainer")
def animal_trainer():
	return render_template("animal-trainer.html")

@app.route("/companions-cry")
def companions_cry():
	return render_template("companions-cry.html")

@app.route("/enlarge-companion")
def enlarge_companion():
	return render_template("enlarge-companion.html")

@app.route("/magic-hide")
def magic_hide():
	return render_template("magic-hide.html")

@app.route("/mesmerizing-performance")
def mesmerizing_performance():
	return render_template("mesmerizing-performance.html")

@app.route("/pale-horse")
def pale_horse():
	return render_template("pale-horse.html")

@app.route("/side-by-side")
def side_by_side():
	return render_template("side-by-side.html")

@app.route("/insistent-commands")
def insistent_commands():
	return render_template("insistent-commands.html")

@app.route("/train-animal")
def train_animal():
	return render_template("train-animal.html")

@app.route("/wild-empathy")
def wild_empathy():
	return render_template("wild-empathy.html")

@app.route("/air-domain-disperse-into-air")
def air_domain_disperse_into_air():
	return render_template("air-domain-disperse-into-air.html")

@app.route("/air-domain-pushing-gust")
def air_domain_pushing_gust():
	return render_template("air-domain-pushing-gust.html")

@app.route("/aspect-of-the-beast")
def aspect_of_the_beast():
	return render_template("aspect-of-the-beast.html")

@app.route("/cold-domain-diamond-dust")
def cold_domain_diamond_dust():
	return render_template("cold-domain-diamond-dust.html")

@app.route("/cold-domain-winter-bolt")
def cold_domain_winter_bolt():
	return render_template("cold-domain-winter-bolt.html")

@app.route("/dust-domain-dust-storm")
def dust_domain_dust_storm():
	return render_template("dust-domain-dust-storm.html")

@app.route("/dust-domain-parch")
def dust_domain_parch():
	return render_template("dust-domain-parch.html")

@app.route("/elemental-bloodline-focus-elemental-toss")
def elemental_bloodline_focus_elemental_toss():
	return render_template("elemental-bloodline-focus-elemental-toss.html")

@app.route("/elemental-bloodline-focus-elemental-motion")
def elemental_bloodline_focus_elemental_motion():
	return render_template("elemental-bloodline-focus-elemental-motion.html")

@app.route("/elemental-bloodline-focus-elemental-blast")
def elemental_bloodline_focus_elemental_blast():
	return render_template("elemental-bloodline-focus-elemental-blast.html")

@app.route("/fey-bloodline-focus-faerie-dust")
def fey_bloodline_focus_faerie_dust():
	return render_template("fey-bloodline-focus-faerie-dust.html")

@app.route("/fey-bloodline-focus-fey-disappearance")
def fey_bloodline_focus_fey_disappearance():
	return render_template("fey-bloodline-focus-fey-disappearance.html")

@app.route("/fire-domain-fire-ray")
def fire_domain_fire_ray():
	return render_template("fire-domain-fire-ray.html")

@app.route("/fire-domain-flame-barrier")
def fire_domain_flame_barrier():
	return render_template("fire-domain-flame-barrier.html")

@app.route("/storm-order")
def storm_order():
	return render_template("storm-order.html")

@app.route("/lightning-domain-bottle-the-lightning")
def lightning_domain_bottle_the_lightning():
	return render_template("lightning-domain-bottle-the-lightning.html")

@app.route("/lightning-domain-charged-javelin")
def lightning_domain_charged_javelin():
	return render_template("lightning-domain-charged-javelin.html")

@app.route("/nature-domain-vibrant-thorns")
def nature_domain_vibrant_thorns():
	return render_template("nature-domain-vibrant-thorns.html")

@app.route("/nymph-bloodline-focus-nymphs-token")
def nymph_bloodline_focus_nymphs_token():
	return render_template("nymph-bloodline-focus-nymphs-token.html")

@app.route("/nymph-bloodline-focus-blinding-beauty")
def nymph_bloodline_focus_blinding_beauty():
	return render_template("nymph-bloodline-focus-blinding-beauty.html")

@app.route("/nymph-bloodline-focus-establishing-ward")
def nymph_bloodline_focus_establishing_ward():
	return render_template("nymph-bloodline-focus-establishing-ward.html")

@app.route("/virulent")
def virulent():
	return render_template("virulent.html")

@app.route("/plague-domain-divine-plagues")
def plague_domain_divine_plagues():
	return render_template("plague-domain-divine-plagues.html")

@app.route("/plague-domain-foul-miasma")
def plague_domain_foul_miasma():
	return render_template("plague-domain-foul-miasma.html")

@app.route("/tempest-surge")
def tempest_surge():
	return render_template("tempest-surge.html")

@app.route("/storm-retribution")
def storm_retribution():
	return render_template("storm-retribution.html")

@app.route("/swarm")
def swarm():
	return render_template("swarm.html")

@app.route("/swarm-domain-swarm-form")
def swarm_domain_swarm_form():
	return render_template("swarm-domain-swarm-form.html")

@app.route("/water-domain-downpour")
def water_domain_downpour():
	return render_template("water-domain-downpour.html")

@app.route("/water-domain-tidal-surge")
def water_domain_tidal_surge():
	return render_template("water-domain-tidal-surge.html")

@app.route("/cavalier-banner")
def cavalier_banner():
	return render_template("cavalier-banner.html")

@app.route("/cavaliers-charge")
def cavaliers_charge():
	return render_template("cavaliers-charge.html")

@app.route("/defend-mount")
def defend_mount():
	return render_template("defend-mount.html")

@app.route("/express-rider")
def express_rider():
	return render_template("express-rider.html")

@app.route("/quick-mount")
def quick_mount():
	return render_template("quick-mount.html")

@app.route("/ride")
def ride():
	return render_template("ride.html")

@app.route("/trampling-charge")
def trampling_charge():
	return render_template("trampling-charge.html")

@app.route("/unseat")
def unseat():
	return render_template("unseat.html")

@app.route("/green-empathy")
def green_empathy():
	return render_template("green-empathy.html")

@app.route("/magical-mobility")
def magical_mobility():
	return render_template("magical-mobility.html")

@app.route("/primal-aegis")
def primal_aegis():
	return render_template("primal-aegis.html")

@app.route("/influence-nature")
def influence_nature():
	return render_template("influence-nature.html")

@app.route("/natural-medicine")
def natural_medicine():
	return render_template("natural-medicine.html")

@app.route("/fresh-ingredients")
def fresh_ingredients():
	return render_template("fresh-ingredients.html")

@app.route("/form-control")
def form_control():
	return render_template("form-control.html")

@app.route("/reactive-transformation")
def reactive_transformation():
	return render_template("reactive-transformation.html")

@app.route("/heal-companion")
def heal_companion():
	return render_template("heal-companion.html")

@app.route("/auspicious-mount")
def auspicious_mount():
	return render_template("auspicious-mount.html")

@app.route("/earth-domain-localized-quake")
def earth_domain_localized_quake():
	return render_template("earth-domain-localized-quake.html")

@app.route("/earth-domain-hurtling-stone")
def earth_domain_hurtling_stone():
	return render_template("earth-domain-hurtling-stone.html")

@app.route("/bizarre-magic")
def bizarre_magic():
	return render_template("bizarre-magic.html")

@app.route("/deceptive-worship")
def deceptive_worship():
	return render_template("deceptive-worship.html")

@app.route("/living-hair")
def living_hair():
	return render_template("living-hair.html")

@app.route("/aberrant-bloodline-focus-tentacular-limbs")
def aberrant_bloodline_focus_tentacular_limbs():
	return render_template("aberrant-bloodline-focus-tentacular-limbs.html")

@app.route("/aberrant-bloodline-focus-unusual-anatomy")
def aberrant_bloodline_focus_unusual_anatomy():
	return render_template("aberrant-bloodline-focus-unusual-anatomy.html")

@app.route("/abomination-domain-fearful-feast")
def abomination_domain_fearful_feast():
	return render_template("abomination-domain-fearful-feast.html")

@app.route("/abomination-domain-lift-natures-caul")
def abomination_domain_lift_natures_caul():
	return render_template("abomination-domain-lift-natures-caul.html")

@app.route("/cackle")
def cackle():
	return render_template("cackle.html")

@app.route("/decay-domain-fallow-field")
def decay_domain_fallow_field():
	return render_template("decay-domain-fallow-field.html")

@app.route("/decay-domain-withering-grasp")
def decay_domain_withering_grasp():
	return render_template("decay-domain-withering-grasp.html")

@app.route("/delirium-domain-ephemeral-hazards")
def delirium_domain_ephemeral_hazards():
	return render_template("delirium-domain-ephemeral-hazards.html")

@app.route("/delirium-domain-hyperfocus")
def delirium_domain_hyperfocus():
	return render_template("delirium-domain-hyperfocus.html")

@app.route("/discern-secrets")
def discern_secrets():
	return render_template("discern-secrets.html")

@app.route("/disturbing-knowledge")
def disturbing_knowledge():
	return render_template("disturbing-knowledge.html")

@app.route("/dreams-domain-dreamers-call")
def dreams_domain_dreamers_call():
	return render_template("dreams-domain-dreamers-call.html")

@app.route("/dreams-domain-sweet-dream")
def dreams_domain_sweet_dream():
	return render_template("dreams-domain-sweet-dream.html")

@app.route("/eldritch-nails")
def eldritch_nails():
	return render_template("eldritch-nails.html")

@app.route("/fate-domain-read-domain")
def fate_domain_read_domain():
	return render_template("fate-domain-read-domain.html")

@app.route("/fate-domain-tempt-fate")
def fate_domain_tempt_fate():
	return render_template("fate-domain-tempt-fate.html")

@app.route("/hag-bloodline-focus-jealous-hex")
def hag_bloodline_focus_jealous_hex():
	return render_template("hag-bloodline-focus-jealous-hex.html")

@app.route("/hag-bloodline-focus-youre-mine")
def hag_bloodline_focus_youre_mine():
	return render_template("hag-bloodline-focus-youre-mine.html")

@app.route("/hag-bloodline-focus-horrific-visage")
def hag_bloodline_focus_horrific_visage():
	return render_template("hag-bloodline-focus-horrific-visage.html")

@app.route("/lesson-of-protection")
def lesson_of_protection():
	return render_template("lesson-of-protection.html")

@app.route("/lesson-of-shadow")
def lesson_of_shadow():
	return render_template("lesson-of-shadow.html")

@app.route("/lesson-of-the-elements")
def lesson_of_the_elements():
	return render_template("lesson-of-the-elements.html")

@app.route("/lesson-of-the-frozen-queen")
def lesson_of_the_frozen_queen():
	return render_template("lesson-of-the-frozen-queen.html")

@app.route("/lesson-of-vengeance")
def lesson_of_vengeance():
	return render_template("lesson-of-vengeance.html")

@app.route("/moon-domain-moon-beam")
def moon_domain_moon_beam():
	return render_template("moon-domain-moon-beam.html")

@app.route("/moon-domain-touch-of-the-moon")
def moon_domain_touch_of_the_moon():
	return render_template("moon-domain-touch-of-the-moon.html")

@app.route("/split-the-tongue")
def split_the_tongue():
	return render_template("split-the-tongue.html")

@app.route("/nudge-fate")
def nudge_fate():
	return render_template("nudge-fate.html")

@app.route("/phase-familiar")
def phase_familiar():
	return render_template("phase-familiar.html")

@app.route("/shadow-bloodline-focus-dim-the-light")
def shadow_bloodline_focus_dim_the_light():
	return render_template("shadow-bloodline-focus-dim-the-light.html")

@app.route("/shadow-bloodline-focus-steal-shadow")
def shadow_bloodline_focus_steal_shadow():
	return render_template("shadow-bloodline-focus-steal-shadow.html")

@app.route("/shadow-bloodline-focus-consuming-darkness")
def shadow_bloodline_focus_consuming_darkness():
	return render_template("shadow-bloodline-focus-consuming-darkness.html")

@app.route("/shroud-of-night")
def shroud_of_night():
	return render_template("shroud-of-night.html")

@app.route("/sorrow-domain-lament")
def sorrow_domain_lament():
	return render_template("sorrow-domain-lament.html")

@app.route("/soul-domain-ectoplasmic-interstice")
def soul_domain_ectoplasmic_interstice():
	return render_template("soul-domain-ectoplasmic-interstice.html")

@app.route("/spirit-object")
def spirit_object():
	return render_template("spirit-object.html")

@app.route("/star-domain-asterism")
def star_domain_asterism():
	return render_template("star-domain-asterism.html")

@app.route("/star-domain-zenith-star")
def star_domain_zenith_star():
	return render_template("star-domain-zenith-star.html")

@app.route("/stoke-the-heart")
def stoke_the_heart():
	return render_template("stoke-the-heart.html")

@app.route("/void-domain-door-to-the-beyond")
def void_domain_door_to_the_beyond():
	return render_template("void-domain-door-to-the-beyond.html")

@app.route("/void-domain-empty-inside")
def void_domain_empty_inside():
	return render_template("void-domain-empty-inside.html")

@app.route("/wilding-word")
def wilding_word():
	return render_template("wilding-word.html")

@app.route("/schooled-in-secrets")
def schooled_in_secrets():
	return render_template("schooled-in-secrets.html")

@app.route("/combat-reading")
def combat_reading():
	return render_template("combat-reading.html")

@app.route("/eclectic-skill")
def eclectic_skill():
	return render_template("eclectic-skill.html")

@app.route("/oddity-identification")
def oddity_identification():
	return render_template("oddity-identification.html")

@app.route("/scholarly-defense")
def scholarly_defense():
	return render_template("scholarly-defense.html")

@app.route("/root-magic")
def root_magic():
	return render_template("root-magic.html")

@app.route("/peer-beyond")
def peer_beyond():
	return render_template("peer-beyond.html")

@app.route("/naga-domain-ordained-purpose")
def naga_domain_ordained_purpose():
	return render_template("naga-domain-ordained-purpose.html")

@app.route("/spirit-hunter")
def spirit_hunter():
	return render_template("spirit-hunter.html")

@app.route("/spectral-strike")
def spectral_strike():
	return render_template("spectral-strike.html")

@app.route("/graves-voice")
def graves_voice():
	return render_template("graves-voice.html")

@app.route("/investigate-haunting")
def investigate_haunting():
	return render_template("investigate-haunting.html")

@app.route("/clinging-ice")
def clinging_ice():
	return render_template("clinging-ice.html")

@app.route("/evil-eye")
def evil_eye():
	return render_template("evil-eye.html")

@app.route("/witchs-bottle")
def witchs_bottle():
	return render_template("witchs-bottle.html")

@app.route("/hazard-finder")
def hazard_finder():
	return render_template("hazard-finder.html")

@app.route("/battlefield-surveyor")
def battlefield_surveyor():
	return render_template("battlefield-surveyor.html")

@app.route("/plot-the-future")
def plot_the_future():
	return render_template("plot-the-future.html")

@app.route("/reconstruct-the-scene")
def reconstruct_the_scene():
	return render_template("reconstruct-the-scene.html")

@app.route("/sense-alignment")
def sense_alignment():
	return render_template("sense-alignment.html")

@app.route("/boleras-interrogation")
def boleras_interrogation():
	return render_template("boleras-interrogation.html")

@app.route("/lie-detector")
def lie_detector():
	return render_template("lie-detector.html")

@app.route("/investigate")
def investigate():
	return render_template("investigate.html")

@app.route("/ongoing-investigation")
def ongoing_investigation():
	return render_template("ongoing-investigation.html")

@app.route("/thats-odd")
def thats_odd():
	return render_template("thats-odd.html")

@app.route("/pursue-a-lead")
def pursue_a_lead():
	return render_template("pursue-a-lead.html")

@app.route("/clue-in")
def clue_in():
	return render_template("clue-in.html")

@app.route("/clue-them-all-in")
def clue_them_all_in():
	return render_template("clue-them-all-in.html")

@app.route("/connect-the-dots")
def connect_the_dots():
	return render_template("connect-the-dots.html")

@app.route("/detectives-readiness")
def detectives_readiness():
	return render_template("detectives-readiness.html")

@app.route("/interrogation")
def interrogation():
	return render_template("interrogation.html")

@app.route("/just-one-more-thing")
def just_one_more_thing():
	return render_template("just-one-more-thing.html")

@app.route("/lead-investigator")
def lead_investigator():
	return render_template("lead-investigator.html")

@app.route("/red-herring")
def red_herring():
	return render_template("red-herring.html")

@app.route("/solid-lead")
def solid_lead():
	return render_template("solid-lead.html")

@app.route("/subject-of-opportunity")
def subject_of_opportunity():
	return render_template("subject-of-opportunity.html")

@app.route("/underworld-investigator")
def underworld_investigator():
	return render_template("underworld-investigator.html")

@app.route("/whodunnit")
def whodunnit():
	return render_template("whodunnit.html")

@app.route("/battle-assessment")
def battle_assessment():
	return render_template("battle-assessment.html")

@app.route("/incredible-scout")
def incredible_scout():
	return render_template("incredible-scout.html")

@app.route("/expeditious-search")
def expeditious_search():
	return render_template("expeditious-search.html")

@app.route("/observant-explorer")
def observant_explorer():
	return render_template("observant-explorer.html")

@app.route("/thorough-search")
def thorough_search():
	return render_template("thorough-search.html")

@app.route("/grave-sense")
def grave_sense():
	return render_template("grave-sense.html")

@app.route("/sense-chaos")
def sense_chaos():
	return render_template("sense-chaos.html")

@app.route("/spiritual-sense")
def spiritual_sense():
	return render_template("spiritual-sense.html")

@app.route("/supertaster")
def supertaster():
	return render_template("supertaster.html")

@app.route("/instinctive-strike")
def instinctive_strike():
	return render_template("instinctive-strike.html")

@app.route("/sense-evil")
def sense_evil():
	return render_template("sense-evil.html")

@app.route("/sense-good")
def sense_good():
	return render_template("sense-good.html")

@app.route("/sense-the-unseen")
def sense_the_unseen():
	return render_template("sense-the-unseen.html")

@app.route("/soulsight")
def soulsight():
	return render_template("soulsight.html")

@app.route("/foresee-danger")
def foresee_danger():
	return render_template("foresee-danger.html")

@app.route("/predictable")
def predictable():
	return render_template("predictable.html")

@app.route("/edgewatch-detective")
def edgewatch_detective():
	return render_template("edgewatch-detective.html")

@app.route("/anticipate-ambush")
def anticipate_ambush():
	return render_template("anticipate-ambush.html")

@app.route("/allegro")
def allegro():
	return render_template("allegro.html")

@app.route("/inspire-courage")
def inspire_courage():
	return render_template("inspire-courage.html")

@app.route("/inspire-defense")
def inspire_defense():
	return render_template("inspire-defense.html")

@app.route("/inspire-heroics")
def inspire_heroics():
	return render_template("inspire-heroics.html")

@app.route("/lingering-composition")
def lingering_composition():
	return render_template("lingering-composition.html")

@app.route("/annotate-composition")
def annotate_composition():
	return render_template("annotate-composition.html")

@app.route("/call-and-response")
def call_and_response():
	return render_template("call-and-response.html")

@app.route("/courageous-onslaught")
def courageous_onslaught():
	return render_template("courageous-onslaught.html")

@app.route("/disrupting-actions")
def disrupting_actions():
	return render_template("disrupting-actions.html")

@app.route("/courageous-opportunity")
def courageous_opportunity():
	return render_template("courageous-opportunity.html")

@app.route("/sorrow-domain-overflowing-sorrow")
def sorrow_domain_overflowing_sorrow():
	return render_template("sorrow-domain-overflowing-sorrow.html")

@app.route("/lesson-of-dreams")
def lesson_of_dreams():
	return render_template("lesson-of-dreams.html")

@app.route("/defensive-coordination")
def defensive_coordination():
	return render_template("defensive-coordination.html")

@app.route("/directed-audience")
def directed_audience():
	return render_template("directed-audience.html")

@app.route("/dirge-of-doom")
def dirge_of_doom():
	return render_template("dirge-of-doom.html")

@app.route("/discordant-voice")
def discordant_voice():
	return render_template("discordant-voice.html")

@app.route("/earworm")
def earworm():
	return render_template("earworm.html")

@app.route("/well-versed")
def well_versed():
	return render_template("well-versed.html")

@app.route("/educate-allies")
def educate_allies():
	return render_template("educate-allies.html")

@app.route("/fatal-aria")
def fatal_aria():
	return render_template("fatal-aria.html")

@app.route("/harmonize")
def harmonize():
	return render_template("harmonize.html")

@app.route("/inspire-competence")
def inspire_competence():
	return render_template("inspire-competence.html")

@app.route("/loremasters-etude")
def loremasters_etude():
	return render_template("loremasters-etude.html")

@app.route("/ode-to-ouroboros")
def ode_to_ouroboros():
	return render_template("ode-to-ouroboros.html")

@app.route("/pied-piping")
def pied_piping():
	return render_template("pied-piping.html")

@app.route("/resounding-finale")
def resounding_finale():
	return render_template("resounding-finale.html")

@app.route("/shared-assault")
def shared_assault():
	return render_template("shared-assault.html")

@app.route("/silvers-refrain")
def silvers_refrain():
	return render_template("silvers-refrain.html")

@app.route("/song-of-the-fallen")
def song_of_the_fallen():
	return render_template("song-of-the-fallen.html")

@app.route("/songs-of-strength")
def songs_of_strength():
	return render_template("songs-of-strength.html")

@app.route("/symphony-of-the-unfettered-heart")
def symphony_of_the_unfettered_heart():
	return render_template("symphony-of-the-unfettered-heart.html")

@app.route("/triple-time")
def triple_time():
	return render_template("triple-time.html")

@app.route("/triumphant-inspiration")
def triumphant_inspiration():
	return render_template("triumphant-inspiration.html")

@app.route("/unusual-composition")
def unusual_composition():
	return render_template("unusual-composition.html")

@app.route("/vigorous-inspiration")
def vigorous_inspiration():
	return render_template("vigorous-inspiration.html")

@app.route("/courageous-advance")
def courageous_advance():
	return render_template("courageous-advance.html")

@app.route("/courageous-assault")
def courageous_assault():
	return render_template("courageous-assault.html")

@app.route("/distracting-performance")
def distracting_performance():
	return render_template("distracting-performance.html")

@app.route("/gladiator")
def gladiator():
	return render_template("gladiator.html")

@app.route("/play-to-the-crowd")
def play_to_the_crowd():
	return render_template("play-to-the-crowd.html")

@app.route("/call-your-shot")
def call_your_shot():
	return render_template("call-your-shot.html")

@app.route("/fascinating-performance")
def fascinating_performance():
	return render_template("fascinating-performance.html")

@app.route("/flourishing-finish")
def flourishing_finish():
	return render_template("flourishing-finish.html")

@app.route("/focused-fascination")
def focused_fascination():
	return render_template("focused-fascination.html")

@app.route("/juggle")
def juggle():
	return render_template("juggle.html")

@app.route("/focused-juggler")
def focused_juggler():
	return render_template("focused-juggler.html")

@app.route("/quick-juggle")
def quick_juggle():
	return render_template("quick-juggle.html")

@app.route("/reflexive-catch")
def reflexive_catch():
	return render_template("reflexive-catch.html")

@app.route("/virtuosic-performance")
def virtuosic_performance():
	return render_template("virtuosic-performance.html")

@app.route("/acting")
def acting():
	return render_template("acting.html")

@app.route("/fancy-moves")
def fancy_moves():
	return render_template("fancy-moves.html")

@app.route("/impressive-performance")
def impressive_performance():
	return render_template("impressive-performance.html")

@app.route("/versatile-performance")
def versatile_performance():
	return render_template("versatile-performance.html")

@app.route("/quick-juggler")
def quick_juggler():
	return render_template("quick-juggler.html")

@app.route("/never-tire")
def never_tire():
	return render_template("never-tire.html")

@app.route("/reverberate")
def reverberate():
	return render_template("reverberate.html")

@app.route("/orthographic-mastery")
def orthographic_mastery():
	return render_template("orthographic-mastery.html")

@app.route("/all-knowledge-skills")
def all_knowledge_skills():
	return render_template("all-knowledge-skills.html")

@app.route("/devoted-focus")
def devoted_focus():
	return render_template("devoted-focus.html")

@app.route("/moment-of-clarity")
def moment_of_clarity():
	return render_template("moment-of-clarity.html")

@app.route("/surging-focus")
def surging_focus():
	return render_template("surging-focus.html")

@app.route("/transcribe-moment")
def transcribe_moment():
	return render_template("transcribe-moment.html")

@app.route("/great-boaster")
def great_boaster():
	return render_template("great-boaster.html")

@app.route("/spot-translate")
def spot_translate():
	return render_template("spot-translate.html")

@app.route("/tongue-of-the-sun-and-moon")
def tongue_of_the_sun_and_moon():
	return render_template("tongue-of-the-sun-and-moon.html")

@app.route("/liberators-drive")
def liberators_drive():
	return render_template("liberators-drive.html")

@app.route("/practiced-guidance")
def practiced_guidance():
	return render_template("practiced-guidance.html")

@app.route("/scarecrow")
def scarecrow():
	return render_template("scarecrow.html")

@app.route("/seasoned-pro")
def seasoned_pro():
	return render_template("seasoned-pro.html")

@app.route("/gossip-lore")
def gossip_lore():
	return render_template("gossip-lore.html")

@app.route("/legendary-professional")
def legendary_professional():
	return render_template("legendary-professional.html")

@app.route("/unmistakable-lore")
def unmistakable_lore():
	return render_template("unmistakable-lore.html")

@app.route("/inspiring-marshal-stance")
def inspiring_marshal_stance():
	return render_template("inspiring-marshal-stance.html")

@app.route("/snap-out-of-it")
def snap_out_of_it():
	return render_template("snap-out-of-it.html")

@app.route("/tactical-cadence")
def tactical_cadence():
	return render_template("tactical-cadence.html")

@app.route("/to-battle")
def to_battle():
	return render_template("to-battle.html")

@app.route("/dread-marshal-stance")
def dread_marshal_stance():
	return render_template("dread-marshal-stance.html")

@app.route("/scrollmaster")
def scrollmaster():
	return render_template("scrollmaster.html")

@app.route("/oozemorph")
def oozemorph():
	return render_template("oozemorph.html")

@app.route("/hideous-ululation")
def hideous_ululation():
	return render_template("hideous-ululation.html")

@app.route("/ooze-empathy")
def ooze_empathy():
	return render_template("ooze-empathy.html")

@app.route("/rubbery-skin")
def rubbery_skin():
	return render_template("rubbery-skin.html")

@app.route("/vacate-vision")
def vacate_vision():
	return render_template("vacate-vision.html")

@app.route("/able-ritualist")
def able_ritualist():
	return render_template("able-ritualist.html")

@app.route("/assured-ritualist")
def assured_ritualist():
	return render_template("assured-ritualist.html")

@app.route("/flexible-ritualist")
def flexible_ritualist():
	return render_template("flexible-ritualist.html")

@app.route("/resourceful-ritualist")
def resourceful_ritualist():
	return render_template("resourceful-ritualist.html")

@app.route("/speedy-rituals")
def speedy_rituals():
	return render_template("speedy-rituals.html")

@app.route("/cognitive-crossover")
def cognitive_crossover():
	return render_template("cognitive-crossover.html")

@app.route("/deductive-improvisation")
def deductive_improvisation():
	return render_template("deductive-improvisation.html")

@app.route("/expeditious-inspection")
def expeditious_inspection():
	return render_template("expeditious-inspection.html")

@app.route("/flexible-studies")
def flexible_studies():
	return render_template("flexible-studies.html")

@app.route("/untrained-improvisation")
def untrained_improvisation():
	return render_template("untrained-improvisation.html")

@app.route("/tricksters-ace")
def tricksters_ace():
	return render_template("tricksters-ace.html")

@app.route("/incredible-luck")
def incredible_luck():
	return render_template("incredible-luck.html")

@app.route("/diamond-soul")
def diamond_soul():
	return render_template("diamond-soul.html")

@app.route("/impossible-technique")
def impossible_technique():
	return render_template("impossible-technique.html")

@app.route("/keen-follower")
def keen_follower():
	return render_template("keen-follower.html")

@app.route("/swordmasters-assist")
def swordmasters_assist():
	return render_template("swordmasters-assist.html")

@app.route("/divine-guidance")
def divine_guidance():
	return render_template("divine-guidance.html")

@app.route("/angelic-bloodline-focus-angelic-halo")
def angelic_bloodline_focus_angelic_halo():
	return render_template("angelic-bloodline-focus-angelic-halo.html")

@app.route("/angelic-bloodline-focus-celestial-brand")
def angelic_bloodline_focus_celestial_brand():
	return render_template("angelic-bloodline-focus-celestial-brand.html")

@app.route("/demonic-bloodline-focus-gluttons-jaw")
def demonic_bloodline_focus_gluttons_jaw():
	return render_template("demonic-bloodline-focus-gluttons-jaw.html")

@app.route("/diabolic-bloodline-focus-diabolic-edict")
def diabolic_bloodline_focus_diabolic_edict():
	return render_template("diabolic-bloodline-focus-diabolic-edict.html")

@app.route("/diabolic-bloodline-focus-embrace-the-pit")
def diabolic_bloodline_focus_embrace_the_pit():
	return render_template("diabolic-bloodline-focus-embrace-the-pit.html")

@app.route("/psychopomp-bloodline-focus-sepulchral-mask")
def psychopomp_bloodline_focus_sepulchral_mask():
	return render_template("psychopomp-bloodline-focus-sepulchral-mask.html")

@app.route("/psychopomp-bloodline-focus-spirit-veil")
def psychopomp_bloodline_focus_spirit_veil():
	return render_template("psychopomp-bloodline-focus-spirit-veil.html")

@app.route("/diabolic-bloodline-focus-hellfire-plume")
def diabolic_bloodline_focus_hellfire_plume():
	return render_template("diabolic-bloodline-focus-hellfire-plume.html")

@app.route("/demonic-bloodline-focus-swamp-of-sloth")
def demonic_bloodline_focus_swamp_of_sloth():
	return render_template("demonic-bloodline-focus-swamp-of-sloth.html")

@app.route("/demonic-bloodline-focus-abyssal-wrath")
def demonic_bloodline_focus_abyssal_wrath():
	return render_template("demonic-bloodline-focus-abyssal-wrath.html")

@app.route("/psychopomp-bloodline-focus-shepard-of-souls")
def psychopomp_bloodline_focus_shepard_of_souls():
	return render_template("psychopomp-bloodline-focus-shepard-of-souls.html")

@app.route("/undead-bloodline-focus-drain-life")
def undead_bloodline_focus_drain_life():
	return render_template("undead-bloodline-focus-drain-life.html")

@app.route("/undead-bloodline-focus-grasping-grave")
def undead_bloodline_focus_grasping_grave():
	return render_template("undead-bloodline-focus-grasping-grave.html")

@app.route("/light-of-revelation")
def light_of_revelation():
	return render_template("light-of-revelation.html")

@app.route("/ambition-domain-blind-ambition")
def ambition_domain_blind_ambition():
	return render_template("ambition-domain-blind-ambition.html")

@app.route("/ambition-domain-competitive-edge")
def ambition_domain_competitive_edge():
	return render_template("ambition-domain-competitive-edge.html")

@app.route("/confidence-domain-delusional-pride")
def confidence_domain_delusional_pride():
	return render_template("confidence-domain-delusional-pride.html")

@app.route("/confidence-domain-veil-of-confidence")
def confidence_domain_veil_of_confidence():
	return render_template("confidence-domain-veil-of-confidence.html")

@app.route("/death-domain-deaths-call")
def death_domain_deaths_call():
	return render_template("death-domain-deaths-call.html")

@app.route("/death-domain-eradicate-undeath")
def death_domain_eradicate_undeath():
	return render_template("death-domain-eradicate-undeath.html")

@app.route("/destruction-domain-cry-of-destruction")
def destruction_domain_cry_of_destruction():
	return render_template("destruction-domain-cry-of-destruction.html")

@app.route("/destruction-domain-destructive-aura")
def destruction_domain_destructive_aura():
	return render_template("destruction-domain-destructive-aura.html")

@app.route("/deitys-protection")
def deitys_protection():
	return render_template("deitys-protection.html")

@app.route("/duty-domain-dutiful-challenge")
def duty_domain_dutiful_challenge():
	return render_template("duty-domain-dutiful-challenge.html")

@app.route("/duty-domain-oathkeepers-insignia")
def duty_domain_oathkeepers_insignia():
	return render_template("duty-domain-oathkeepers-insignia.html")

@app.route("/healing-domain-healers-blessing")
def healing_domain_healers_blessing():
	return render_template("healing-domain-healers-blessing.html")

@app.route("/luck-domain-bit-of-luck")
def luck_domain_bit_of_luck():
	return render_template("luck-domain-bit-of-luck.html")

@app.route("/luck-domain-lucky-break")
def luck_domain_lucky_break():
	return render_template("luck-domain-lucky-break.html")

@app.route("/pain-domain-savor-the-sting-8156902")
def pain_domain_savor_the_sting_8156902():
	return render_template("pain-domain-savor-the-sting-8156902.html")

@app.route("/pain-domain-retributive-pain")
def pain_domain_retributive_pain():
	return render_template("pain-domain-retributive-pain.html")

@app.route("/perfection-domain-perfected-form")
def perfection_domain_perfected_form():
	return render_template("perfection-domain-perfected-form.html")

@app.route("/perfection-domain-perfected-mind")
def perfection_domain_perfected_mind():
	return render_template("perfection-domain-perfected-mind.html")

@app.route("/protection-domain-protectors-sacrifice")
def protection_domain_protectors_sacrifice():
	return render_template("protection-domain-protectors-sacrifice.html")

@app.route("/protection-domain-protectors-sphere")
def protection_domain_protectors_sphere():
	return render_template("protection-domain-protectors-sphere.html")

@app.route("/repose-domain-font-of-serenity")
def repose_domain_font_of_serenity():
	return render_template("repose-domain-font-of-serenity.html")

@app.route("/repose-domain-share-burden")
def repose_domain_share_burden():
	return render_template("repose-domain-share-burden.html")

@app.route("/shield-of-faith")
def shield_of_faith():
	return render_template("shield-of-faith.html")

@app.route("/sun-domain-dazzling-flash")
def sun_domain_dazzling_flash():
	return render_template("sun-domain-dazzling-flash.html")

@app.route("/sun-domain-positive-luminance")
def sun_domain_positive_luminance():
	return render_template("sun-domain-positive-luminance.html")

@app.route("/toll-domain-practice-makes-perfect")
def toll_domain_practice_makes_perfect():
	return render_template("toll-domain-practice-makes-perfect.html")

@app.route("/toll-domain-tireless-worker")
def toll_domain_tireless_worker():
	return render_template("toll-domain-tireless-worker.html")

@app.route("/truth-domain-word-of-truth")
def truth_domain_word_of_truth():
	return render_template("truth-domain-word-of-truth.html")

@app.route("/truth-domain-glimpse-of-truth")
def truth_domain_glimpse_of_truth():
	return render_template("truth-domain-glimpse-of-truth.html")

@app.route("/undeath-domain-spell-malignant")
def undeath_domain_spell_malignant():
	return render_template("undeath-domain-spell-malignant.html")

@app.route("/undeath-domain-touch-of-undeath")
def undeath_domain_touch_of_undeath():
	return render_template("undeath-domain-touch-of-undeath.html")

@app.route("/vigil-domain-object-memory")
def vigil_domain_object_memory():
	return render_template("vigil-domain-object-memory.html")

@app.route("/vigil-domain-remember-the-lost")
def vigil_domain_remember_the_lost():
	return render_template("vigil-domain-remember-the-lost.html")

@app.route("/shield-block")
def shield_block():
	return render_template("shield-block.html")

@app.route("/emblazon-antimagic")
def emblazon_antimagic():
	return render_template("emblazon-antimagic.html")

@app.route("/emblazon-armament")
def emblazon_armament():
	return render_template("emblazon-armament.html")

@app.route("/emblazon-energy")
def emblazon_energy():
	return render_template("emblazon-energy.html")

@app.route("/emblazon-divinity")
def emblazon_divinity():
	return render_template("emblazon-divinity.html")

@app.route("/premonition-of-avoidance")
def premonition_of_avoidance():
	return render_template("premonition-of-avoidance.html")

@app.route("/shared-avoidance")
def shared_avoidance():
	return render_template("shared-avoidance.html")

@app.route("/spiritual-explorer")
def spiritual_explorer():
	return render_template("spiritual-explorer.html")

@app.route("/aura-of-faith")
def aura_of_faith():
	return render_template("aura-of-faith.html")

@app.route("/aura-of-righteousness")
def aura_of_righteousness():
	return render_template("aura-of-righteousness.html")

@app.route("/divine-grace")
def divine_grace():
	return render_template("divine-grace.html")

@app.route("/hellknight-armiger")
def hellknight_armiger():
	return render_template("hellknight-armiger.html")

@app.route("/false-faith")
def false_faith():
	return render_template("false-faith.html")

@app.route("/oracular-warning")
def oracular_warning():
	return render_template("oracular-warning.html")

@app.route("/pilgrims-token")
def pilgrims_token():
	return render_template("pilgrims-token.html")

@app.route("/diabolic-certitude")
def diabolic_certitude():
	return render_template("diabolic-certitude.html")

@app.route("/student-of-the-canon")
def student_of_the_canon():
	return render_template("student-of-the-canon.html")

@app.route("/glean-lore")
def glean_lore():
	return render_template("glean-lore.html")

@app.route("/accelerating-touch")
def accelerating_touch():
	return render_template("accelerating-touch.html")

@app.route("/amplifying-touch")
def amplifying_touch():
	return render_template("amplifying-touch.html")

@app.route("/heal-mount")
def heal_mount():
	return render_template("heal-mount.html")

@app.route("/mercy")
def mercy():
	return render_template("mercy.html")

@app.route("/affliction-mercy")
def affliction_mercy():
	return render_template("affliction-mercy.html")

@app.route("/elucidating-mercy")
def elucidating_mercy():
	return render_template("elucidating-mercy.html")

@app.route("/greater-mercy")
def greater_mercy():
	return render_template("greater-mercy.html")

@app.route("/invigorating-mercy")
def invigorating_mercy():
	return render_template("invigorating-mercy.html")

@app.route("/rejuvenating-touch")
def rejuvenating_touch():
	return render_template("rejuvenating-touch.html")

@app.route("/resilient-touch")
def resilient_touch():
	return render_template("resilient-touch.html")

@app.route("/ultimate-mercy")
def ultimate_mercy():
	return render_template("ultimate-mercy.html")

@app.route("/vengeful-oath")
def vengeful_oath():
	return render_template("vengeful-oath.html")

@app.route("/litany-against-sloth")
def litany_against_sloth():
	return render_template("litany-against-sloth.html")

@app.route("/litany-against-wrath")
def litany_against_wrath():
	return render_template("litany-against-wrath.html")

@app.route("/litany-of-depravity")
def litany_of_depravity():
	return render_template("litany-of-depravity.html")

@app.route("/litany-of-righteousness")
def litany_of_righteousness():
	return render_template("litany-of-righteousness.html")

@app.route("/litany-of-self-interest")
def litany_of_self_interest():
	return render_template("litany-of-self-interest.html")

@app.route("/exhort-the-faithful")
def exhort_the_faithful():
	return render_template("exhort-the-faithful.html")

@app.route("/battle-prayer")
def battle_prayer():
	return render_template("battle-prayer.html")

@app.route("/eternal-bane")
def eternal_bane():
	return render_template("eternal-bane.html")

@app.route("/touch-of-corruption")
def touch_of_corruption():
	return render_template("touch-of-corruption.html")

@app.route("/cruelty")
def cruelty():
	return render_template("cruelty.html")

@app.route("/greater-cruelty")
def greater_cruelty():
	return render_template("greater-cruelty.html")

@app.route("/knight-reclaimant")
def knight_reclaimant():
	return render_template("knight-reclaimant.html")

@app.route("/lastwall-warden")
def lastwall_warden():
	return render_template("lastwall-warden.html")

@app.route("/suns-fury")
def suns_fury():
	return render_template("suns-fury.html")

@app.route("/smite-evil")
def smite_evil():
	return render_template("smite-evil.html")

@app.route("/smite-good")
def smite_good():
	return render_template("smite-good.html")

@app.route("/champions-sacrifice")
def champions_sacrifice():
	return render_template("champions-sacrifice.html")

@app.route("/invoke-the-crimson-oath")
def invoke_the_crimson_oath():
	return render_template("invoke-the-crimson-oath.html")

@app.route("/stance")
def stance():
	return render_template("stance.html")

@app.route("/anchoring-aura")
def anchoring_aura():
	return render_template("anchoring-aura.html")

@app.route("/aura-of-life")
def aura_of_life():
	return render_template("aura-of-life.html")

@app.route("/aura-of-preservation")
def aura_of_preservation():
	return render_template("aura-of-preservation.html")

@app.route("/enforce-oath")
def enforce_oath():
	return render_template("enforce-oath.html")

@app.route("/wyrmbane-aura")
def wyrmbane_aura():
	return render_template("wyrmbane-aura.html")

@app.route("/banishing-blow")
def banishing_blow():
	return render_template("banishing-blow.html")

@app.route("/destructive-vengeance")
def destructive_vengeance():
	return render_template("destructive-vengeance.html")

@app.route("/antipaladins-divine-smite")
def antipaladins_divine_smite():
	return render_template("antipaladins-divine-smite.html")

@app.route("/divine-reflexes")
def divine_reflexes():
	return render_template("divine-reflexes.html")

@app.route("/gruesome-strike")
def gruesome_strike():
	return render_template("gruesome-strike.html")

@app.route("/iron-command")
def iron_command():
	return render_template("iron-command.html")

@app.route("/iron-repercussions")
def iron_repercussions():
	return render_template("iron-repercussions.html")

@app.route("/weight-of-guilt")
def weight_of_guilt():
	return render_template("weight-of-guilt.html")

@app.route("/lasting-doubt")
def lasting_doubt():
	return render_template("lasting-doubt.html")

@app.route("/liberating-step")
def liberating_step():
	return render_template("liberating-step.html")

@app.route("/liberating-oath")
def liberating_oath():
	return render_template("liberating-oath.html")

@app.route("/liberating-stride")
def liberating_stride():
	return render_template("liberating-stride.html")

@app.route("/liberating-divine-smite")
def liberating_divine_smite():
	return render_template("liberating-divine-smite.html")

@app.route("/liberators-exalt")
def liberators_exalt():
	return render_template("liberators-exalt.html")

@app.route("/lightslayer-oath")
def lightslayer_oath():
	return render_template("lightslayer-oath.html")

@app.route("/selfish-shield")
def selfish_shield():
	return render_template("selfish-shield.html")

@app.route("/ongoing-selfishness")
def ongoing_selfishness():
	return render_template("ongoing-selfishness.html")

@app.route("/retributive-strike")
def retributive_strike():
	return render_template("retributive-strike.html")

@app.route("/paladins-divine-smite")
def paladins_divine_smite():
	return render_template("paladins-divine-smite.html")

@app.route("/paladins-exalt")
def paladins_exalt():
	return render_template("paladins-exalt.html")

@app.route("/ranged-reprisal")
def ranged_reprisal():
	return render_template("ranged-reprisal.html")

@app.route("/redeemers-divine-smite")
def redeemers_divine_smite():
	return render_template("redeemers-divine-smite.html")

@app.route("/redeemers-exalt")
def redeemers_exalt():
	return render_template("redeemers-exalt.html")

@app.route("/redemptive-oath")
def redemptive_oath():
	return render_template("redemptive-oath.html")

@app.route("/retributive-oath")
def retributive_oath():
	return render_template("retributive-oath.html")

@app.route("/tyrants-divine-smite")
def tyrants_divine_smite():
	return render_template("tyrants-divine-smite.html")

@app.route("/tyrants-exalt")
def tyrants_exalt():
	return render_template("tyrants-exalt.html")

@app.route("/unimpeded-step")
def unimpeded_step():
	return render_template("unimpeded-step.html")

@app.route("/vicious-vengeance")
def vicious_vengeance():
	return render_template("vicious-vengeance.html")

@app.route("/instrument-of-slaughter")
def instrument_of_slaughter():
	return render_template("instrument-of-slaughter.html")

@app.route("/blade-of-justice")
def blade_of_justice():
	return render_template("blade-of-justice.html")

@app.route("/instrument-of-zeal")
def instrument_of_zeal():
	return render_template("instrument-of-zeal.html")

@app.route("/align-armament")
def align_armament():
	return render_template("align-armament.html")

@app.route("/blade-of-law")
def blade_of_law():
	return render_template("blade-of-law.html")

@app.route("/extend-align-armament")
def extend_align_armament():
	return render_template("extend-align-armament.html")

@app.route("/aegis-of-arnisant")
def aegis_of_arnisant():
	return render_template("aegis-of-arnisant.html")

@app.route("/shield-ally")
def shield_ally():
	return render_template("shield-ally.html")

@app.route("/shield-paragon")
def shield_paragon():
	return render_template("shield-paragon.html")

@app.route("/corrupted-shield")
def corrupted_shield():
	return render_template("corrupted-shield.html")

@app.route("/blade-of-crimson-oath")
def blade_of_crimson_oath():
	return render_template("blade-of-crimson-oath.html")

@app.route("/endure-deaths-touch")
def endure_deaths_touch():
	return render_template("endure-deaths-touch.html")

@app.route("/lastwall-warden-2790495")
def lastwall_warden_2790495():
	return render_template("lastwall-warden-2790495.html")

@app.route("/reaper-of-repose")
def reaper_of_repose():
	return render_template("reaper-of-repose.html")

@app.route("/sunblade")
def sunblade():
	return render_template("sunblade.html")

@app.route("/aura-of-vengeance")
def aura_of_vengeance():
	return render_template("aura-of-vengeance.html")

@app.route("/antipaladins-exalt")
def antipaladins_exalt():
	return render_template("antipaladins-exalt.html")

@app.route("/desecrators-divine-smite")
def desecrators_divine_smite():
	return render_template("desecrators-divine-smite.html")

@app.route("/desecrators-exalt")
def desecrators_exalt():
	return render_template("desecrators-exalt.html")

@app.route("/aura-of-unbreakable-virtue")
def aura_of_unbreakable_virtue():
	return render_template("aura-of-unbreakable-virtue.html")

@app.route("/a-home-in-every-port")
def a_home_in_every_port():
	return render_template("a-home-in-every-port.html")

@app.route("/courtly-graces")
def courtly_graces():
	return render_template("courtly-graces.html")

@app.route("/connections")
def connections():
	return render_template("connections.html")

@app.route("/streetwise")
def streetwise():
	return render_template("streetwise.html")

@app.route("/criminal-connections")
def criminal_connections():
	return render_template("criminal-connections.html")

@app.route("/quick-contacts")
def quick_contacts():
	return render_template("quick-contacts.html")

@app.route("/settlement-scholastics")
def settlement_scholastics():
	return render_template("settlement-scholastics.html")

@app.route("/underground-network")
def underground_network():
	return render_template("underground-network.html")

@app.route("/glean-contents")
def glean_contents():
	return render_template("glean-contents.html")

@app.route("/legendary-codebreaker")
def legendary_codebreaker():
	return render_template("legendary-codebreaker.html")

@app.route("/multilingual-cypher")
def multilingual_cypher():
	return render_template("multilingual-cypher.html")

@app.route("/scholastic-contextualization")
def scholastic_contextualization():
	return render_template("scholastic-contextualization.html")

@app.route("/prescient-consumable")
def prescient_consumable():
	return render_template("prescient-consumable.html")

@app.route("/predictive-purchaser")
def predictive_purchaser():
	return render_template("predictive-purchaser.html")

@app.route("/prescient-planner")
def prescient_planner():
	return render_template("prescient-planner.html")

@app.route("/wealth-domain-precious-metals")
def wealth_domain_precious_metals():
	return render_template("wealth-domain-precious-metals.html")

@app.route("/wealth-domain-appearance-of-wealth-6497474")
def wealth_domain_appearance_of_wealth_6497474():
	return render_template("wealth-domain-appearance-of-wealth-6497474.html")

@app.route("/cities-domain-face-in-the-crowd")
def cities_domain_face_in_the_crowd():
	return render_template("cities-domain-face-in-the-crowd.html")

@app.route("/cities-of-domain-pulse-of-the-city")
def cities_of_domain_pulse_of_the_city():
	return render_template("cities-of-domain-pulse-of-the-city.html")

@app.route("/hireling-manager")
def hireling_manager():
	return render_template("hireling-manager.html")

@app.route("/archeologist")
def archeologist():
	return render_template("archeologist.html")

@app.route("/scholastic-identification")
def scholastic_identification():
	return render_template("scholastic-identification.html")

@app.route("/biographical-eye")
def biographical_eye():
	return render_template("biographical-eye.html")

@app.route("/crude-communication")
def crude_communication():
	return render_template("crude-communication.html")

@app.route("/multilingual")
def multilingual():
	return render_template("multilingual.html")

@app.route("/legendary-linguist")
def legendary_linguist():
	return render_template("legendary-linguist.html")

@app.route("/phonetic-training")
def phonetic_training():
	return render_template("phonetic-training.html")

@app.route("/read-lips")
def read_lips():
	return render_template("read-lips.html")

@app.route("/sign-language")
def sign_language():
	return render_template("sign-language.html")

@app.route("/city-guard")
def city_guard():
	return render_template("city-guard.html")

@app.route("/know-the-beat")
def know_the_beat():
	return render_template("know-the-beat.html")

@app.route("/eye-for-numbers")
def eye_for_numbers():
	return render_template("eye-for-numbers.html")

@app.route("/accustomization")
def accustomization():
	return render_template("accustomization.html")

@app.route("/party-crasher")
def party_crasher():
	return render_template("party-crasher.html")

@app.route("/read-shibboleths")
def read_shibboleths():
	return render_template("read-shibboleths.html")

@app.route("/implausible-purchase")
def implausible_purchase():
	return render_template("implausible-purchase.html")

@app.route("/society-feats")
def society_feats():
	return render_template("society-feats.html")

@app.route("/retain-absorbed-spell")
def retain_absorbed_spell():
	return render_template("retain-absorbed-spell.html")

@app.route("/bond-conservation")
def bond_conservation():
	return render_template("bond-conservation.html")

@app.route("/call-bonded-item")
def call_bonded_item():
	return render_template("call-bonded-item.html")

@app.route("/superior-bond")
def superior_bond():
	return render_template("superior-bond.html")

@app.route("/familiars-language")
def familiars_language():
	return render_template("familiars-language.html")

@app.route("/improved-familiar-attunement")
def improved_familiar_attunement():
	return render_template("improved-familiar-attunement.html")

@app.route("/charged-creation")
def charged_creation():
	return render_template("charged-creation.html")

@app.route("/familiar-conduit")
def familiar_conduit():
	return render_template("familiar-conduit.html")

@app.route("/improved-familiar")
def improved_familiar():
	return render_template("improved-familiar.html")

@app.route("/incredible-familiar")
def incredible_familiar():
	return render_template("incredible-familiar.html")

@app.route("/baba-yagas-patronage")
def baba_yagas_patronage():
	return render_template("baba-yagas-patronage.html")

@app.route("/familiar-mascot")
def familiar_mascot():
	return render_template("familiar-mascot.html")

@app.route("/leshy-familiar-secrets")
def leshy_familiar_secrets():
	return render_template("leshy-familiar-secrets.html")

@app.route("/mask-familiar")
def mask_familiar():
	return render_template("mask-familiar.html")

@app.route("/mutable-familiar")
def mutable_familiar():
	return render_template("mutable-familiar.html")

@app.route("/halcyon-speaker")
def halcyon_speaker():
	return render_template("halcyon-speaker.html")

@app.route("/cascade-bearers-spellcasting")
def cascade_bearers_spellcasting():
	return render_template("cascade-bearers-spellcasting.html")

@app.route("/dualistic-synergy")
def dualistic_synergy():
	return render_template("dualistic-synergy.html")

@app.route("/fulminating-synergy")
def fulminating_synergy():
	return render_template("fulminating-synergy.html")

@app.route("/shared-synergy")
def shared_synergy():
	return render_template("shared-synergy.html")

@app.route("/synergistic-spell")
def synergistic_spell():
	return render_template("synergistic-spell.html")

@app.route("/harming-hands")
def harming_hands():
	return render_template("harming-hands.html")

@app.route("/improved-command-undead")
def improved_command_undead():
	return render_template("improved-command-undead.html")

@app.route("/necrotic-infusion")
def necrotic_infusion():
	return render_template("necrotic-infusion.html")

@app.route("/sap-life")
def sap_life():
	return render_template("sap-life.html")

@app.route("/vile-desecration")
def vile_desecration():
	return render_template("vile-desecration.html")

@app.route("/healing-hands")
def healing_hands():
	return render_template("healing-hands.html")

@app.route("/turn-undead")
def turn_undead():
	return render_template("turn-undead.html")

@app.route("/cremate-undead")
def cremate_undead():
	return render_template("cremate-undead.html")

@app.route("/denier-of-destruction")
def denier_of_destruction():
	return render_template("denier-of-destruction.html")

@app.route("/heroic-recovery")
def heroic_recovery():
	return render_template("heroic-recovery.html")

@app.route("/holy-castigation")
def holy_castigation():
	return render_template("holy-castigation.html")

@app.route("/castigating-weapon")
def castigating_weapon():
	return render_template("castigating-weapon.html")

@app.route("/improved-communal-healing")
def improved_communal_healing():
	return render_template("improved-communal-healing.html")

@app.route("/radiant-infusion")
def radiant_infusion():
	return render_template("radiant-infusion.html")

@app.route("/cast-down")
def cast_down():
	return render_template("cast-down.html")

@app.route("/channel-smite")
def channel_smite():
	return render_template("channel-smite.html")

@app.route("/defensive-recovery")
def defensive_recovery():
	return render_template("defensive-recovery.html")

@app.route("/directed-channel")
def directed_channel():
	return render_template("directed-channel.html")

@app.route("/echoing-channel")
def echoing_channel():
	return render_template("echoing-channel.html")

@app.route("/fast-channel")
def fast_channel():
	return render_template("fast-channel.html")

@app.route("/metamagic-channel")
def metamagic_channel():
	return render_template("metamagic-channel.html")

@app.route("/blood-component")
def blood_component():
	return render_template("blood-component.html")

@app.route("/effortless-concentration")
def effortless_concentration():
	return render_template("effortless-concentration.html")

@app.route("/eschew-materials")
def eschew_materials():
	return render_template("eschew-materials.html")

@app.route("/spell-penetration")
def spell_penetration():
	return render_template("spell-penetration.html")

@app.route("/steady-spellcasting")
def steady_spellcasting():
	return render_template("steady-spellcasting.html")

@app.route("/ward-casting")
def ward_casting():
	return render_template("ward-casting.html")

@app.route("/aberrant-bloodline-focus-aberrant-whispers")
def aberrant_bloodline_focus_aberrant_whispers():
	return render_template("aberrant-bloodline-focus-aberrant-whispers.html")

@app.route("/ancestral-blood-magic")
def ancestral_blood_magic():
	return render_template("ancestral-blood-magic.html")

@app.route("/anoint-ally")
def anoint_ally():
	return render_template("anoint-ally.html")

@app.route("/bloodline-metamorphasis")
def bloodline_metamorphasis():
	return render_template("bloodline-metamorphasis.html")

@app.route("/bloodline-mutation")
def bloodline_mutation():
	return render_template("bloodline-mutation.html")

@app.route("/demonic-bloodline")
def demonic_bloodline():
	return render_template("demonic-bloodline.html")

@app.route("/angelic-bloodline")
def angelic_bloodline():
	return render_template("angelic-bloodline.html")

@app.route("/diabolic-bloodline")
def diabolic_bloodline():
	return render_template("diabolic-bloodline.html")

@app.route("/draconic-bloodline")
def draconic_bloodline():
	return render_template("draconic-bloodline.html")

@app.route("/elemental-bloodline")
def elemental_bloodline():
	return render_template("elemental-bloodline.html")

@app.route("/entreat-the-forbearers")
def entreat_the_forbearers():
	return render_template("entreat-the-forbearers.html")

@app.route("/fey-bloodline")
def fey_bloodline():
	return render_template("fey-bloodline.html")

@app.route("/genie-bloodline")
def genie_bloodline():
	return render_template("genie-bloodline.html")

@app.route("/hag-bloodline")
def hag_bloodline():
	return render_template("hag-bloodline.html")

@app.route("/imperial-bloodline")
def imperial_bloodline():
	return render_template("imperial-bloodline.html")

@app.route("/nymph-bloodline")
def nymph_bloodline():
	return render_template("nymph-bloodline.html")

@app.route("/occult-evolution")
def occult_evolution():
	return render_template("occult-evolution.html")

@app.route("/pscyhopomp-bloodline")
def pscyhopomp_bloodline():
	return render_template("pscyhopomp-bloodline.html")

@app.route("/shadow-bloodline")
def shadow_bloodline():
	return render_template("shadow-bloodline.html")

@app.route("/tenacious-blood-magic")
def tenacious_blood_magic():
	return render_template("tenacious-blood-magic.html")

@app.route("/undead-bloodline")
def undead_bloodline():
	return render_template("undead-bloodline.html")

@app.route("/bespell-weapon")
def bespell_weapon():
	return render_template("bespell-weapon.html")

@app.route("/diverting-vortex")
def diverting_vortex():
	return render_template("diverting-vortex.html")

@app.route("/divine-weapon")
def divine_weapon():
	return render_template("divine-weapon.html")

@app.route("/verdant-weapon")
def verdant_weapon():
	return render_template("verdant-weapon.html")

@app.route("/pristine-weapon")
def pristine_weapon():
	return render_template("pristine-weapon.html")

@app.route("/replenishment-of-war")
def replenishment_of_war():
	return render_template("replenishment-of-war.html")

@app.route("/shared-replenishment")
def shared_replenishment():
	return render_template("shared-replenishment.html")

@app.route("/conceal-spell")
def conceal_spell():
	return render_template("conceal-spell.html")

@app.route("/current-spell")
def current_spell():
	return render_template("current-spell.html")

@app.route("/forcible-energy")
def forcible_energy():
	return render_template("forcible-energy.html")

@app.route("/melodious-spell")
def melodious_spell():
	return render_template("melodious-spell.html")

@app.route("/metamagical-experimentation")
def metamagical_experimentation():
	return render_template("metamagical-experimentation.html")

@app.route("/overwhelming-energy")
def overwhelming_energy():
	return render_template("overwhelming-energy.html")

@app.route("/primal-summons")
def primal_summons():
	return render_template("primal-summons.html")

@app.route("/quickened-casting")
def quickened_casting():
	return render_template("quickened-casting.html")

@app.route("/reach-spell")
def reach_spell():
	return render_template("reach-spell.html")

@app.route("/redirection")
def redirection():
	return render_template("redirection.html")

@app.route("/spiritual-infusion")
def spiritual_infusion():
	return render_template("spiritual-infusion.html")

@app.route("/split-shot")
def split_shot():
	return render_template("split-shot.html")

@app.route("/surreptitious-spellcasting")
def surreptitious_spellcasting():
	return render_template("surreptitious-spellcasting.html")

@app.route("/through-spell")
def through_spell():
	return render_template("through-spell.html")

@app.route("/widen-spell")
def widen_spell():
	return render_template("widen-spell.html")

@app.route("/echoing-spell")
def echoing_spell():
	return render_template("echoing-spell.html")

@app.route("/energy-ablation")
def energy_ablation():
	return render_template("energy-ablation.html")

@app.route("/energy-fusion")
def energy_fusion():
	return render_template("energy-fusion.html")

@app.route("/portentous-spell")
def portentous_spell():
	return render_template("portentous-spell.html")

@app.route("/recover-spell")
def recover_spell():
	return render_template("recover-spell.html")

@app.route("/safeguard-spell")
def safeguard_spell():
	return render_template("safeguard-spell.html")

@app.route("/scintillating-spell")
def scintillating_spell():
	return render_template("scintillating-spell.html")

@app.route("/silent-spell")
def silent_spell():
	return render_template("silent-spell.html")

@app.route("/sow-spell")
def sow_spell():
	return render_template("sow-spell.html")

@app.route("/spell-relay")
def spell_relay():
	return render_template("spell-relay.html")

@app.route("/spell-shroud")
def spell_shroud():
	return render_template("spell-shroud.html")

@app.route("/terraforming-spell")
def terraforming_spell():
	return render_template("terraforming-spell.html")

@app.route("/pesh-skin")
def pesh_skin():
	return render_template("pesh-skin.html")

@app.route("/divine-aegis")
def divine_aegis():
	return render_template("divine-aegis.html")

@app.route("/energy-ward")
def energy_ward():
	return render_template("energy-ward.html")

@app.route("/energetic-resonance")
def energetic_resonance():
	return render_template("energetic-resonance.html")

@app.route("/diviner-sense")
def diviner_sense():
	return render_template("diviner-sense.html")

@app.route("/cantrip-expansion")
def cantrip_expansion():
	return render_template("cantrip-expansion.html")

@app.route("/ancestral-mage")
def ancestral_mage():
	return render_template("ancestral-mage.html")

@app.route("/crossblood-evolution")
def crossblood_evolution():
	return render_template("crossblood-evolution.html")

@app.route("/mysterious-repertoire")
def mysterious_repertoire():
	return render_template("mysterious-repertoire.html")

@app.route("/greater-crossblood-evolution")
def greater_crossblood_evolution():
	return render_template("greater-crossblood-evolution.html")

@app.route("/communal-sustain")
def communal_sustain():
	return render_template("communal-sustain.html")

@app.route("/witchs-charge")
def witchs_charge():
	return render_template("witchs-charge.html")

@app.route("/witchs-communion")
def witchs_communion():
	return render_template("witchs-communion.html")

@app.route("/linked-focus")
def linked_focus():
	return render_template("linked-focus.html")

@app.route("/universalist")
def universalist():
	return render_template("universalist.html")

@app.route("/familiars-eyes")
def familiars_eyes():
	return render_template("familiars-eyes.html")

@app.route("/ebb-and-flow")
def ebb_and_flow():
	return render_template("ebb-and-flow.html")

@app.route("/martyr")
def martyr():
	return render_template("martyr.html")

@app.route("/remediate")
def remediate():
	return render_template("remediate.html")

@app.route("/psychopomp-bloodline")
def psychopomp_bloodline():
	return render_template("psychopomp-bloodline.html")

@app.route("/dangerous-sorcery")
def dangerous_sorcery():
	return render_template("dangerous-sorcery.html")

@app.route("/surging-might")
def surging_might():
	return render_template("surging-might.html")

@app.route("/nonlethal-spell")
def nonlethal_spell():
	return render_template("nonlethal-spell.html")

@app.route("/verdant-presence")
def verdant_presence():
	return render_template("verdant-presence.html")

@app.route("/pinpoint-poisoner")
def pinpoint_poisoner():
	return render_template("pinpoint-poisoner.html")

@app.route("/noisy")
def noisy():
	return render_template("noisy.html")

@app.route("/armored-stealth")
def armored_stealth():
	return render_template("armored-stealth.html")

@app.route("/lost-in-the-crowd")
def lost_in_the_crowd():
	return render_template("lost-in-the-crowd.html")

@app.route("/crowd-mastery")
def crowd_mastery():
	return render_template("crowd-mastery.html")

@app.route("/light")
def light():
	return render_template("light.html")

@app.route("/darkness-domain-cloak-of-shadow")
def darkness_domain_cloak_of_shadow():
	return render_template("darkness-domain-cloak-of-shadow.html")

@app.route("/darkness-domain-darkened-eyes")
def darkness_domain_darkened_eyes():
	return render_template("darkness-domain-darkened-eyes.html")

@app.route("/secrecy-domain-forced-quiet")
def secrecy_domain_forced_quiet():
	return render_template("secrecy-domain-forced-quiet.html")

@app.route("/secrecy-domain-safeguard-secret")
def secrecy_domain_safeguard_secret():
	return render_template("secrecy-domain-safeguard-secret.html")

@app.route("/shadow-magic-shadow-jump")
def shadow_magic_shadow_jump():
	return render_template("shadow-magic-shadow-jump.html")

@app.route("/fanes-escape")
def fanes_escape():
	return render_template("fanes-escape.html")

@app.route("/senses")
def senses():
	return render_template("senses.html")

@app.route("/foil-senses")
def foil_senses():
	return render_template("foil-senses.html")

@app.route("/sneak-savant")
def sneak_savant():
	return render_template("sneak-savant.html")

@app.route("/fleeting-shadow")
def fleeting_shadow():
	return render_template("fleeting-shadow.html")

@app.route("/swift-sneak")
def swift_sneak():
	return render_template("swift-sneak.html")

@app.route("/tactical-entry")
def tactical_entry():
	return render_template("tactical-entry.html")

@app.route("/shadowdancer")
def shadowdancer():
	return render_template("shadowdancer.html")

@app.route("/experienced-smuggler")
def experienced_smuggler():
	return render_template("experienced-smuggler.html")

@app.route("/shadow-mark")
def shadow_mark():
	return render_template("shadow-mark.html")

@app.route("/ambushing-knockdown")
def ambushing_knockdown():
	return render_template("ambushing-knockdown.html")

@app.route("/scouts-pounce")
def scouts_pounce():
	return render_template("scouts-pounce.html")

@app.route("/startling-appearance")
def startling_appearance():
	return render_template("startling-appearance.html")

@app.route("/stunning-appearance")
def stunning_appearance():
	return render_template("stunning-appearance.html")

@app.route("/frightening-appearance")
def frightening_appearance():
	return render_template("frightening-appearance.html")

@app.route("/subtle-shank")
def subtle_shank():
	return render_template("subtle-shank.html")

@app.route("/quiet-allies")
def quiet_allies():
	return render_template("quiet-allies.html")

@app.route("/underhanded-assault")
def underhanded_assault():
	return render_template("underhanded-assault.html")

@app.route("/shadow-hunter")
def shadow_hunter():
	return render_template("shadow-hunter.html")

@app.route("/terrain-stalker-2875549")
def terrain_stalker_2875549():
	return render_template("terrain-stalker-2875549.html")

@app.route("/terrain-scout")
def terrain_scout():
	return render_template("terrain-scout.html")

@app.route("/wardens-step")
def wardens_step():
	return render_template("wardens-step.html")

@app.route("/legendary-sneak")
def legendary_sneak():
	return render_template("legendary-sneak.html")

@app.route("/spring-from-the-shadows")
def spring_from_the_shadows():
	return render_template("spring-from-the-shadows.html")

@app.route("/camouflage")
def camouflage():
	return render_template("camouflage.html")

@app.route("/stealth-feats")
def stealth_feats():
	return render_template("stealth-feats.html")

@app.route("/lesson-of-snow")
def lesson_of_snow():
	return render_template("lesson-of-snow.html")

@app.route("/afflictions")
def afflictions():
	return render_template("afflictions.html")

@app.route("/lesson-of-death")
def lesson_of_death():
	return render_template("lesson-of-death.html")

@app.route("/lesson-of-renewal")
def lesson_of_renewal():
	return render_template("lesson-of-renewal.html")

@app.route("/lumberjack")
def lumberjack():
	return render_template("lumberjack.html")

@app.route("/natures-edge")
def natures_edge():
	return render_template("natures-edge.html")

@app.route("/survey-wildlife")
def survey_wildlife():
	return render_template("survey-wildlife.html")

@app.route("/wild-stride")
def wild_stride():
	return render_template("wild-stride.html")

@app.route("/favored-terrain")
def favored_terrain():
	return render_template("favored-terrain.html")

@app.route("/acclimatization")
def acclimatization():
	return render_template("acclimatization.html")

@app.route("/horizon-walker")
def horizon_walker():
	return render_template("horizon-walker.html")

@app.route("/perpetual-scout")
def perpetual_scout():
	return render_template("perpetual-scout.html")

@app.route("/sure-foot")
def sure_foot():
	return render_template("sure-foot.html")

@app.route("/terrain-expertise")
def terrain_expertise():
	return render_template("terrain-expertise.html")

@app.route("/terrain-mastery")
def terrain_mastery():
	return render_template("terrain-mastery.html")

@app.route("/ephemeral-tracking")
def ephemeral_tracking():
	return render_template("ephemeral-tracking.html")

@app.route("/environmental-grace")
def environmental_grace():
	return render_template("environmental-grace.html")

@app.route("/planar-survival")
def planar_survival():
	return render_template("planar-survival.html")

@app.route("/survival-of-desolation")
def survival_of_desolation():
	return render_template("survival-of-desolation.html")

@app.route("/wandering-oasis")
def wandering_oasis():
	return render_template("wandering-oasis.html")

@app.route("/axe-climber")
def axe_climber():
	return render_template("axe-climber.html")

@app.route("/legendary-guide")
def legendary_guide():
	return render_template("legendary-guide.html")

@app.route("/pirate")
def pirate():
	return render_template("pirate.html")

@app.route("/rope-runner")
def rope_runner():
	return render_template("rope-runner.html")

@app.route("/wild-stride-3036686")
def wild_stride_3036686():
	return render_template("wild-stride-3036686.html")

@app.route("/ultimate-skirmisher")
def ultimate_skirmisher():
	return render_template("ultimate-skirmisher.html")

@app.route("/woodland-stride")
def woodland_stride():
	return render_template("woodland-stride.html")

@app.route("/storm-born")
def storm_born():
	return render_template("storm-born.html")

@app.route("/wilderness-spotter")
def wilderness_spotter():
	return render_template("wilderness-spotter.html")

@app.route("/wortwitch")
def wortwitch():
	return render_template("wortwitch.html")

@app.route("/forager")
def forager():
	return render_template("forager.html")

@app.route("/rain-scribe-sustenance")
def rain_scribe_sustenance():
	return render_template("rain-scribe-sustenance.html")

@app.route("/rugged-survivalist")
def rugged_survivalist():
	return render_template("rugged-survivalist.html")

@app.route("/experienced-tracker")
def experienced_tracker():
	return render_template("experienced-tracker.html")

@app.route("/swift-tracker")
def swift_tracker():
	return render_template("swift-tracker.html")

@app.route("/trackless-step")
def trackless_step():
	return render_template("trackless-step.html")

@app.route("/dead-reckoning")
def dead_reckoning():
	return render_template("dead-reckoning.html")

@app.route("/terrain-transposition")
def terrain_transposition():
	return render_template("terrain-transposition.html")

@app.route("/environmental-explorer")
def environmental_explorer():
	return render_template("environmental-explorer.html")

@app.route("/survival-feats")
def survival_feats():
	return render_template("survival-feats.html")

@app.route("/slice-and-swipe")
def slice_and_swipe():
	return render_template("slice-and-swipe.html")

@app.route("/stab-and-snag")
def stab_and_snag():
	return render_template("stab-and-snag.html")

@app.route("/quick-unlock")
def quick_unlock():
	return render_template("quick-unlock.html")

@app.route("/concealed-legerdemain")
def concealed_legerdemain():
	return render_template("concealed-legerdemain.html")

@app.route("/pickpocket")
def pickpocket():
	return render_template("pickpocket.html")

@app.route("/plant-evidence")
def plant_evidence():
	return render_template("plant-evidence.html")

@app.route("/legendary-thief")
def legendary_thief():
	return render_template("legendary-thief.html")

@app.route("/steal-spell")
def steal_spell():
	return render_template("steal-spell.html")

@app.route("/steal-essence")
def steal_essence():
	return render_template("steal-essence.html")

@app.route("/subtle-theft")
def subtle_theft():
	return render_template("subtle-theft.html")

@app.route("/sabotage")
def sabotage():
	return render_template("sabotage.html")

@app.route("/careful-explorer")
def careful_explorer():
	return render_template("careful-explorer.html")

@app.route("/delay-trap")
def delay_trap():
	return render_template("delay-trap.html")

@app.route("/everyone-duck")
def everyone_duck():
	return render_template("everyone-duck.html")

@app.route("/gifted-disarmer")
def gifted_disarmer():
	return render_template("gifted-disarmer.html")

@app.route("/trapbreakers-luck")
def trapbreakers_luck():
	return render_template("trapbreakers-luck.html")

@app.route("/wary-disarmament")
def wary_disarmament():
	return render_template("wary-disarmament.html")

@app.route("/cartwheel-dodge")
def cartwheel_dodge():
	return render_template("cartwheel-dodge.html")

@app.route("/daring-act")
def daring_act():
	return render_template("daring-act.html")

@app.route("/daredevils-gambit")
def daredevils_gambit():
	return render_template("daredevils-gambit.html")

@app.route("/daring-flourish")
def daring_flourish():
	return render_template("daring-flourish.html")

@app.route("/furious-sprint")
def furious_sprint():
	return render_template("furious-sprint.html")

@app.route("/light-step-1100854")
def light_step_1100854():
	return render_template("light-step-1100854.html")

@app.route("/swift-elusion")
def swift_elusion():
	return render_template("swift-elusion.html")

@app.route("/acrobatics-class-feats")
def acrobatics_class_feats():
	return render_template("acrobatics-class-feats.html")

@app.route("/armigers-mobility")
def armigers_mobility():
	return render_template("armigers-mobility.html")

@app.route("/armor-assist")
def armor_assist():
	return render_template("armor-assist.html")

@app.route("/armor-specialist")
def armor_specialist():
	return render_template("armor-specialist.html")

@app.route("/armored-rebuff")
def armored_rebuff():
	return render_template("armored-rebuff.html")

@app.route("/bulwark")
def bulwark():
	return render_template("bulwark.html")

@app.route("/mighty-bulwark")
def mighty_bulwark():
	return render_template("mighty-bulwark.html")

@app.route("/greater-interpose")
def greater_interpose():
	return render_template("greater-interpose.html")

@app.route("/overpowering-charge")
def overpowering_charge():
	return render_template("overpowering-charge.html")

@app.route("/mobility")
def mobility():
	return render_template("mobility.html")

@app.route("/guarded-movement")
def guarded_movement():
	return render_template("guarded-movement.html")

@app.route("/brutal-bully")
def brutal_bully():
	return render_template("brutal-bully.html")

@app.route("/sudden-charge")
def sudden_charge():
	return render_template("sudden-charge.html")

@app.route("/no-escape")
def no_escape():
	return render_template("no-escape.html")

@app.route("/ship-to-ship")
def ship_to_ship():
	return render_template("ship-to-ship.html")

@app.route("/sudden-leap")
def sudden_leap():
	return render_template("sudden-leap.html")

@app.route("/winding-flow")
def winding_flow():
	return render_template("winding-flow.html")

@app.route("/determined-dash")
def determined_dash():
	return render_template("determined-dash.html")

@app.route("/farabellas-flip")
def farabellas_flip():
	return render_template("farabellas-flip.html")

@app.route("/brutal-critical")
def brutal_critical():
	return render_template("brutal-critical.html")

@app.route("/savage-critical")
def savage_critical():
	return render_template("savage-critical.html")

@app.route("/unbalancing-blow")
def unbalancing_blow():
	return render_template("unbalancing-blow.html")

@app.route("/sidestep")
def sidestep():
	return render_template("sidestep.html")

@app.route("/spring-attack")
def spring_attack():
	return render_template("spring-attack.html")

@app.route("/great-cleave")
def great_cleave():
	return render_template("great-cleave.html")

@app.route("/quick-reversal")
def quick_reversal():
	return render_template("quick-reversal.html")

@app.route("/swipe")
def swipe():
	return render_template("swipe.html")

@app.route("/whirlwind-strike")
def whirlwind_strike():
	return render_template("whirlwind-strike.html")

@app.route("/disarming-assault")
def disarming_assault():
	return render_template("disarming-assault.html")

@app.route("/disarming-flair")
def disarming_flair():
	return render_template("disarming-flair.html")

@app.route("/relentless-disarm")
def relentless_disarm():
	return render_template("relentless-disarm.html")

@app.route("/quick-draw")
def quick_draw():
	return render_template("quick-draw.html")

@app.route("/ultimate-flexibility")
def ultimate_flexibility():
	return render_template("ultimate-flexibility.html")

@app.route("/deny-support")
def deny_support():
	return render_template("deny-support.html")

@app.route("/overextending-feint")
def overextending_feint():
	return render_template("overextending-feint.html")

@app.route("/scoundrel")
def scoundrel():
	return render_template("scoundrel.html")

@app.route("/scouts-charge")
def scouts_charge():
	return render_template("scouts-charge.html")

@app.route("/gravity-weapon")
def gravity_weapon():
	return render_template("gravity-weapon.html")

@app.route("/zeal-domain-weapon-surge")
def zeal_domain_weapon_surge():
	return render_template("zeal-domain-weapon-surge.html")

@app.route("/felling-strike")
def felling_strike():
	return render_template("felling-strike.html")

@app.route("/mobile-magical-combat")
def mobile_magical_combat():
	return render_template("mobile-magical-combat.html")

@app.route("/combat-grab")
def combat_grab():
	return render_template("combat-grab.html")

@app.route("/crushing-grab")
def crushing_grab():
	return render_template("crushing-grab.html")

@app.route("/dazing-blow")
def dazing_blow():
	return render_template("dazing-blow.html")

@app.route("/embrace-the-pain")
def embrace_the_pain():
	return render_template("embrace-the-pain.html")

@app.route("/furious-grab")
def furious_grab():
	return render_template("furious-grab.html")

@app.route("/impaling-thrust")
def impaling_thrust():
	return render_template("impaling-thrust.html")

@app.route("/collateral-dash")
def collateral_dash():
	return render_template("collateral-dash.html")

@app.route("/whirling-throw")
def whirling_throw():
	return render_template("whirling-throw.html")

@app.route("/battle-planner")
def battle_planner():
	return render_template("battle-planner.html")

@app.route("/zeal-domain-zeal-for-battle")
def zeal_domain_zeal_for_battle():
	return render_template("zeal-domain-zeal-for-battle.html")

@app.route("/surprise-attack")
def surprise_attack():
	return render_template("surprise-attack.html")

@app.route("/swaggering-initiative")
def swaggering_initiative():
	return render_template("swaggering-initiative.html")

@app.route("/dread-striker")
def dread_striker():
	return render_template("dread-striker.html")

@app.route("/fearsome-brute")
def fearsome_brute():
	return render_template("fearsome-brute.html")

@app.route("/intimidating-strike")
def intimidating_strike():
	return render_template("intimidating-strike.html")

@app.route("/deadly-grace")
def deadly_grace():
	return render_template("deadly-grace.html")

@app.route("/devastator")
def devastator():
	return render_template("devastator.html")

@app.route("/furious-focus")
def furious_focus():
	return render_template("furious-focus.html")

@app.route("/certain-strike")
def certain_strike():
	return render_template("certain-strike.html")

@app.route("/exacting-strike")
def exacting_strike():
	return render_template("exacting-strike.html")

@app.route("/follow-up-assault")
def follow_up_assault():
	return render_template("follow-up-assault.html")

@app.route("/perfected-form")
def perfected_form():
	return render_template("perfected-form.html")

@app.route("/overwhelming-blow")
def overwhelming_blow():
	return render_template("overwhelming-blow.html")

@app.route("/death")
def death():
	return render_template("death.html")

@app.route("/angel-of-death")
def angel_of_death():
	return render_template("angel-of-death.html")

@app.route("/assassinate")
def assassinate():
	return render_template("assassinate.html")

@app.route("/expert-backstabber")
def expert_backstabber():
	return render_template("expert-backstabber.html")

@app.route("/lunging-stance")
def lunging_stance():
	return render_template("lunging-stance.html")

@app.route("/combat-reflexes")
def combat_reflexes():
	return render_template("combat-reflexes.html")

@app.route("/desperate-finisher")
def desperate_finisher():
	return render_template("desperate-finisher.html")

@app.route("/disorienting-opening")
def disorienting_opening():
	return render_template("disorienting-opening.html")

@app.route("/disruptive-stance")
def disruptive_stance():
	return render_template("disruptive-stance.html")

@app.route("/felicitous-riposte")
def felicitous_riposte():
	return render_template("felicitous-riposte.html")

@app.route("/impassible-wall-stance")
def impassible_wall_stance():
	return render_template("impassible-wall-stance.html")

@app.route("/impossible-riposte")
def impossible_riposte():
	return render_template("impossible-riposte.html")

@app.route("/opportune-backstab")
def opportune_backstab():
	return render_template("opportune-backstab.html")

@app.route("/reactive-interference")
def reactive_interference():
	return render_template("reactive-interference.html")

@app.route("/reflexive-riposte")
def reflexive_riposte():
	return render_template("reflexive-riposte.html")

@app.route("/stand-still")
def stand_still():
	return render_template("stand-still.html")

@app.route("/stay-down")
def stay_down():
	return render_template("stay-down.html")

@app.route("/achaekeks-grip")
def achaekeks_grip():
	return render_template("achaekeks-grip.html")

@app.route("/achaekeks-sense")
def achaekeks_sense():
	return render_template("achaekeks-sense.html")

@app.route("/fading")
def fading():
	return render_template("fading.html")

@app.route("/vernai-training")
def vernai_training():
	return render_template("vernai-training.html")

@app.route("/blind-fight")
def blind_fight():
	return render_template("blind-fight.html")

@app.route("/revealing-stab")
def revealing_stab():
	return render_template("revealing-stab.html")

@app.route("/awesome-blow")
def awesome_blow():
	return render_template("awesome-blow.html")

@app.route("/shove-down")
def shove_down():
	return render_template("shove-down.html")

@app.route("/annihilating-swing")
def annihilating_swing():
	return render_template("annihilating-swing.html")

@app.route("/brutal-beating")
def brutal_beating():
	return render_template("brutal-beating.html")

@app.route("/demanding-challenge")
def demanding_challenge():
	return render_template("demanding-challenge.html")

@app.route("/harrying-strike")
def harrying_strike():
	return render_template("harrying-strike.html")

@app.route("/head-stomp")
def head_stomp():
	return render_template("head-stomp.html")

@app.route("/instant-opening")
def instant_opening():
	return render_template("instant-opening.html")

@app.route("/master-strike")
def master_strike():
	return render_template("master-strike.html")

@app.route("/resounding-blow")
def resounding_blow():
	return render_template("resounding-blow.html")

@app.route("/snagging-strike")
def snagging_strike():
	return render_template("snagging-strike.html")

@app.route("/murderers-circle")
def murderers_circle():
	return render_template("murderers-circle.html")

@app.route("/vivacious-evisceration")
def vivacious_evisceration():
	return render_template("vivacious-evisceration.html")

@app.route("/advantageous-assault")
def advantageous_assault():
	return render_template("advantageous-assault.html")

@app.route("/snatch-arrow")
def snatch_arrow():
	return render_template("snatch-arrow.html")

@app.route("/deaths-door")
def deaths_door():
	return render_template("deaths-door.html")

@app.route("/deny-advantage")
def deny_advantage():
	return render_template("deny-advantage.html")

@app.route("/nimble-roll")
def nimble_roll():
	return render_template("nimble-roll.html")

@app.route("/reflexive-grip")
def reflexive_grip():
	return render_template("reflexive-grip.html")

@app.route("/smash-from-the-air")
def smash_from_the_air():
	return render_template("smash-from-the-air.html")

@app.route("/master-of-many-styles")
def master_of_many_styles():
	return render_template("master-of-many-styles.html")

@app.route("/prevailing-position")
def prevailing_position():
	return render_template("prevailing-position.html")

@app.route("/back-to-back")
def back_to_back():
	return render_template("back-to-back.html")

@app.route("/coordinated-charge")
def coordinated_charge():
	return render_template("coordinated-charge.html")

@app.route("/coordinated-distraction")
def coordinated_distraction():
	return render_template("coordinated-distraction.html")

@app.route("/deft-combat-cooperation")
def deft_combat_cooperation():
	return render_template("deft-combat-cooperation.html")

@app.route("/gang-up")
def gang_up():
	return render_template("gang-up.html")

@app.route("/knight-vigilant")
def knight_vigilant():
	return render_template("knight-vigilant.html")

@app.route("/leave-an-opening")
def leave_an_opening():
	return render_template("leave-an-opening.html")

@app.route("/scouts-warning")
def scouts_warning():
	return render_template("scouts-warning.html")

@app.route("/target-of-opportunity")
def target_of_opportunity():
	return render_template("target-of-opportunity.html")

@app.route("/topple-foe")
def topple_foe():
	return render_template("topple-foe.html")

@app.route("/vigils-walls-rise-anew")
def vigils_walls_rise_anew():
	return render_template("vigils-walls-rise-anew.html")

@app.route("/protect-ally")
def protect_ally():
	return render_template("protect-ally.html")

@app.route("/rallying-charge")
def rallying_charge():
	return render_template("rallying-charge.html")

@app.route("/stave-off-catastrophe")
def stave_off_catastrophe():
	return render_template("stave-off-catastrophe.html")

@app.route("/leading-dance")
def leading_dance():
	return render_template("leading-dance.html")

@app.route("/sleeper-hold")
def sleeper_hold():
	return render_template("sleeper-hold.html")

@app.route("/tangle-of-battle")
def tangle_of_battle():
	return render_template("tangle-of-battle.html")

@app.route("/lunge")
def lunge():
	return render_template("lunge.html")

@app.route("/blood-debilitations")
def blood_debilitations():
	return render_template("blood-debilitations.html")

@app.route("/critical-debilitations")
def critical_debilitations():
	return render_template("critical-debilitations.html")

@app.route("/double-debilitation")
def double_debilitation():
	return render_template("double-debilitation.html")

@app.route("/eldritch-debilitation")
def eldritch_debilitation():
	return render_template("eldritch-debilitation.html")

@app.route("/methodical-debilitation")
def methodical_debilitation():
	return render_template("methodical-debilitation.html")

@app.route("/precise-debilitation")
def precise_debilitation():
	return render_template("precise-debilitation.html")

@app.route("/tactical-debilitation")
def tactical_debilitation():
	return render_template("tactical-debilitation.html")

@app.route("/vicious-debilitation")
def vicious_debilitation():
	return render_template("vicious-debilitation.html")

@app.route("/tactic")
def tactic():
	return render_template("tactic.html")

@app.route("/hunt-prey")
def hunt_prey():
	return render_template("hunt-prey.html")

@app.route("/outwit")
def outwit():
	return render_template("outwit.html")

@app.route("/posse")
def posse():
	return render_template("posse.html")

@app.route("/double-prey")
def double_prey():
	return render_template("double-prey.html")

@app.route("/wardens-boon")
def wardens_boon():
	return render_template("wardens-boon.html")

@app.route("/shared-prey")
def shared_prey():
	return render_template("shared-prey.html")

@app.route("/swift-track-prey")
def swift_track_prey():
	return render_template("swift-track-prey.html")

@app.route("/to-the-ends-of-the-earth")
def to_the_ends_of_the_earth():
	return render_template("to-the-ends-of-the-earth.html")

@app.route("/triple-threat")
def triple_threat():
	return render_template("triple-threat.html")

@app.route("/greater-outwit")
def greater_outwit():
	return render_template("greater-outwit.html")

@app.route("/wardens-guidance")
def wardens_guidance():
	return render_template("wardens-guidance.html")

@app.route("/rangers-companion")
def rangers_companion():
	return render_template("rangers-companion.html")

@app.route("/rangers-masterful-companion")
def rangers_masterful_companion():
	return render_template("rangers-masterful-companion.html")

@app.route("/hunters-vision")
def hunters_vision():
	return render_template("hunters-vision.html")

@app.route("/flurry")
def flurry():
	return render_template("flurry.html")

@app.route("/precision")
def precision():
	return render_template("precision.html")

@app.route("/greater-precision")
def greater_precision():
	return render_template("greater-precision.html")

@app.route("/additional-recollection")
def additional_recollection():
	return render_template("additional-recollection.html")

@app.route("/monster-warden")
def monster_warden():
	return render_template("monster-warden.html")

@app.route("/master-monster-hunter")
def master_monster_hunter():
	return render_template("master-monster-hunter.html")

@app.route("/disrupt-prey")
def disrupt_prey():
	return render_template("disrupt-prey.html")

@app.route("/rangers-snap-grapple")
def rangers_snap_grapple():
	return render_template("rangers-snap-grapple.html")

@app.route("/second-sting")
def second_sting():
	return render_template("second-sting.html")

@app.route("/twin-takedown")
def twin_takedown():
	return render_template("twin-takedown.html")

@app.route("/deadly-aim")
def deadly_aim():
	return render_template("deadly-aim.html")

@app.route("/distracting-shot")
def distracting_shot():
	return render_template("distracting-shot.html")

@app.route("/greater-distracting-shot")
def greater_distracting_shot():
	return render_template("greater-distracting-shot.html")

@app.route("/hunted-shot")
def hunted_shot():
	return render_template("hunted-shot.html")

@app.route("/hunters-aim")
def hunters_aim():
	return render_template("hunters-aim.html")

@app.route("/penetrating-shot")
def penetrating_shot():
	return render_template("penetrating-shot.html")

@app.route("/targeting-shot")
def targeting_shot():
	return render_template("targeting-shot.html")

@app.route("/favored-enemy")
def favored_enemy():
	return render_template("favored-enemy.html")

@app.route("/after-you")
def after_you():
	return render_template("after-you.html")

@app.route("/combination-finisher")
def combination_finisher():
	return render_template("combination-finisher.html")

@app.route("/continuous-flair")
def continuous_flair():
	return render_template("continuous-flair.html")

@app.route("/derring-do")
def derring_do():
	return render_template("derring-do.html")

@app.route("/disarming-panache")
def disarming_panache():
	return render_template("disarming-panache.html")

@app.route("/impaling-finisher")
def impaling_finisher():
	return render_template("impaling-finisher.html")

@app.route("/dual-finisher")
def dual_finisher():
	return render_template("dual-finisher.html")

@app.route("/precise-finisher")
def precise_finisher():
	return render_template("precise-finisher.html")

@app.route("/stunning-finisher")
def stunning_finisher():
	return render_template("stunning-finisher.html")

@app.route("/targeting-finisher")
def targeting_finisher():
	return render_template("targeting-finisher.html")

@app.route("/unbalancing-finisher")
def unbalancing_finisher():
	return render_template("unbalancing-finisher.html")

@app.route("/vivacious-speed")
def vivacious_speed():
	return render_template("vivacious-speed.html")

@app.route("/finishing-follow")
def finishing_follow():
	return render_template("finishing-follow.html")

@app.route("/flamboyant-athlete")
def flamboyant_athlete():
	return render_template("flamboyant-athlete.html")

@app.route("/flamboyant-cruelty")
def flamboyant_cruelty():
	return render_template("flamboyant-cruelty.html")

@app.route("/mobile-finisher")
def mobile_finisher():
	return render_template("mobile-finisher.html")

@app.route("/flamboyant-leap")
def flamboyant_leap():
	return render_template("flamboyant-leap.html")

@app.route("/perfect-finisher")
def perfect_finisher():
	return render_template("perfect-finisher.html")

@app.route("/rage")
def rage():
	return render_template("rage.html")

@app.route("/animal-skin")
def animal_skin():
	return render_template("animal-skin.html")

@app.route("/furious-bully")
def furious_bully():
	return render_template("furious-bully.html")

@app.route("/come-and-get-me")
def come_and_get_me():
	return render_template("come-and-get-me.html")

@app.route("/share-rage")
def share_rage():
	return render_template("share-rage.html")

@app.route("/contagious-rage")
def contagious_rage():
	return render_template("contagious-rage.html")

@app.route("/draconic-arrogance")
def draconic_arrogance():
	return render_template("draconic-arrogance.html")

@app.route("/dragons-rage-wings")
def dragons_rage_wings():
	return render_template("dragons-rage-wings.html")

@app.route("/dragons-rage-breath")
def dragons_rage_breath():
	return render_template("dragons-rage-breath.html")

@app.route("/furious-finish")
def furious_finish():
	return render_template("furious-finish.html")

@app.route("/furious-vengeance")
def furious_vengeance():
	return render_template("furious-vengeance.html")

@app.route("/giants-stature")
def giants_stature():
	return render_template("giants-stature.html")

@app.route("/giants-lunge")
def giants_lunge():
	return render_template("giants-lunge.html")

@app.route("/mage-hunter")
def mage_hunter():
	return render_template("mage-hunter.html")

@app.route("/mighty-rage")
def mighty_rage():
	return render_template("mighty-rage.html")

@app.route("/moment-of-clarity-4338219")
def moment_of_clarity_4338219():
	return render_template("moment-of-clarity-4338219.html")

@app.route("/nocturnal-sense")
def nocturnal_sense():
	return render_template("nocturnal-sense.html")

@app.route("/predators-pounce")
def predators_pounce():
	return render_template("predators-pounce.html")

@app.route("/quick-rage")
def quick_rage():
	return render_template("quick-rage.html")

@app.route("/raging-thrower")
def raging_thrower():
	return render_template("raging-thrower.html")

@app.route("/reckless-abandon-131641")
def reckless_abandon_131641():
	return render_template("reckless-abandon-131641.html")

@app.route("/renewed-vigor")
def renewed_vigor():
	return render_template("renewed-vigor.html")

@app.route("/scouring-rage")
def scouring_rage():
	return render_template("scouring-rage.html")

@app.route("/second-wind")
def second_wind():
	return render_template("second-wind.html")

@app.route("/shattering-blows")
def shattering_blows():
	return render_template("shattering-blows.html")

@app.route("/spirits-interference")
def spirits_interference():
	return render_template("spirits-interference.html")

@app.route("/spirits-wrath")
def spirits_wrath():
	return render_template("spirits-wrath.html")

@app.route("/spiritual-guides")
def spiritual_guides():
	return render_template("spiritual-guides.html")

@app.route("/sunder-spell")
def sunder_spell():
	return render_template("sunder-spell.html")

@app.route("/sunder-enchantment")
def sunder_enchantment():
	return render_template("sunder-enchantment.html")

@app.route("/titans-structure")
def titans_structure():
	return render_template("titans-structure.html")

@app.route("/unstoppable-juggernaut")
def unstoppable_juggernaut():
	return render_template("unstoppable-juggernaut.html")

@app.route("/vengeful-strike")
def vengeful_strike():
	return render_template("vengeful-strike.html")

@app.route("/wounded-rage")
def wounded_rage():
	return render_template("wounded-rage.html")

@app.route("/supernatural-senses")
def supernatural_senses():
	return render_template("supernatural-senses.html")

@app.route("/athletic-strategem")
def athletic_strategem():
	return render_template("athletic-strategem.html")

@app.route("/shared-strategem")
def shared_strategem():
	return render_template("shared-strategem.html")

@app.route("/didactic-strike")
def didactic_strike():
	return render_template("didactic-strike.html")

@app.route("/known-weakness")
def known_weakness():
	return render_template("known-weakness.html")

@app.route("/ongoing-strategy")
def ongoing_strategy():
	return render_template("ongoing-strategy.html")

@app.route("/scalpels-point")
def scalpels_point():
	return render_template("scalpels-point.html")

@app.route("/strategic-assessment")
def strategic_assessment():
	return render_template("strategic-assessment.html")

@app.route("/strategic-bypass")
def strategic_bypass():
	return render_template("strategic-bypass.html")

@app.route("/takedown-expert")
def takedown_expert():
	return render_template("takedown-expert.html")

@app.route("/analyze-weakness")
def analyze_weakness():
	return render_template("analyze-weakness.html")

@app.route("/magical-trickster")
def magical_trickster():
	return render_template("magical-trickster.html")

@app.route("/mug")
def mug():
	return render_template("mug.html")

@app.route("/ruffian")
def ruffian():
	return render_template("ruffian.html")

@app.route("/dispelling-slice")
def dispelling_slice():
	return render_template("dispelling-slice.html")

@app.route("/powerful-sneak")
def powerful_sneak():
	return render_template("powerful-sneak.html")

@app.route("/the-harder-they-fall")
def the_harder_they_fall():
	return render_template("the-harder-they-fall.html")

@app.route("/enduring-debilitation")
def enduring_debilitation():
	return render_template("enduring-debilitation.html")

@app.route("/mimic-protections")
def mimic_protections():
	return render_template("mimic-protections.html")

@app.route("/swift-prey")
def swift_prey():
	return render_template("swift-prey.html")

@app.route("/monster-hunter")
def monster_hunter():
	return render_template("monster-hunter.html")

@app.route("/legendary-monster-hunter")
def legendary_monster_hunter():
	return render_template("legendary-monster-hunter.html")

@app.route("/panache")
def panache():
	return render_template("panache.html")

@app.route("/confident-finisher")
def confident_finisher():
	return render_template("confident-finisher.html")

@app.route("/battledancer")
def battledancer():
	return render_template("battledancer.html")

@app.route("/braggart")
def braggart():
	return render_template("braggart.html")

@app.route("/fencer")
def fencer():
	return render_template("fencer.html")

@app.route("/gymnast")
def gymnast():
	return render_template("gymnast.html")

@app.route("/wit")
def wit():
	return render_template("wit.html")

@app.route("/bleeding-finisher")
def bleeding_finisher():
	return render_template("bleeding-finisher.html")

@app.route("/eternal-confidence")
def eternal_confidence():
	return render_template("eternal-confidence.html")

@app.route("/flying-blade")
def flying_blade():
	return render_template("flying-blade.html")

@app.route("/lethal-finisher")
def lethal_finisher():
	return render_template("lethal-finisher.html")

@app.route("/perfect-clarity")
def perfect_clarity():
	return render_template("perfect-clarity.html")

@app.route("/vivacious-bravado")
def vivacious_bravado():
	return render_template("vivacious-bravado.html")

@app.route("/mystic-strikes")
def mystic_strikes():
	return render_template("mystic-strikes.html")

@app.route("/adamantine-strikes")
def adamantine_strikes():
	return render_template("adamantine-strikes.html")

@app.route("/monastic-weaponry")
def monastic_weaponry():
	return render_template("monastic-weaponry.html")

@app.route("/ancestral-weaponry")
def ancestral_weaponry():
	return render_template("ancestral-weaponry.html")

@app.route("/ancestral-weapon-familiarity")
def ancestral_weapon_familiarity():
	return render_template("ancestral-weapon-familiarity.html")

@app.route("/blazing-talon-surge")
def blazing_talon_surge():
	return render_template("blazing-talon-surge.html")

@app.route("/brawling-focus")
def brawling_focus():
	return render_template("brawling-focus.html")

@app.route("/rain-of-embers-stance")
def rain_of_embers_stance():
	return render_template("rain-of-embers-stance.html")

@app.route("/cobra-envenom")
def cobra_envenom():
	return render_template("cobra-envenom.html")

@app.route("/crane-flutter")
def crane_flutter():
	return render_template("crane-flutter.html")

@app.route("/cross-the-final-horizon")
def cross_the_final_horizon():
	return render_template("cross-the-final-horizon.html")

@app.route("/stumbling-stance")
def stumbling_stance():
	return render_template("stumbling-stance.html")

@app.route("/dragon-stance")
def dragon_stance():
	return render_template("dragon-stance.html")

@app.route("/dragon-roar")
def dragon_roar():
	return render_template("dragon-roar.html")

@app.route("/explosive-death-drop")
def explosive_death_drop():
	return render_template("explosive-death-drop.html")

@app.route("/flurry-of-blows")
def flurry_of_blows():
	return render_template("flurry-of-blows.html")

@app.route("/flurry-of-maneuvers")
def flurry_of_maneuvers():
	return render_template("flurry-of-maneuvers.html")

@app.route("/monastic-archer-stance")
def monastic_archer_stance():
	return render_template("monastic-archer-stance.html")

@app.route("/focused-shot")
def focused_shot():
	return render_template("focused-shot.html")

@app.route("/gorilla-stance")
def gorilla_stance():
	return render_template("gorilla-stance.html")

@app.route("/gorilla-pound")
def gorilla_pound():
	return render_template("gorilla-pound.html")

@app.route("/animal-instinct")
def animal_instinct():
	return render_template("animal-instinct.html")

@app.route("/dragon-instinct")
def dragon_instinct():
	return render_template("dragon-instinct.html")

@app.route("/fury-instinct")
def fury_instinct():
	return render_template("fury-instinct.html")

@app.route("/giant-instinct")
def giant_instinct():
	return render_template("giant-instinct.html")

@app.route("/spirit-instinct")
def spirit_instinct():
	return render_template("spirit-instinct.html")

@app.route("/ironblood-stance")
def ironblood_stance():
	return render_template("ironblood-stance.html")

@app.route("/ironblood-surge")
def ironblood_surge():
	return render_template("ironblood-surge.html")

@app.route("/metal-strikes")
def metal_strikes():
	return render_template("metal-strikes.html")

@app.route("/peafowl-stance")
def peafowl_stance():
	return render_template("peafowl-stance.html")

@app.route("/peafowl-strut")
def peafowl_strut():
	return render_template("peafowl-strut.html")

@app.route("/pinning-fire")
def pinning_fire():
	return render_template("pinning-fire.html")

@app.route("/return-fire")
def return_fire():
	return render_template("return-fire.html")

@app.route("/shooting-stars-stance")
def shooting_stars_stance():
	return render_template("shooting-stars-stance.html")

@app.route("/stumbling-feint")
def stumbling_feint():
	return render_template("stumbling-feint.html")

@app.route("/stunning-fist")
def stunning_fist():
	return render_template("stunning-fist.html")

@app.route("/movement-types")
def movement_types():
	return render_template("movement-types.html")

@app.route("/forced-movement")
def forced_movement():
	return render_template("forced-movement.html")

@app.route("/tangled-forest-rake")
def tangled_forest_rake():
	return render_template("tangled-forest-rake.html")

@app.route("/tiger-stance")
def tiger_stance():
	return render_template("tiger-stance.html")

@app.route("/tiger-slash")
def tiger_slash():
	return render_template("tiger-slash.html")

@app.route("/triangle-shot")
def triangle_shot():
	return render_template("triangle-shot.html")

@app.route("/whirling-blade-stance")
def whirling_blade_stance():
	return render_template("whirling-blade-stance.html")

@app.route("/wolf-stance")
def wolf_stance():
	return render_template("wolf-stance.html")

@app.route("/wolf-drag")
def wolf_drag():
	return render_template("wolf-drag.html")

@app.route("/abundant-step")
def abundant_step():
	return render_template("abundant-step.html")

@app.route("/ki-strike")
def ki_strike():
	return render_template("ki-strike.html")

@app.route("/elemental-fist")
def elemental_fist():
	return render_template("elemental-fist.html")

@app.route("/endurance-of-the-rooted-tree")
def endurance_of_the_rooted_tree():
	return render_template("endurance-of-the-rooted-tree.html")

@app.route("/ki-blast")
def ki_blast():
	return render_template("ki-blast.html")

@app.route("/ki-center")
def ki_center():
	return render_template("ki-center.html")

@app.route("/ki-form")
def ki_form():
	return render_template("ki-form.html")

@app.route("/ki-rush")
def ki_rush():
	return render_template("ki-rush.html")

@app.route("/medusas-wrath")
def medusas_wrath():
	return render_template("medusas-wrath.html")

@app.route("/overwhelming-breath")
def overwhelming_breath():
	return render_template("overwhelming-breath.html")

@app.route("/perfect-strike")
def perfect_strike():
	return render_template("perfect-strike.html")

@app.route("/quivering-palm")
def quivering_palm():
	return render_template("quivering-palm.html")

@app.route("/sacred-ki")
def sacred_ki():
	return render_template("sacred-ki.html")

@app.route("/unblinking-flame-revelation")
def unblinking_flame_revelation():
	return render_template("unblinking-flame-revelation.html")

@app.route("/unbreaking-wave-advance")
def unbreaking_wave_advance():
	return render_template("unbreaking-wave-advance.html")

@app.route("/untwisting-iron-buffer")
def untwisting_iron_buffer():
	return render_template("untwisting-iron-buffer.html")

@app.route("/wild-wind-initiate")
def wild_wind_initiate():
	return render_template("wild-wind-initiate.html")

@app.route("/wild-winds-gust")
def wild_winds_gust():
	return render_template("wild-winds-gust.html")

@app.route("/wind-jump")
def wind_jump():
	return render_template("wind-jump.html")

@app.route("/fuse-stance")
def fuse_stance():
	return render_template("fuse-stance.html")

@app.route("/deadly-strikes")
def deadly_strikes():
	return render_template("deadly-strikes.html")

@app.route("/disrupt-ki")
def disrupt_ki():
	return render_template("disrupt-ki.html")

@app.route("/flinging-blow")
def flinging_blow():
	return render_template("flinging-blow.html")

@app.route("/flying-kick")
def flying_kick():
	return render_template("flying-kick.html")

@app.route("/knockback-strike")
def knockback_strike():
	return render_template("knockback-strike.html")

@app.route("/one-inch-punch")
def one_inch_punch():
	return render_template("one-inch-punch.html")

@app.route("/one-millimeter-punch")
def one_millimeter_punch():
	return render_template("one-millimeter-punch.html")

@app.route("/form-lock")
def form_lock():
	return render_template("form-lock.html")

@app.route("/speaking-sky")
def speaking_sky():
	return render_template("speaking-sky.html")

@app.route("/sky-and-heaven-stance")
def sky_and_heaven_stance():
	return render_template("sky-and-heaven-stance.html")

@app.route("/mountain-stance")
def mountain_stance():
	return render_template("mountain-stance.html")

@app.route("/mountain-stronghold")
def mountain_stronghold():
	return render_template("mountain-stronghold.html")

@app.route("/mountain-quake")
def mountain_quake():
	return render_template("mountain-quake.html")

@app.route("/shadows-web")
def shadows_web():
	return render_template("shadows-web.html")

@app.route("/tangled-forest-stance")
def tangled_forest_stance():
	return render_template("tangled-forest-stance.html")

@app.route("/diamond-fists")
def diamond_fists():
	return render_template("diamond-fists.html")

@app.route("/improvised-weapon-fighter")
def improvised_weapon_fighter():
	return render_template("improvised-weapon-fighter.html")

@app.route("/splash-7476201")
def splash_7476201():
	return render_template("splash-7476201.html")

@app.route("/weapon-critical-specialization-effects")
def weapon_critical_specialization_effects():
	return render_template("weapon-critical-specialization-effects.html")

@app.route("/improvised-critical")
def improvised_critical():
	return render_template("improvised-critical.html")

@app.route("/improvised-pummel")
def improvised_pummel():
	return render_template("improvised-pummel.html")

@app.route("/makeshift-strike")
def makeshift_strike():
	return render_template("makeshift-strike.html")

@app.route("/oversized-throw")
def oversized_throw():
	return render_template("oversized-throw.html")

@app.route("/shattering-strike-3539424")
def shattering_strike_3539424():
	return render_template("shattering-strike-3539424.html")

@app.route("/surprise-strike")
def surprise_strike():
	return render_template("surprise-strike.html")

@app.route("/fanes-fourberie")
def fanes_fourberie():
	return render_template("fanes-fourberie.html")

@app.route("/archers-aim")
def archers_aim():
	return render_template("archers-aim.html")

@app.route("/arrow-of-death")
def arrow_of_death():
	return render_template("arrow-of-death.html")

@app.route("/press")
def press():
	return render_template("press.html")

@app.route("/assisting-shot")
def assisting_shot():
	return render_template("assisting-shot.html")

@app.route("/bullseye")
def bullseye():
	return render_template("bullseye.html")

@app.route("/crossbow-terror")
def crossbow_terror():
	return render_template("crossbow-terror.html")

@app.route("/debilitating-shot")
def debilitating_shot():
	return render_template("debilitating-shot.html")

@app.route("/double-shot")
def double_shot():
	return render_template("double-shot.html")

@app.route("/enchanting-arrow")
def enchanting_arrow():
	return render_template("enchanting-arrow.html")

@app.route("/far-shot")
def far_shot():
	return render_template("far-shot.html")

@app.route("/far-throw")
def far_throw():
	return render_template("far-throw.html")

@app.route("/forceful-shot")
def forceful_shot():
	return render_template("forceful-shot.html")

@app.route("/impossible-volley")
def impossible_volley():
	return render_template("impossible-volley.html")

@app.route("/incredible-ricochet")
def incredible_ricochet():
	return render_template("incredible-ricochet.html")

@app.route("/incredible-aim")
def incredible_aim():
	return render_template("incredible-aim.html")

@app.route("/lobbed-attack")
def lobbed_attack():
	return render_template("lobbed-attack.html")

@app.route("/viper-eldritch-arrow")
def viper_eldritch_arrow():
	return render_template("viper-eldritch-arrow.html")

@app.route("/shining-eldritch-arrow")
def shining_eldritch_arrow():
	return render_template("shining-eldritch-arrow.html")

@app.route("/beacon-shot-eldritch-arrow")
def beacon_shot_eldritch_arrow():
	return render_template("beacon-shot-eldritch-arrow.html")

@app.route("/antler-eldritch-arrow")
def antler_eldritch_arrow():
	return render_template("antler-eldritch-arrow.html")

@app.route("/vine-eldritch-arrow")
def vine_eldritch_arrow():
	return render_template("vine-eldritch-arrow.html")

@app.route("/climbing-bolt-eldritch-arrow")
def climbing_bolt_eldritch_arrow():
	return render_template("climbing-bolt-eldritch-arrow.html")

@app.route("/triple-shot")
def triple_shot():
	return render_template("triple-shot.html")

@app.route("/multishot-stance")
def multishot_stance():
	return render_template("multishot-stance.html")

@app.route("/mobile-shot-stance")
def mobile_shot_stance():
	return render_template("mobile-shot-stance.html")

@app.route("/opportune-throw")
def opportune_throw():
	return render_template("opportune-throw.html")

@app.route("/parting-shot")
def parting_shot():
	return render_template("parting-shot.html")

@app.route("/penetrating-projectile")
def penetrating_projectile():
	return render_template("penetrating-projectile.html")

@app.route("/perfect-shot")
def perfect_shot():
	return render_template("perfect-shot.html")

@app.route("/phase-arrow")
def phase_arrow():
	return render_template("phase-arrow.html")

@app.route("/point-blank-shot")
def point_blank_shot():
	return render_template("point-blank-shot.html")

@app.route("/precious-arrow")
def precious_arrow():
	return render_template("precious-arrow.html")

@app.route("/quick-shot")
def quick_shot():
	return render_template("quick-shot.html")

@app.route("/rebounding-toss")
def rebounding_toss():
	return render_template("rebounding-toss.html")

@app.route("/shootists-draw")
def shootists_draw():
	return render_template("shootists-draw.html")

@app.route("/repeating-hand-crossbow")
def repeating_hand_crossbow():
	return render_template("repeating-hand-crossbow.html")

@app.route("/ricochet-stance")
def ricochet_stance():
	return render_template("ricochet-stance.html")

@app.route("/ricochet-feint")
def ricochet_feint():
	return render_template("ricochet-feint.html")

@app.route("/running-reload")
def running_reload():
	return render_template("running-reload.html")

@app.route("/seeker-arrow")
def seeker_arrow():
	return render_template("seeker-arrow.html")

@app.route("/strong-arm")
def strong_arm():
	return render_template("strong-arm.html")

@app.route("/aggressive-block")
def aggressive_block():
	return render_template("aggressive-block.html")

@app.route("/buckler-expertise")
def buckler_expertise():
	return render_template("buckler-expertise.html")

@app.route("/buckler-dance")
def buckler_dance():
	return render_template("buckler-dance.html")

@app.route("/destructive-block")
def destructive_block():
	return render_template("destructive-block.html")

@app.route("/disarming-block")
def disarming_block():
	return render_template("disarming-block.html")

@app.route("/divine-shield-wall")
def divine_shield_wall():
	return render_template("divine-shield-wall.html")

@app.route("/everstand-stance")
def everstand_stance():
	return render_template("everstand-stance.html")

@app.route("/everstand-strike")
def everstand_strike():
	return render_template("everstand-strike.html")

@app.route("/reflexive-shield")
def reflexive_shield():
	return render_template("reflexive-shield.html")

@app.route("/improved-reflexive-shield")
def improved_reflexive_shield():
	return render_template("improved-reflexive-shield.html")

@app.route("/nimble-shield-hand")
def nimble_shield_hand():
	return render_template("nimble-shield-hand.html")

@app.route("/defend")
def defend():
	return render_template("defend.html")

@app.route("/practiced-defender")
def practiced_defender():
	return render_template("practiced-defender.html")

@app.route("/quick-block")
def quick_block():
	return render_template("quick-block.html")

@app.route("/reactive-shield")
def reactive_shield():
	return render_template("reactive-shield.html")

@app.route("/rescuers-press")
def rescuers_press():
	return render_template("rescuers-press.html")

@app.route("/second-shield")
def second_shield():
	return render_template("second-shield.html")

@app.route("/shield-of-grace")
def shield_of_grace():
	return render_template("shield-of-grace.html")

@app.route("/shield-salvation")
def shield_salvation():
	return render_template("shield-salvation.html")

@app.route("/paragons-guard")
def paragons_guard():
	return render_template("paragons-guard.html")

@app.route("/shield-of-reckoning")
def shield_of_reckoning():
	return render_template("shield-of-reckoning.html")

@app.route("/shielded-stride")
def shielded_stride():
	return render_template("shielded-stride.html")

@app.route("/disarming-stance")
def disarming_stance():
	return render_template("disarming-stance.html")

@app.route("/disarming-twist")
def disarming_twist():
	return render_template("disarming-twist.html")

@app.route("/flourish")
def flourish():
	return render_template("flourish.html")

@app.route("/two-handed")
def two_handed():
	return render_template("two-handed.html")

@app.route("/dual-handed-assault")
def dual_handed_assault():
	return render_template("dual-handed-assault.html")

@app.route("/dueling-parry")
def dueling_parry():
	return render_template("dueling-parry.html")

@app.route("/dueling-dance")
def dueling_dance():
	return render_template("dueling-dance.html")

@app.route("/dueling-reposte")
def dueling_reposte():
	return render_template("dueling-reposte.html")

@app.route("/duelists-challenge")
def duelists_challenge():
	return render_template("duelists-challenge.html")

@app.route("/duelists-edge")
def duelists_edge():
	return render_template("duelists-edge.html")

@app.route("/guardians-deflection")
def guardians_deflection():
	return render_template("guardians-deflection.html")

@app.route("/guiding-finish")
def guiding_finish():
	return render_template("guiding-finish.html")

@app.route("/guiding-reposte")
def guiding_reposte():
	return render_template("guiding-reposte.html")

@app.route("/improved-dueling-reposte")
def improved_dueling_reposte():
	return render_template("improved-dueling-reposte.html")

@app.route("/saving-slash")
def saving_slash():
	return render_template("saving-slash.html")

@app.route("/selfless-parry")
def selfless_parry():
	return render_template("selfless-parry.html")

@app.route("/student-of-the-dueling-arts")
def student_of_the_dueling_arts():
	return render_template("student-of-the-dueling-arts.html")

@app.route("/unnerving-prowess")
def unnerving_prowess():
	return render_template("unnerving-prowess.html")

@app.route("/avalanche-strike")
def avalanche_strike():
	return render_template("avalanche-strike.html")

@app.route("/clear-the-way")
def clear_the_way():
	return render_template("clear-the-way.html")

@app.route("/hammer-quake")
def hammer_quake():
	return render_template("hammer-quake.html")

@app.route("/shoving-sweep")
def shoving_sweep():
	return render_template("shoving-sweep.html")

@app.route("/positioning-assault")
def positioning_assault():
	return render_template("positioning-assault.html")

@app.route("/impossible-flurry")
def impossible_flurry():
	return render_template("impossible-flurry.html")

@app.route("/accurate-flurry")
def accurate_flurry():
	return render_template("accurate-flurry.html")

@app.route("/double-slice")
def double_slice():
	return render_template("double-slice.html")

@app.route("/dual-onslaught")
def dual_onslaught():
	return render_template("dual-onslaught.html")

@app.route("/dual-thrower")
def dual_thrower():
	return render_template("dual-thrower.html")

@app.route("/dual-weapon-reload")
def dual_weapon_reload():
	return render_template("dual-weapon-reload.html")

@app.route("/flensing-slice")
def flensing_slice():
	return render_template("flensing-slice.html")

@app.route("/graceful-poise")
def graceful_poise():
	return render_template("graceful-poise.html")

@app.route("/twin-parry")
def twin_parry():
	return render_template("twin-parry.html")

@app.route("/twin-reposte-939707")
def twin_reposte_939707():
	return render_template("twin-reposte-939707.html")

@app.route("/improved-twin-reposte")
def improved_twin_reposte():
	return render_template("improved-twin-reposte.html")

@app.route("/twinned-defense")
def twinned_defense():
	return render_template("twinned-defense.html")

@app.route("/two-weapon-flurry")
def two_weapon_flurry():
	return render_template("two-weapon-flurry.html")

@app.route("/flinging-shove")
def flinging_shove():
	return render_template("flinging-shove.html")

@app.route("/powerful-shove")
def powerful_shove():
	return render_template("powerful-shove.html")

@app.route("/hurling-charge")
def hurling_charge():
	return render_template("hurling-charge.html")

@app.route("/quick-stow-1658530")
def quick_stow_1658530():
	return render_template("quick-stow-1658530.html")

@app.route("/brutality")
def brutality():
	return render_template("brutality.html")

@app.route("/exotic-weapon-training")
def exotic_weapon_training():
	return render_template("exotic-weapon-training.html")

@app.route("/stage-fighting")
def stage_fighting():
	return render_template("stage-fighting.html")

@app.route("/agile-grace")
def agile_grace():
	return render_template("agile-grace.html")

@app.route("/axe-thrower")
def axe_thrower():
	return render_template("axe-thrower.html")

@app.route("/staff-acrobat")
def staff_acrobat():
	return render_template("staff-acrobat.html")

@app.route("/pivot-strike")
def pivot_strike():
	return render_template("pivot-strike.html")

@app.route("/weapon-proficiency")
def weapon_proficiency():
	return render_template("weapon-proficiency.html")

@app.route("/whirlwind-staff")
def whirlwind_staff():
	return render_template("whirlwind-staff.html")

@app.route("/widen-the-gap")
def widen_the_gap():
	return render_template("widen-the-gap.html")

@app.route("/reloading-trick")
def reloading_trick():
	return render_template("reloading-trick.html")

@app.route("/shield-warden")
def shield_warden():
	return render_template("shield-warden.html")

@app.route("/brutish-shove")
def brutish_shove():
	return render_template("brutish-shove.html")

@app.route("/dual-weapon-blitz")
def dual_weapon_blitz():
	return render_template("dual-weapon-blitz.html")

@app.route("/brutal-finish")
def brutal_finish():
	return render_template("brutal-finish.html")

@app.route("/twin-feint")
def twin_feint():
	return render_template("twin-feint.html")

@app.route("/twin-distraction")
def twin_distraction():
	return render_template("twin-distraction.html")

@app.route("/levering-strike")
def levering_strike():
	return render_template("levering-strike.html")

@app.route("/staff-sweep")
def staff_sweep():
	return render_template("staff-sweep.html")

@app.route("/bullying-staff")
def bullying_staff():
	return render_template("bullying-staff.html")

@app.route("/infectious-enthusiasm")
def infectious_enthusiasm():
	return render_template("infectious-enthusiasm.html")

@app.route("/puff-of-poison")
def puff_of_poison():
	return render_template("puff-of-poison.html")

@app.route("/acid-splash")
def acid_splash():
	return render_template("acid-splash.html")

@app.route("/chill-touch")
def chill_touch():
	return render_template("chill-touch.html")

@app.route("/dancing-lights")
def dancing_lights():
	return render_template("dancing-lights.html")

@app.route("/daze")
def daze():
	return render_template("daze.html")

@app.route("/bullhorn")
def bullhorn():
	return render_template("bullhorn.html")

@app.route("/detect-magic-9339784")
def detect_magic_9339784():
	return render_template("detect-magic-9339784.html")

@app.route("/electric-arc")
def electric_arc():
	return render_template("electric-arc.html")

@app.route("/gale-blast")
def gale_blast():
	return render_template("gale-blast.html")

@app.route("/ghost-sound")
def ghost_sound():
	return render_template("ghost-sound.html")

@app.route("/gouging-claw")
def gouging_claw():
	return render_template("gouging-claw.html")

@app.route("/light-224996")
def light_224996():
	return render_template("light-224996.html")

@app.route("/mage-hand")
def mage_hand():
	return render_template("mage-hand.html")

@app.route("/message")
def message():
	return render_template("message.html")

@app.route("/produce-flame")
def produce_flame():
	return render_template("produce-flame.html")

@app.route("/ray-of-frost")
def ray_of_frost():
	return render_template("ray-of-frost.html")

@app.route("/read-aura")
def read_aura():
	return render_template("read-aura.html")

@app.route("/scatter-scree")
def scatter_scree():
	return render_template("scatter-scree.html")

@app.route("/shield")
def shield():
	return render_template("shield.html")

@app.route("/sigil")
def sigil():
	return render_template("sigil.html")

@app.route("/spout")
def spout():
	return render_template("spout.html")

@app.route("/tanglefoot")
def tanglefoot():
	return render_template("tanglefoot.html")

@app.route("/telekinetic-projectile")
def telekinetic_projectile():
	return render_template("telekinetic-projectile.html")

@app.route("/disrupt-undead")
def disrupt_undead():
	return render_template("disrupt-undead.html")

@app.route("/divine-lance")
def divine_lance():
	return render_template("divine-lance.html")

@app.route("/forbidding-ward")
def forbidding_ward():
	return render_template("forbidding-ward.html")

@app.route("/guidance")
def guidance():
	return render_template("guidance.html")

@app.route("/haunting-hymn")
def haunting_hymn():
	return render_template("haunting-hymn.html")

@app.route("/know-direction")
def know_direction():
	return render_template("know-direction.html")

@app.route("/read-the-air")
def read_the_air():
	return render_template("read-the-air.html")

@app.route("/stabilize")
def stabilize():
	return render_template("stabilize.html")

@app.route("/wash-your-luck")
def wash_your_luck():
	return render_template("wash-your-luck.html")

@app.route("/protect-companion")
def protect_companion():
	return render_template("protect-companion.html")

@app.route("/tame")
def tame():
	return render_template("tame.html")

@app.route("/join-pasts")
def join_pasts():
	return render_template("join-pasts.html")

@app.route("/disbelieving-illusions")
def disbelieving_illusions():
	return render_template("disbelieving-illusions.html")

@app.route("/power-lift")
def power_lift():
	return render_template("power-lift.html")

@app.route("/athletics-str")
def athletics_str():
	return render_template("athletics-str.html")

@app.route("/elemental-zone")
def elemental_zone():
	return render_template("elemental-zone.html")

@app.route("/misdirection")
def misdirection():
	return render_template("misdirection.html")

@app.route("/identifying-spells")
def identifying_spells():
	return render_template("identifying-spells.html")

@app.route("/animal-messenger")
def animal_messenger():
	return render_template("animal-messenger.html")

@app.route("/animus-mine")
def animus_mine():
	return render_template("animus-mine.html")

@app.route("/augury")
def augury():
	return render_template("augury.html")

@app.route("/barkskin")
def barkskin():
	return render_template("barkskin.html")

@app.route("/befitting-attire")
def befitting_attire():
	return render_template("befitting-attire.html")

@app.route("/blistering-invective")
def blistering_invective():
	return render_template("blistering-invective.html")

@app.route("/blood-vendetta")
def blood_vendetta():
	return render_template("blood-vendetta.html")

@app.route("/blur")
def blur():
	return render_template("blur.html")

@app.route("/brand-the-impenitent")
def brand_the_impenitent():
	return render_template("brand-the-impenitent.html")

@app.route("/charitable-urge")
def charitable_urge():
	return render_template("charitable-urge.html")

@app.route("/comprehend-language")
def comprehend_language():
	return render_template("comprehend-language.html")

@app.route("/continual-flame")
def continual_flame():
	return render_template("continual-flame.html")

@app.route("/darkness")
def darkness():
	return render_template("darkness.html")

@app.route("/deafness-3457243")
def deafness_3457243():
	return render_template("deafness-3457243.html")

@app.route("/dismantle")
def dismantle():
	return render_template("dismantle.html")

@app.route("/dispel-magic")
def dispel_magic():
	return render_template("dispel-magic.html")

@app.route("/endure-elements")
def endure_elements():
	return render_template("endure-elements.html")

@app.route("/enlarge")
def enlarge():
	return render_template("enlarge.html")

@app.route("/expeditious-excavation")
def expeditious_excavation():
	return render_template("expeditious-excavation.html")

@app.route("/extract-poison")
def extract_poison():
	return render_template("extract-poison.html")

@app.route("/false-life")
def false_life():
	return render_template("false-life.html")

@app.route("/fear-the-sun")
def fear_the_sun():
	return render_template("fear-the-sun.html")

@app.route("/feast-of-ashes")
def feast_of_ashes():
	return render_template("feast-of-ashes.html")

@app.route("/final-sacrifice")
def final_sacrifice():
	return render_template("final-sacrifice.html")

@app.route("/flame-wisp")
def flame_wisp():
	return render_template("flame-wisp.html")

@app.route("/gentle-repose")
def gentle_repose():
	return render_template("gentle-repose.html")

@app.route("/glitterdust")
def glitterdust():
	return render_template("glitterdust.html")

@app.route("/heat-metal")
def heat_metal():
	return render_template("heat-metal.html")

@app.route("/hideous-laughter")
def hideous_laughter():
	return render_template("hideous-laughter.html")

@app.route("/humanoid-form")
def humanoid_form():
	return render_template("humanoid-form.html")

@app.route("/ignite-fireworks")
def ignite_fireworks():
	return render_template("ignite-fireworks.html")

@app.route("/illusory-creature")
def illusory_creature():
	return render_template("illusory-creature.html")

@app.route("/breath-of-drought")
def breath_of_drought():
	return render_template("breath-of-drought.html")

@app.route("/calm-emotions")
def calm_emotions():
	return render_template("calm-emotions.html")

@app.route("/clawsong")
def clawsong():
	return render_template("clawsong.html")

@app.route("/enhance-victuals")
def enhance_victuals():
	return render_template("enhance-victuals.html")

@app.route("/entangle")
def entangle():
	return render_template("entangle.html")

@app.route("/fungal-hyphae")
def fungal_hyphae():
	return render_template("fungal-hyphae.html")

@app.route("/ghoulish-cravings")
def ghoulish_cravings():
	return render_template("ghoulish-cravings.html")

@app.route("/grave-impressions")
def grave_impressions():
	return render_template("grave-impressions.html")

@app.route("/guiding-star")
def guiding_star():
	return render_template("guiding-star.html")

@app.route("/impeccable-flow")
def impeccable_flow():
	return render_template("impeccable-flow.html")

@app.route("/instant-armor")
def instant_armor():
	return render_template("instant-armor.html")

@app.route("/invisibility")
def invisibility():
	return render_template("invisibility.html")

@app.route("/iron-gut")
def iron_gut():
	return render_template("iron-gut.html")

@app.route("/lucky-number")
def lucky_number():
	return render_template("lucky-number.html")

@app.route("/magic-mouth")
def magic_mouth():
	return render_template("magic-mouth.html")

@app.route("/magnetic-attraction")
def magnetic_attraction():
	return render_template("magnetic-attraction.html")

@app.route("/magnetic-repulsion")
def magnetic_repulsion():
	return render_template("magnetic-repulsion.html")

@app.route("/mimic-undead")
def mimic_undead():
	return render_template("mimic-undead.html")

@app.route("/mind-games")
def mind_games():
	return render_template("mind-games.html")

@app.route("/obscuring-mist")
def obscuring_mist():
	return render_template("obscuring-mist.html")

@app.route("/paranoia-1770706")
def paranoia_1770706():
	return render_template("paranoia-1770706.html")

@app.route("/penumbral-disguise")
def penumbral_disguise():
	return render_template("penumbral-disguise.html")

@app.route("/persistent-servant")
def persistent_servant():
	return render_template("persistent-servant.html")

@app.route("/phantasmal-treasure")
def phantasmal_treasure():
	return render_template("phantasmal-treasure.html")

@app.route("/phantom-crowd")
def phantom_crowd():
	return render_template("phantom-crowd.html")

@app.route("/remove-paralysis")
def remove_paralysis():
	return render_template("remove-paralysis.html")

@app.route("/resist-energy")
def resist_energy():
	return render_template("resist-energy.html")

@app.route("/restoration")
def restoration():
	return render_template("restoration.html")

@app.route("/restore-senses")
def restore_senses():
	return render_template("restore-senses.html")

@app.route("/sea-surge")
def sea_surge():
	return render_template("sea-surge.html")

@app.route("/see-invisibility")
def see_invisibility():
	return render_template("see-invisibility.html")

@app.route("/shatter")
def shatter():
	return render_template("shatter.html")

@app.route("/shield-other")
def shield_other():
	return render_template("shield-other.html")

@app.route("/shrink")
def shrink():
	return render_template("shrink.html")

@app.route("/silence")
def silence():
	return render_template("silence.html")

@app.route("/slough-skin")
def slough_skin():
	return render_template("slough-skin.html")

@app.route("/sonata-span")
def sonata_span():
	return render_template("sonata-span.html")

@app.route("/speak-with-animals")
def speak_with_animals():
	return render_template("speak-with-animals.html")

@app.route("/spectral-hand")
def spectral_hand():
	return render_template("spectral-hand.html")

@app.route("/spider-climb")
def spider_climb():
	return render_template("spider-climb.html")

@app.route("/spirit-sense")
def spirit_sense():
	return render_template("spirit-sense.html")

@app.route("/spiritual-weapon")
def spiritual_weapon():
	return render_template("spiritual-weapon.html")

@app.route("/status")
def status():
	return render_template("status.html")

@app.route("/sudden-blight")
def sudden_blight():
	return render_template("sudden-blight.html")

@app.route("/sudden-bolt")
def sudden_bolt():
	return render_template("sudden-bolt.html")

@app.route("/telekinetic-manuever")
def telekinetic_manuever():
	return render_template("telekinetic-manuever.html")

@app.route("/thundering-dominance")
def thundering_dominance():
	return render_template("thundering-dominance.html")

@app.route("/timely-tutor")
def timely_tutor():
	return render_template("timely-tutor.html")

@app.route("/touch-of-idiocy")
def touch_of_idiocy():
	return render_template("touch-of-idiocy.html")

@app.route("/tree-shape")
def tree_shape():
	return render_template("tree-shape.html")

@app.route("/umbral-extraction")
def umbral_extraction():
	return render_template("umbral-extraction.html")

@app.route("/undetectable-alignment")
def undetectable_alignment():
	return render_template("undetectable-alignment.html")

@app.route("/vomit-swarm")
def vomit_swarm():
	return render_template("vomit-swarm.html")

@app.route("/warriors-regret")
def warriors_regret():
	return render_template("warriors-regret.html")

@app.route("/water-breathing")
def water_breathing():
	return render_template("water-breathing.html")

@app.route("/water-walk")
def water_walk():
	return render_template("water-walk.html")

@app.route("/web")
def web():
	return render_template("web.html")

@app.route("/acidic-burst")
def acidic_burst():
	return render_template("acidic-burst.html")

@app.route("/air-bubble")
def air_bubble():
	return render_template("air-bubble.html")

@app.route("/airburst")
def airburst():
	return render_template("airburst.html")

@app.route("/alarm")
def alarm():
	return render_template("alarm.html")

@app.route("/animate-rope")
def animate_rope():
	return render_template("animate-rope.html")

@app.route("/ant-haul")
def ant_haul():
	return render_template("ant-haul.html")

@app.route("/anticipate-peril")
def anticipate_peril():
	return render_template("anticipate-peril.html")

@app.route("/bane")
def bane():
	return render_template("bane.html")

@app.route("/bless")
def bless():
	return render_template("bless.html")

@app.route("/befuddle")
def befuddle():
	return render_template("befuddle.html")

@app.route("/breadcrumbs")
def breadcrumbs():
	return render_template("breadcrumbs.html")

@app.route("/charm")
def charm():
	return render_template("charm.html")

@app.route("/color-spray")
def color_spray():
	return render_template("color-spray.html")

@app.route("/command")
def command():
	return render_template("command.html")

@app.route("/deja-vu")
def deja_vu():
	return render_template("deja-vu.html")

@app.route("/detect-alignment")
def detect_alignment():
	return render_template("detect-alignment.html")

@app.route("/detect-poison")
def detect_poison():
	return render_template("detect-poison.html")

@app.route("/disrupting-weapons")
def disrupting_weapons():
	return render_template("disrupting-weapons.html")

@app.route("/echoing-weapon")
def echoing_weapon():
	return render_template("echoing-weapon.html")

@app.route("/endure")
def endure():
	return render_template("endure.html")

@app.route("/illusory-disguise")
def illusory_disguise():
	return render_template("illusory-disguise.html")

@app.route("/exchange-image")
def exchange_image():
	return render_template("exchange-image.html")

@app.route("/fear-8000793")
def fear_8000793():
	return render_template("fear-8000793.html")

@app.route("/feather-fall")
def feather_fall():
	return render_template("feather-fall.html")

@app.route("/fleet-step")
def fleet_step():
	return render_template("fleet-step.html")

@app.route("/floating-disk")
def floating_disk():
	return render_template("floating-disk.html")

@app.route("/friendfetch")
def friendfetch():
	return render_template("friendfetch.html")

@app.route("/goblin-pox")
def goblin_pox():
	return render_template("goblin-pox.html")

@app.route("/gravitational-pull")
def gravitational_pull():
	return render_template("gravitational-pull.html")

@app.route("/grease")
def grease():
	return render_template("grease.html")

@app.route("/gust-of-wind")
def gust_of_wind():
	return render_template("gust-of-wind.html")

@app.route("/ill-omen")
def ill_omen():
	return render_template("ill-omen.html")

@app.route("/illusory-object")
def illusory_object():
	return render_template("illusory-object.html")

@app.route("/invisible-item")
def invisible_item():
	return render_template("invisible-item.html")

@app.route("/item-facade")
def item_facade():
	return render_template("item-facade.html")

@app.route("/jump")
def jump():
	return render_template("jump.html")

@app.route("/juvenile-companion")
def juvenile_companion():
	return render_template("juvenile-companion.html")

@app.route("/liberating-command")
def liberating_command():
	return render_template("liberating-command.html")

@app.route("/lock")
def lock():
	return render_template("lock.html")

@app.route("/longstrider")
def longstrider():
	return render_template("longstrider.html")

@app.route("/lose-the-path")
def lose_the_path():
	return render_template("lose-the-path.html")

@app.route("/mage-armor")
def mage_armor():
	return render_template("mage-armor.html")

@app.route("/magic-aura")
def magic_aura():
	return render_template("magic-aura.html")

@app.route("/magic-missile")
def magic_missile():
	return render_template("magic-missile.html")

@app.route("/magic-stone")
def magic_stone():
	return render_template("magic-stone.html")

@app.route("/magic-weapon")
def magic_weapon():
	return render_template("magic-weapon.html")

@app.route("/magic-fang")
def magic_fang():
	return render_template("magic-fang.html")

@app.route("/mending")
def mending():
	return render_template("mending.html")

@app.route("/message-rune")
def message_rune():
	return render_template("message-rune.html")

@app.route("/mindlink")
def mindlink():
	return render_template("mindlink.html")

@app.route("/mud-pit")
def mud_pit():
	return render_template("mud-pit.html")

@app.route("/necromancers-generosity")
def necromancers_generosity():
	return render_template("necromancers-generosity.html")

@app.route("/negate-aroma")
def negate_aroma():
	return render_template("negate-aroma.html")

@app.route("/nudge-the-odds")
def nudge_the_odds():
	return render_template("nudge-the-odds.html")

@app.route("/object-reading")
def object_reading():
	return render_template("object-reading.html")

@app.route("/pass-without-trace")
def pass_without_trace():
	return render_template("pass-without-trace.html")

@app.route("/penumbral-shroud")
def penumbral_shroud():
	return render_template("penumbral-shroud.html")

@app.route("/personal-rain-cloud")
def personal_rain_cloud():
	return render_template("personal-rain-cloud.html")

@app.route("/pet-cache")
def pet_cache():
	return render_template("pet-cache.html")

@app.route("/pocket-library")
def pocket_library():
	return render_template("pocket-library.html")

@app.route("/protection")
def protection():
	return render_template("protection.html")

@app.route("/protector-tree")
def protector_tree():
	return render_template("protector-tree.html")

@app.route("/purify-food-and-drink")
def purify_food_and_drink():
	return render_template("purify-food-and-drink.html")

@app.route("/putrefy-food-and-drink")
def putrefy_food_and_drink():
	return render_template("putrefy-food-and-drink.html")

@app.route("/quick-sort")
def quick_sort():
	return render_template("quick-sort.html")

@app.route("/ray-of-enfeeblement")
def ray_of_enfeeblement():
	return render_template("ray-of-enfeeblement.html")

@app.route("/restyle")
def restyle():
	return render_template("restyle.html")

@app.route("/sanctuary")
def sanctuary():
	return render_template("sanctuary.html")

@app.route("/scouring-sand")
def scouring_sand():
	return render_template("scouring-sand.html")

@app.route("/seashell-of-stolen-sound")
def seashell_of_stolen_sound():
	return render_template("seashell-of-stolen-sound.html")

@app.route("/share-lore")
def share_lore():
	return render_template("share-lore.html")

@app.route("/shattering-gem")
def shattering_gem():
	return render_template("shattering-gem.html")

@app.route("/shillelagh")
def shillelagh():
	return render_template("shillelagh.html")

@app.route("/shockwave")
def shockwave():
	return render_template("shockwave.html")

@app.route("/sleep")
def sleep():
	return render_template("sleep.html")

@app.route("/spirit-link")
def spirit_link():
	return render_template("spirit-link.html")

@app.route("/swampcall")
def swampcall():
	return render_template("swampcall.html")

@app.route("/synchronize")
def synchronize():
	return render_template("synchronize.html")

@app.route("/temporary-tool")
def temporary_tool():
	return render_template("temporary-tool.html")

@app.route("/tether")
def tether():
	return render_template("tether.html")

@app.route("/thicket-of-knives")
def thicket_of_knives():
	return render_template("thicket-of-knives.html")

@app.route("/thoughtful-gift")
def thoughtful_gift():
	return render_template("thoughtful-gift.html")

@app.route("/true-strike")
def true_strike():
	return render_template("true-strike.html")

@app.route("/unseen-servant")
def unseen_servant():
	return render_template("unseen-servant.html")

@app.route("/ventriloquism")
def ventriloquism():
	return render_template("ventriloquism.html")

@app.route("/verdant-sprout")
def verdant_sprout():
	return render_template("verdant-sprout.html")

@app.route("/verminous-lure")
def verminous_lure():
	return render_template("verminous-lure.html")

@app.route("/create-food")
def create_food():
	return render_template("create-food.html")

@app.route("/create-water")
def create_water():
	return render_template("create-water.html")

@app.route("/faerie-fire")
def faerie_fire():
	return render_template("faerie-fire.html")

@app.route("/fungal-infestation")
def fungal_infestation():
	return render_template("fungal-infestation.html")

@app.route("/death-knell")
def death_knell():
	return render_template("death-knell.html")

@app.route("/mirror-image")
def mirror_image():
	return render_template("mirror-image.html")

@app.route("/schadenfreude")
def schadenfreude():
	return render_template("schadenfreude.html")

@app.route("/shape-wood")
def shape_wood():
	return render_template("shape-wood.html")

@app.route("/force-bolt")
def force_bolt():
	return render_template("force-bolt.html")

@app.route("/elemental-tempest")
def elemental_tempest():
	return render_template("elemental-tempest.html")

@app.route("/arcana-feats")
def arcana_feats():
	return render_template("arcana-feats.html")

@app.route("/spider-sting")
def spider_sting():
	return render_template("spider-sting.html")

@app.route("/acid-arrow")
def acid_arrow():
	return render_template("acid-arrow.html")

@app.route("/admonishing-ray")
def admonishing_ray():
	return render_template("admonishing-ray.html")

@app.route("/agitate")
def agitate():
	return render_template("agitate.html")

@app.route("/animal-allies-9723296")
def animal_allies_9723296():
	return render_template("animal-allies-9723296.html")

@app.route("/animated-assault")
def animated_assault():
	return render_template("animated-assault.html")

@app.route("/ash-cloud")
def ash_cloud():
	return render_template("ash-cloud.html")

@app.route("/biting-words")
def biting_words():
	return render_template("biting-words.html")

@app.route("/burning-hands")
def burning_hands():
	return render_template("burning-hands.html")

@app.route("/chilling-spray")
def chilling_spray():
	return render_template("chilling-spray.html")

@app.route("/concordant-choir")
def concordant_choir():
	return render_template("concordant-choir.html")

@app.route("/draw-ire")
def draw_ire():
	return render_template("draw-ire.html")

@app.route("/feral-shades")
def feral_shades():
	return render_template("feral-shades.html")

@app.route("/flaming-sphere")
def flaming_sphere():
	return render_template("flaming-sphere.html")

@app.route("/grim-tendrils")
def grim_tendrils():
	return render_template("grim-tendrils.html")

@app.route("/horizon-thunder-sphere")
def horizon_thunder_sphere():
	return render_template("horizon-thunder-sphere.html")

@app.route("/hydraulic-push")
def hydraulic_push():
	return render_template("hydraulic-push.html")

@app.route("/imp-sting")
def imp_sting():
	return render_template("imp-sting.html")

@app.route("/noxious-vapors")
def noxious_vapors():
	return render_template("noxious-vapors.html")

@app.route("/phantom-pain")
def phantom_pain():
	return render_template("phantom-pain.html")

@app.route("/rime-slick")
def rime_slick():
	return render_template("rime-slick.html")

@app.route("/scorching-ray")
def scorching_ray():
	return render_template("scorching-ray.html")

@app.route("/shocking-grasp-91486")
def shocking_grasp_91486():
	return render_template("shocking-grasp-91486.html")

@app.route("/snowball")
def snowball():
	return render_template("snowball.html")

@app.route("/sound-burst")
def sound_burst():
	return render_template("sound-burst.html")

@app.route("/worms-repast")
def worms_repast():
	return render_template("worms-repast.html")

@app.route("/bottomless-stomach")
def bottomless_stomach():
	return render_template("bottomless-stomach.html")

@app.route("/harm")
def harm():
	return render_template("harm.html")

@app.route("/agonizing-despair")
def agonizing_despair():
	return render_template("agonizing-despair.html")

@app.route("/air-walk")
def air_walk():
	return render_template("air-walk.html")

@app.route("/anathemic-reprisal")
def anathemic_reprisal():
	return render_template("anathemic-reprisal.html")

@app.route("/animal-vision")
def animal_vision():
	return render_template("animal-vision.html")

@app.route("/aqueous-orb")
def aqueous_orb():
	return render_template("aqueous-orb.html")

@app.route("/aromatic-lure")
def aromatic_lure():
	return render_template("aromatic-lure.html")

@app.route("/bestial-curse")
def bestial_curse():
	return render_template("bestial-curse.html")

@app.route("/call-the-blood")
def call_the_blood():
	return render_template("call-the-blood.html")

@app.route("/chroma-leach")
def chroma_leach():
	return render_template("chroma-leach.html")

@app.route("/chromatic-armor")
def chromatic_armor():
	return render_template("chromatic-armor.html")

@app.route("/chilling-darkness")
def chilling_darkness():
	return render_template("chilling-darkness.html")

@app.route("/claim-curse")
def claim_curse():
	return render_template("claim-curse.html")

@app.route("/circle-of-protection")
def circle_of_protection():
	return render_template("circle-of-protection.html")

@app.route("/clairaudience")
def clairaudience():
	return render_template("clairaudience.html")

@app.route("/clairvoyance")
def clairvoyance():
	return render_template("clairvoyance.html")

@app.route("/cloak-of-light")
def cloak_of_light():
	return render_template("cloak-of-light.html")

@app.route("/hazardous-terrain")
def hazardous_terrain():
	return render_template("hazardous-terrain.html")

@app.route("/structure")
def structure():
	return render_template("structure.html")

@app.route("/cup-of-dust")
def cup_of_dust():
	return render_template("cup-of-dust.html")

@app.route("/daydreamers-curse")
def daydreamers_curse():
	return render_template("daydreamers-curse.html")

@app.route("/clownish-curse")
def clownish_curse():
	return render_template("clownish-curse.html")

@app.route("/confusion")
def confusion():
	return render_template("confusion.html")

@app.route("/coral-eruption")
def coral_eruption():
	return render_template("coral-eruption.html")

@app.route("/countless-eyes")
def countless_eyes():
	return render_template("countless-eyes.html")

@app.route("/cozy-cabin")
def cozy_cabin():
	return render_template("cozy-cabin.html")

@app.route("/crashing-wave")
def crashing_wave():
	return render_template("crashing-wave.html")

@app.route("/creation")
def creation():
	return render_template("creation.html")

@app.route("/crisis-of-faith")
def crisis_of_faith():
	return render_template("crisis-of-faith.html")

@app.route("/curse-of-lost-time")
def curse_of_lost_time():
	return render_template("curse-of-lost-time.html")

@app.route("/days-weight")
def days_weight():
	return render_template("days-weight.html")

@app.route("/detect-scrying")
def detect_scrying():
	return render_template("detect-scrying.html")

@app.route("/dimension-door")
def dimension_door():
	return render_template("dimension-door.html")

@app.route("/dimensional-anchor")
def dimensional_anchor():
	return render_template("dimensional-anchor.html")

@app.route("/discern-lies")
def discern_lies():
	return render_template("discern-lies.html")

@app.route("/distracting-chatter")
def distracting_chatter():
	return render_template("distracting-chatter.html")

@app.route("/divine-wrath")
def divine_wrath():
	return render_template("divine-wrath.html")

@app.route("/fireball")
def fireball():
	return render_template("fireball.html")

@app.route("/draw-the-lightning")
def draw_the_lightning():
	return render_template("draw-the-lightning.html")

@app.route("/dream-message")
def dream_message():
	return render_template("dream-message.html")

@app.route("/dull-ambition")
def dull_ambition():
	return render_template("dull-ambition.html")

@app.route("/earthbind")
def earthbind():
	return render_template("earthbind.html")

@app.route("/elemental-absorption")
def elemental_absorption():
	return render_template("elemental-absorption.html")

@app.route("/elemental-annihilation-wave")
def elemental_annihilation_wave():
	return render_template("elemental-annihilation-wave.html")

@app.route("/elemental-gift")
def elemental_gift():
	return render_template("elemental-gift.html")

@app.route("/enervation")
def enervation():
	return render_template("enervation.html")

@app.route("/enthrall")
def enthrall():
	return render_template("enthrall.html")

@app.route("/envenom-companion")
def envenom_companion():
	return render_template("envenom-companion.html")

@app.route("/sustain-a-spell")
def sustain_a_spell():
	return render_template("sustain-a-spell.html")

@app.route("/familiars-face")
def familiars_face():
	return render_template("familiars-face.html")

@app.route("/favorable-review")
def favorable_review():
	return render_template("favorable-review.html")

@app.route("/feet-to-fins")
def feet_to_fins():
	return render_template("feet-to-fins.html")

@app.route("/fire-shield")
def fire_shield():
	return render_template("fire-shield.html")

@app.route("/fly-9005114")
def fly_9005114():
	return render_template("fly-9005114.html")

@app.route("/forgotten-lines")
def forgotten_lines():
	return render_template("forgotten-lines.html")

@app.route("/gaseous-form")
def gaseous_form():
	return render_template("gaseous-form.html")

@app.route("/gasping-marsh")
def gasping_marsh():
	return render_template("gasping-marsh.html")

@app.route("/ghostly-weapon")
def ghostly_weapon():
	return render_template("ghostly-weapon.html")

@app.route("/girzanjes-march")
def girzanjes_march():
	return render_template("girzanjes-march.html")

@app.route("/glibness")
def glibness():
	return render_template("glibness.html")

@app.route("/globe-of-invulnerability")
def globe_of_invulnerability():
	return render_template("globe-of-invulnerability.html")

@app.route("/glyph-of-warding")
def glyph_of_warding():
	return render_template("glyph-of-warding.html")

@app.route("/gravity-well")
def gravity_well():
	return render_template("gravity-well.html")

@app.route("/ghostly-tragedy")
def ghostly_tragedy():
	return render_template("ghostly-tragedy.html")

@app.route("/hallucinatory-terrain")
def hallucinatory_terrain():
	return render_template("hallucinatory-terrain.html")

@app.route("/haste")
def haste():
	return render_template("haste.html")

@app.route("/heroism")
def heroism():
	return render_template("heroism.html")

@app.route("/holy-cascade")
def holy_cascade():
	return render_template("holy-cascade.html")

@app.route("/hydraulic-torrent")
def hydraulic_torrent():
	return render_template("hydraulic-torrent.html")

@app.route("/hypercognition")
def hypercognition():
	return render_template("hypercognition.html")

@app.route("/hypnotic-pattern")
def hypnotic_pattern():
	return render_template("hypnotic-pattern.html")

@app.route("/ice-storm")
def ice_storm():
	return render_template("ice-storm.html")

@app.route("/impending-doom")
def impending_doom():
	return render_template("impending-doom.html")

@app.route("/infectious-melody")
def infectious_melody():
	return render_template("infectious-melody.html")

@app.route("/internal-insurrection")
def internal_insurrection():
	return render_template("internal-insurrection.html")

@app.route("/levitate")
def levitate():
	return render_template("levitate.html")

@app.route("/invisibility-sphere")
def invisibility_sphere():
	return render_template("invisibility-sphere.html")

@app.route("/invisibility-curtain")
def invisibility_curtain():
	return render_template("invisibility-curtain.html")

@app.route("/life-connection")
def life_connection():
	return render_template("life-connection.html")

@app.route("/lightning-bolt")
def lightning_bolt():
	return render_template("lightning-bolt.html")

@app.route("/locate")
def locate():
	return render_template("locate.html")

@app.route("/mad-monkeys")
def mad_monkeys():
	return render_template("mad-monkeys.html")

@app.route("/magic-mailbox")
def magic_mailbox():
	return render_template("magic-mailbox.html")

@app.route("/magnetic-acceleration")
def magnetic_acceleration():
	return render_template("magnetic-acceleration.html")

@app.route("/magical-fetters")
def magical_fetters():
	return render_template("magical-fetters.html")

@app.route("/meld-into-stone")
def meld_into_stone():
	return render_template("meld-into-stone.html")

@app.route("/mind-of-menace")
def mind_of_menace():
	return render_template("mind-of-menace.html")

@app.route("/mind-reading")
def mind_reading():
	return render_template("mind-reading.html")

@app.route("/mirrors-misfortune")
def mirrors_misfortune():
	return render_template("mirrors-misfortune.html")

@app.route("/modify-memory")
def modify_memory():
	return render_template("modify-memory.html")

@app.route("/moonlight-ray")
def moonlight_ray():
	return render_template("moonlight-ray.html")

@app.route("/murderous-vine")
def murderous_vine():
	return render_template("murderous-vine.html")

@app.route("/neutralize-poison")
def neutralize_poison():
	return render_template("neutralize-poison.html")

@app.route("/necrotic-radiation")
def necrotic_radiation():
	return render_template("necrotic-radiation.html")

@app.route("/nondetection")
def nondetection():
	return render_template("nondetection.html")

@app.route("/nightmare")
def nightmare():
	return render_template("nightmare.html")

@app.route("/oneiric-mire")
def oneiric_mire():
	return render_template("oneiric-mire.html")

@app.route("/organsight")
def organsight():
	return render_template("organsight.html")

@app.route("/outcasts-curse")
def outcasts_curse():
	return render_template("outcasts-curse.html")

@app.route("/painful-vibrations")
def painful_vibrations():
	return render_template("painful-vibrations.html")

@app.route("/perseis-precautions")
def perseis_precautions():
	return render_template("perseis-precautions.html")

@app.route("/petal-storm")
def petal_storm():
	return render_template("petal-storm.html")

@app.route("/phantasmal-killer")
def phantasmal_killer():
	return render_template("phantasmal-killer.html")

@app.route("/phantom-prison")
def phantom_prison():
	return render_template("phantom-prison.html")

@app.route("/pillar-of-water")
def pillar_of_water():
	return render_template("pillar-of-water.html")

@app.route("/private-sanctum")
def private_sanctum():
	return render_template("private-sanctum.html")

@app.route("/pyrotechnics")
def pyrotechnics():
	return render_template("pyrotechnics.html")

@app.route("/read-omens")
def read_omens():
	return render_template("read-omens.html")

@app.route("/resounding-barrier")
def resounding_barrier():
	return render_template("resounding-barrier.html")

@app.route("/reflective-scales")
def reflective_scales():
	return render_template("reflective-scales.html")

@app.route("/remove-curse")
def remove_curse():
	return render_template("remove-curse.html")

@app.route("/remove-disease")
def remove_disease():
	return render_template("remove-disease.html")

@app.route("/replicate")
def replicate():
	return render_template("replicate.html")

@app.route("/resilient-sphere")
def resilient_sphere():
	return render_template("resilient-sphere.html")

@app.route("/roaring-applause")
def roaring_applause():
	return render_template("roaring-applause.html")

@app.route("/rouse-skeletons")
def rouse_skeletons():
	return render_template("rouse-skeletons.html")

@app.route("/rusting-grasp")
def rusting_grasp():
	return render_template("rusting-grasp.html")

@app.route("/rope-trick")
def rope_trick():
	return render_template("rope-trick.html")

@app.route("/sanctified-ground")
def sanctified_ground():
	return render_template("sanctified-ground.html")

@app.route("/sanguine-mist")
def sanguine_mist():
	return render_template("sanguine-mist.html")

@app.route("/savants-curse")
def savants_curse():
	return render_template("savants-curse.html")

@app.route("/sculpt-sound")
def sculpt_sound():
	return render_template("sculpt-sound.html")

@app.route("/seal-fate")
def seal_fate():
	return render_template("seal-fate.html")

@app.route("/searing-light")
def searing_light():
	return render_template("searing-light.html")

@app.route("/secret-page")
def secret_page():
	return render_template("secret-page.html")

@app.route("/shadow-projectile")
def shadow_projectile():
	return render_template("shadow-projectile.html")

@app.route("/shape-stone")
def shape_stone():
	return render_template("shape-stone.html")

@app.route("/shift-blame")
def shift_blame():
	return render_template("shift-blame.html")

@app.route("/shifting-sand")
def shifting_sand():
	return render_template("shifting-sand.html")

@app.route("/show-the-way")
def show_the_way():
	return render_template("show-the-way.html")

@app.route("/shrink-item")
def shrink_item():
	return render_template("shrink-item.html")

@app.route("/solid-fog")
def solid_fog():
	return render_template("solid-fog.html")

@app.route("/soothing-blossoms")
def soothing_blossoms():
	return render_template("soothing-blossoms.html")

@app.route("/speak-with-plants-3775319")
def speak_with_plants_3775319():
	return render_template("speak-with-plants-3775319.html")

@app.route("/spell-immunity")
def spell_immunity():
	return render_template("spell-immunity.html")

@app.route("/spike-stones")
def spike_stones():
	return render_template("spike-stones.html")

@app.route("/spiritual-anamnesis")
def spiritual_anamnesis():
	return render_template("spiritual-anamnesis.html")

@app.route("/spiritual-attunement")
def spiritual_attunement():
	return render_template("spiritual-attunement.html")

@app.route("/stinking-cloud")
def stinking_cloud():
	return render_template("stinking-cloud.html")

@app.route("/stoneskin")
def stoneskin():
	return render_template("stoneskin.html")

@app.route("/sudden-recollection")
def sudden_recollection():
	return render_template("sudden-recollection.html")

@app.route("/suggestion")
def suggestion():
	return render_template("suggestion.html")

@app.route("/swarming-wasp-stings")
def swarming_wasp_stings():
	return render_template("swarming-wasp-stings.html")

@app.route("/talking-corpse")
def talking_corpse():
	return render_template("talking-corpse.html")

@app.route("/telepathy")
def telepathy():
	return render_template("telepathy.html")

@app.route("/threefold-aspect")
def threefold_aspect():
	return render_template("threefold-aspect.html")

@app.route("/time-jump")
def time_jump():
	return render_template("time-jump.html")

@app.route("/tortoise-and-the-hare")
def tortoise_and_the_hare():
	return render_template("tortoise-and-the-hare.html")

@app.route("/umbral-graft")
def umbral_graft():
	return render_template("umbral-graft.html")

@app.route("/unseasonable-squall")
def unseasonable_squall():
	return render_template("unseasonable-squall.html")

@app.route("/vampiric-maiden")
def vampiric_maiden():
	return render_template("vampiric-maiden.html")

@app.route("/vampiric-touch")
def vampiric_touch():
	return render_template("vampiric-touch.html")

@app.route("/variable-gravity")
def variable_gravity():
	return render_template("variable-gravity.html")

@app.route("/veil")
def veil():
	return render_template("veil.html")

@app.route("/wall-of-fire")
def wall_of_fire():
	return render_template("wall-of-fire.html")

@app.route("/wall-of-radiance")
def wall_of_radiance():
	return render_template("wall-of-radiance.html")

@app.route("/wall-of-shadow")
def wall_of_shadow():
	return render_template("wall-of-shadow.html")

@app.route("/wall-of-thorns")
def wall_of_thorns():
	return render_template("wall-of-thorns.html")

@app.route("/wall-of-water")
def wall_of_water():
	return render_template("wall-of-water.html")

@app.route("/wall-of-wind")
def wall_of_wind():
	return render_template("wall-of-wind.html")

@app.route("/wanderers-guide")
def wanderers_guide():
	return render_template("wanderers-guide.html")

@app.route("/warding-aggression")
def warding_aggression():
	return render_template("warding-aggression.html")

@app.route("/weapon-storm")
def weapon_storm():
	return render_template("weapon-storm.html")

@app.route("/web-of-eyes")
def web_of_eyes():
	return render_template("web-of-eyes.html")

@app.route("/whirling-scarves")
def whirling_scarves():
	return render_template("whirling-scarves.html")

@app.route("/winning-streak")
def winning_streak():
	return render_template("winning-streak.html")

@app.route("/zone-of-truth")
def zone_of_truth():
	return render_template("zone-of-truth.html")

@app.route("/bind-undead")
def bind_undead():
	return render_template("bind-undead.html")

@app.route("/blazing-dive")
def blazing_dive():
	return render_template("blazing-dive.html")

@app.route("/blindness-6255307")
def blindness_6255307():
	return render_template("blindness-6255307.html")

@app.route("/blink")
def blink():
	return render_template("blink.html")

@app.route("/bloodspray-curse")
def bloodspray_curse():
	return render_template("bloodspray-curse.html")

@app.route("/freedom-of-movement")
def freedom_of_movement():
	return render_template("freedom-of-movement.html")

@app.route("/ocular-overload")
def ocular_overload():
	return render_template("ocular-overload.html")

@app.route("/paralyze")
def paralyze():
	return render_template("paralyze.html")

@app.route("/pernicious-poltergeist")
def pernicious_poltergeist():
	return render_template("pernicious-poltergeist.html")

@app.route("/safe-passage")
def safe_passage():
	return render_template("safe-passage.html")

@app.route("/slow")
def slow():
	return render_template("slow.html")

@app.route("/abyssal-plague")
def abyssal_plague():
	return render_template("abyssal-plague.html")

@app.route("/acid-storm")
def acid_storm():
	return render_template("acid-storm.html")

@app.route("/aura-of-the-unremarkable")
def aura_of_the_unremarkable():
	return render_template("aura-of-the-unremarkable.html")

@app.route("/baleful-polymorph")
def baleful_polymorph():
	return render_template("baleful-polymorph.html")

@app.route("/bandits-doom")
def bandits_doom():
	return render_template("bandits-doom.html")

@app.route("/banishment")
def banishment():
	return render_template("banishment.html")

@app.route("/black-tentacles")
def black_tentacles():
	return render_template("black-tentacles.html")

@app.route("/blackfingers-blades")
def blackfingers_blades():
	return render_template("blackfingers-blades.html")

@app.route("/blade-barrier")
def blade_barrier():
	return render_template("blade-barrier.html")

@app.route("/blanket-of-stars")
def blanket_of_stars():
	return render_template("blanket-of-stars.html")

@app.route("/blazing-fissure")
def blazing_fissure():
	return render_template("blazing-fissure.html")

@app.route("/blessing-of-defiance")
def blessing_of_defiance():
	return render_template("blessing-of-defiance.html")

@app.route("/blinding-fury")
def blinding_fury():
	return render_template("blinding-fury.html")

@app.route("/blink-charge")
def blink_charge():
	return render_template("blink-charge.html")

@app.route("/blister")
def blister():
	return render_template("blister.html")

@app.route("/blood-feast")
def blood_feast():
	return render_template("blood-feast.html")

@app.route("/cast-into-time")
def cast_into_time():
	return render_template("cast-into-time.html")

@app.route("/chain-lightning")
def chain_lightning():
	return render_template("chain-lightning.html")

@app.route("/chameleon-coat")
def chameleon_coat():
	return render_template("chameleon-coat.html")

@app.route("/chromatic-image")
def chromatic_image():
	return render_template("chromatic-image.html")

@app.route("/cloak-of-colors")
def cloak_of_colors():
	return render_template("cloak-of-colors.html")

@app.route("/cloudkill")
def cloudkill():
	return render_template("cloudkill.html")

@app.route("/collective-transposition")
def collective_transposition():
	return render_template("collective-transposition.html")

@app.route("/cone-of-cold")
def cone_of_cold():
	return render_template("cone-of-cold.html")

@app.route("/control-water")
def control_water():
	return render_template("control-water.html")

@app.route("/crushing-despair")
def crushing_despair():
	return render_template("crushing-despair.html")

@app.route("/death-ward")
def death_ward():
	return render_template("death-ward.html")

@app.route("/disintegrate")
def disintegrate():
	return render_template("disintegrate.html")

@app.route("/dominate")
def dominate():
	return render_template("dominate.html")

@app.route("/dreaming-potential")
def dreaming_potential():
	return render_template("dreaming-potential.html")

@app.route("/drop-dead")
def drop_dead():
	return render_template("drop-dead.html")

@app.route("/ectoplasmic-expulsion")
def ectoplasmic_expulsion():
	return render_template("ectoplasmic-expulsion.html")

@app.route("/elemental-confluence")
def elemental_confluence():
	return render_template("elemental-confluence.html")

@app.route("/false-vision")
def false_vision():
	return render_template("false-vision.html")

@app.route("/feeblemind")
def feeblemind():
	return render_template("feeblemind.html")

@app.route("/field-of-life")
def field_of_life():
	return render_template("field-of-life.html")

@app.route("/fire-seeds")
def fire_seeds():
	return render_template("fire-seeds.html")

@app.route("/flame-strike")
def flame_strike():
	return render_template("flame-strike.html")

@app.route("/flame-vortex")
def flame_vortex():
	return render_template("flame-vortex.html")

@app.route("/flammable-fumes")
def flammable_fumes():
	return render_template("flammable-fumes.html")

@app.route("/flesh-to-stone")
def flesh_to_stone():
	return render_template("flesh-to-stone.html")

@app.route("/flowing-strike")
def flowing_strike():
	return render_template("flowing-strike.html")

@app.route("/fly-5624108")
def fly_5624108():
	return render_template("fly-5624108.html")

@app.route("/forceful-hand")
def forceful_hand():
	return render_template("forceful-hand.html")

@app.route("/geyser")
def geyser():
	return render_template("geyser.html")

@app.route("/glimmer-of-charm")
def glimmer_of_charm():
	return render_template("glimmer-of-charm.html")

@app.route("/grisly-growths")
def grisly_growths():
	return render_template("grisly-growths.html")

@app.route("/halcyon-infusion")
def halcyon_infusion():
	return render_template("halcyon-infusion.html")

@app.route("/hallucination")
def hallucination():
	return render_template("hallucination.html")

@app.route("/illusory-scene")
def illusory_scene():
	return render_template("illusory-scene.html")

@app.route("/impaling-spike")
def impaling_spike():
	return render_template("impaling-spike.html")

@app.route("/healing-well")
def healing_well():
	return render_template("healing-well.html")

@app.route("/inevitable-disaster")
def inevitable_disaster():
	return render_template("inevitable-disaster.html")

@app.route("/invoke-spirits")
def invoke_spirits():
	return render_template("invoke-spirits.html")

@app.route("/lightning-storm")
def lightning_storm():
	return render_template("lightning-storm.html")

@app.route("/mantle-of-the-frozen-heart")
def mantle_of_the_frozen_heart():
	return render_template("mantle-of-the-frozen-heart.html")

@app.route("/mantle-of-the-magma-heart")
def mantle_of_the_magma_heart():
	return render_template("mantle-of-the-magma-heart.html")

@app.route("/mariners-curse")
def mariners_curse():
	return render_template("mariners-curse.html")

@app.route("/mind-probe")
def mind_probe():
	return render_template("mind-probe.html")

@app.route("/mirecloak")
def mirecloak():
	return render_template("mirecloak.html")

@app.route("/mirror-malefactors")
def mirror_malefactors():
	return render_template("mirror-malefactors.html")

@app.route("/mislead")
def mislead():
	return render_template("mislead.html")

@app.route("/moon-frenzy")
def moon_frenzy():
	return render_template("moon-frenzy.html")

@app.route("/natures-reprisal")
def natures_reprisal():
	return render_template("natures-reprisal.html")

@app.route("/necrotize")
def necrotize():
	return render_template("necrotize.html")

@app.route("/passwall")
def passwall():
	return render_template("passwall.html")

@app.route("/phantasmal-calamity")
def phantasmal_calamity():
	return render_template("phantasmal-calamity.html")

@app.route("/pillars-of-sand")
def pillars_of_sand():
	return render_template("pillars-of-sand.html")

@app.route("/portrait-of-the-artist")
def portrait_of_the_artist():
	return render_template("portrait-of-the-artist.html")

@app.route("/prying-eye")
def prying_eye():
	return render_template("prying-eye.html")

@app.route("/purple-worm-sting")
def purple_worm_sting():
	return render_template("purple-worm-sting.html")

@app.route("/ravening-maw")
def ravening_maw():
	return render_template("ravening-maw.html")

@app.route("/repelling-pulse")
def repelling_pulse():
	return render_template("repelling-pulse.html")

@app.route("/repulsion")
def repulsion():
	return render_template("repulsion.html")

@app.route("/return-beacon")
def return_beacon():
	return render_template("return-beacon.html")

@app.route("/rewinding-step")
def rewinding_step():
	return render_template("rewinding-step.html")

@app.route("/rip-the-spirit")
def rip_the_spirit():
	return render_template("rip-the-spirit.html")

@app.route("/secret-chest")
def secret_chest():
	return render_template("secret-chest.html")

@app.route("/scrying")
def scrying():
	return render_template("scrying.html")

@app.route("/sending")
def sending():
	return render_template("sending.html")

@app.route("/shadow-blast")
def shadow_blast():
	return render_template("shadow-blast.html")

@app.route("/spirit-blast")
def spirit_blast():
	return render_template("spirit-blast.html")

@app.route("/spiritual-guardian")
def spiritual_guardian():
	return render_template("spiritual-guardian.html")

@app.route("/stormburst")
def stormburst():
	return render_template("stormburst.html")

@app.route("/strange-geometry")
def strange_geometry():
	return render_template("strange-geometry.html")

@app.route("/synaptic-pulse")
def synaptic_pulse():
	return render_template("synaptic-pulse.html")

@app.route("/synesthesia")
def synesthesia():
	return render_template("synesthesia.html")

@app.route("/telekinetic-haul")
def telekinetic_haul():
	return render_template("telekinetic-haul.html")

@app.route("/tangling-creepers")
def tangling_creepers():
	return render_template("tangling-creepers.html")

@app.route("/unexpected-transposition")
def unexpected_transposition():
	return render_template("unexpected-transposition.html")

@app.route("/vampiric-exsanguination")
def vampiric_exsanguination():
	return render_template("vampiric-exsanguination.html")

@app.route("/vibrant-pattern")
def vibrant_pattern():
	return render_template("vibrant-pattern.html")

@app.route("/wall-of-force")
def wall_of_force():
	return render_template("wall-of-force.html")

@app.route("/wall-of-ice")
def wall_of_ice():
	return render_template("wall-of-ice.html")

@app.route("/wall-of-stone")
def wall_of_stone():
	return render_template("wall-of-stone.html")

@app.route("/wyvern-sting")
def wyvern_sting():
	return render_template("wyvern-sting.html")

@app.route("/zealous-conviction")
def zealous_conviction():
	return render_template("zealous-conviction.html")

@app.route("/scintillating-safeguard")
def scintillating_safeguard():
	return render_template("scintillating-safeguard.html")

@app.route("/shadow-syphon")
def shadow_syphon():
	return render_template("shadow-syphon.html")

@app.route("/spellwrack")
def spellwrack():
	return render_template("spellwrack.html")

@app.route("/stone-tell")
def stone_tell():
	return render_template("stone-tell.html")

@app.route("/stone-to-flesh")
def stone_to_flesh():
	return render_template("stone-to-flesh.html")

@app.route("/subconscious-suggestion")
def subconscious_suggestion():
	return render_template("subconscious-suggestion.html")

@app.route("/telepathic-bond")
def telepathic_bond():
	return render_template("telepathic-bond.html")

@app.route("/temporal-ward")
def temporal_ward():
	return render_template("temporal-ward.html")

@app.route("/temporary-glyph")
def temporary_glyph():
	return render_template("temporary-glyph.html")

@app.route("/tongues")
def tongues():
	return render_template("tongues.html")

@app.route("/transmute-rock-to-mud")
def transmute_rock_to_mud():
	return render_template("transmute-rock-to-mud.html")

@app.route("/tree-stride")
def tree_stride():
	return render_template("tree-stride.html")

@app.route("/true-seeing")
def true_seeing():
	return render_template("true-seeing.html")

@app.route("/wall-of-flesh")
def wall_of_flesh():
	return render_template("wall-of-flesh.html")

@app.route("/zero-gravity")
def zero_gravity():
	return render_template("zero-gravity.html")

@app.route("/all-is-one-one-is-all")
def all_is_one_one_is_all():
	return render_template("all-is-one-one-is-all.html")

@app.route("/antimagic-field")
def antimagic_field():
	return render_template("antimagic-field.html")

@app.route("/blightburn-blast")
def blightburn_blast():
	return render_template("blightburn-blast.html")

@app.route("/burning-blossoms")
def burning_blossoms():
	return render_template("burning-blossoms.html")

@app.route("/deitys-strike")
def deitys_strike():
	return render_template("deitys-strike.html")

@app.route("/deluge")
def deluge():
	return render_template("deluge.html")

@app.route("/devour-life")
def devour_life():
	return render_template("devour-life.html")

@app.route("/disappearance")
def disappearance():
	return render_template("disappearance.html")

@app.route("/divine-armageddon")
def divine_armageddon():
	return render_template("divine-armageddon.html")

@app.route("/divine-aura")
def divine_aura():
	return render_template("divine-aura.html")

@app.route("/divine-decree")
def divine_decree():
	return render_template("divine-decree.html")

@app.route("/divine-inspiration")
def divine_inspiration():
	return render_template("divine-inspiration.html")

@app.route("/divine-vessel")
def divine_vessel():
	return render_template("divine-vessel.html")

@app.route("/dream-council")
def dream_council():
	return render_template("dream-council.html")

@app.route("/duplicate-foe")
def duplicate_foe():
	return render_template("duplicate-foe.html")

@app.route("/eclipse-burst")
def eclipse_burst():
	return render_template("eclipse-burst.html")

@app.route("/energy-aegis")
def energy_aegis():
	return render_template("energy-aegis.html")

@app.route("/entrancing-eyes")
def entrancing_eyes():
	return render_template("entrancing-eyes.html")

@app.route("/ethereal-jaunt")
def ethereal_jaunt():
	return render_template("ethereal-jaunt.html")

@app.route("/corrosive-body")
def corrosive_body():
	return render_template("corrosive-body.html")

@app.route("/frigid-flurry")
def frigid_flurry():
	return render_template("frigid-flurry.html")

@app.route("/horrid-wilting")
def horrid_wilting():
	return render_template("horrid-wilting.html")

@app.route("/inexhaustible-cynicism")
def inexhaustible_cynicism():
	return render_template("inexhaustible-cynicism.html")

@app.route("/leng-sting")
def leng_sting():
	return render_template("leng-sting.html")

@app.route("/mask-of-terror")
def mask_of_terror():
	return render_template("mask-of-terror.html")

@app.route("/mind-blank")
def mind_blank():
	return render_template("mind-blank.html")

@app.route("/moment-of-renewal")
def moment_of_renewal():
	return render_template("moment-of-renewal.html")

@app.route("/moonburst")
def moonburst():
	return render_template("moonburst.html")

@app.route("/planeshift")
def planeshift():
	return render_template("planeshift.html")

@app.route("/polar-ray")
def polar_ray():
	return render_template("polar-ray.html")

@app.route("/possession")
def possession():
	return render_template("possession.html")

@app.route("/power-word-blind")
def power_word_blind():
	return render_template("power-word-blind.html")

@app.route("/prismatic-armor")
def prismatic_armor():
	return render_template("prismatic-armor.html")

@app.route("/project-image")
def project_image():
	return render_template("project-image.html")

@app.route("/punishing-winds")
def punishing_winds():
	return render_template("punishing-winds.html")

@app.route("/retrocognition")
def retrocognition():
	return render_template("retrocognition.html")

@app.route("/reverse-gravity")
def reverse_gravity():
	return render_template("reverse-gravity.html")

@app.route("/scintillating-pattern")
def scintillating_pattern():
	return render_template("scintillating-pattern.html")

@app.route("/shadow-raid")
def shadow_raid():
	return render_template("shadow-raid.html")

@app.route("/spell-turning")
def spell_turning():
	return render_template("spell-turning.html")

@app.route("/spirit-song")
def spirit_song():
	return render_template("spirit-song.html")

@app.route("/spiritual-epidemic")
def spiritual_epidemic():
	return render_template("spiritual-epidemic.html")

@app.route("/summon-archmage")
def summon_archmage():
	return render_template("summon-archmage.html")

@app.route("/summon-deific-herald")
def summon_deific_herald():
	return render_template("summon-deific-herald.html")

@app.route("/sunburst")
def sunburst():
	return render_template("sunburst.html")

@app.route("/tempest-of-shades")
def tempest_of_shades():
	return render_template("tempest-of-shades.html")

@app.route("/time-beacon")
def time_beacon():
	return render_template("time-beacon.html")

@app.route("/true-target")
def true_target():
	return render_template("true-target.html")

@app.route("/uncontrollable-dance")
def uncontrollable_dance():
	return render_template("uncontrollable-dance.html")

@app.route("/undermine-reality")
def undermine_reality():
	return render_template("undermine-reality.html")

@app.route("/unfettered-pack")
def unfettered_pack():
	return render_template("unfettered-pack.html")

@app.route("/unrelenting-observation")
def unrelenting_observation():
	return render_template("unrelenting-observation.html")

@app.route("/visions-of-danger")
def visions_of_danger():
	return render_template("visions-of-danger.html")

@app.route("/volcanic-eruption")
def volcanic_eruption():
	return render_template("volcanic-eruption.html")

@app.route("/warp-mind")
def warp_mind():
	return render_template("warp-mind.html")

@app.route("/whirlwind")
def whirlwind():
	return render_template("whirlwind.html")

@app.route("/boil-blood")
def boil_blood():
	return render_template("boil-blood.html")

@app.route("/canticle-of-everlasting-grief")
def canticle_of_everlasting_grief():
	return render_template("canticle-of-everlasting-grief.html")

@app.route("/clone-companion")
def clone_companion():
	return render_template("clone-companion.html")

@app.route("/contingency")
def contingency():
	return render_template("contingency.html")

@app.route("/control-sand")
def control_sand():
	return render_template("control-sand.html")

@app.route("/dimensional-lock")
def dimensional_lock():
	return render_template("dimensional-lock.html")

@app.route("/discern-location")
def discern_location():
	return render_template("discern-location.html")

@app.route("/earthquake")
def earthquake():
	return render_template("earthquake.html")

@app.route("/fiery-body")
def fiery_body():
	return render_template("fiery-body.html")

@app.route("/finger-of-death")
def finger_of_death():
	return render_template("finger-of-death.html")

@app.route("/force-cage")
def force_cage():
	return render_template("force-cage.html")

@app.route("/power-word-stun")
def power_word_stun():
	return render_template("power-word-stun.html")

@app.route("/prismatic-wall")
def prismatic_wall():
	return render_template("prismatic-wall.html")

@app.route("/return-to-essence")
def return_to_essence():
	return render_template("return-to-essence.html")

@app.route("/golem")
def golem():
	return render_template("golem.html")

@app.route("/frightful-presence-monster")
def frightful_presence_monster():
	return render_template("frightful-presence-monster.html")

@app.route("/polymorph")
def polymorph():
	return render_template("polymorph.html")

@app.route("/grab-monster-ability")
def grab_monster_ability():
	return render_template("grab-monster-ability.html")

@app.route("/trample-monster-ability")
def trample_monster_ability():
	return render_template("trample-monster-ability.html")

@app.route("/swallow-whole-monster-ability")
def swallow_whole_monster_ability():
	return render_template("swallow-whole-monster-ability.html")

@app.route("/constrict-monster-action")
def constrict_monster_action():
	return render_template("constrict-monster-action.html")

@app.route("/pest-form")
def pest_form():
	return render_template("pest-form.html")

@app.route("/swarm-9641624")
def swarm_9641624():
	return render_template("swarm-9641624.html")

@app.route("/aquatic")
def aquatic():
	return render_template("aquatic.html")

@app.route("/amphibious-6493034")
def amphibious_6493034():
	return render_template("amphibious-6493034.html")

@app.route("/narwhal")
def narwhal():
	return render_template("narwhal.html")

@app.route("/piranah-swarm")
def piranah_swarm():
	return render_template("piranah-swarm.html")

@app.route("/aasimar-redeemer")
def aasimar_redeemer():
	return render_template("aasimar-redeemer.html")

@app.route("/abandoned-zealot")
def abandoned_zealot():
	return render_template("abandoned-zealot.html")

@app.route("/abrikandilu-wrecker-demon")
def abrikandilu_wrecker_demon():
	return render_template("abrikandilu-wrecker-demon.html")

@app.route("/adamantine-golem")
def adamantine_golem():
	return render_template("adamantine-golem.html")

@app.route("/adhukait")
def adhukait():
	return render_template("adhukait.html")

@app.route("/adlet-thrower")
def adlet_thrower():
	return render_template("adlet-thrower.html")

@app.route("/tiger")
def tiger():
	return render_template("tiger.html")

@app.route("/rhinoceros")
def rhinoceros():
	return render_template("rhinoceros.html")

@app.route("/emperor-cobra")
def emperor_cobra():
	return render_template("emperor-cobra.html")

@app.route("/cave-bear")
def cave_bear():
	return render_template("cave-bear.html")

@app.route("/dire-wolf")
def dire_wolf():
	return render_template("dire-wolf.html")

@app.route("/giant-moray-eel")
def giant_moray_eel():
	return render_template("giant-moray-eel.html")

@app.route("/owlbear")
def owlbear():
	return render_template("owlbear.html")

@app.route("/giant-tarantula")
def giant_tarantula():
	return render_template("giant-tarantula.html")

@app.route("/great-white-shark")
def great_white_shark():
	return render_template("great-white-shark.html")

@app.route("/elephant")
def elephant():
	return render_template("elephant.html")

@app.route("/megalania")
def megalania():
	return render_template("megalania.html")

@app.route("/blood-boar")
def blood_boar():
	return render_template("blood-boar.html")

@app.route("/improved-grab")
def improved_grab():
	return render_template("improved-grab.html")

@app.route("/giant-squid")
def giant_squid():
	return render_template("giant-squid.html")

@app.route("/deadly-mantis")
def deadly_mantis():
	return render_template("deadly-mantis.html")

@app.route("/megaprimatus")
def megaprimatus():
	return render_template("megaprimatus.html")

@app.route("/aurumvorax")
def aurumvorax():
	return render_template("aurumvorax.html")

@app.route("/bulette")
def bulette():
	return render_template("bulette.html")

@app.route("/krooth")
def krooth():
	return render_template("krooth.html")

@app.route("/lion")
def lion():
	return render_template("lion.html")

@app.route("/grizzly-bear")
def grizzly_bear():
	return render_template("grizzly-bear.html")

@app.route("/giant-wasp")
def giant_wasp():
	return render_template("giant-wasp.html")

@app.route("/gryphon")
def gryphon():
	return render_template("gryphon.html")

@app.route("/quetzcoatlus")
def quetzcoatlus():
	return render_template("quetzcoatlus.html")

@app.route("/mist-stalker")
def mist_stalker():
	return render_template("mist-stalker.html")

@app.route("/filth-fire")
def filth_fire():
	return render_template("filth-fire.html")

@app.route("/earthen-destrier")
def earthen_destrier():
	return render_template("earthen-destrier.html")

@app.route("/living-thunderclap")
def living_thunderclap():
	return render_template("living-thunderclap.html")

@app.route("/living-landslide")
def living_landslide():
	return render_template("living-landslide.html")

@app.route("/living-waterfall")
def living_waterfall():
	return render_template("living-waterfall.html")

@app.route("/living-whirlwind")
def living_whirlwind():
	return render_template("living-whirlwind.html")

@app.route("/living-wildfire")
def living_wildfire():
	return render_template("living-wildfire.html")

@app.route("/belker")
def belker():
	return render_template("belker.html")

@app.route("/blizzardborn")
def blizzardborn():
	return render_template("blizzardborn.html")

@app.route("/sand-sentry")
def sand_sentry():
	return render_template("sand-sentry.html")

@app.route("/striding-fire")
def striding_fire():
	return render_template("striding-fire.html")

@app.route("/invisible-stalker")
def invisible_stalker():
	return render_template("invisible-stalker.html")

@app.route("/quatoid")
def quatoid():
	return render_template("quatoid.html")

@app.route("/salamander")
def salamander():
	return render_template("salamander.html")

@app.route("/xorn")
def xorn():
	return render_template("xorn.html")

@app.route("/summon-construct")
def summon_construct():
	return render_template("summon-construct.html")

@app.route("/dryad")
def dryad():
	return render_template("dryad.html")

@app.route("/tooth-fairy-swarm")
def tooth_fairy_swarm():
	return render_template("tooth-fairy-swarm.html")

@app.route("/unicorn")
def unicorn():
	return render_template("unicorn.html")

@app.route("/minion")
def minion():
	return render_template("minion.html")

@app.route("/pixie")
def pixie():
	return render_template("pixie.html")

@app.route("/satyr")
def satyr():
	return render_template("satyr.html")

@app.route("/redcap")
def redcap():
	return render_template("redcap.html")

@app.route("/kelpie")
def kelpie():
	return render_template("kelpie.html")

@app.route("/grimstalker")
def grimstalker():
	return render_template("grimstalker.html")

@app.route("/lurker-in-light")
def lurker_in_light():
	return render_template("lurker-in-light.html")

@app.route("/eloko")
def eloko():
	return render_template("eloko.html")

@app.route("/elananx")
def elananx():
	return render_template("elananx.html")

@app.route("/pummeling-rubble")
def pummeling_rubble():
	return render_template("pummeling-rubble.html")

@app.route("/lampad")
def lampad():
	return render_template("lampad.html")

@app.route("/summon-fey")
def summon_fey():
	return render_template("summon-fey.html")

@app.route("/esobok")
def esobok():
	return render_template("esobok.html")

@app.route("/hell-hound")
def hell_hound():
	return render_template("hell-hound.html")

@app.route("/lantern-archon")
def lantern_archon():
	return render_template("lantern-archon.html")

@app.route("/summon-lesser-servitor")
def summon_lesser_servitor():
	return render_template("summon-lesser-servitor.html")

@app.route("/arboreal-warden")
def arboreal_warden():
	return render_template("arboreal-warden.html")

@app.route("/calathgar")
def calathgar():
	return render_template("calathgar.html")

@app.route("/myceloid")
def myceloid():
	return render_template("myceloid.html")

@app.route("/awakened-tree")
def awakened_tree():
	return render_template("awakened-tree.html")

@app.route("/basidirond")
def basidirond():
	return render_template("basidirond.html")

@app.route("/wizard-sponge")
def wizard_sponge():
	return render_template("wizard-sponge.html")

@app.route("/arboreal-reaper")
def arboreal_reaper():
	return render_template("arboreal-reaper.html")

@app.route("/tendriculos")
def tendriculos():
	return render_template("tendriculos.html")

@app.route("/scythe-tree")
def scythe_tree():
	return render_template("scythe-tree.html")

@app.route("/arboreal-regeant")
def arboreal_regeant():
	return render_template("arboreal-regeant.html")

@app.route("/counteflora")
def counteflora():
	return render_template("counteflora.html")

@app.route("/dezullon")
def dezullon():
	return render_template("dezullon.html")

@app.route("/drakauthix")
def drakauthix():
	return render_template("drakauthix.html")

@app.route("/summon-plant-or-fungus")
def summon_plant_or_fungus():
	return render_template("summon-plant-or-fungus.html")

@app.route("/lilend")
def lilend():
	return render_template("lilend.html")

@app.route("/naunet")
def naunet():
	return render_template("naunet.html")

@app.route("/nabasu-glutton-demon")
def nabasu_glutton_demon():
	return render_template("nabasu-glutton-demon.html")

@app.route("/einherjar")
def einherjar():
	return render_template("einherjar.html")

@app.route("/garuda")
def garuda():
	return render_template("garuda.html")

@app.route("/vrock")
def vrock():
	return render_template("vrock.html")

@app.route("/summon-anarch")
def summon_anarch():
	return render_template("summon-anarch.html")

@app.route("/axiomite")
def axiomite():
	return render_template("axiomite.html")

@app.route("/erinyes-fury-devil")
def erinyes_fury_devil():
	return render_template("erinyes-fury-devil.html")

@app.route("/legion-archon")
def legion_archon():
	return render_template("legion-archon.html")

@app.route("/sacristan")
def sacristan():
	return render_template("sacristan.html")

@app.route("/zelekhut")
def zelekhut():
	return render_template("zelekhut.html")

@app.route("/summon-axiom")
def summon_axiom():
	return render_template("summon-axiom.html")

@app.route("/balisse-confessor-angel")
def balisse_confessor_angel():
	return render_template("balisse-confessor-angel.html")

@app.route("/procyal")
def procyal():
	return render_template("procyal.html")

@app.route("/summon-celestial")
def summon_celestial():
	return render_template("summon-celestial.html")

@app.route("/movanic-deva")
def movanic_deva():
	return render_template("movanic-deva.html")

@app.route("/monadic-deva")
def monadic_deva():
	return render_template("monadic-deva.html")

@app.route("/adult-black-dragon")
def adult_black_dragon():
	return render_template("adult-black-dragon.html")

@app.route("/summon-dragon")
def summon_dragon():
	return render_template("summon-dragon.html")

@app.route("/destrachan")
def destrachan():
	return render_template("destrachan.html")

@app.route("/rend-monster-ability")
def rend_monster_ability():
	return render_template("rend-monster-ability.html")

@app.route("/gug")
def gug():
	return render_template("gug.html")

@app.route("/ofalth")
def ofalth():
	return render_template("ofalth.html")

@app.route("/summon-entity")
def summon_entity():
	return render_template("summon-entity.html")

@app.route("/hellcat")
def hellcat():
	return render_template("hellcat.html")

@app.route("/invidiak")
def invidiak():
	return render_template("invidiak.html")

@app.route("/night-hag")
def night_hag():
	return render_template("night-hag.html")

@app.route("/leukodaemon-pestilence-demon")
def leukodaemon_pestilence_demon():
	return render_template("leukodaemon-pestilence-demon.html")

@app.route("/summon-fiend")
def summon_fiend():
	return render_template("summon-fiend.html")

@app.route("/catch")
def catch():
	return render_template("catch.html")

@app.route("/hill-giant")
def hill_giant():
	return render_template("hill-giant.html")

@app.route("/ettin")
def ettin():
	return render_template("ettin.html")

@app.route("/fire-giant")
def fire_giant():
	return render_template("fire-giant.html")

@app.route("/frost-giant")
def frost_giant():
	return render_template("frost-giant.html")

@app.route("/summon-giant")
def summon_giant():
	return render_template("summon-giant.html")

@app.route("/giant-mosquito")
def giant_mosquito():
	return render_template("giant-mosquito.html")

@app.route("/giant-dragonfly")
def giant_dragonfly():
	return render_template("giant-dragonfly.html")

@app.route("/giant-eagle")
def giant_eagle():
	return render_template("giant-eagle.html")

@app.route("/anklyosaurus")
def anklyosaurus():
	return render_template("anklyosaurus.html")

@app.route("/stegosaurus")
def stegosaurus():
	return render_template("stegosaurus.html")

@app.route("/triceratops")
def triceratops():
	return render_template("triceratops.html")

@app.route("/tyrannosaurus")
def tyrannosaurus():
	return render_template("tyrannosaurus.html")

@app.route("/dinosaur-form")
def dinosaur_form():
	return render_template("dinosaur-form.html")

@app.route("/engulf")
def engulf():
	return render_template("engulf.html")

@app.route("/gelatinous-cube")
def gelatinous_cube():
	return render_template("gelatinous-cube.html")

@app.route("/blood-ooze")
def blood_ooze():
	return render_template("blood-ooze.html")

@app.route("/black-pudding")
def black_pudding():
	return render_template("black-pudding.html")

@app.route("/verdurous-ooze")
def verdurous_ooze():
	return render_template("verdurous-ooze.html")

@app.route("/ooze-form")
def ooze_form():
	return render_template("ooze-form.html")

@app.route("/chuul")
def chuul():
	return render_template("chuul.html")

@app.route("/aerial-form")
def aerial_form():
	return render_template("aerial-form.html")

@app.route("/quoppopak")
def quoppopak():
	return render_template("quoppopak.html")

@app.route("/gogiteth")
def gogiteth():
	return render_template("gogiteth.html")

@app.route("/aberrant-form")
def aberrant_form():
	return render_template("aberrant-form.html")

@app.route("/nessian-warhound")
def nessian_warhound():
	return render_template("nessian-warhound.html")

@app.route("/hellwasp-swarm")
def hellwasp_swarm():
	return render_template("hellwasp-swarm.html")

@app.route("/kalavakus-slaver-demon")
def kalavakus_slaver_demon():
	return render_template("kalavakus-slaver-demon.html")

@app.route("/piscodaemon-venom-daemon")
def piscodaemon_venom_daemon():
	return render_template("piscodaemon-venom-daemon.html")

@app.route("/fiend-form")
def fiend_form():
	return render_template("fiend-form.html")

@app.route("/dragon-form")
def dragon_form():
	return render_template("dragon-form.html")

@app.route("/magma-scorpion")
def magma_scorpion():
	return render_template("magma-scorpion.html")

@app.route("/tidal-master")
def tidal_master():
	return render_template("tidal-master.html")

@app.route("/elemental-form")
def elemental_form():
	return render_template("elemental-form.html")

@app.route("/giant-flytrap")
def giant_flytrap():
	return render_template("giant-flytrap.html")

@app.route("/plant-form")
def plant_form():
	return render_template("plant-form.html")

@app.route("/nereid")
def nereid():
	return render_template("nereid.html")

@app.route("/millindemalion")
def millindemalion():
	return render_template("millindemalion.html")

@app.route("/fey-form")
def fey_form():
	return render_template("fey-form.html")

@app.route("/shield-archon")
def shield_archon():
	return render_template("shield-archon.html")

@app.route("/angel-form")
def angel_form():
	return render_template("angel-form.html")

@app.route("/purple-worm")
def purple_worm():
	return render_template("purple-worm.html")

@app.route("/sea-serpent")
def sea_serpent():
	return render_template("sea-serpent.html")

@app.route("/monstrosity-form")
def monstrosity_form():
	return render_template("monstrosity-form.html")

@app.route("/elven-absynthe")
def elven_absynthe():
	return render_template("elven-absynthe.html")

@app.route("/alcohol")
def alcohol():
	return render_template("alcohol.html")

@app.route("/qat")
def qat():
	return render_template("qat.html")

@app.route("/bloodeye-coffee")
def bloodeye_coffee():
	return render_template("bloodeye-coffee.html")

@app.route("/flayleaf")
def flayleaf():
	return render_template("flayleaf.html")

@app.route("/refined-pesh")
def refined_pesh():
	return render_template("refined-pesh.html")

@app.route("/grit")
def grit():
	return render_template("grit.html")

@app.route("/groina")
def groina():
	return render_template("groina.html")

@app.route("/blood-sap")
def blood_sap():
	return render_template("blood-sap.html")

@app.route("/shiver")
def shiver():
	return render_template("shiver.html")

@app.route("/dreamtime-tea")
def dreamtime_tea():
	return render_template("dreamtime-tea.html")

@app.route("/zerk")
def zerk():
	return render_template("zerk.html")

@app.route("/diluted-hype")
def diluted_hype():
	return render_template("diluted-hype.html")

@app.route("/cytillesh")
def cytillesh():
	return render_template("cytillesh.html")

@app.route("/demon-dust")
def demon_dust():
	return render_template("demon-dust.html")

@app.route("/succubus-kiss")
def succubus_kiss():
	return render_template("succubus-kiss.html")

@app.route("/scour")
def scour():
	return render_template("scour.html")

@app.route("/hype")
def hype():
	return render_template("hype.html")

@app.route("/plasma-hype")
def plasma_hype():
	return render_template("plasma-hype.html")

@app.route("/popdust")
def popdust():
	return render_template("popdust.html")

@app.route("/tindertwig")
def tindertwig():
	return render_template("tindertwig.html")

@app.route("/snake-oil")
def snake_oil():
	return render_template("snake-oil.html")

@app.route("/blindpepper-tube")
def blindpepper_tube():
	return render_template("blindpepper-tube.html")

@app.route("/bookthief-brew")
def bookthief_brew():
	return render_template("bookthief-brew.html")

@app.route("/forensic-dye")
def forensic_dye():
	return render_template("forensic-dye.html")

@app.route("/ghost-ink")
def ghost_ink():
	return render_template("ghost-ink.html")

@app.route("/sunrod")
def sunrod():
	return render_template("sunrod.html")

@app.route("/lovers-ink")
def lovers_ink():
	return render_template("lovers-ink.html")

@app.route("/origin-unguent")
def origin_unguent():
	return render_template("origin-unguent.html")

@app.route("/silvensheen")
def silvensheen():
	return render_template("silvensheen.html")

@app.route("/impossible-cake")
def impossible_cake():
	return render_template("impossible-cake.html")

@app.route("/cold-iron-blanch")
def cold_iron_blanch():
	return render_template("cold-iron-blanch.html")

@app.route("/quickpatch-glue")
def quickpatch_glue():
	return render_template("quickpatch-glue.html")

@app.route("/swamp-lily-quilt")
def swamp_lily_quilt():
	return render_template("swamp-lily-quilt.html")

@app.route("/aurifying-salts")
def aurifying_salts():
	return render_template("aurifying-salts.html")

@app.route("/timeless-salts")
def timeless_salts():
	return render_template("timeless-salts.html")

@app.route("/fungal-walk-musk")
def fungal_walk_musk():
	return render_template("fungal-walk-musk.html")

@app.route("/universal-solvent")
def universal_solvent():
	return render_template("universal-solvent.html")

@app.route("/smokestick")
def smokestick():
	return render_template("smokestick.html")

@app.route("/dragons-blood-pudding")
def dragons_blood_pudding():
	return render_template("dragons-blood-pudding.html")

@app.route("/bloodhound-mask")
def bloodhound_mask():
	return render_template("bloodhound-mask.html")

@app.route("/metalmist-sphere")
def metalmist_sphere():
	return render_template("metalmist-sphere.html")

@app.route("/skinstich-salve")
def skinstich_salve():
	return render_template("skinstich-salve.html")

@app.route("/sovereign-glue")
def sovereign_glue():
	return render_template("sovereign-glue.html")

@app.route("/cold-comfort")
def cold_comfort():
	return render_template("cold-comfort.html")

@app.route("/vermin-repellent-agent")
def vermin_repellent_agent():
	return render_template("vermin-repellent-agent.html")

@app.route("/brewers-regret")
def brewers_regret():
	return render_template("brewers-regret.html")

@app.route("/green-gut")
def green_gut():
	return render_template("green-gut.html")

@app.route("/false-death")
def false_death():
	return render_template("false-death.html")

@app.route("/looters-lethargy")
def looters_lethargy():
	return render_template("looters-lethargy.html")

@app.route("/black-adder-venom")
def black_adder_venom():
	return render_template("black-adder-venom.html")

@app.route("/black-smear-poison")
def black_smear_poison():
	return render_template("black-smear-poison.html")

@app.route("/spear-frog-poison")
def spear_frog_poison():
	return render_template("spear-frog-poison.html")

@app.route("/giant-centipede-venom")
def giant_centipede_venom():
	return render_template("giant-centipede-venom.html")

@app.route("/toad-tears")
def toad_tears():
	return render_template("toad-tears.html")

@app.route("/yellow-musk-vial")
def yellow_musk_vial():
	return render_template("yellow-musk-vial.html")

@app.route("/violet-venom")
def violet_venom():
	return render_template("violet-venom.html")

@app.route("/beladonna")
def beladonna():
	return render_template("beladonna.html")

@app.route("/arsenic")
def arsenic():
	return render_template("arsenic.html")

@app.route("/leaden-leg")
def leaden_leg():
	return render_template("leaden-leg.html")

@app.route("/graveroot")
def graveroot():
	return render_template("graveroot.html")

@app.route("/blue-dragonfly-poison")
def blue_dragonfly_poison():
	return render_template("blue-dragonfly-poison.html")

@app.route("/hunting-spider-venom")
def hunting_spider_venom():
	return render_template("hunting-spider-venom.html")

@app.route("/giant-scorpion-venom")
def giant_scorpion_venom():
	return render_template("giant-scorpion-venom.html")

@app.route("/forgetful-ink")
def forgetful_ink():
	return render_template("forgetful-ink.html")

@app.route("/isolation-draught")
def isolation_draught():
	return render_template("isolation-draught.html")

@app.route("/sloughing-toxin")
def sloughing_toxin():
	return render_template("sloughing-toxin.html")

@app.route("/addlebrain")
def addlebrain():
	return render_template("addlebrain.html")

@app.route("/malyass-root-paste")
def malyass_root_paste():
	return render_template("malyass-root-paste.html")

@app.route("/knockout-dram")
def knockout_dram():
	return render_template("knockout-dram.html")

@app.route("/lich-dust")
def lich_dust():
	return render_template("lich-dust.html")

@app.route("/abysium-powder")
def abysium_powder():
	return render_template("abysium-powder.html")

@app.route("/wyvern-poison")
def wyvern_poison():
	return render_template("wyvern-poison.html")

@app.route("/wolfsbane")
def wolfsbane():
	return render_template("wolfsbane.html")

@app.route("/fearweed")
def fearweed():
	return render_template("fearweed.html")

@app.route("/honeyscent")
def honeyscent():
	return render_template("honeyscent.html")

@app.route("/blightburn-resin")
def blightburn_resin():
	return render_template("blightburn-resin.html")

@app.route("/hunger-oil")
def hunger_oil():
	return render_template("hunger-oil.html")

@app.route("/mage-bane")
def mage_bane():
	return render_template("mage-bane.html")

@app.route("/slumber-wine")
def slumber_wine():
	return render_template("slumber-wine.html")

@app.route("/spell-eating-pitch")
def spell_eating_pitch():
	return render_template("spell-eating-pitch.html")

@app.route("/deathcap-powder")
def deathcap_powder():
	return render_template("deathcap-powder.html")

@app.route("/spectral-nightshade")
def spectral_nightshade():
	return render_template("spectral-nightshade.html")

@app.route("/gorgons-breath")
def gorgons_breath():
	return render_template("gorgons-breath.html")

@app.route("/daylight-vapor")
def daylight_vapor():
	return render_template("daylight-vapor.html")

@app.route("/death-knell-powder")
def death_knell_powder():
	return render_template("death-knell-powder.html")

@app.route("/liars-demise")
def liars_demise():
	return render_template("liars-demise.html")

@app.route("/mindfog-mist")
def mindfog_mist():
	return render_template("mindfog-mist.html")

@app.route("/lifeblight-residue")
def lifeblight_residue():
	return render_template("lifeblight-residue.html")

@app.route("/weeping-midnight")
def weeping_midnight():
	return render_template("weeping-midnight.html")

@app.route("/cerulean-scourge")
def cerulean_scourge():
	return render_template("cerulean-scourge.html")

@app.route("/dragon-bile")
def dragon_bile():
	return render_template("dragon-bile.html")

@app.route("/brimstone-fumes")
def brimstone_fumes():
	return render_template("brimstone-fumes.html")

@app.route("/frenzy-oil")
def frenzy_oil():
	return render_template("frenzy-oil.html")

@app.route("/repulsion-resin")
def repulsion_resin():
	return render_template("repulsion-resin.html")

@app.route("/hemlock")
def hemlock():
	return render_template("hemlock.html")

@app.route("/kings-sleep")
def kings_sleep():
	return render_template("kings-sleep.html")

@app.route("/black-lotus-extract")
def black_lotus_extract():
	return render_template("black-lotus-extract.html")

@app.route("/oblivion-essence")
def oblivion_essence():
	return render_template("oblivion-essence.html")

@app.route("/tears-of-death")
def tears_of_death():
	return render_template("tears-of-death.html")

@app.route("/addiction")
def addiction():
	return render_template("addiction.html")

@app.route("/addiction-suppressant")
def addiction_suppressant():
	return render_template("addiction-suppressant.html")

@app.route("/antidote")
def antidote():
	return render_template("antidote.html")

@app.route("/antiplague")
def antiplague():
	return render_template("antiplague.html")

@app.route("/cheetahs-elixir")
def cheetahs_elixir():
	return render_template("cheetahs-elixir.html")

@app.route("/lastwall-soup")
def lastwall_soup():
	return render_template("lastwall-soup.html")

@app.route("/leapers-elixir")
def leapers_elixir():
	return render_template("leapers-elixir.html")

@app.route("/bestial-mutagen")
def bestial_mutagen():
	return render_template("bestial-mutagen.html")

@app.route("/cognitive-mutagen")
def cognitive_mutagen():
	return render_template("cognitive-mutagen.html")

@app.route("/drakeheart-mutagen")
def drakeheart_mutagen():
	return render_template("drakeheart-mutagen.html")

@app.route("/eagle-eye-elixir")
def eagle_eye_elixir():
	return render_template("eagle-eye-elixir.html")

@app.route("/juggernaut-mutagen")
def juggernaut_mutagen():
	return render_template("juggernaut-mutagen.html")

@app.route("/quicksilver-mutagen")
def quicksilver_mutagen():
	return render_template("quicksilver-mutagen.html")

@app.route("/energy-mutagen")
def energy_mutagen():
	return render_template("energy-mutagen.html")

@app.route("/serene-mutagen")
def serene_mutagen():
	return render_template("serene-mutagen.html")

@app.route("/silvertongue-mutagen")
def silvertongue_mutagen():
	return render_template("silvertongue-mutagen.html")

@app.route("/skeptics-elixir")
def skeptics_elixir():
	return render_template("skeptics-elixir.html")

@app.route("/sinew-shock-serum")
def sinew_shock_serum():
	return render_template("sinew-shock-serum.html")

@app.route("/darkvision-elixir")
def darkvision_elixir():
	return render_template("darkvision-elixir.html")

@app.route("/infiltrators-elixir")
def infiltrators_elixir():
	return render_template("infiltrators-elixir.html")

@app.route("/focus-cathartic")
def focus_cathartic():
	return render_template("focus-cathartic.html")

@app.route("/bravos-brew")
def bravos_brew():
	return render_template("bravos-brew.html")

@app.route("/cats-eye-elixir")
def cats_eye_elixir():
	return render_template("cats-eye-elixir.html")

@app.route("/olfactory-obfuscator")
def olfactory_obfuscator():
	return render_template("olfactory-obfuscator.html")

@app.route("/spiderfoot-brew")
def spiderfoot_brew():
	return render_template("spiderfoot-brew.html")

@app.route("/stonefist-elixir")
def stonefist_elixir():
	return render_template("stonefist-elixir.html")

@app.route("/bombers-eye-elixir")
def bombers_eye_elixir():
	return render_template("bombers-eye-elixir.html")

@app.route("/salamander-elixir")
def salamander_elixir():
	return render_template("salamander-elixir.html")

@app.route("/winter-wolf-elixir")
def winter_wolf_elixir():
	return render_template("winter-wolf-elixir.html")

@app.route("/mistform-elixir")
def mistform_elixir():
	return render_template("mistform-elixir.html")

@app.route("/sea-touch-elixir")
def sea_touch_elixir():
	return render_template("sea-touch-elixir.html")

@app.route("/stone-body-mutagen")
def stone_body_mutagen():
	return render_template("stone-body-mutagen.html")

@app.route("/malleable-mixture")
def malleable_mixture():
	return render_template("malleable-mixture.html")

@app.route("/mnemonic-acid")
def mnemonic_acid():
	return render_template("mnemonic-acid.html")

@app.route("/acid-flask")
def acid_flask():
	return render_template("acid-flask.html")

@app.route("/blight-bomb")
def blight_bomb():
	return render_template("blight-bomb.html")

@app.route("/dread-ampoule")
def dread_ampoule():
	return render_template("dread-ampoule.html")

@app.route("/ghost-charge")
def ghost_charge():
	return render_template("ghost-charge.html")

@app.route("/necrotic-bomb")
def necrotic_bomb():
	return render_template("necrotic-bomb.html")

@app.route("/peshpine-grenade")
def peshpine_grenade():
	return render_template("peshpine-grenade.html")

@app.route("/redpitch-bomb")
def redpitch_bomb():
	return render_template("redpitch-bomb.html")

@app.route("/tanglefoot-bag")
def tanglefoot_bag():
	return render_template("tanglefoot-bag.html")

@app.route("/thunderstone")
def thunderstone():
	return render_template("thunderstone.html")

@app.route("/alignment-ampoule")
def alignment_ampoule():
	return render_template("alignment-ampoule.html")

@app.route("/junk-bomb")
def junk_bomb():
	return render_template("junk-bomb.html")

@app.route("/pressure-bomb")
def pressure_bomb():
	return render_template("pressure-bomb.html")

@app.route("/sulfur-bomb")
def sulfur_bomb():
	return render_template("sulfur-bomb.html")

@app.route("/vexing-vapor")
def vexing_vapor():
	return render_template("vexing-vapor.html")

@app.route("/dwarven-daisy")
def dwarven_daisy():
	return render_template("dwarven-daisy.html")

@app.route("/blindpepper-bomb")
def blindpepper_bomb():
	return render_template("blindpepper-bomb.html")

@app.route("/frost-vial")
def frost_vial():
	return render_template("frost-vial.html")

@app.route("/base-armor-rules")
def base_armor_rules():
	return render_template("base-armor-rules.html")

@app.route("/padded-armor")
def padded_armor():
	return render_template("padded-armor.html")

@app.route("/comfort")
def comfort():
	return render_template("comfort.html")

@app.route("/leather-armor")
def leather_armor():
	return render_template("leather-armor.html")

@app.route("/studded-leather")
def studded_leather():
	return render_template("studded-leather.html")

@app.route("/flexible-9314415")
def flexible_9314415():
	return render_template("flexible-9314415.html")

@app.route("/noisy-8581790")
def noisy_8581790():
	return render_template("noisy-8581790.html")

@app.route("/chain-shirt")
def chain_shirt():
	return render_template("chain-shirt.html")

@app.route("/hide-armor")
def hide_armor():
	return render_template("hide-armor.html")

@app.route("/scale-mail")
def scale_mail():
	return render_template("scale-mail.html")

@app.route("/chain-mail")
def chain_mail():
	return render_template("chain-mail.html")

@app.route("/breastplate")
def breastplate():
	return render_template("breastplate.html")

@app.route("/splint-mail")
def splint_mail():
	return render_template("splint-mail.html")

@app.route("/half-plate")
def half_plate():
	return render_template("half-plate.html")

@app.route("/bulwark-6066934")
def bulwark_6066934():
	return render_template("bulwark-6066934.html")

@app.route("/full-plate")
def full_plate():
	return render_template("full-plate.html")

@app.route("/unarmed-strike")
def unarmed_strike():
	return render_template("unarmed-strike.html")

@app.route("/battle-lute")
def battle_lute():
	return render_template("battle-lute.html")

@app.route("/juggling-club")
def juggling_club():
	return render_template("juggling-club.html")

@app.route("/dagger")
def dagger():
	return render_template("dagger.html")

@app.route("/club")
def club():
	return render_template("club.html")

@app.route("/clan-dagger-3460910")
def clan_dagger_3460910():
	return render_template("clan-dagger-3460910.html")

@app.route("/katar")
def katar():
	return render_template("katar.html")

@app.route("/knuckle-duster")
def knuckle_duster():
	return render_template("knuckle-duster.html")

@app.route("/longspear")
def longspear():
	return render_template("longspear.html")

@app.route("/light-mace")
def light_mace():
	return render_template("light-mace.html")

@app.route("/mace")
def mace():
	return render_template("mace.html")

@app.route("/morningstar")
def morningstar():
	return render_template("morningstar.html")

@app.route("/sickle")
def sickle():
	return render_template("sickle.html")

@app.route("/spear")
def spear():
	return render_template("spear.html")

@app.route("/spiked-gauntlet")
def spiked_gauntlet():
	return render_template("spiked-gauntlet.html")

@app.route("/throwing-knife")
def throwing_knife():
	return render_template("throwing-knife.html")

@app.route("/thundermace")
def thundermace():
	return render_template("thundermace.html")

@app.route("/tri-bladed-katar")
def tri_bladed_katar():
	return render_template("tri-bladed-katar.html")

@app.route("/asp-coil")
def asp_coil():
	return render_template("asp-coil.html")

@app.route("/staff")
def staff():
	return render_template("staff.html")

@app.route("/bastard-sword")
def bastard_sword():
	return render_template("bastard-sword.html")

@app.route("/battle-axe")
def battle_axe():
	return render_template("battle-axe.html")

@app.route("/bladed-scarf")
def bladed_scarf():
	return render_template("bladed-scarf.html")

@app.route("/bo-staff")
def bo_staff():
	return render_template("bo-staff.html")

@app.route("/boarding-axe")
def boarding_axe():
	return render_template("boarding-axe.html")

@app.route("/boarding-pike")
def boarding_pike():
	return render_template("boarding-pike.html")

@app.route("/buugeng")
def buugeng():
	return render_template("buugeng.html")

@app.route("/claw-blade")
def claw_blade():
	return render_template("claw-blade.html")

@app.route("/combat-grapnel")
def combat_grapnel():
	return render_template("combat-grapnel.html")

@app.route("/dueling-spear")
def dueling_spear():
	return render_template("dueling-spear.html")

@app.route("/elven-branched-spear")
def elven_branched_spear():
	return render_template("elven-branched-spear.html")

@app.route("/elven-curved-blade")
def elven_curved_blade():
	return render_template("elven-curved-blade.html")

@app.route("/exquisite-sword-cane")
def exquisite_sword_cane():
	return render_template("exquisite-sword-cane.html")

@app.route("/exquisite-sword-cane-sheath")
def exquisite_sword_cane_sheath():
	return render_template("exquisite-sword-cane-sheath.html")

@app.route("/falchion")
def falchion():
	return render_template("falchion.html")

@app.route("/fangwire")
def fangwire():
	return render_template("fangwire.html")

@app.route("/fauchard")
def fauchard():
	return render_template("fauchard.html")

@app.route("/fighting-fan")
def fighting_fan():
	return render_template("fighting-fan.html")

@app.route("/fighting-stick")
def fighting_stick():
	return render_template("fighting-stick.html")

@app.route("/filchers-fork")
def filchers_fork():
	return render_template("filchers-fork.html")

@app.route("/flail")
def flail():
	return render_template("flail.html")

@app.route("/gaff")
def gaff():
	return render_template("gaff.html")

@app.route("/glaive")
def glaive():
	return render_template("glaive.html")

@app.route("/gnome-hooked-hammer")
def gnome_hooked_hammer():
	return render_template("gnome-hooked-hammer.html")

@app.route("/greataxe")
def greataxe():
	return render_template("greataxe.html")

@app.route("/greatclub")
def greatclub():
	return render_template("greatclub.html")

@app.route("/greatpick")
def greatpick():
	return render_template("greatpick.html")

@app.route("/greatsword")
def greatsword():
	return render_template("greatsword.html")

@app.route("/griffon-cane")
def griffon_cane():
	return render_template("griffon-cane.html")

@app.route("/guisarme")
def guisarme():
	return render_template("guisarme.html")

@app.route("/halberd")
def halberd():
	return render_template("halberd.html")

@app.route("/adze")
def adze():
	return render_template("adze.html")

@app.route("/hand-adze")
def hand_adze():
	return render_template("hand-adze.html")

@app.route("/injection-spear")
def injection_spear():
	return render_template("injection-spear.html")

@app.route("/kama")
def kama():
	return render_template("kama.html")

@app.route("/katana")
def katana():
	return render_template("katana.html")

@app.route("/khakkara")
def khakkara():
	return render_template("khakkara.html")

@app.route("/hatchet")
def hatchet():
	return render_template("hatchet.html")

@app.route("/khopesh")
def khopesh():
	return render_template("khopesh.html")

@app.route("/kukri")
def kukri():
	return render_template("kukri.html")

@app.route("/kusarigama")
def kusarigama():
	return render_template("kusarigama.html")

@app.route("/lance")
def lance():
	return render_template("lance.html")

@app.route("/leiomana")
def leiomana():
	return render_template("leiomana.html")

@app.route("/light-hammer")
def light_hammer():
	return render_template("light-hammer.html")

@app.route("/lion-scythe")
def lion_scythe():
	return render_template("lion-scythe.html")

@app.route("/longsword")
def longsword():
	return render_template("longsword.html")

@app.route("/machete")
def machete():
	return render_template("machete.html")

@app.route("/main-gauche")
def main_gauche():
	return render_template("main-gauche.html")

@app.route("/mambele")
def mambele():
	return render_template("mambele.html")

@app.route("/maul")
def maul():
	return render_template("maul.html")

@app.route("/meteor-hammer")
def meteor_hammer():
	return render_template("meteor-hammer.html")

@app.route("/monkeys-fist")
def monkeys_fist():
	return render_template("monkeys-fist.html")

@app.route("/naginata")
def naginata():
	return render_template("naginata.html")

@app.route("/nine-ring-sword")
def nine_ring_sword():
	return render_template("nine-ring-sword.html")

@app.route("/nunchuku")
def nunchuku():
	return render_template("nunchuku.html")

@app.route("/ogre-hook")
def ogre_hook():
	return render_template("ogre-hook.html")

@app.route("/orc-knuckle-dagger")
def orc_knuckle_dagger():
	return render_template("orc-knuckle-dagger.html")

@app.route("/pick")
def pick():
	return render_template("pick.html")

@app.route("/piranha-kiss")
def piranha_kiss():
	return render_template("piranha-kiss.html")

@app.route("/polytool")
def polytool():
	return render_template("polytool.html")

@app.route("/probing-cane")
def probing_cane():
	return render_template("probing-cane.html")

@app.route("/ranseur")
def ranseur():
	return render_template("ranseur.html")

@app.route("/rapier")
def rapier():
	return render_template("rapier.html")

@app.route("/rungu")
def rungu():
	return render_template("rungu.html")

@app.route("/sai")
def sai():
	return render_template("sai.html")

@app.route("/sap")
def sap():
	return render_template("sap.html")

@app.route("/scimitar")
def scimitar():
	return render_template("scimitar.html")

@app.route("/scorpion-whip")
def scorpion_whip():
	return render_template("scorpion-whip.html")

@app.route("/scourge")
def scourge():
	return render_template("scourge.html")

@app.route("/scythe")
def scythe():
	return render_template("scythe.html")

@app.route("/shauth-blade")
def shauth_blade():
	return render_template("shauth-blade.html")

@app.route("/shield-bash")
def shield_bash():
	return render_template("shield-bash.html")

@app.route("/shield-boss")
def shield_boss():
	return render_template("shield-boss.html")

@app.route("/shield-spikes")
def shield_spikes():
	return render_template("shield-spikes.html")

@app.route("/shortsword")
def shortsword():
	return render_template("shortsword.html")

@app.route("/spiked-chain")
def spiked_chain():
	return render_template("spiked-chain.html")

@app.route("/starknife")
def starknife():
	return render_template("starknife.html")

@app.route("/sword-cane")
def sword_cane():
	return render_template("sword-cane.html")

@app.route("/tekko-kagi")
def tekko_kagi():
	return render_template("tekko-kagi.html")

@app.route("/temple-sword")
def temple_sword():
	return render_template("temple-sword.html")

@app.route("/tengu-gale-blade")
def tengu_gale_blade():
	return render_template("tengu-gale-blade.html")

@app.route("/tonfa")
def tonfa():
	return render_template("tonfa.html")

@app.route("/trident")
def trident():
	return render_template("trident.html")

@app.route("/umbrella-injector")
def umbrella_injector():
	return render_template("umbrella-injector.html")

@app.route("/urumi")
def urumi():
	return render_template("urumi.html")

@app.route("/wakizashi")
def wakizashi():
	return render_template("wakizashi.html")

@app.route("/war-flail")
def war_flail():
	return render_template("war-flail.html")

@app.route("/war-razor")
def war_razor():
	return render_template("war-razor.html")

@app.route("/warhammer")
def warhammer():
	return render_template("warhammer.html")

@app.route("/whip")
def whip():
	return render_template("whip.html")

@app.route("/wish-blade")
def wish_blade():
	return render_template("wish-blade.html")

@app.route("/wish-knife")
def wish_knife():
	return render_template("wish-knife.html")

@app.route("/aklys")
def aklys():
	return render_template("aklys.html")

@app.route("/aldori-dueling-sword")
def aldori_dueling_sword():
	return render_template("aldori-dueling-sword.html")

@app.route("/bladed-diabolo")
def bladed_diabolo():
	return render_template("bladed-diabolo.html")

@app.route("/bladed-hoop")
def bladed_hoop():
	return render_template("bladed-hoop.html")

@app.route("/butchering-axe")
def butchering_axe():
	return render_template("butchering-axe.html")

@app.route("/butterfly-sword")
def butterfly_sword():
	return render_template("butterfly-sword.html")

@app.route("/dwarven-war-axe")
def dwarven_war_axe():
	return render_template("dwarven-war-axe.html")

@app.route("/hook-sword")
def hook_sword():
	return render_template("hook-sword.html")

@app.route("/karambit")
def karambit():
	return render_template("karambit.html")

@app.route("/orc-necksplitter")
def orc_necksplitter():
	return render_template("orc-necksplitter.html")

@app.route("/rhoka-sword")
def rhoka_sword():
	return render_template("rhoka-sword.html")

@app.route("/sawtooth-saber")
def sawtooth_saber():
	return render_template("sawtooth-saber.html")

@app.route("/shauth-lash")
def shauth_lash():
	return render_template("shauth-lash.html")

@app.route("/sickle-saber")
def sickle_saber():
	return render_template("sickle-saber.html")

@app.route("/spiral-rapier")
def spiral_rapier():
	return render_template("spiral-rapier.html")

@app.route("/switchscythe")
def switchscythe():
	return render_template("switchscythe.html")

@app.route("/tamchal-chakram")
def tamchal_chakram():
	return render_template("tamchal-chakram.html")

@app.route("/tricky-pick")
def tricky_pick():
	return render_template("tricky-pick.html")

@app.route("/whip-claw")
def whip_claw():
	return render_template("whip-claw.html")

@app.route("/wind-and-fire-wheel")
def wind_and_fire_wheel():
	return render_template("wind-and-fire-wheel.html")

@app.route("/alchemical-crossbow")
def alchemical_crossbow():
	return render_template("alchemical-crossbow.html")

@app.route("/arrows")
def arrows():
	return render_template("arrows.html")

@app.route("/blowgun-darts")
def blowgun_darts():
	return render_template("blowgun-darts.html")

@app.route("/bolts")
def bolts():
	return render_template("bolts.html")

@app.route("/sling-bullets")
def sling_bullets():
	return render_template("sling-bullets.html")

@app.route("/blowgun")
def blowgun():
	return render_template("blowgun.html")

@app.route("/heavy-crossbow")
def heavy_crossbow():
	return render_template("heavy-crossbow.html")

@app.route("/hand-crossbow")
def hand_crossbow():
	return render_template("hand-crossbow.html")

@app.route("/dart")
def dart():
	return render_template("dart.html")

@app.route("/crossbow")
def crossbow():
	return render_template("crossbow.html")

@app.route("/javelin")
def javelin():
	return render_template("javelin.html")

@app.route("/sling")
def sling():
	return render_template("sling.html")

@app.route("/alchemical-bomb")
def alchemical_bomb():
	return render_template("alchemical-bomb.html")

@app.route("/bola")
def bola():
	return render_template("bola.html")

@app.route("/chakram")
def chakram():
	return render_template("chakram.html")

@app.route("/composite-longbow")
def composite_longbow():
	return render_template("composite-longbow.html")

@app.route("/composite-shortbow")
def composite_shortbow():
	return render_template("composite-shortbow.html")

@app.route("/halfling-slingstaff")
def halfling_slingstaff():
	return render_template("halfling-slingstaff.html")

@app.route("/shortbow")
def shortbow():
	return render_template("shortbow.html")

@app.route("/shuriken")
def shuriken():
	return render_template("shuriken.html")

@app.route("/sun-shot")
def sun_shot():
	return render_template("sun-shot.html")

@app.route("/thunder-sling")
def thunder_sling():
	return render_template("thunder-sling.html")

@app.route("/wooden-taws")
def wooden_taws():
	return render_template("wooden-taws.html")

@app.route("/daikyu")
def daikyu():
	return render_template("daikyu.html")

@app.route("/hongali-hornbow")
def hongali_hornbow():
	return render_template("hongali-hornbow.html")

@app.route("/taw-launcher")
def taw_launcher():
	return render_template("taw-launcher.html")

@app.route("/resonant")
def resonant():
	return render_template("resonant.html")

@app.route("/free-hand-4441605")
def free_hand_4441605():
	return render_template("free-hand-4441605.html")

@app.route("/holly-and-mistletoe")
def holly_and_mistletoe():
	return render_template("holly-and-mistletoe.html")

@app.route("/puzzle-box")
def puzzle_box():
	return render_template("puzzle-box.html")

@app.route("/candle")
def candle():
	return render_template("candle.html")

@app.route("/chalk")
def chalk():
	return render_template("chalk.html")

@app.route("/clay")
def clay():
	return render_template("clay.html")

@app.route("/oil")
def oil():
	return render_template("oil.html")

@app.route("/sack")
def sack():
	return render_template("sack.html")

@app.route("/ten-foot-pole")
def ten_foot_pole():
	return render_template("ten-foot-pole.html")

@app.route("/torch")
def torch():
	return render_template("torch.html")

@app.route("/bedroll")
def bedroll():
	return render_template("bedroll.html")

@app.route("/soap")
def soap():
	return render_template("soap.html")

@app.route("/ball")
def ball():
	return render_template("ball.html")

@app.route("/ladder")
def ladder():
	return render_template("ladder.html")

@app.route("/kite")
def kite():
	return render_template("kite.html")

@app.route("/bandalore")
def bandalore():
	return render_template("bandalore.html")

@app.route("/flint-and-steel")
def flint_and_steel():
	return render_template("flint-and-steel.html")

@app.route("/water-purifier")
def water_purifier():
	return render_template("water-purifier.html")

@app.route("/mask")
def mask():
	return render_template("mask.html")

@app.route("/waterskin")
def waterskin():
	return render_template("waterskin.html")

@app.route("/signal-whistle")
def signal_whistle():
	return render_template("signal-whistle.html")

@app.route("/air-bladder")
def air_bladder():
	return render_template("air-bladder.html")

@app.route("/backpack")
def backpack():
	return render_template("backpack.html")

@app.route("/blocks")
def blocks():
	return render_template("blocks.html")

@app.route("/clothing")
def clothing():
	return render_template("clothing.html")

@app.route("/disguise-kit")
def disguise_kit():
	return render_template("disguise-kit.html")

@app.route("/doll")
def doll():
	return render_template("doll.html")

@app.route("/grappling-hook")
def grappling_hook():
	return render_template("grappling-hook.html")

@app.route("/hammer")
def hammer():
	return render_template("hammer.html")

@app.route("/powder")
def powder():
	return render_template("powder.html")

@app.route("/religious-symbol")
def religious_symbol():
	return render_template("religious-symbol.html")

@app.route("/shield-sconce")
def shield_sconce():
	return render_template("shield-sconce.html")

@app.route("/writing-set")
def writing_set():
	return render_template("writing-set.html")

@app.route("/grappling-arrow")
def grappling_arrow():
	return render_template("grappling-arrow.html")

@app.route("/lock-4874732")
def lock_4874732():
	return render_template("lock-4874732.html")

@app.route("/marbles")
def marbles():
	return render_template("marbles.html")

@app.route("/merchant-scale")
def merchant_scale():
	return render_template("merchant-scale.html")

@app.route("/saddlebags")
def saddlebags():
	return render_template("saddlebags.html")

@app.route("/caltrops")
def caltrops():
	return render_template("caltrops.html")

@app.route("/manacles")
def manacles():
	return render_template("manacles.html")

@app.route("/thieves-tools")
def thieves_tools():
	return render_template("thieves-tools.html")

@app.route("/rations")
def rations():
	return render_template("rations.html")

@app.route("/tool")
def tool():
	return render_template("tool.html")

@app.route("/climbing-kit")
def climbing_kit():
	return render_template("climbing-kit.html")

@app.route("/crowbar")
def crowbar():
	return render_template("crowbar.html")

@app.route("/dueling-cape")
def dueling_cape():
	return render_template("dueling-cape.html")

@app.route("/games")
def games():
	return render_template("games.html")

@app.route("/material-component-pouch")
def material_component_pouch():
	return render_template("material-component-pouch.html")

@app.route("/parrying-scabbard")
def parrying_scabbard():
	return render_template("parrying-scabbard.html")

@app.route("/playing-cards")
def playing_cards():
	return render_template("playing-cards.html")

@app.route("/rope")
def rope():
	return render_template("rope.html")

@app.route("/tear-away-clothing")
def tear_away_clothing():
	return render_template("tear-away-clothing.html")

@app.route("/windup-toy-carriage")
def windup_toy_carriage():
	return render_template("windup-toy-carriage.html")

@app.route("/wheelbarrow")
def wheelbarrow():
	return render_template("wheelbarrow.html")

@app.route("/chest")
def chest():
	return render_template("chest.html")

@app.route("/lantern")
def lantern():
	return render_template("lantern.html")

@app.route("/fishing-tackle")
def fishing_tackle():
	return render_template("fishing-tackle.html")

@app.route("/musical-instrument")
def musical_instrument():
	return render_template("musical-instrument.html")

@app.route("/tent")
def tent():
	return render_template("tent.html")

@app.route("/brass-ear")
def brass_ear():
	return render_template("brass-ear.html")

@app.route("/compass")
def compass():
	return render_template("compass.html")

@app.route("/cookware")
def cookware():
	return render_template("cookware.html")

@app.route("/depth-gauge")
def depth_gauge():
	return render_template("depth-gauge.html")

@app.route("/mirror")
def mirror():
	return render_template("mirror.html")

@app.route("/net")
def net():
	return render_template("net.html")

@app.route("/paint-set")
def paint_set():
	return render_template("paint-set.html")

@app.route("/religious-text")
def religious_text():
	return render_template("religious-text.html")

@app.route("/rubbing-set")
def rubbing_set():
	return render_template("rubbing-set.html")

@app.route("/wax-key-blank")
def wax_key_blank():
	return render_template("wax-key-blank.html")

@app.route("/adventurers-pack")
def adventurers_pack():
	return render_template("adventurers-pack.html")

@app.route("/extendible-pincer")
def extendible_pincer():
	return render_template("extendible-pincer.html")

@app.route("/jellyfish-lamp")
def jellyfish_lamp():
	return render_template("jellyfish-lamp.html")

@app.route("/repair-kit")
def repair_kit():
	return render_template("repair-kit.html")

@app.route("/alchemists-tools")
def alchemists_tools():
	return render_template("alchemists-tools.html")

@app.route("/comealong")
def comealong():
	return render_template("comealong.html")

@app.route("/folding-ladder")
def folding_ladder():
	return render_template("folding-ladder.html")

@app.route("/grappling-gun")
def grappling_gun():
	return render_template("grappling-gun.html")

@app.route("/hourglass")
def hourglass():
	return render_template("hourglass.html")

@app.route("/artisans-tools")
def artisans_tools():
	return render_template("artisans-tools.html")

@app.route("/chain")
def chain():
	return render_template("chain.html")

@app.route("/tack")
def tack():
	return render_template("tack.html")

@app.route("/alchemists-lab")
def alchemists_lab():
	return render_template("alchemists-lab.html")

@app.route("/buoyancy-vest")
def buoyancy_vest():
	return render_template("buoyancy-vest.html")

@app.route("/familiar-satchel")
def familiar_satchel():
	return render_template("familiar-satchel.html")

@app.route("/glass-cutter")
def glass_cutter():
	return render_template("glass-cutter.html")

@app.route("/healers-tools")
def healers_tools():
	return render_template("healers-tools.html")

@app.route("/snare-kit")
def snare_kit():
	return render_template("snare-kit.html")

@app.route("/swim-fins")
def swim_fins():
	return render_template("swim-fins.html")

@app.route("/false-manacles")
def false_manacles():
	return render_template("false-manacles.html")

@app.route("/snowshoes")
def snowshoes():
	return render_template("snowshoes.html")

@app.route("/clockwork-dial")
def clockwork_dial():
	return render_template("clockwork-dial.html")

@app.route("/spyglass")
def spyglass():
	return render_template("spyglass.html")

@app.route("/igniter")
def igniter():
	return render_template("igniter.html")

@app.route("/waterproof-journal")
def waterproof_journal():
	return render_template("waterproof-journal.html")

@app.route("/communication-bangle")
def communication_bangle():
	return render_template("communication-bangle.html")

@app.route("/mechanical-torch")
def mechanical_torch():
	return render_template("mechanical-torch.html")

@app.route("/timepiece")
def timepiece():
	return render_template("timepiece.html")

@app.route("/clockwork-megaphone")
def clockwork_megaphone():
	return render_template("clockwork-megaphone.html")

@app.route("/deployable-cover")
def deployable_cover():
	return render_template("deployable-cover.html")

@app.route("/swarmsuit")
def swarmsuit():
	return render_template("swarmsuit.html")

@app.route("/book-of-translation")
def book_of_translation():
	return render_template("book-of-translation.html")

@app.route("/experimental-clothing")
def experimental_clothing():
	return render_template("experimental-clothing.html")

@app.route("/periscope")
def periscope():
	return render_template("periscope.html")

@app.route("/day-goggles")
def day_goggles():
	return render_template("day-goggles.html")

@app.route("/sturdy-satchel")
def sturdy_satchel():
	return render_template("sturdy-satchel.html")

@app.route("/scholarly-journal")
def scholarly_journal():
	return render_template("scholarly-journal.html")

@app.route("/camouflage-suit")
def camouflage_suit():
	return render_template("camouflage-suit.html")

@app.route("/recovery-bladder")
def recovery_bladder():
	return render_template("recovery-bladder.html")

@app.route("/survey-map")
def survey_map():
	return render_template("survey-map.html")

@app.route("/portable-ram")
def portable_ram():
	return render_template("portable-ram.html")

@app.route("/smoked-goggles")
def smoked_goggles():
	return render_template("smoked-goggles.html")

@app.route("/concealed-sheath")
def concealed_sheath():
	return render_template("concealed-sheath.html")

@app.route("/detectives-kit")
def detectives_kit():
	return render_template("detectives-kit.html")

@app.route("/fingerprinting-kit")
def fingerprinting_kit():
	return render_template("fingerprinting-kit.html")

@app.route("/handcuffs")
def handcuffs():
	return render_template("handcuffs.html")

@app.route("/magnifying-glass")
def magnifying_glass():
	return render_template("magnifying-glass.html")

@app.route("/cartographers-kit")
def cartographers_kit():
	return render_template("cartographers-kit.html")

@app.route("/pickpockets-tailoring")
def pickpockets_tailoring():
	return render_template("pickpockets-tailoring.html")

@app.route("/piton")
def piton():
	return render_template("piton.html")

@app.route("/grappling-bolt")
def grappling_bolt():
	return render_template("grappling-bolt.html")

@app.route("/astrolabe")
def astrolabe():
	return render_template("astrolabe.html")

@app.route("/fake-blood-pack")
def fake_blood_pack():
	return render_template("fake-blood-pack.html")

@app.route("/alchemical-drugs")
def alchemical_drugs():
	return render_template("alchemical-drugs.html")

@app.route("/sneezing-powder")
def sneezing_powder():
	return render_template("sneezing-powder.html")

@app.route("/lethargy-poison-2242769")
def lethargy_poison_2242769():
	return render_template("lethargy-poison-2242769.html")

@app.route("/stupor-poison")
def stupor_poison():
	return render_template("stupor-poison.html")

@app.route("/shadow-essence")
def shadow_essence():
	return render_template("shadow-essence.html")

@app.route("/purple-worm-venom")
def purple_worm_venom():
	return render_template("purple-worm-venom.html")

@app.route("/nightmare-vapor")
def nightmare_vapor():
	return render_template("nightmare-vapor.html")

@app.route("/alchemical-poisons")
def alchemical_poisons():
	return render_template("alchemical-poisons.html")

@app.route("/comprehension-elixir")
def comprehension_elixir():
	return render_template("comprehension-elixir.html")

@app.route("/alchemists-fire")
def alchemists_fire():
	return render_template("alchemists-fire.html")

@app.route("/bottled-lightning")
def bottled_lightning():
	return render_template("bottled-lightning.html")

@app.route("/alchemical-bombs")
def alchemical_bombs():
	return render_template("alchemical-bombs.html")

@app.route("/all-spells")
def all_spells():
	return render_template("all-spells.html")

@app.route("/quench")
def quench():
	return render_template("quench.html")

@app.route("/radiant-field")
def radiant_field():
	return render_template("radiant-field.html")

@app.route("/darkvision-5323541")
def darkvision_5323541():
	return render_template("darkvision-5323541.html")

@app.route("/rapid-adaptation")
def rapid_adaptation():
	return render_template("rapid-adaptation.html")

@app.route("/reapers-lantern")
def reapers_lantern():
	return render_template("reapers-lantern.html")

@app.route("/remove-fear")
def remove_fear():
	return render_template("remove-fear.html")

@app.route("/historic-allies")
def historic_allies():
	return render_template("historic-allies.html")

@app.route("/killjoy")
def killjoy():
	return render_template("killjoy.html")

@app.route("/duty")
def duty():
	return render_template("duty.html")

@app.route("/selfish")
def selfish():
	return render_template("selfish.html")

@app.route("/research-ritualized-casting")
def research_ritualized_casting():
	return render_template("research-ritualized-casting.html")

@app.route("/bulk-and-lifting")
def bulk_and_lifting():
	return render_template("bulk-and-lifting.html")

@app.route("/ghoul")
def ghoul():
	return render_template("ghoul.html")

@app.route("/plague-zombie")
def plague_zombie():
	return render_template("plague-zombie.html")

@app.route("/flaming-skull")
def flaming_skull():
	return render_template("flaming-skull.html")

@app.route("/skeletal-champion")
def skeletal_champion():
	return render_template("skeletal-champion.html")

@app.route("/zombie-brute")
def zombie_brute():
	return render_template("zombie-brute.html")

@app.route("/mummy-guardian")
def mummy_guardian():
	return render_template("mummy-guardian.html")

@app.route("/shadow")
def shadow():
	return render_template("shadow.html")

@app.route("/zombie-hulk")
def zombie_hulk():
	return render_template("zombie-hulk.html")

@app.route("/dread-wraith")
def dread_wraith():
	return render_template("dread-wraith.html")

@app.route("/graveknight")
def graveknight():
	return render_template("graveknight.html")

@app.route("/mohrg")
def mohrg():
	return render_template("mohrg.html")

@app.route("/fell-rider")
def fell_rider():
	return render_template("fell-rider.html")

@app.route("/beast-tamer")
def beast_tamer():
	return render_template("beast-tamer.html")

@app.route("/polyglot")
def polyglot():
	return render_template("polyglot.html")

@app.route("/unassuming-dedication")
def unassuming_dedication():
	return render_template("unassuming-dedication.html")

@app.route("/undead-companion")
def undead_companion():
	return render_template("undead-companion.html")

@app.route("/defy-the-darkness")
def defy_the_darkness():
	return render_template("defy-the-darkness.html")

@app.route("/corgi-mount")
def corgi_mount():
	return render_template("corgi-mount.html")

@app.route("/tupilaq-carver")
def tupilaq_carver():
	return render_template("tupilaq-carver.html")

@app.route("/animate-dead")
def animate_dead():
	return render_template("animate-dead.html")

@app.route("/phantom-steed")
def phantom_steed():
	return render_template("phantom-steed.html")

@app.route("/summon-instrument")
def summon_instrument():
	return render_template("summon-instrument.html")

@app.route("/crystal-shards")
def crystal_shards():
	return render_template("crystal-shards.html")

@app.route("/concecrate")
def concecrate():
	return render_template("concecrate.html")

@app.route("/elemental-sentinel")
def elemental_sentinel():
	return render_template("elemental-sentinel.html")

@app.route("/fey-abeyance")
def fey_abeyance():
	return render_template("fey-abeyance.html")

@app.route("/heartbond")
def heartbond():
	return render_template("heartbond.html")

@app.route("/arcane-weaving")
def arcane_weaving():
	return render_template("arcane-weaving.html")

@app.route("/atone")
def atone():
	return render_template("atone.html")

@app.route("/awaken-portal")
def awaken_portal():
	return render_template("awaken-portal.html")

@app.route("/blight")
def blight():
	return render_template("blight.html")

@app.route("/repair-public-work")
def repair_public_work():
	return render_template("repair-public-work.html")

@app.route("/concealments-curtain")
def concealments_curtain():
	return render_template("concealments-curtain.html")

@app.route("/geas")
def geas():
	return render_template("geas.html")

@app.route("/guardians-aegis")
def guardians_aegis():
	return render_template("guardians-aegis.html")

@app.route("/mystic-carriage")
def mystic_carriage():
	return render_template("mystic-carriage.html")

@app.route("/plant-growth")
def plant_growth():
	return render_template("plant-growth.html")

@app.route("/rest-eternal")
def rest_eternal():
	return render_template("rest-eternal.html")

@app.route("/simulacrum")
def simulacrum():
	return render_template("simulacrum.html")

@app.route("/tattoo-whisperers")
def tattoo_whisperers():
	return render_template("tattoo-whisperers.html")

@app.route("/unseen-custodians")
def unseen_custodians():
	return render_template("unseen-custodians.html")

@app.route("/asmodean-wager")
def asmodean_wager():
	return render_template("asmodean-wager.html")

@app.route("/astral-projection")
def astral_projection():
	return render_template("astral-projection.html")

@app.route("/awaken-animal")
def awaken_animal():
	return render_template("awaken-animal.html")

@app.route("/awaken-object")
def awaken_object():
	return render_template("awaken-object.html")

@app.route("/call-spirit")
def call_spirit():
	return render_template("call-spirit.html")

@app.route("/commune")
def commune():
	return render_template("commune.html")

@app.route("/commune-with-nature")
def commune_with_nature():
	return render_template("commune-with-nature.html")

@app.route("/dread-ambience")
def dread_ambience():
	return render_template("dread-ambience.html")

@app.route("/ideal-mimicry")
def ideal_mimicry():
	return render_template("ideal-mimicry.html")

@app.route("/mind-swap")
def mind_swap():
	return render_template("mind-swap.html")

@app.route("/mosquito-blight")
def mosquito_blight():
	return render_template("mosquito-blight.html")

@app.route("/planar-ally")
def planar_ally():
	return render_template("planar-ally.html")

@app.route("/primal-call")
def primal_call():
	return render_template("primal-call.html")

@app.route("/statuette")
def statuette():
	return render_template("statuette.html")

@app.route("/terminate-bloodline")
def terminate_bloodline():
	return render_template("terminate-bloodline.html")

@app.route("/the-worlds-a-stage")
def the_worlds_a_stage():
	return render_template("the-worlds-a-stage.html")

@app.route("/waters-of-prediction")
def waters_of_prediction():
	return render_template("waters-of-prediction.html")

@app.route("/ward-domain")
def ward_domain():
	return render_template("ward-domain.html")

@app.route("/bathe-in-blood")
def bathe_in_blood():
	return render_template("bathe-in-blood.html")

@app.route("/control-weather")
def control_weather():
	return render_template("control-weather.html")

@app.route("/planar-traits")
def planar_traits():
	return render_template("planar-traits.html")

@app.route("/create-demiplane")
def create_demiplane():
	return render_template("create-demiplane.html")

@app.route("/freedom")
def freedom():
	return render_template("freedom.html")

@app.route("/imprisonment")
def imprisonment():
	return render_template("imprisonment.html")

@app.route("/legend-lore")
def legend_lore():
	return render_template("legend-lore.html")

@app.route("/remove-greater-curse")
def remove_greater_curse():
	return render_template("remove-greater-curse.html")

@app.route("/summoned")
def summoned():
	return render_template("summoned.html")

@app.route("/summon-elemental")
def summon_elemental():
	return render_template("summon-elemental.html")

@app.route("/chromatic-wall")
def chromatic_wall():
	return render_template("chromatic-wall.html")

@app.route("/prismatic-spray")
def prismatic_spray():
	return render_template("prismatic-spray.html")

@app.route("/maze-of-locked-doors")
def maze_of_locked_doors():
	return render_template("maze-of-locked-doors.html")

@app.route("/maze")
def maze():
	return render_template("maze.html")

@app.route("/magnificent-mansion")
def magnificent_mansion():
	return render_template("magnificent-mansion.html")

@app.route("/righteous-might")
def righteous_might():
	return render_template("righteous-might.html")

@app.route("/gray-shadow")
def gray_shadow():
	return render_template("gray-shadow.html")

@app.route("/mimic")
def mimic():
	return render_template("mimic.html")

@app.route("/ravenous-portal")
def ravenous_portal():
	return render_template("ravenous-portal.html")

@app.route("/knock")
def knock():
	return render_template("knock.html")

@app.route("/imprint-message")
def imprint_message():
	return render_template("imprint-message.html")

@app.route("/familiar")
def familiar():
	return render_template("familiar.html")

@app.route("/sleep-eldritch-arrow")
def sleep_eldritch_arrow():
	return render_template("sleep-eldritch-arrow.html")

@app.route("/unfolding-wind-rush")
def unfolding_wind_rush():
	return render_template("unfolding-wind-rush.html")

@app.route("/quaking-stomp")
def quaking_stomp():
	return render_template("quaking-stomp.html")

@app.route("/dragon-transformation")
def dragon_transformation():
	return render_template("dragon-transformation.html")

@app.route("/animal-rage")
def animal_rage():
	return render_template("animal-rage.html")

@app.route("/parry-and-riposte")
def parry_and_riposte():
	return render_template("parry-and-riposte.html")

@app.route("/legendary-shot")
def legendary_shot():
	return render_template("legendary-shot.html")

@app.route("/rangers-twin-riposte")
def rangers_twin_riposte():
	return render_template("rangers-twin-riposte.html")

@app.route("/mantis-form")
def mantis_form():
	return render_template("mantis-form.html")

@app.route("/vexing-tumble")
def vexing_tumble():
	return render_template("vexing-tumble.html")

@app.route("/nameless-anonymity")
def nameless_anonymity():
	return render_template("nameless-anonymity.html")

@app.route("/hidden-paragon")
def hidden_paragon():
	return render_template("hidden-paragon.html")

@app.route("/shadow-magic-dance-of-darkness")
def shadow_magic_dance_of_darkness():
	return render_template("shadow-magic-dance-of-darkness.html")

@app.route("/shadow-illusion")
def shadow_illusion():
	return render_template("shadow-illusion.html")

@app.route("/fey-caller")
def fey_caller():
	return render_template("fey-caller.html")

@app.route("/detect-magic")
def detect_magic():
	return render_template("detect-magic.html")

@app.route("/spell-tinker")
def spell_tinker():
	return render_template("spell-tinker.html")

@app.route("/interweave-dispel")
def interweave_dispel():
	return render_template("interweave-dispel.html")

@app.route("/elaborate-flourish")
def elaborate_flourish():
	return render_template("elaborate-flourish.html")

@app.route("/swift-banishment")
def swift_banishment():
	return render_template("swift-banishment.html")

@app.route("/aberrant-bloodline")
def aberrant_bloodline():
	return render_template("aberrant-bloodline.html")

@app.route("/form-retention")
def form_retention():
	return render_template("form-retention.html")

@app.route("/command-undead")
def command_undead():
	return render_template("command-undead.html")

@app.route("/persistent-creation")
def persistent_creation():
	return render_template("persistent-creation.html")

@app.route("/magical-scholastics")
def magical_scholastics():
	return render_template("magical-scholastics.html")

@app.route("/greater-magical-scholastics")
def greater_magical_scholastics():
	return render_template("greater-magical-scholastics.html")

@app.route("/eternal-blessing")
def eternal_blessing():
	return render_template("eternal-blessing.html")

@app.route("/holy-water")
def holy_water():
	return render_template("holy-water.html")

@app.route("/sanctify-water")
def sanctify_water():
	return render_template("sanctify-water.html")

@app.route("/undead-bloodline-focus-undeaths-blessing")
def undead_bloodline_focus_undeaths_blessing():
	return render_template("undead-bloodline-focus-undeaths-blessing.html")

@app.route("/angelic-bloodline-focus-angelic-wings")
def angelic_bloodline_focus_angelic_wings():
	return render_template("angelic-bloodline-focus-angelic-wings.html")

@app.route("/read-disaster")
def read_disaster():
	return render_template("read-disaster.html")

@app.route("/true-perception")
def true_perception():
	return render_template("true-perception.html")

@app.route("/lesson-of-mischief")
def lesson_of_mischief():
	return render_template("lesson-of-mischief.html")

@app.route("/familiar-form")
def familiar_form():
	return render_template("familiar-form.html")

@app.route("/plant-shape-3221644")
def plant_shape_3221644():
	return render_template("plant-shape-3221644.html")

@app.route("/rangers-bramble")
def rangers_bramble():
	return render_template("rangers-bramble.html")

@app.route("/thousand-faces")
def thousand_faces():
	return render_template("thousand-faces.html")

@app.route("/dragon-shape")
def dragon_shape():
	return render_template("dragon-shape.html")

@app.route("/monstrocity-shape")
def monstrocity_shape():
	return render_template("monstrocity-shape.html")

@app.route("/soaring-shape")
def soaring_shape():
	return render_template("soaring-shape.html")

@app.route("/ferocious-shape")
def ferocious_shape():
	return render_template("ferocious-shape.html")

@app.route("/elemental-shape")
def elemental_shape():
	return render_template("elemental-shape.html")

@app.route("/wild-shape")
def wild_shape():
	return render_template("wild-shape.html")

@app.route("/verdant-metamorphosis")
def verdant_metamorphosis():
	return render_template("verdant-metamorphosis.html")

@app.route("/green-tongue")
def green_tongue():
	return render_template("green-tongue.html")

@app.route("/mounted-shield")
def mounted_shield():
	return render_template("mounted-shield.html")

@app.route("/stormwind-flight")
def stormwind_flight():
	return render_template("stormwind-flight.html")

@app.route("/swarm-domain-swarm-sense")
def swarm_domain_swarm_sense():
	return render_template("swarm-domain-swarm-sense.html")

@app.route("/invoke-disaster")
def invoke_disaster():
	return render_template("invoke-disaster.html")

@app.route("/wind-caller")
def wind_caller():
	return render_template("wind-caller.html")

@app.route("/impaling-briars")
def impaling_briars():
	return render_template("impaling-briars.html")

@app.route("/fey-bloodline-focus-fey-glamour")
def fey_bloodline_focus_fey_glamour():
	return render_template("fey-bloodline-focus-fey-glamour.html")

@app.route("/bonded-guardian")
def bonded_guardian():
	return render_template("bonded-guardian.html")

@app.route("/beast-speaker")
def beast_speaker():
	return render_template("beast-speaker.html")

@app.route("/stealthy-companion")
def stealthy_companion():
	return render_template("stealthy-companion.html")

@app.route("/talented-companion")
def talented_companion():
	return render_template("talented-companion.html")

@app.route("/animal-companion")
def animal_companion():
	return render_template("animal-companion.html")

@app.route("/tyranny-domain-commanding-lash")
def tyranny_domain_commanding_lash():
	return render_template("tyranny-domain-commanding-lash.html")

@app.route("/minion-guise")
def minion_guise():
	return render_template("minion-guise.html")

@app.route("/perfect-distraction")
def perfect_distraction():
	return render_template("perfect-distraction.html")

@app.route("/snare-rules")
def snare_rules():
	return render_template("snare-rules.html")

@app.route("/alarm-snare")
def alarm_snare():
	return render_template("alarm-snare.html")

@app.route("/appetizing-flavor-snare")
def appetizing_flavor_snare():
	return render_template("appetizing-flavor-snare.html")

@app.route("/caltrop-snare")
def caltrop_snare():
	return render_template("caltrop-snare.html")

@app.route("/dust-pods")
def dust_pods():
	return render_template("dust-pods.html")

@app.route("/hampering-snare")
def hampering_snare():
	return render_template("hampering-snare.html")

@app.route("/marking-snare")
def marking_snare():
	return render_template("marking-snare.html")

@app.route("/signaling-snare")
def signaling_snare():
	return render_template("signaling-snare.html")

@app.route("/spike-snare")
def spike_snare():
	return render_template("spike-snare.html")

@app.route("/flare-snare")
def flare_snare():
	return render_template("flare-snare.html")

@app.route("/deadweight-snare")
def deadweight_snare():
	return render_template("deadweight-snare.html")

@app.route("/expulsion-snare")
def expulsion_snare():
	return render_template("expulsion-snare.html")

@app.route("/noisemaker-snare")
def noisemaker_snare():
	return render_template("noisemaker-snare.html")

@app.route("/static-snare")
def static_snare():
	return render_template("static-snare.html")

@app.route("/thunder-snare")
def thunder_snare():
	return render_template("thunder-snare.html")

@app.route("/clockwork-chirper")
def clockwork_chirper():
	return render_template("clockwork-chirper.html")

@app.route("/rock-ripper-snare")
def rock_ripper_snare():
	return render_template("rock-ripper-snare.html")

@app.route("/grasping-tree")
def grasping_tree():
	return render_template("grasping-tree.html")

@app.route("/torrent-snare")
def torrent_snare():
	return render_template("torrent-snare.html")

@app.route("/fire-box")
def fire_box():
	return render_template("fire-box.html")

@app.route("/detonating-gears-snare")
def detonating_gears_snare():
	return render_template("detonating-gears-snare.html")

@app.route("/acid-spitter")
def acid_spitter():
	return render_template("acid-spitter.html")

@app.route("/biting-snare")
def biting_snare():
	return render_template("biting-snare.html")

@app.route("/hobbling-snare")
def hobbling_snare():
	return render_template("hobbling-snare.html")

@app.route("/stalker-bane-snare")
def stalker_bane_snare():
	return render_template("stalker-bane-snare.html")

@app.route("/tar-rocket-snare")
def tar_rocket_snare():
	return render_template("tar-rocket-snare.html")

@app.route("/trip-snare")
def trip_snare():
	return render_template("trip-snare.html")

@app.route("/warning-snare")
def warning_snare():
	return render_template("warning-snare.html")

@app.route("/boom-snare")
def boom_snare():
	return render_template("boom-snare.html")

@app.route("/glittering-snare")
def glittering_snare():
	return render_template("glittering-snare.html")

@app.route("/fang-snare")
def fang_snare():
	return render_template("fang-snare.html")

@app.route("/clinging-ooze-snare")
def clinging_ooze_snare():
	return render_template("clinging-ooze-snare.html")

@app.route("/tin-cobra")
def tin_cobra():
	return render_template("tin-cobra.html")

@app.route("/flame-drake-snare")
def flame_drake_snare():
	return render_template("flame-drake-snare.html")

@app.route("/pummeling-snare")
def pummeling_snare():
	return render_template("pummeling-snare.html")

@app.route("/wet-shock-snare")
def wet_shock_snare():
	return render_template("wet-shock-snare.html")

@app.route("/mirror-ball-snare")
def mirror_ball_snare():
	return render_template("mirror-ball-snare.html")

@app.route("/nauseating-snare")
def nauseating_snare():
	return render_template("nauseating-snare.html")

@app.route("/piercing-whistle-snare")
def piercing_whistle_snare():
	return render_template("piercing-whistle-snare.html")

@app.route("/envenomed-snare")
def envenomed_snare():
	return render_template("envenomed-snare.html")

@app.route("/bomb-snare")
def bomb_snare():
	return render_template("bomb-snare.html")

@app.route("/grasping-snare")
def grasping_snare():
	return render_template("grasping-snare.html")

@app.route("/rusting-snare")
def rusting_snare():
	return render_template("rusting-snare.html")

@app.route("/striking-snare")
def striking_snare():
	return render_template("striking-snare.html")

@app.route("/spirit-snare")
def spirit_snare():
	return render_template("spirit-snare.html")

@app.route("/frost-worm-snare")
def frost_worm_snare():
	return render_template("frost-worm-snare.html")

@app.route("/puff-dragon")
def puff_dragon():
	return render_template("puff-dragon.html")

@app.route("/binding-snare")
def binding_snare():
	return render_template("binding-snare.html")

@app.route("/burning-badger-guts-snare")
def burning_badger_guts_snare():
	return render_template("burning-badger-guts-snare.html")

@app.route("/mudrock-snare")
def mudrock_snare():
	return render_template("mudrock-snare.html")

@app.route("/snagging-hook-snare")
def snagging_hook_snare():
	return render_template("snagging-hook-snare.html")

@app.route("/scything-blade-snare")
def scything_blade_snare():
	return render_template("scything-blade-snare.html")

@app.route("/bleeding-spines-snare")
def bleeding_spines_snare():
	return render_template("bleeding-spines-snare.html")

@app.route("/stunning-snare")
def stunning_snare():
	return render_template("stunning-snare.html")

@app.route("/shrapnel-snare")
def shrapnel_snare():
	return render_template("shrapnel-snare.html")

@app.route("/snares")
def snares():
	return render_template("snares.html")

@app.route("/snare-crafting")
def snare_crafting():
	return render_template("snare-crafting.html")

@app.route("/stone-communion")
def stone_communion():
	return render_template("stone-communion.html")

@app.route("/attunement-to-stone")
def attunement_to_stone():
	return render_template("attunement-to-stone.html")

@app.route("/judgement-of-the-monolith")
def judgement_of_the_monolith():
	return render_template("judgement-of-the-monolith.html")

@app.route("/ka-stone-ritual")
def ka_stone_ritual():
	return render_template("ka-stone-ritual.html")

@app.route("/lethargy-poison")
def lethargy_poison():
	return render_template("lethargy-poison.html")

@app.route("/eye-of-the-arclords")
def eye_of_the_arclords():
	return render_template("eye-of-the-arclords.html")

@app.route("/arcane-sense")
def arcane_sense():
	return render_template("arcane-sense.html")

@app.route("/magical-hideaway")
def magical_hideaway():
	return render_template("magical-hideaway.html")

@app.route("/invisibility-cloak")
def invisibility_cloak():
	return render_template("invisibility-cloak.html")

@app.route("/shape-of-the-dragon")
def shape_of_the_dragon():
	return render_template("shape-of-the-dragon.html")

@app.route("/perpetual-surgeon")
def perpetual_surgeon():
	return render_template("perpetual-surgeon.html")

@app.route("/subtle-delivery")
def subtle_delivery():
	return render_template("subtle-delivery.html")

@app.route("/mindblank-mutagen")
def mindblank_mutagen():
	return render_template("mindblank-mutagen.html")

@app.route("/invincible-mutagen")
def invincible_mutagen():
	return render_template("invincible-mutagen.html")

@app.route("/glib-mutagen")
def glib_mutagen():
	return render_template("glib-mutagen.html")

@app.route("/genius-mutagen")
def genius_mutagen():
	return render_template("genius-mutagen.html")

@app.route("/elastic-mutagen")
def elastic_mutagen():
	return render_template("elastic-mutagen.html")

@app.route("/miracle-worker")
def miracle_worker():
	return render_template("miracle-worker.html")

@app.route("/tumbling-opportunist")
def tumbling_opportunist():
	return render_template("tumbling-opportunist.html")

@app.route("/fortify-shield")
def fortify_shield():
	return render_template("fortify-shield.html")

@app.route("/shadow-pact")
def shadow_pact():
	return render_template("shadow-pact.html")

@app.route("/anarchic-arcana")
def anarchic_arcana():
	return render_template("anarchic-arcana.html")

@app.route("/plant-shape")
def plant_shape():
	return render_template("plant-shape.html")

@app.route("/breath-paragon")
def breath_paragon():
	return render_template("breath-paragon.html")

@app.route("/alchemical-crafting")
def alchemical_crafting():
	return render_template("alchemical-crafting.html")

@app.route("/alchemical-items")
def alchemical_items():
	return render_template("alchemical-items.html")

@app.route("/warrior-feats")
def warrior_feats():
	return render_template("warrior-feats.html")

@app.route("/focus-spells")
def focus_spells():
	return render_template("focus-spells.html")

@app.route("/gauntlet")
def gauntlet():
	return render_template("gauntlet.html")

@app.route("/absent-minded")
def absent_minded():
	return render_template("absent-minded.html")

@app.route("/gill-hook")
def gill_hook():
	return render_template("gill-hook.html")

@app.route("/longbow")
def longbow():
	return render_template("longbow.html")

@app.route("/sun-sling")
def sun_sling():
	return render_template("sun-sling.html")

@app.route("/weapons-list")
def weapons_list():
	return render_template("weapons-list.html")

@app.route("/crane-stance")
def crane_stance():
	return render_template("crane-stance.html")

@app.route("/clinging-shadows-stance")
def clinging_shadows_stance():
	return render_template("clinging-shadows-stance.html")

@app.route("/cobra-stance")
def cobra_stance():
	return render_template("cobra-stance.html")

@app.route("/powerful-fist")
def powerful_fist():
	return render_template("powerful-fist.html")

@app.route("/ritual-rules")
def ritual_rules():
	return render_template("ritual-rules.html")

@app.route("/ritual-list")
def ritual_list():
	return render_template("ritual-list.html")

@app.route("/chromatic-ray")
def chromatic_ray():
	return render_template("chromatic-ray.html")

@app.route("/arcane-spells")
def arcane_spells():
	return render_template("arcane-spells.html")

@app.route("/knockdown-monster-ability")
def knockdown_monster_ability():
	return render_template("knockdown-monster-ability.html")

@app.route("/shadow-mage-occult-caster")
def shadow_mage_occult_caster():
	return render_template("shadow-mage-occult-caster.html")

@app.route("/encounter-mode")
def encounter_mode():
	return render_template("encounter-mode.html")

@app.route("/animal-form")
def animal_form():
	return render_template("animal-form.html")

@app.route("/arcane-cascade")
def arcane_cascade():
	return render_template("arcane-cascade.html")

@app.route("/laughing-shadow")
def laughing_shadow():
	return render_template("laughing-shadow.html")

@app.route("/inexorable-iron")
def inexorable_iron():
	return render_template("inexorable-iron.html")

@app.route("/raise-a-tome")
def raise_a_tome():
	return render_template("raise-a-tome.html")

@app.route("/sparkling-targe")
def sparkling_targe():
	return render_template("sparkling-targe.html")

@app.route("/twisting-tree")
def twisting_tree():
	return render_template("twisting-tree.html")

@app.route("/maguss-analysis")
def maguss_analysis():
	return render_template("maguss-analysis.html")

@app.route("/force-fang")
def force_fang():
	return render_template("force-fang.html")

@app.route("/spell-parry")
def spell_parry():
	return render_template("spell-parry.html")

@app.route("/devastating-spellstrike")
def devastating_spellstrike():
	return render_template("devastating-spellstrike.html")

@app.route("/distracting-spellstrike")
def distracting_spellstrike():
	return render_template("distracting-spellstrike.html")

@app.route("/emergency-targe")
def emergency_targe():
	return render_template("emergency-targe.html")

@app.route("/starlit-eyes")
def starlit_eyes():
	return render_template("starlit-eyes.html")

@app.route("/shielded-tome")
def shielded_tome():
	return render_template("shielded-tome.html")

@app.route("/capture-magic")
def capture_magic():
	return render_template("capture-magic.html")

@app.route("/runic-impression")
def runic_impression():
	return render_template("runic-impression.html")

@app.route("/dazzling-block")
def dazzling_block():
	return render_template("dazzling-block.html")

@app.route("/rapid-recharge")
def rapid_recharge():
	return render_template("rapid-recharge.html")

@app.route("/sustaining-steel")
def sustaining_steel():
	return render_template("sustaining-steel.html")

@app.route("/preternatural-parry")
def preternatural_parry():
	return render_template("preternatural-parry.html")

@app.route("/expansive-spellstrike")
def expansive_spellstrike():
	return render_template("expansive-spellstrike.html")

@app.route("/spirit-sheath")
def spirit_sheath():
	return render_template("spirit-sheath.html")

@app.route("/cascade-countermeasure")
def cascade_countermeasure():
	return render_template("cascade-countermeasure.html")

@app.route("/spell-swipe")
def spell_swipe():
	return render_template("spell-swipe.html")

@app.route("/cascading-ray")
def cascading_ray():
	return render_template("cascading-ray.html")

@app.route("/dimensional-disappearance")
def dimensional_disappearance():
	return render_template("dimensional-disappearance.html")

@app.route("/lunging-spellstrike")
def lunging_spellstrike():
	return render_template("lunging-spellstrike.html")

@app.route("/meteoric-spellstrike")
def meteoric_spellstrike():
	return render_template("meteoric-spellstrike.html")

@app.route("/overwhelming-spellstrike")
def overwhelming_spellstrike():
	return render_template("overwhelming-spellstrike.html")

@app.route("/arcane-shroud")
def arcane_shroud():
	return render_template("arcane-shroud.html")

@app.route("/hasted-assault")
def hasted_assault():
	return render_template("hasted-assault.html")

@app.route("/dispelling-spellstrike")
def dispelling_spellstrike():
	return render_template("dispelling-spellstrike.html")

@app.route("/resounding-cascade")
def resounding_cascade():
	return render_template("resounding-cascade.html")

@app.route("/whirlwind-spell")
def whirlwind_spell():
	return render_template("whirlwind-spell.html")

@app.route("/long-strider")
def long_strider():
	return render_template("long-strider.html")

@app.route("/eldritch-archer")
def eldritch_archer():
	return render_template("eldritch-archer.html")

@app.route("/cauldron")
def cauldron():
	return render_template("cauldron.html")

@app.route("/temporary-potions")
def temporary_potions():
	return render_template("temporary-potions.html")

@app.route("/intimidating-prowess")
def intimidating_prowess():
	return render_template("intimidating-prowess.html")

@app.route("/intimidation-feats")
def intimidation_feats():
	return render_template("intimidation-feats.html")

@app.route("/incapacitation")
def incapacitation():
	return render_template("incapacitation.html")

@app.route("/shadow-walk")
def shadow_walk():
	return render_template("shadow-walk.html")

@app.route("/glimpse-of-redemption")
def glimpse_of_redemption():
	return render_template("glimpse-of-redemption.html")

@app.route("/elite-manticore")
def elite_manticore():
	return render_template("elite-manticore.html")

@app.route("/ghost")
def ghost():
	return render_template("ghost.html")

@app.route("/ghost-mage")
def ghost_mage():
	return render_template("ghost-mage.html")

@app.route("/bestial")
def bestial():
	return render_template("bestial.html")

@app.route("/chummy")
def chummy():
	return render_template("chummy.html")

@app.route("/fanaticism")
def fanaticism():
	return render_template("fanaticism.html")

@app.route("/hidebound")
def hidebound():
	return render_template("hidebound.html")

@app.route("/laziness")
def laziness():
	return render_template("laziness.html")

@app.route("/low-empathy")
def low_empathy():
	return render_template("low-empathy.html")

@app.route("/megalomania")
def megalomania():
	return render_template("megalomania.html")

@app.route("/overconfident")
def overconfident():
	return render_template("overconfident.html")

@app.route("/magical-crafting")
def magical_crafting():
	return render_template("magical-crafting.html")

@app.route("/buckler")
def buckler():
	return render_template("buckler.html")

@app.route("/wooden-shield")
def wooden_shield():
	return render_template("wooden-shield.html")

@app.route("/steel-shield")
def steel_shield():
	return render_template("steel-shield.html")

@app.route("/tower-shield")
def tower_shield():
	return render_template("tower-shield.html")

@app.route("/shield-rules")
def shield_rules():
	return render_template("shield-rules.html")

@app.route("/critical-misses")
def critical_misses():
	return render_template("critical-misses.html")

@app.route("/crafters-appraisal")
def crafters_appraisal():
	return render_template("crafters-appraisal.html")

@app.route("/evanescent-wings")
def evanescent_wings():
	return render_template("evanescent-wings.html")

@app.route("/spellstrike")
def spellstrike():
	return render_template("spellstrike.html")

@app.route("/improved-knockback")
def improved_knockback():
	return render_template("improved-knockback.html")

@app.route("/all-about-complications")
def all_about_complications():
	return render_template("all-about-complications.html")

@app.route("/alchemical-tools")
def alchemical_tools():
	return render_template("alchemical-tools.html")

@app.route("/mana-oil")
def mana_oil():
	return render_template("mana-oil.html")

@app.route("/assassin")
def assassin():
	return render_template("assassin.html")

@app.route("/poisonous-deluge")
def poisonous_deluge():
	return render_template("poisonous-deluge.html")

@app.route("/rope-master")
def rope_master():
	return render_template("rope-master.html")

@app.route("/athletics-class-feats")
def athletics_class_feats():
	return render_template("athletics-class-feats.html")

@app.route("/innocent-butterfly")
def innocent_butterfly():
	return render_template("innocent-butterfly.html")

@app.route("/beneath-notice")
def beneath_notice():
	return render_template("beneath-notice.html")

@app.route("/deception-feats")
def deception_feats():
	return render_template("deception-feats.html")

@app.route("/phoenix-bloodline-focus-shroud-of-flame")
def phoenix_bloodline_focus_shroud_of_flame():
	return render_template("phoenix-bloodline-focus-shroud-of-flame.html")

@app.route("/phoenix-bloodline-focus-cleansing-flames")
def phoenix_bloodline_focus_cleansing_flames():
	return render_template("phoenix-bloodline-focus-cleansing-flames.html")

@app.route("/all-the-time-in-the-world")
def all_the_time_in_the_world():
	return render_template("all-the-time-in-the-world.html")

@app.route("/perception-feats")
def perception_feats():
	return render_template("perception-feats.html")

@app.route("/head-of-the-night-parade")
def head_of_the_night_parade():
	return render_template("head-of-the-night-parade.html")

@app.route("/criminal-dedication")
def criminal_dedication():
	return render_template("criminal-dedication.html")

@app.route("/worldsphere-gravity")
def worldsphere_gravity():
	return render_template("worldsphere-gravity.html")

@app.route("/shift-spell")
def shift_spell():
	return render_template("shift-spell.html")

@app.route("/phoenix-bloodline")
def phoenix_bloodline():
	return render_template("phoenix-bloodline.html")

@app.route("/ruby-resurrection")
def ruby_resurrection():
	return render_template("ruby-resurrection.html")

@app.route("/extradimensional-stash")
def extradimensional_stash():
	return render_template("extradimensional-stash.html")

@app.route("/thievery-feats")
def thievery_feats():
	return render_template("thievery-feats.html")

@app.route("/entwined-energy-ki")
def entwined_energy_ki():
	return render_template("entwined-energy-ki.html")

@app.route("/wronged-monks-wrath")
def wronged_monks_wrath():
	return render_template("wronged-monks-wrath.html")

@app.route("/jellyfish-stance")
def jellyfish_stance():
	return render_template("jellyfish-stance.html")

@app.route("/effortless-reach")
def effortless_reach():
	return render_template("effortless-reach.html")

@app.route("/electric-counter")
def electric_counter():
	return render_template("electric-counter.html")

@app.route("/sense-ki")
def sense_ki():
	return render_template("sense-ki.html")

@app.route("/vitality-manipulating-stance")
def vitality_manipulating_stance():
	return render_template("vitality-manipulating-stance.html")

@app.route("/sever-space")
def sever_space():
	return render_template("sever-space.html")

@app.route("/whirlwind-toss")
def whirlwind_toss():
	return render_template("whirlwind-toss.html")

@app.route("/ghost-eater")
def ghost_eater():
	return render_template("ghost-eater.html")

@app.route("/reach-beyond")
def reach_beyond():
	return render_template("reach-beyond.html")

@app.route("/disrupting-strikes")
def disrupting_strikes():
	return render_template("disrupting-strikes.html")

@app.route("/ever-distant-defense")
def ever_distant_defense():
	return render_template("ever-distant-defense.html")

@app.route("/six-pillars-stance")
def six_pillars_stance():
	return render_template("six-pillars-stance.html")

@app.route("/maneuvering-spell")
def maneuvering_spell():
	return render_template("maneuvering-spell.html")

@app.route("/touch-focus")
def touch_focus():
	return render_template("touch-focus.html")

@app.route("/warrior-spellcaster-feats")
def warrior_spellcaster_feats():
	return render_template("warrior-spellcaster-feats.html")

@app.route("/vivacious-afterimage")
def vivacious_afterimage():
	return render_template("vivacious-afterimage.html")

@app.route("/time-dilation-cascade")
def time_dilation_cascade():
	return render_template("time-dilation-cascade.html")

@app.route("/changelog-march-10-2022")
def changelog_march_10_2022():
	return render_template("changelog-march-10-2022.html")

@app.route("/ogre-glutton")
def ogre_glutton():
	return render_template("ogre-glutton.html")

@app.route("/harpy")
def harpy():
	return render_template("harpy.html")

@app.route("/banshee")
def banshee():
	return render_template("banshee.html")

@app.route("/zombie-sharks")
def zombie_sharks():
	return render_template("zombie-sharks.html")

@app.route("/orc-marauder")
def orc_marauder():
	return render_template("orc-marauder.html")

@app.route("/approximate")
def approximate():
	return render_template("approximate.html")

@app.route("/what-is-this-game")
def what_is_this_game():
	return render_template("what-is-this-game.html")

@app.route("/crimson-shroud")
def crimson_shroud():
	return render_template("crimson-shroud.html")

@app.route("/blade-ally")
def blade_ally():
	return render_template("blade-ally.html")

@app.route("/religion-warrior-feats")
def religion_warrior_feats():
	return render_template("religion-warrior-feats.html")

@app.route("/radiant-blade-spirit")
def radiant_blade_spirit():
	return render_template("radiant-blade-spirit.html")

@app.route("/witchs-hut")
def witchs_hut():
	return render_template("witchs-hut.html")

@app.route("/snare-specialist")
def snare_specialist():
	return render_template("snare-specialist.html")

@app.route("/heal-animal")
def heal_animal():
	return render_template("heal-animal.html")

@app.route("/nature-domain-natures-bounty")
def nature_domain_natures_bounty():
	return render_template("nature-domain-natures-bounty.html")

@app.route("/phoenix-bloodline-focus-rejuvenating-flames")
def phoenix_bloodline_focus_rejuvenating_flames():
	return render_template("phoenix-bloodline-focus-rejuvenating-flames.html")

@app.route("/focused-locks")
def focused_locks():
	return render_template("focused-locks.html")

@app.route("/composition-spells")
def composition_spells():
	return render_template("composition-spells.html")

@app.route("/runescarred")
def runescarred():
	return render_template("runescarred.html")

@app.route("/minor-magic")
def minor_magic():
	return render_template("minor-magic.html")

@app.route("/elite-anchorite-of-talos")
def elite_anchorite_of_talos():
	return render_template("elite-anchorite-of-talos.html")

@app.route("/adult-white-dragon")
def adult_white_dragon():
	return render_template("adult-white-dragon.html")

@app.route("/elite-white-dragon")
def elite_white_dragon():
	return render_template("elite-white-dragon.html")

@app.route("/prestidigitation")
def prestidigitation():
	return render_template("prestidigitation.html")

@app.route("/inner-radiance-torrent")
def inner_radiance_torrent():
	return render_template("inner-radiance-torrent.html")

@app.route("/elite-mimic")
def elite_mimic():
	return render_template("elite-mimic.html")

@app.route("/assassin-5866037")
def assassin_5866037():
	return render_template("assassin-5866037.html")

@app.route("/gnome-in-an-auto-turret")
def gnome_in_an_auto_turret():
	return render_template("gnome-in-an-auto-turret.html")

@app.route("/ochre-jelly")
def ochre_jelly():
	return render_template("ochre-jelly.html")

@app.route("/redclaw-orc-ranger")
def redclaw_orc_ranger():
	return render_template("redclaw-orc-ranger.html")

@app.route("/cutthroat-thug")
def cutthroat_thug():
	return render_template("cutthroat-thug.html")

@app.route("/redclaw-orc-skirmishers")
def redclaw_orc_skirmishers():
	return render_template("redclaw-orc-skirmishers.html")

@app.route("/heroes-feast")
def heroes_feast():
	return render_template("heroes-feast.html")

@app.route("/school-specialist")
def school_specialist():
	return render_template("school-specialist.html")

@app.route("/spell-prodigy")
def spell_prodigy():
	return render_template("spell-prodigy.html")

@app.route("/debilitating-strike")
def debilitating_strike():
	return render_template("debilitating-strike.html")

@app.route("/relentless-stalker")
def relentless_stalker():
	return render_template("relentless-stalker.html")

@app.route("/crafting-feats")
def crafting_feats():
	return render_template("crafting-feats.html")

@app.route("/living-monolith")
def living_monolith():
	return render_template("living-monolith.html")

@app.route("/perform-surgery")
def perform_surgery():
	return render_template("perform-surgery.html")

@app.route("/stabilize-injuries")
def stabilize_injuries():
	return render_template("stabilize-injuries.html")

@app.route("/medicine-int")
def medicine_int():
	return render_template("medicine-int.html")

@app.route("/hit-locations")
def hit_locations():
	return render_template("hit-locations.html")

@app.route("/body-fruit")
def body_fruit():
	return render_template("body-fruit.html")

@app.route("/glory-and-valor")
def glory_and_valor():
	return render_template("glory-and-valor.html")

@app.route("/dying")
def dying():
	return render_template("dying.html")

@app.route("/death-dying-and-recovery")
def death_dying_and_recovery():
	return render_template("death-dying-and-recovery.html")

@app.route("/incredibly-hardy")
def incredibly_hardy():
	return render_template("incredibly-hardy.html")

@app.route("/internal-cohesion")
def internal_cohesion():
	return render_template("internal-cohesion.html")

@app.route("/regenerative-blood")
def regenerative_blood():
	return render_template("regenerative-blood.html")

@app.route("/rejuvenation")
def rejuvenation():
	return render_template("rejuvenation.html")

@app.route("/revivification")
def revivification():
	return render_template("revivification.html")

@app.route("/revivifying-mutagen")
def revivifying_mutagen():
	return render_template("revivifying-mutagen.html")

@app.route("/consume-spell")
def consume_spell():
	return render_template("consume-spell.html")

@app.route("/familiars")
def familiars():
	return render_template("familiars.html")

@app.route("/communal-healing")
def communal_healing():
	return render_template("communal-healing.html")

@app.route("/magic-hands")
def magic_hands():
	return render_template("magic-hands.html")

@app.route("/resurrectionist")
def resurrectionist():
	return render_template("resurrectionist.html")

@app.route("/healing")
def healing():
	return render_template("healing.html")

@app.route("/healing-transformation")
def healing_transformation():
	return render_template("healing-transformation.html")

@app.route("/superstition-instinct")
def superstition_instinct():
	return render_template("superstition-instinct.html")

@app.route("/shall-not-falter-shall-not-rout")
def shall_not_falter_shall_not_rout():
	return render_template("shall-not-falter-shall-not-rout.html")

@app.route("/numb-to-death")
def numb_to_death():
	return render_template("numb-to-death.html")

@app.route("/fast-recovery")
def fast_recovery():
	return render_template("fast-recovery.html")

@app.route("/life-syphon")
def life_syphon():
	return render_template("life-syphon.html")

@app.route("/align-ki")
def align_ki():
	return render_template("align-ki.html")

@app.route("/warrior-ki-arts-feats")
def warrior_ki_arts_feats():
	return render_template("warrior-ki-arts-feats.html")

@app.route("/battle-medicine")
def battle_medicine():
	return render_template("battle-medicine.html")

@app.route("/superior-medic")
def superior_medic():
	return render_template("superior-medic.html")

@app.route("/godless-healing")
def godless_healing():
	return render_template("godless-healing.html")

@app.route("/continual-recovery")
def continual_recovery():
	return render_template("continual-recovery.html")

@app.route("/risky-surgery")
def risky_surgery():
	return render_template("risky-surgery.html")

@app.route("/nature-feats")
def nature_feats():
	return render_template("nature-feats.html")

@app.route("/soothing-mist")
def soothing_mist():
	return render_template("soothing-mist.html")

@app.route("/wholeness-of-body")
def wholeness_of_body():
	return render_template("wholeness-of-body.html")

@app.route("/lesson-of-life")
def lesson_of_life():
	return render_template("lesson-of-life.html")

@app.route("/goodberry")
def goodberry():
	return render_template("goodberry.html")

@app.route("/occultism-feats")
def occultism_feats():
	return render_template("occultism-feats.html")

@app.route("/performance-feats")
def performance_feats():
	return render_template("performance-feats.html")

@app.route("/healing-domain-rebuke-death")
def healing_domain_rebuke_death():
	return render_template("healing-domain-rebuke-death.html")

@app.route("/lay-on-hands")
def lay_on_hands():
	return render_template("lay-on-hands.html")

@app.route("/religion-feats")
def religion_feats():
	return render_template("religion-feats.html")

@app.route("/heal")
def heal():
	return render_template("heal.html")

@app.route("/soothing-spring")
def soothing_spring():
	return render_template("soothing-spring.html")

@app.route("/positive-attunement")
def positive_attunement():
	return render_template("positive-attunement.html")

@app.route("/primal-spells")
def primal_spells():
	return render_template("primal-spells.html")

@app.route("/vital-beacon")
def vital_beacon():
	return render_template("vital-beacon.html")

@app.route("/occult-spells")
def occult_spells():
	return render_template("occult-spells.html")

@app.route("/healing-plaster")
def healing_plaster():
	return render_template("healing-plaster.html")

@app.route("/medicine-feats")
def medicine_feats():
	return render_template("medicine-feats.html")

@app.route("/soften-fall")
def soften_fall():
	return render_template("soften-fall.html")

@app.route("/ward-opening")
def ward_opening():
	return render_template("ward-opening.html")

@app.route("/elemental-shield")
def elemental_shield():
	return render_template("elemental-shield.html")

@app.route("/kinetic-shield")
def kinetic_shield():
	return render_template("kinetic-shield.html")

@app.route("/esoteric-shield")
def esoteric_shield():
	return render_template("esoteric-shield.html")

@app.route("/waterproofing")
def waterproofing():
	return render_template("waterproofing.html")

@app.route("/sight-ward")
def sight_ward():
	return render_template("sight-ward.html")

@app.route("/sound-ward")
def sound_ward():
	return render_template("sound-ward.html")

@app.route("/reflect-blow")
def reflect_blow():
	return render_template("reflect-blow.html")

@app.route("/resist-motion")
def resist_motion():
	return render_template("resist-motion.html")

@app.route("/soothing-ballad")
def soothing_ballad():
	return render_template("soothing-ballad.html")

@app.route("/armor-proficiency")
def armor_proficiency():
	return render_template("armor-proficiency.html")

@app.route("/quick-copy")
def quick_copy():
	return render_template("quick-copy.html")

@app.route("/transfer-ink")
def transfer_ink():
	return render_template("transfer-ink.html")

@app.route("/formation-master")
def formation_master():
	return render_template("formation-master.html")

@app.route("/squad-tactics")
def squad_tactics():
	return render_template("squad-tactics.html")

@app.route("/mirror-shield")
def mirror_shield():
	return render_template("mirror-shield.html")

@app.route("/reflecting-reposte")
def reflecting_reposte():
	return render_template("reflecting-reposte.html")

@app.route("/warrior-weapon-style-feats")
def warrior_weapon_style_feats():
	return render_template("warrior-weapon-style-feats.html")

@app.route("/water-born")
def water_born():
	return render_template("water-born.html")

@app.route("/swim")
def swim():
	return render_template("swim.html")

@app.route("/water-dancer")
def water_dancer():
	return render_template("water-dancer.html")

@app.route("/natural-swimmer")
def natural_swimmer():
	return render_template("natural-swimmer.html")

@app.route("/strong-swimmer")
def strong_swimmer():
	return render_template("strong-swimmer.html")

@app.route("/aquatic-adaptation")
def aquatic_adaptation():
	return render_template("aquatic-adaptation.html")

@app.route("/avenge-ally")
def avenge_ally():
	return render_template("avenge-ally.html")

@app.route("/pride-in-arms")
def pride_in_arms():
	return render_template("pride-in-arms.html")

@app.route("/shoulder-the-load")
def shoulder_the_load():
	return render_template("shoulder-the-load.html")

@app.route("/cover-foibles")
def cover_foibles():
	return render_template("cover-foibles.html")

@app.route("/touch-telepath")
def touch_telepath():
	return render_template("touch-telepath.html")

@app.route("/helpful")
def helpful():
	return render_template("helpful.html")

@app.route("/battleforger")
def battleforger():
	return render_template("battleforger.html")

@app.route("/innocuous")
def innocuous():
	return render_template("innocuous.html")

@app.route("/oath-keeper")
def oath_keeper():
	return render_template("oath-keeper.html")

@app.route("/dragons-breath")
def dragons_breath():
	return render_template("dragons-breath.html")

@app.route("/yamarajs-grandeur")
def yamarajs_grandeur():
	return render_template("yamarajs-grandeur.html")

@app.route("/ancestral-friend")
def ancestral_friend():
	return render_template("ancestral-friend.html")

@app.route("/heat-acclimatization")
def heat_acclimatization():
	return render_template("heat-acclimatization.html")

@app.route("/cold-acclimatization")
def cold_acclimatization():
	return render_template("cold-acclimatization.html")

@app.route("/terrain-skirmisher-538899")
def terrain_skirmisher_538899():
	return render_template("terrain-skirmisher-538899.html")

@app.route("/wilderness-survivor")
def wilderness_survivor():
	return render_template("wilderness-survivor.html")

@app.route("/environmental-stalker")
def environmental_stalker():
	return render_template("environmental-stalker.html")

@app.route("/uncanny-cheeks")
def uncanny_cheeks():
	return render_template("uncanny-cheeks.html")

@app.route("/hardy-traveler")
def hardy_traveler():
	return render_template("hardy-traveler.html")

@app.route("/scout")
def scout():
	return render_template("scout.html")

@app.route("/inspirit-hazard")
def inspirit_hazard():
	return render_template("inspirit-hazard.html")

@app.route("/bounce-back")
def bounce_back():
	return render_template("bounce-back.html")

@app.route("/vivacious-conduit")
def vivacious_conduit():
	return render_template("vivacious-conduit.html")

@app.route("/ghost-hunter")
def ghost_hunter():
	return render_template("ghost-hunter.html")

@app.route("/spirit-strike")
def spirit_strike():
	return render_template("spirit-strike.html")

@app.route("/occult-resistance")
def occult_resistance():
	return render_template("occult-resistance.html")

@app.route("/steely-gaze")
def steely_gaze():
	return render_template("steely-gaze.html")

@app.route("/climbing-appendage")
def climbing_appendage():
	return render_template("climbing-appendage.html")

@app.route("/scavenger")
def scavenger():
	return render_template("scavenger.html")

@app.route("/fluid-squeeze")
def fluid_squeeze():
	return render_template("fluid-squeeze.html")

@app.route("/powerful-claws")
def powerful_claws():
	return render_template("powerful-claws.html")

@app.route("/aggravating-scratch")
def aggravating_scratch():
	return render_template("aggravating-scratch.html")

@app.route("/accursed-claws")
def accursed_claws():
	return render_template("accursed-claws.html")

@app.route("/increased-consumption")
def increased_consumption():
	return render_template("increased-consumption.html")

@app.route("/slow-eater")
def slow_eater():
	return render_template("slow-eater.html")

@app.route("/dependents")
def dependents():
	return render_template("dependents.html")

@app.route("/all-class-and-skill-feats")
def all_class_and_skill_feats():
	return render_template("all-class-and-skill-feats.html")

@app.route("/long-lived-3256488")
def long_lived_3256488():
	return render_template("long-lived-3256488.html")

@app.route("/expert-rider")
def expert_rider():
	return render_template("expert-rider.html")

@app.route("/animal-allies")
def animal_allies():
	return render_template("animal-allies.html")

@app.route("/aquatic-ambusher")
def aquatic_ambusher():
	return render_template("aquatic-ambusher.html")

@app.route("/guided-by-the-stars")
def guided_by_the_stars():
	return render_template("guided-by-the-stars.html")

@app.route("/read-the-stars")
def read_the_stars():
	return render_template("read-the-stars.html")

@app.route("/heir-of-the-saoc")
def heir_of_the_saoc():
	return render_template("heir-of-the-saoc.html")

@app.route("/saoc-astrology")
def saoc_astrology():
	return render_template("saoc-astrology.html")

@app.route("/swim-speed")
def swim_speed():
	return render_template("swim-speed.html")

@app.route("/animal-order-elocutionist")
def animal_order_elocutionist():
	return render_template("animal-order-elocutionist.html")

@app.route("/complications")
def complications():
	return render_template("complications.html")

@app.route("/beastkin")
def beastkin():
	return render_template("beastkin.html")

@app.route("/critter-shape")
def critter_shape():
	return render_template("critter-shape.html")

@app.route("/lifetime-climber")
def lifetime_climber():
	return render_template("lifetime-climber.html")

@app.route("/adept-climber")
def adept_climber():
	return render_template("adept-climber.html")

@app.route("/avenge-the-fallen")
def avenge_the_fallen():
	return render_template("avenge-the-fallen.html")

@app.route("/cant-fall-here")
def cant_fall_here():
	return render_template("cant-fall-here.html")

@app.route("/call-of-elysium")
def call_of_elysium():
	return render_template("call-of-elysium.html")

@app.route("/mindfulness")
def mindfulness():
	return render_template("mindfulness.html")

@app.route("/we-march-on")
def we_march_on():
	return render_template("we-march-on.html")

@app.route("/handy")
def handy():
	return render_template("handy.html")

@app.route("/inventive-offensive")
def inventive_offensive():
	return render_template("inventive-offensive.html")

@app.route("/natural-charm")
def natural_charm():
	return render_template("natural-charm.html")

@app.route("/voice-modulation")
def voice_modulation():
	return render_template("voice-modulation.html")

@app.route("/bright-soul")
def bright_soul():
	return render_template("bright-soul.html")

@app.route("/chaotic-elemental-resistance")
def chaotic_elemental_resistance():
	return render_template("chaotic-elemental-resistance.html")

@app.route("/elemental-bulwark")
def elemental_bulwark():
	return render_template("elemental-bulwark.html")

@app.route("/flame-jump")
def flame_jump():
	return render_template("flame-jump.html")

@app.route("/smoke-blending")
def smoke_blending():
	return render_template("smoke-blending.html")

@app.route("/invoke-the-elements")
def invoke_the_elements():
	return render_template("invoke-the-elements.html")

@app.route("/the-shroud")
def the_shroud():
	return render_template("the-shroud.html")

@app.route("/tidal-shield")
def tidal_shield():
	return render_template("tidal-shield.html")

@app.route("/water-strider")
def water_strider():
	return render_template("water-strider.html")

@app.route("/breath-weapon")
def breath_weapon():
	return render_template("breath-weapon.html")

@app.route("/elemental-reprisal")
def elemental_reprisal():
	return render_template("elemental-reprisal.html")

@app.route("/elemental-assault")
def elemental_assault():
	return render_template("elemental-assault.html")

@app.route("/elemental-heart")
def elemental_heart():
	return render_template("elemental-heart.html")

@app.route("/guided-strike")
def guided_strike():
	return render_template("guided-strike.html")

@app.route("/radiant-burst")
def radiant_burst():
	return render_template("radiant-burst.html")

@app.route("/scorching-disarm")
def scorching_disarm():
	return render_template("scorching-disarm.html")

@app.route("/torcher")
def torcher():
	return render_template("torcher.html")

@app.route("/palpable-enmity-6347319")
def palpable_enmity_6347319():
	return render_template("palpable-enmity-6347319.html")

@app.route("/cloud-gazer")
def cloud_gazer():
	return render_template("cloud-gazer.html")

@app.route("/street-dwellers")
def street_dwellers():
	return render_template("street-dwellers.html")

@app.route("/body-storage")
def body_storage():
	return render_template("body-storage.html")

@app.route("/hazard-expertise")
def hazard_expertise():
	return render_template("hazard-expertise.html")

@app.route("/wary-skulker")
def wary_skulker():
	return render_template("wary-skulker.html")

@app.route("/between-the-plates")
def between_the_plates():
	return render_template("between-the-plates.html")

@app.route("/cause-hesitation")
def cause_hesitation():
	return render_template("cause-hesitation.html")

@app.route("/cling")
def cling():
	return render_template("cling.html")

@app.route("/cornered-fury")
def cornered_fury():
	return render_template("cornered-fury.html")

@app.route("/dashing-snatch")
def dashing_snatch():
	return render_template("dashing-snatch.html")

@app.route("/empathetic-plea")
def empathetic_plea():
	return render_template("empathetic-plea.html")

@app.route("/graceful-dance")
def graceful_dance():
	return render_template("graceful-dance.html")

@app.route("/grasping-reach")
def grasping_reach():
	return render_template("grasping-reach.html")

@app.route("/saving-throw-feats")
def saving_throw_feats():
	return render_template("saving-throw-feats.html")

@app.route("/lifebloods-call")
def lifebloods_call():
	return render_template("lifebloods-call.html")

@app.route("/olethross-decree")
def olethross_decree():
	return render_template("olethross-decree.html")

@app.route("/tactical-reposition")
def tactical_reposition():
	return render_template("tactical-reposition.html")

@app.route("/sudden-hop")
def sudden_hop():
	return render_template("sudden-hop.html")

@app.route("/terrain-advantage")
def terrain_advantage():
	return render_template("terrain-advantage.html")

@app.route("/to-the-last")
def to_the_last():
	return render_template("to-the-last.html")

@app.route("/cat-nap")
def cat_nap():
	return render_template("cat-nap.html")

@app.route("/ferocity")
def ferocity():
	return render_template("ferocity.html")

@app.route("/robust-vitality")
def robust_vitality():
	return render_template("robust-vitality.html")

@app.route("/healing-factor")
def healing_factor():
	return render_template("healing-factor.html")

@app.route("/stoutness")
def stoutness():
	return render_template("stoutness.html")

@app.route("/mystical-mending")
def mystical_mending():
	return render_template("mystical-mending.html")

@app.route("/nine-lives")
def nine_lives():
	return render_template("nine-lives.html")

@app.route("/spell-devourer")
def spell_devourer():
	return render_template("spell-devourer.html")

@app.route("/victorious-vigor")
def victorious_vigor():
	return render_template("victorious-vigor.html")

@app.route("/blessed-blood")
def blessed_blood():
	return render_template("blessed-blood.html")

@app.route("/magical-strikes")
def magical_strikes():
	return render_template("magical-strikes.html")

@app.route("/fiendish-strikes")
def fiendish_strikes():
	return render_template("fiendish-strikes.html")

@app.route("/enforced-order")
def enforced_order():
	return render_template("enforced-order.html")

@app.route("/celestial-strikes")
def celestial_strikes():
	return render_template("celestial-strikes.html")

@app.route("/halo")
def halo():
	return render_template("halo.html")

@app.route("/radiate-glory")
def radiate_glory():
	return render_template("radiate-glory.html")

@app.route("/intimidating-mein")
def intimidating_mein():
	return render_template("intimidating-mein.html")

@app.route("/remorseless-lash")
def remorseless_lash():
	return render_template("remorseless-lash.html")

@app.route("/cultural-expertise")
def cultural_expertise():
	return render_template("cultural-expertise.html")

@app.route("/dynamic-skill")
def dynamic_skill():
	return render_template("dynamic-skill.html")

@app.route("/theoretical-acumen")
def theoretical_acumen():
	return render_template("theoretical-acumen.html")

@app.route("/clever-improvisor")
def clever_improvisor():
	return render_template("clever-improvisor.html")

@app.route("/chance-death")
def chance_death():
	return render_template("chance-death.html")

@app.route("/eat-fortune")
def eat_fortune():
	return render_template("eat-fortune.html")

@app.route("/impose-order")
def impose_order():
	return render_template("impose-order.html")

@app.route("/extremely-lucky")
def extremely_lucky():
	return render_template("extremely-lucky.html")

@app.route("/tradition-countermeasures")
def tradition_countermeasures():
	return render_template("tradition-countermeasures.html")

@app.route("/bouncy")
def bouncy():
	return render_template("bouncy.html")

@app.route("/powerful-leaps")
def powerful_leaps():
	return render_template("powerful-leaps.html")

@app.route("/rock-and-roll")
def rock_and_roll():
	return render_template("rock-and-roll.html")

@app.route("/sure-feet")
def sure_feet():
	return render_template("sure-feet.html")

@app.route("/tumbler")
def tumbler():
	return render_template("tumbler.html")

@app.route("/mutate-weapon")
def mutate_weapon():
	return render_template("mutate-weapon.html")

@app.route("/coating-of-slime")
def coating_of_slime():
	return render_template("coating-of-slime.html")

@app.route("/natural-weapon-cunning")
def natural_weapon_cunning():
	return render_template("natural-weapon-cunning.html")

@app.route("/venom")
def venom():
	return render_template("venom.html")

@app.route("/bite-attack")
def bite_attack():
	return render_template("bite-attack.html")

@app.route("/persistent-wounds")
def persistent_wounds():
	return render_template("persistent-wounds.html")

@app.route("/iron-fists")
def iron_fists():
	return render_template("iron-fists.html")

@app.route("/easy-dry")
def easy_dry():
	return render_template("easy-dry.html")

@app.route("/claws")
def claws():
	return render_template("claws.html")

@app.route("/scooper")
def scooper():
	return render_template("scooper.html")

@app.route("/observant")
def observant():
	return render_template("observant.html")

@app.route("/aloofness")
def aloofness():
	return render_template("aloofness.html")

@app.route("/ward-against-corruption")
def ward_against_corruption():
	return render_template("ward-against-corruption.html")

@app.route("/grim-insight")
def grim_insight():
	return render_template("grim-insight.html")

@app.route("/evade-doom")
def evade_doom():
	return render_template("evade-doom.html")

@app.route("/stubborn-persistence")
def stubborn_persistence():
	return render_template("stubborn-persistence.html")

@app.route("/resilient-body")
def resilient_body():
	return render_template("resilient-body.html")

@app.route("/resist-persistent-damage")
def resist_persistent_damage():
	return render_template("resist-persistent-damage.html")

@app.route("/common-resistance")
def common_resistance():
	return render_template("common-resistance.html")

@app.route("/uncommon-resistance")
def uncommon_resistance():
	return render_template("uncommon-resistance.html")

@app.route("/stone-bones")
def stone_bones():
	return render_template("stone-bones.html")

@app.route("/dragonscaled")
def dragonscaled():
	return render_template("dragonscaled.html")

@app.route("/flexible-morality")
def flexible_morality():
	return render_template("flexible-morality.html")

@app.route("/blunt-snout")
def blunt_snout():
	return render_template("blunt-snout.html")

@app.route("/deaths-drums")
def deaths_drums():
	return render_template("deaths-drums.html")

@app.route("/child-of-light")
def child_of_light():
	return render_template("child-of-light.html")

@app.route("/death-warden")
def death_warden():
	return render_template("death-warden.html")

@app.route("/gutsy")
def gutsy():
	return render_template("gutsy.html")

@app.route("/haughty-obstinacy")
def haughty_obstinacy():
	return render_template("haughty-obstinacy.html")

@app.route("/jinxed-5569781")
def jinxed_5569781():
	return render_template("jinxed-5569781.html")

@app.route("/know-oneself")
def know_oneself():
	return render_template("know-oneself.html")

@app.route("/lab-rat")
def lab_rat():
	return render_template("lab-rat.html")

@app.route("/dreamer")
def dreamer():
	return render_template("dreamer.html")

@app.route("/plumekin")
def plumekin():
	return render_template("plumekin.html")

@app.route("/tide-hardened")
def tide_hardened():
	return render_template("tide-hardened.html")

@app.route("/augment-senses")
def augment_senses():
	return render_template("augment-senses.html")

@app.route("/bloodhound")
def bloodhound():
	return render_template("bloodhound.html")

@app.route("/darkvision")
def darkvision():
	return render_template("darkvision.html")

@app.route("/shadowsight")
def shadowsight():
	return render_template("shadowsight.html")

@app.route("/whisper-kind")
def whisper_kind():
	return render_template("whisper-kind.html")

@app.route("/spotting-as-one")
def spotting_as_one():
	return render_template("spotting-as-one.html")

@app.route("/slip-into-the-shadow")
def slip_into_the_shadow():
	return render_template("slip-into-the-shadow.html")

@app.route("/unexpected-shift")
def unexpected_shift():
	return render_template("unexpected-shift.html")

@app.route("/close-quarters")
def close_quarters():
	return render_template("close-quarters.html")

@app.route("/scamper-underfoot")
def scamper_underfoot():
	return render_template("scamper-underfoot.html")

@app.route("/dance-underfoot")
def dance_underfoot():
	return render_template("dance-underfoot.html")

@app.route("/tiny")
def tiny():
	return render_template("tiny.html")

@app.route("/shifting-colors")
def shifting_colors():
	return render_template("shifting-colors.html")

@app.route("/folksy-patter")
def folksy_patter():
	return render_template("folksy-patter.html")

@app.route("/project-persona")
def project_persona():
	return render_template("project-persona.html")

@app.route("/surge")
def surge():
	return render_template("surge.html")

@app.route("/photosynthesis")
def photosynthesis():
	return render_template("photosynthesis.html")

@app.route("/distracting-song")
def distracting_song():
	return render_template("distracting-song.html")

@app.route("/catchy-tune")
def catchy_tune():
	return render_template("catchy-tune.html")

@app.route("/lightning-tongue")
def lightning_tongue():
	return render_template("lightning-tongue.html")

@app.route("/useful-bonus-appendage")
def useful_bonus_appendage():
	return render_template("useful-bonus-appendage.html")

@app.route("/warmask")
def warmask():
	return render_template("warmask.html")

@app.route("/ancestral-shieldbearer")
def ancestral_shieldbearer():
	return render_template("ancestral-shieldbearer.html")

@app.route("/clan-dagger")
def clan_dagger():
	return render_template("clan-dagger.html")

@app.route("/improvisational-warrior")
def improvisational_warrior():
	return render_template("improvisational-warrior.html")

@app.route("/leech-clipper")
def leech_clipper():
	return render_template("leech-clipper.html")

@app.route("/wings")
def wings():
	return render_template("wings.html")

@app.route("/bomb-maker")
def bomb_maker():
	return render_template("bomb-maker.html")

@app.route("/splash-control")
def splash_control():
	return render_template("splash-control.html")

@app.route("/debilitating-bomb")
def debilitating_bomb():
	return render_template("debilitating-bomb.html")

@app.route("/far-lobber")
def far_lobber():
	return render_template("far-lobber.html")

@app.route("/artokuss-fire")
def artokuss_fire():
	return render_template("artokuss-fire.html")

@app.route("/combine-elixers")
def combine_elixers():
	return render_template("combine-elixers.html")

@app.route("/alchemical-healer")
def alchemical_healer():
	return render_template("alchemical-healer.html")

@app.route("/merciful-elixir")
def merciful_elixir():
	return render_template("merciful-elixir.html")

@app.route("/mutagenic-discovery")
def mutagenic_discovery():
	return render_template("mutagenic-discovery.html")

@app.route("/mutagenist")
def mutagenist():
	return render_template("mutagenist.html")

@app.route("/chemical-contagion")
def chemical_contagion():
	return render_template("chemical-contagion.html")

@app.route("/poison-weapon")
def poison_weapon():
	return render_template("poison-weapon.html")

@app.route("/tenacious-toxins")
def tenacious_toxins():
	return render_template("tenacious-toxins.html")

@app.route("/toxicologist")
def toxicologist():
	return render_template("toxicologist.html")

@app.route("/braggart-7341319")
def braggart_7341319():
	return render_template("braggart-7341319.html")

@app.route("/inspired-methodology")
def inspired_methodology():
	return render_template("inspired-methodology.html")

@app.route("/upstage")
def upstage():
	return render_template("upstage.html")

@app.route("/group-infiltration")
def group_infiltration():
	return render_template("group-infiltration.html")

@app.route("/liberator")
def liberator():
	return render_template("liberator.html")

@app.route("/immediate-aid")
def immediate_aid():
	return render_template("immediate-aid.html")

@app.route("/cut-the-bonds")
def cut_the_bonds():
	return render_template("cut-the-bonds.html")

@app.route("/marshals-aura")
def marshals_aura():
	return render_template("marshals-aura.html")

@app.route("/cadence-call")
def cadence_call():
	return render_template("cadence-call.html")

@app.route("/steel-yourself")
def steel_yourself():
	return render_template("steel-yourself.html")

@app.route("/eidetic-memorization")
def eidetic_memorization():
	return render_template("eidetic-memorization.html")

@app.route("/efficient-rituals")
def efficient_rituals():
	return render_template("efficient-rituals.html")

@app.route("/charmed-life")
def charmed_life():
	return render_template("charmed-life.html")

@app.route("/quick-warning")
def quick_warning():
	return render_template("quick-warning.html")

@app.route("/deft-cooperation")
def deft_cooperation():
	return render_template("deft-cooperation.html")

@app.route("/focus-ally")
def focus_ally():
	return render_template("focus-ally.html")

@app.route("/watch-and-learn")
def watch_and_learn():
	return render_template("watch-and-learn.html")

@app.route("/absorb-spell")
def absorb_spell():
	return render_template("absorb-spell.html")

@app.route("/clever-counterspell")
def clever_counterspell():
	return render_template("clever-counterspell.html")

@app.route("/reflect-spell")
def reflect_spell():
	return render_template("reflect-spell.html")

@app.route("/physical-evolution")
def physical_evolution():
	return render_template("physical-evolution.html")

@app.route("/counterspell")
def counterspell():
	return render_template("counterspell.html")

@app.route("/second-chance-enchantment")
def second_chance_enchantment():
	return render_template("second-chance-enchantment.html")

@app.route("/enhanced-familiar")
def enhanced_familiar():
	return render_template("enhanced-familiar.html")

@app.route("/sneak-attack")
def sneak_attack():
	return render_template("sneak-attack.html")

@app.route("/warrior-tactic-feats")
def warrior_tactic_feats():
	return render_template("warrior-tactic-feats.html")

@app.route("/impossible-striker")
def impossible_striker():
	return render_template("impossible-striker.html")

@app.route("/sly-striker")
def sly_striker():
	return render_template("sly-striker.html")

@app.route("/twist-the-knife")
def twist_the_knife():
	return render_template("twist-the-knife.html")

@app.route("/formation-training")
def formation_training():
	return render_template("formation-training.html")

@app.route("/legendary-performer")
def legendary_performer():
	return render_template("legendary-performer.html")

@app.route("/craft")
def craft():
	return render_template("craft.html")

@app.route("/magic-item-rules")
def magic_item_rules():
	return render_template("magic-item-rules.html")

@app.route("/sacrifice-armor")
def sacrifice_armor():
	return render_template("sacrifice-armor.html")

@app.route("/mark-for-death")
def mark_for_death():
	return render_template("mark-for-death.html")

@app.route("/second-skin")
def second_skin():
	return render_template("second-skin.html")

@app.route("/agile-maneuvers")
def agile_maneuvers():
	return render_template("agile-maneuvers.html")

@app.route("/barreling-charge")
def barreling_charge():
	return render_template("barreling-charge.html")

@app.route("/cleave")
def cleave():
	return render_template("cleave.html")

@app.route("/dragging-strike")
def dragging_strike():
	return render_template("dragging-strike.html")

@app.route("/flat-footed")
def flat_footed():
	return render_template("flat-footed.html")

@app.route("/flanking")
def flanking():
	return render_template("flanking.html")

@app.route("/grapple")
def grapple():
	return render_template("grapple.html")

@app.route("/disarm")
def disarm():
	return render_template("disarm.html")

@app.route("/trip")
def trip():
	return render_template("trip.html")

@app.route("/shove")
def shove():
	return render_template("shove.html")

@app.route("/mixed-maneuver")
def mixed_maneuver():
	return render_template("mixed-maneuver.html")

@app.route("/unbalancing-sweep")
def unbalancing_sweep():
	return render_template("unbalancing-sweep.html")

@app.route("/combat-flexibility")
def combat_flexibility():
	return render_template("combat-flexibility.html")

@app.route("/distracting-feint")
def distracting_feint():
	return render_template("distracting-feint.html")

@app.route("/thrash")
def thrash():
	return render_template("thrash.html")

@app.route("/shatter-defenses")
def shatter_defenses():
	return render_template("shatter-defenses.html")

@app.route("/power-attack")
def power_attack():
	return render_template("power-attack.html")

@app.route("/attack-of-opportunity")
def attack_of_opportunity():
	return render_template("attack-of-opportunity.html")

@app.route("/deflect-arrow")
def deflect_arrow():
	return render_template("deflect-arrow.html")

@app.route("/opportune-riposte")
def opportune_riposte():
	return render_template("opportune-riposte.html")

@app.route("/preparation")
def preparation():
	return render_template("preparation.html")

@app.route("/red-mantis-assassin")
def red_mantis_assassin():
	return render_template("red-mantis-assassin.html")

@app.route("/knockback")
def knockback():
	return render_template("knockback.html")

@app.route("/boasters-challenge")
def boasters_challenge():
	return render_template("boasters-challenge.html")

@app.route("/pin-to-the-spot")
def pin_to_the_spot():
	return render_template("pin-to-the-spot.html")

@app.route("/nimble-dodge")
def nimble_dodge():
	return render_template("nimble-dodge.html")

@app.route("/stance-savant")
def stance_savant():
	return render_template("stance-savant.html")

@app.route("/shoulder-catastrophe")
def shoulder_catastrophe():
	return render_template("shoulder-catastrophe.html")

@app.route("/knockdown")
def knockdown():
	return render_template("knockdown.html")

@app.route("/warrior-general-feats")
def warrior_general_feats():
	return render_template("warrior-general-feats.html")

@app.route("/devise-a-strategem")
def devise_a_strategem():
	return render_template("devise-a-strategem.html")

@app.route("/accompany")
def accompany():
	return render_template("accompany.html")

@app.route("/learning-epiphanies-and-experience-points")
def learning_epiphanies_and_experience_points():
	return render_template("learning-epiphanies-and-experience-points.html")

@app.route("/wound-thresholds-and-healing")
def wound_thresholds_and_healing():
	return render_template("wound-thresholds-and-healing.html")

@app.route("/silencing-strike")
def silencing_strike():
	return render_template("silencing-strike.html")

@app.route("/divine-spells")
def divine_spells():
	return render_template("divine-spells.html")

@app.route("/greater-flurry")
def greater_flurry():
	return render_template("greater-flurry.html")

@app.route("/lava-soul")
def lava_soul():
	return render_template("lava-soul.html")

@app.route("/inveigle")
def inveigle():
	return render_template("inveigle.html")

@app.route("/marked")
def marked():
	return render_template("marked.html")

@app.route("/shattering-strike")
def shattering_strike():
	return render_template("shattering-strike.html")

@app.route("/elixir-of-life")
def elixir_of_life():
	return render_template("elixir-of-life.html")

@app.route("/alchemical-elixirs")
def alchemical_elixirs():
	return render_template("alchemical-elixirs.html")

@app.route("/lunacy")
def lunacy():
	return render_template("lunacy.html")

@app.route("/hymn-of-healing")
def hymn_of_healing():
	return render_template("hymn-of-healing.html")

@app.route("/house-of-imaginary-walls")
def house_of_imaginary_walls():
	return render_template("house-of-imaginary-walls.html")

@app.route("/make-an-impression")
def make_an_impression():
	return render_template("make-an-impression.html")

@app.route("/diplomacy-chr")
def diplomacy_chr():
	return render_template("diplomacy-chr.html")

@app.route("/intimidation-chr")
def intimidation_chr():
	return render_template("intimidation-chr.html")

@app.route("/deception-chr")
def deception_chr():
	return render_template("deception-chr.html")

@app.route("/magic-domain-mystic-beacon")
def magic_domain_mystic_beacon():
	return render_template("magic-domain-mystic-beacon.html")

@app.route("/dhampire")
def dhampire():
	return render_template("dhampire.html")

@app.route("/regenerate")
def regenerate():
	return render_template("regenerate.html")

@app.route("/advanced-alchemy")
def advanced_alchemy():
	return render_template("advanced-alchemy.html")

@app.route("/alchemist")
def alchemist():
	return render_template("alchemist.html")

@app.route("/quick-alchemy")
def quick_alchemy():
	return render_template("quick-alchemy.html")

@app.route("/professional-feats")
def professional_feats():
	return render_template("professional-feats.html")

@app.route("/disturbing-defense")
def disturbing_defense():
	return render_template("disturbing-defense.html")

@app.route("/peculiar-anatomy")
def peculiar_anatomy():
	return render_template("peculiar-anatomy.html")

@app.route("/uncanny-suction")
def uncanny_suction():
	return render_template("uncanny-suction.html")

@app.route("/scroll-savant")
def scroll_savant():
	return render_template("scroll-savant.html")

@app.route("/new-cantrips")
def new_cantrips():
	return render_template("new-cantrips.html")

@app.route("/equipment-list")
def equipment_list():
	return render_template("equipment-list.html")

@app.route("/character-creation-guide")
def character_creation_guide():
	return render_template("character-creation-guide.html")

@app.route("/aapoph-serpentfolk")
def aapoph_serpentfolk():
	return render_template("aapoph-serpentfolk.html")

@app.route("/ankhrav")
def ankhrav():
	return render_template("ankhrav.html")

@app.route("/simple-dcs-by-tier")
def simple_dcs_by_tier():
	return render_template("simple-dcs-by-tier.html")

@app.route("/dance-of-intercession")
def dance_of_intercession():
	return render_template("dance-of-intercession.html")

@app.route("/soothe")
def soothe():
	return render_template("soothe.html")

@app.route("/incredible-companion")
def incredible_companion():
	return render_template("incredible-companion.html")

@app.route("/spellcasting")
def spellcasting():
	return render_template("spellcasting.html")

@app.route("/necrophidius")
def necrophidius():
	return render_template("necrophidius.html")

@app.route("/animated-statue")
def animated_statue():
	return render_template("animated-statue.html")

@app.route("/soulbound-doll")
def soulbound_doll():
	return render_template("soulbound-doll.html")

@app.route("/dig-widget")
def dig_widget():
	return render_template("dig-widget.html")

@app.route("/terra-cotta-soldier")
def terra_cotta_soldier():
	return render_template("terra-cotta-soldier.html")

@app.route("/scarecrow-5701577")
def scarecrow_5701577():
	return render_template("scarecrow-5701577.html")

@app.route("/giant-animated-statue")
def giant_animated_statue():
	return render_template("giant-animated-statue.html")

@app.route("/levaloch")
def levaloch():
	return render_template("levaloch.html")

@app.route("/tupilaq")
def tupilaq():
	return render_template("tupilaq.html")

@app.route("/animated-furnace")
def animated_furnace():
	return render_template("animated-furnace.html")

@app.route("/swordkeeper")
def swordkeeper():
	return render_template("swordkeeper.html")

@app.route("/spiral-centurian")
def spiral_centurian():
	return render_template("spiral-centurian.html")

@app.route("/frost-drake")
def frost_drake():
	return render_template("frost-drake.html")

@app.route("/desert-drake")
def desert_drake():
	return render_template("desert-drake.html")

@app.route("/young-copper-dragon")
def young_copper_dragon():
	return render_template("young-copper-dragon.html")

@app.route("/young-red-dragon")
def young_red_dragon():
	return render_template("young-red-dragon.html")

@app.route("/young-blue-dragon")
def young_blue_dragon():
	return render_template("young-blue-dragon.html")

@app.route("/summon-animal")
def summon_animal():
	return render_template("summon-animal.html")

@app.route("/reincarnate")
def reincarnate():
	return render_template("reincarnate.html")

@app.route("/skeleton-archer")
def skeleton_archer():
	return render_template("skeleton-archer.html")

@app.route("/drain-bonded-item")
def drain_bonded_item():
	return render_template("drain-bonded-item.html")

@app.route("/soul-domain-eject-soul")
def soul_domain_eject_soul():
	return render_template("soul-domain-eject-soul.html")

@app.route("/mature-animal-companion")
def mature_animal_companion():
	return render_template("mature-animal-companion.html")

@app.route("/perception")
def perception():
	return render_template("perception.html")

@app.route("/athletics-v2")
def athletics_v2():
	return render_template("athletics-v2.html")

@app.route("/might-v2")
def might_v2():
	return render_template("might-v2.html")

@app.route("/coordination-v2")
def coordination_v2():
	return render_template("coordination-v2.html")

@app.route("/reconstruct-the-scene-3367166")
def reconstruct_the_scene_3367166():
	return render_template("reconstruct-the-scene-3367166.html")

@app.route("/discover-motivations")
def discover_motivations():
	return render_template("discover-motivations.html")

@app.route("/empathy-v2")
def empathy_v2():
	return render_template("empathy-v2.html")

@app.route("/the-quality-spectrum")
def the_quality_spectrum():
	return render_template("the-quality-spectrum.html")

@app.route("/perform")
def perform():
	return render_template("perform.html")

@app.route("/create-artwork")
def create_artwork():
	return render_template("create-artwork.html")

@app.route("/the-rock")
def the_rock():
	return render_template("the-rock.html")

@app.route("/alchemy-abilities")
def alchemy_abilities():
	return render_template("alchemy-abilities.html")

@app.route("/monster-npc-rules")
def monster_npc_rules():
	return render_template("monster-npc-rules.html")

@app.route("/magic-and-spellcasting")
def magic_and_spellcasting():
	return render_template("magic-and-spellcasting.html")

@app.route("/social-interaction")
def social_interaction():
	return render_template("social-interaction.html")

@app.route("/armor-and-weapon-design")
def armor_and_weapon_design():
	return render_template("armor-and-weapon-design.html")

@app.route("/tiefling-fighter")
def tiefling_fighter():
	return render_template("tiefling-fighter.html")

@app.route("/alchemy")
def alchemy():
	return render_template("alchemy.html")

@app.route("/dwarf-rogue")
def dwarf_rogue():
	return render_template("dwarf-rogue.html")

@app.route("/persuade")
def persuade():
	return render_template("persuade.html")

@app.route("/rogue-abilities")
def rogue_abilities():
	return render_template("rogue-abilities.html")

@app.route("/halfling-wizard")
def halfling_wizard():
	return render_template("halfling-wizard.html")

@app.route("/range-duration-and-area")
def range_duration_and_area():
	return render_template("range-duration-and-area.html")

@app.route("/boosts")
def boosts():
	return render_template("boosts.html")

@app.route("/enhanced-activity-use")
def enhanced_activity_use():
	return render_template("enhanced-activity-use.html")

@app.route("/action-savers")
def action_savers():
	return render_template("action-savers.html")

@app.route("/special-defenses")
def special_defenses():
	return render_template("special-defenses.html")

@app.route("/limits")
def limits():
	return render_template("limits.html")

@app.route("/the-situational-limit")
def the_situational_limit():
	return render_template("the-situational-limit.html")

@app.route("/special-attack")
def special_attack():
	return render_template("special-attack.html")

@app.route("/defense-checks-and-condition-resistance")
def defense_checks_and_condition_resistance():
	return render_template("defense-checks-and-condition-resistance.html")

@app.route("/healing-and-dying")
def healing_and_dying():
	return render_template("healing-and-dying.html")

@app.route("/other-combat-benefits")
def other_combat_benefits():
	return render_template("other-combat-benefits.html")

@app.route("/movement-7447550")
def movement_7447550():
	return render_template("movement-7447550.html")

@app.route("/senses-and-perception")
def senses_and_perception():
	return render_template("senses-and-perception.html")

@app.route("/exploration-4164893")
def exploration_4164893():
	return render_template("exploration-4164893.html")

@app.route("/investigation-and-information")
def investigation_and_information():
	return render_template("investigation-and-information.html")

@app.route("/teamwork")
def teamwork():
	return render_template("teamwork.html")

@app.route("/communication")
def communication():
	return render_template("communication.html")

@app.route("/survival")
def survival():
	return render_template("survival.html")

@app.route("/spellcasting-abilities")
def spellcasting_abilities():
	return render_template("spellcasting-abilities.html")

@app.route("/community-and-society")
def community_and_society():
	return render_template("community-and-society.html")

@app.route("/equipment")
def equipment():
	return render_template("equipment.html")

@app.route("/creating-abilities")
def creating_abilities():
	return render_template("creating-abilities.html")

@app.route("/clandestine-and-rogue")
def clandestine_and_rogue():
	return render_template("clandestine-and-rogue.html")

@app.route("/skills")
def skills():
	return render_template("skills.html")

@app.route("/stealth-and-hiding")
def stealth_and_hiding():
	return render_template("stealth-and-hiding.html")

@app.route("/traps-and-hazards")
def traps_and_hazards():
	return render_template("traps-and-hazards.html")

@app.route("/alter-material")
def alter_material():
	return render_template("alter-material.html")

@app.route("/creation-9164590")
def creation_9164590():
	return render_template("creation-9164590.html")

@app.route("/destroy-material")
def destroy_material():
	return render_template("destroy-material.html")

@app.route("/environmental-control")
def environmental_control():
	return render_template("environmental-control.html")

@app.route("/illusions")
def illusions():
	return render_template("illusions.html")

@app.route("/meta-abilities")
def meta_abilities():
	return render_template("meta-abilities.html")

@app.route("/minions")
def minions():
	return render_template("minions.html")

@app.route("/animal-friends-and-mounts")
def animal_friends_and_mounts():
	return render_template("animal-friends-and-mounts.html")

@app.route("/shapeshifting")
def shapeshifting():
	return render_template("shapeshifting.html")

@app.route("/size")
def size():
	return render_template("size.html")

@app.route("/arrange-a-meeting")
def arrange_a_meeting():
	return render_template("arrange-a-meeting.html")

@app.route("/administration")
def administration():
	return render_template("administration.html")

@app.route("/navigate-unsecured-system")
def navigate_unsecured_system():
	return render_template("navigate-unsecured-system.html")

@app.route("/create-electronic-forgery")
def create_electronic_forgery():
	return render_template("create-electronic-forgery.html")

@app.route("/infiltrate-secure-system")
def infiltrate_secure_system():
	return render_template("infiltrate-secure-system.html")

@app.route("/avoid-system-detection")
def avoid_system_detection():
	return render_template("avoid-system-detection.html")

@app.route("/bypass-countermeasures")
def bypass_countermeasures():
	return render_template("bypass-countermeasures.html")

@app.route("/computers")
def computers():
	return render_template("computers.html")

@app.route("/culture")
def culture():
	return render_template("culture.html")

@app.route("/configure-explosives")
def configure_explosives():
	return render_template("configure-explosives.html")

@app.route("/assess-structures")
def assess_structures():
	return render_template("assess-structures.html")

@app.route("/disable-device")
def disable_device():
	return render_template("disable-device.html")

@app.route("/identify-technology")
def identify_technology():
	return render_template("identify-technology.html")

@app.route("/identify-magic")
def identify_magic():
	return render_template("identify-magic.html")

@app.route("/repair")
def repair():
	return render_template("repair.html")

@app.route("/jury-rig")
def jury_rig():
	return render_template("jury-rig.html")

@app.route("/engineering")
def engineering():
	return render_template("engineering.html")

@app.route("/arcana")
def arcana():
	return render_template("arcana.html")

@app.route("/connect-the-dots-4949769")
def connect_the_dots_4949769():
	return render_template("connect-the-dots-4949769.html")

@app.route("/examine-clue")
def examine_clue():
	return render_template("examine-clue.html")

@app.route("/investigation-v2")
def investigation_v2():
	return render_template("investigation-v2.html")

@app.route("/life-sciences")
def life_sciences():
	return render_template("life-sciences.html")

@app.route("/physical-sciences")
def physical_sciences():
	return render_template("physical-sciences.html")

@app.route("/piloting")
def piloting():
	return render_template("piloting.html")

@app.route("/streetwise-6073864")
def streetwise_6073864():
	return render_template("streetwise-6073864.html")

@app.route("/v2-character-creation")
def v2_character_creation():
	return render_template("v2-character-creation.html")

@app.route("/animal-companions")
def animal_companions():
	return render_template("animal-companions.html")

@app.route("/rallying-cry")
def rallying_cry():
	return render_template("rallying-cry.html")

@app.route("/persistent-alchemy")
def persistent_alchemy():
	return render_template("persistent-alchemy.html")

@app.route("/extend-elixir")
def extend_elixir():
	return render_template("extend-elixir.html")

@app.route("/administer-first-aid-8413834")
def administer_first_aid_8413834():
	return render_template("administer-first-aid-8413834.html")

@app.route("/alchemist-class-feats")
def alchemist_class_feats():
	return render_template("alchemist-class-feats.html")

@app.route("/reckless-abandon")
def reckless_abandon():
	return render_template("reckless-abandon.html")

@app.route("/all-ancestry-feats")
def all_ancestry_feats():
	return render_template("all-ancestry-feats.html")

@app.route("/word-of-recall")
def word_of_recall():
	return render_template("word-of-recall.html")

@app.route("/selective-energy")
def selective_energy():
	return render_template("selective-energy.html")

@app.route("/spellcaster-feats")
def spellcaster_feats():
	return render_template("spellcaster-feats.html")

@app.route("/breath-of-life")
def breath_of_life():
	return render_template("breath-of-life.html")

@app.route("/sacred-defense")
def sacred_defense():
	return render_template("sacred-defense.html")



if __name__ == "__main__":
    app.run(debug=True)
