from flask import Blueprint, request
from flask_login import login_required
from app import format_errors
from app.forms import StashForm
from app.models import db, Stash

stash_routes = Blueprint('stashes', __name__)

@stash_routes.route('/<int:stashId>')
@login_required
def stashes(stashId):
    '''
    Query for a specific stash owned by current user
    '''
    stash = Stash.query.get(stashId)

    if not stash:
        return {"error": "Stash not Found"}, 404

    return stash.to_dict()


@stash_routes.route('', methods=["POST"])
@login_required
def post_a_stash():
    ''' 
    Post a  new Stash to user profile
    '''

    form = StashForm()
    form["crsf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        new_stash = Stash()
        form.populate_obj(new_stash)

        db.session.add(new_stash)
        db.session.commit()

        return new_stash.to_dict()

    if form.errors:
        return ({"errors": format_errors(form.errors)}, 400)


@stash_routes.route("/<int:stashId>", methods=["PUT"])
@login_required
def update_stash(stashId):
    '''
    Update a specific stash
    '''
    stash = Stash.query.get(stashId)

    if not stash:
        return {"error": "Stash not Found"}, 404

    form = StashForm()
    form["crsf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        form.populate_obj(stash)
        db.session.commit()
        return stash.to_dict()

    if form.errors:
        return {"errors": format_errors(form.errors)}, 400


@stash_routes.route("/<int:stashId>", methods=["DELETE"])
@login_required
def delete_stash(stashId):
    '''
    Delete a stash
    '''
    stash = Stash.query.get(stashId)

    if not stash:
        return {"error": "Stash not Found"}, 404

    db.session.delete(stash)
    db.session.commit()

    return {"message": "Stash deleted successfully"}, 200




    


