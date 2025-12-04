from flask import Blueprint, request, jsonify
from db import get_connection

bp = Blueprint("persons", __name__)

@bp.route("/", methods=["POST"])
def add_person():
    data = request.json
    conn = get_connection()
    with conn.cursor() as c:
        c.execute("""
            INSERT INTO personas (nombre, dni, cargo, motivo, destino)
            VALUES (%s, %s, %s, %s, %s)
        """, (data["nombre"], data["dni"], data["cargo"], data["motivo"], data["destino"]))
    conn.commit()
    return {"ok": True, "message": "Persona registrada"}

@bp.route("/", methods=["GET"])
def get_persons():
    conn = get_connection()
    with conn.cursor() as c:
        c.execute("SELECT * FROM personas ORDER BY fecha DESC")
        rows = c.fetchall()
    return jsonify(rows)