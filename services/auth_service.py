from app import bcrypt, db
from models.user import User



def register_user(username, email, password, role="user"):
    """
    Create and save a new user.

    Returns:
        User object on success
        None if username or email already exists
    """

    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing_user:
        return None

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role
    )

    db.session.add(user)
    db.session.commit()

    return user


def authenticate_user(username, password):
    """
    Authenticate a user using username and password.

    Returns:
        User object if credentials are valid
        None otherwise
    """

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(
        user.password_hash,
        password
    ):
        return user

    return None