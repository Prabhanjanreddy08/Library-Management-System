from flask import Blueprint, request
from models import Member
from utils import validate_request_json, create_response
from auth import token_required

members_bp = Blueprint("members", __name__)

@members_bp.route("/members", methods=["GET"])
@token_required
def get_members():
    members = Member.get_all_members()
    return create_response(members)

@members_bp.route("/members", methods=["POST"])
@token_required
def add_member():
    is_valid, error = validate_request_json(["name"])
    if not is_valid:
        return create_response({"error": error}, 400)

    data = request.get_json()
    member = Member.add_member(data["name"])
    return create_response(member, 201)
