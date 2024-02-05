from flask_sqlalchemy import SQLAlchemy

# Se encarga de conectar y crear la base de datos   
db = SQLAlchemy()

# Esta será nuestra tabla padre, sin esta tabla no existen las demas.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    favorites_user = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    # id_films = db.Column(db.Integer, ForeignKey('films.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    id_species = db.Column(db.Integer, db.ForeignKey('species.id'))

    # Este codigo nos ayuda a relacionar tablas. Siempre va el modelo/tabla padre la primera letra mayuscula
    #  el primer '' de donde traemos la info , el segundo la tabla que coge la info y es el nombre de la tabla en min
    # Esto genera otra columna con la información de la tabla people
    people_favorites = db.relationship('Favorites', backref='people', lazy=True)
    # En este caso traemos a la tabla people los vehiculos que cada uno utiliza.
    vehicle = db.relationship('Vehicles', backref='people', lazy=True)
    specie = db.relationship('Species', backref='people', lazy=True)
    # starships = relationship('Starships', backref='people', lazy=True)
    planets = db.relationship('Planets', backref='people', lazy=True)

    def __repr__(self):
        return '<People %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    planets_favorites = db.relationship('Favorites', backref='planets', lazy=True)

    # people = db.relationship('People', backref='planets', lazy=True)


    def __repr__(self):
        return '<Planets %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    # id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    vehicles_favorites = db.relationship('Favorites', backref='vehicles', lazy=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    classification = db.Column(db.String(250), nullable=False)
    designation = db.Column(db.String(250), nullable=False)
    average_heigth = db.Column(db.String(250), nullable=False)
    average_lifespan = db.Column(db.String(250), nullable=False)
    eye_colors = db.Column(db.String(250), nullable=False)
    hair_colors = db.Column(db.String(250), nullable=False)
    skin_colors = db.Column(db.String(250), nullable=False)
    language = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    # id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # species_favorites = db.relationship('Favorites', backref='species', lazy=True)

    def __repr__(self):
        return '<Species %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }



class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    episode_id = db.Column(db.String(250), nullable=False)
    opening_crawl = db.Column(db.String(250), nullable=False)
    director = db.Column(db.String(250), nullable=False)
    producer = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    # id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    # id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    # id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))

    # films_favorites = relationship('favorites', backref='films', lazy=True)
    # people = relationship('People', backref='films', lazy=True)
    # planets = relationship('Planets', backref='films', lazy=True)
    # vehicles = relationship('Vehicles', backref='films', lazy=True)
    # species = relationship('Species', backref='films', lazy=True)
    # starships = relationship('Starships', backref='films', lazy=True)

    def __repr__(self):
        return '<Films %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.title,
            # do not serialize the password, its a security breach
        }    


class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    hiper_drive_rating = db.Column(db.String(250), nullable=False)
    MGLT = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    # id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # starships_favorites = db.relationship('favorites', backref='starships', lazy=True)

    def __repr__(self):
        return '<Starships %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))


    def __repr__(self):
        return '<Favorites %r>' % self.id

    # Serialize permite retornar un objeto con los valores que queremos mostrar.
    def serialize(self):
        return {
            "id": self.id,
            # "name": self.name,
            # do not serialize the password, its a security breach
        }