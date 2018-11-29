from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database import Base, City, Immobile, User
from flask import session as login_session
import httplib2
import os
import sys
import codecs
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask_bootstrap import Bootstrap
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

auth = HTTPBasicAuth()
app = Flask(__name__)
Bootstrap(app)

CLIENT_ID = json.loads(
    open('g_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Realtor City Immobiles"

# Connect to Database and create database session
engine = create_engine('sqlite:///immobilesuser.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@auth.verify_password
def verify_password(username, password):
    user = session.query(User).filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "\nAccess token received %s \n" % access_token


    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    print "App id: %s \n" % app_id
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    print "App secret: %s \n" % app_secret
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    print "Url: %s \n" % url
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    print "Result: %s\n" % result
    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    '''
        Due to the formatting for the result from the server token exchange we have to
        split the token first on commas and select the first index which gives us the key : value
        for the server access token then we split it on colons to pull out the actual token value
        and replace the remaining quotes with nothing so that it can be used directly in the graph
        api calls
    '''
    token = result.split(',')[0].split(':')[1].replace('"', '')
    print "Token: %s\n" % token

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    print "url sent for API access:%s"% url
    print "API JSON result: %s" % result
    data = json.loads(result)
    print "Data: %s\n" % data
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]
    login_session['provider'] = 'facebook'

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    print "User ID: %s" % user_id

    #edit later
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output

@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('g_client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    print "User Google: %s" % user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result.status == 200:
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCities'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCities'))

# User Helper Functions
@auth.verify_password
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


#JSON API to view City Information
@app.route('/city/JSON')
def cityJSON():
    cities = session.query(City).all()
    return jsonify(city=[r.serialize for r in cities])

@app.route('/city/<int:city_id>/immobile/JSON')
def cityImmobileJSON(city_id):
    city = session.query(City).filter_by(id=city_id).one()
    immobiles = session.query(Immobile).filter_by(
        city_id=city_id).all()
    return jsonify(CityImmobiles=[i.serialize for i in immobiles])

@app.route('/city/<int:city_id>/immobile/<int:immobile_id>/JSON')
def ImmobileInfoJSON(city_id, immobile_id):
    Immobile_Info = session.query(Immobile).filter_by(id=immobile_id).one()
    return jsonify(Immobile_Info=Immobile_Info.serialize)

@app.route('/')
@app.route('/city/')
def showCities():
    cities = session.query(City).order_by(asc(City.name))
    #cities = session.query(City).all()
    if 'username' not in login_session:
        return render_template('publicCities.html', cities=cities)
    else:
        return render_template('admCity.html', cities=cities)
    #return "This page shows all cities"

@app.route('/city/new/', methods=['GET', 'POST'])
def newCity():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newcity = City(name=request.form['name'], user_id=login_session['user_id'])
        session.add(newcity)
        session.commit()
        flash('New City %s Successfully Created' % newCity.name)
        return redirect(url_for('showCities'))
    else:
        return render_template('newCity.html')
    #return "This page creates a new city"

@app.route('/city/<int:city_id>/edit/', methods=['GET', 'POST'])
def editCity(city_id):
    editedCity = session.query(City).filter_by(id=city_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedCity.user_id != login_session['user_id']:
        print "\ncity.user_id: %s\n" % editedCity.user_id
        return "<script>function myFunction() {alert('You are not authorized to edit this City. Please create your own city in order to edit.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedCity.name = request.form['name']
            flash('City Successfully Edited %s' % editedCity.name)
            return redirect(url_for('showCities'))
    else:
        return render_template('editedcity.html', city=editedCity)
    #return "This page edit the selected city"

@app.route('/city/<int:city_id>/delete/', methods=['GET', 'POST'])
def deleteCity(city_id):
    cityDelete = session.query(City).filter_by(id=city_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if cityDelete.user_id != login_session['user_id']:
        print "\ncity.user_id: %s\n" % cityDelete.user_id
        return "<script>function myFunction() {alert('You are not authorized to delete this city. Please create your own city in order to delete.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(cityDelete)
        session.commit()
        flash('%s Successfully Deleted' % cityDelete.name)
        return redirect(url_for('showCities'))#, city_id=city_id))
    else:
        return render_template('deleteCity.html', city=cityDelete)
    #return "This page deletes the selected city"

@app.route('/city/<int:city_id>/')
@app.route('/city/<int:city_id>/immobile/')
def showImmobile(city_id):
    city = session.query(City).filter_by(id=city_id).one()
    creator = getUserInfo(city.user_id)
    imms = session.query(Immobile).filter_by(city_id = city_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicImmoCity.html', city = city, immobile = imms, creator=creator)
    else:
        return render_template('admImmoCity.html', city = city, imms = imms, creator=creator)

@app.route('/city/<int:city_id>/immobile/<int:immobile_id>')
def showImmobileDetails(city_id, immobile_id):
    selectedCity = session.query(City).filter_by(id=city_id).one()
    selectedImmobile = session.query(Immobile).filter_by(id=immobile_id).one()
    if 'username' not in login_session:
        #return render_template('publicCities.html', cities=cities)
        return render_template('publicImmoDetails.html', city=selectedCity, imm=selectedImmobile)
    else:
        return render_template('admImmoDetails.html', city=selectedCity, imm=selectedImmobile)
    

@app.route('/city/<int:city_id>/immobile/new/', methods=['GET', 'POST'])
def newImmobile(city_id):
    if 'username' not in login_session:
        return redirect('/login')
    city = session.query(City).filter_by(id=city_id).one()
    if login_session['user_id'] != city.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add immobiles to this city. Please create your own city in order to add immobiles.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        newImm = Immobile(address=request.form['address'],
                          description=request.form['description'],
                          squarefeet=request.form['squarefeet'],
                          bedrooms=request.form['bedrooms'],
                          bathrooms=request.form['bathrooms'],
                          city_id = city_id)
        session.add(newImm)
        session.commit()
        flash('New Immobile %s Successfully Created' % (newImm.name))
        return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('newimmobile.html', city_id=city_id)
    #return "This page creates a new immobile to the specified city"

@app.route('/city/<int:city_id>/immobile/<int:immobile_id>/edit', methods=['GET', 'POST'])
def editImmobile(city_id, immobile_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedImmobile = session.query(Immobile).filter_by(id=immobile_id).one()
    city = session.query(City).filter_by(id=city_id).one()
    if login_session['user_id'] != city.user_id:
        print "\ncity.user_id: %s\n" % city.user_id
        return redirect(url_for('showImmobile', city_id=city_id))
        return "<script>function myFunction() {alert('You are not authorized to edit immobiles to this city. Please create your own city in order to edit immobiles.');}</script><body onload='myFunction()'>"
        
    if request.method == 'POST':
        if request.form['address']:
            editedImmobile.name = request.form['address']
        if request.form['description']:
            editedImmobile.description = request.form['description']
        if request.form['squarefeet']:
            editedImmobile.squarefeet = request.form['squarefeet']
        if request.form['bedrooms']:
            editedImmobile.bathrooms = request.form['bedrooms']
        if request.form['bathrooms']:
            editedImmobile.bedrooms = request.form['bathrooms']
        session.add(editedImmobile)
        session.commit()
        flash('Immobile Successfully Edited')
        return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('editedimmobile.html', city_id=city_id, immobile_id=immobile_id, item=editedImmobile)
    #return "This page edits a certain immobile of the selected city"

@app.route('/city/<int:city_id>/immobile/<int:immobile_id>/delete', methods=['GET', 'POST'])
def deleteImmobile(city_id, immobile_id):
    if 'username' not in login_session:
        return redirect('/login')
    city = session.query(City).filter_by(id=city_id).one()
    deletedimmobile = session.query(Immobile).filter_by(id=immobile_id).one()
    if login_session['user_id'] != city.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete immobiles to this city. Please create your own city in order to delete items.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(deletedimmobile)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showImmobile', city_id=city_id))
    else:
        return render_template('deletedimmobile.html', city_id=city_id, item=deletedimmobile)
    #return "This page deletes a certain immobile of the selected city"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
