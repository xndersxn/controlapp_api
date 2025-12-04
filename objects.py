from flask import Blueprint, request, jsonify
from db import get_connection

bp = Blueprint("objects", __name__)

@bp.route("/", methods=["POST"])
def add_object():
    data = request.json
    conn = get_connection()
    with conn.cursor() as c:
        c.execute("""
            INSERT INTO objetos (codigo, nombre, descripcion, cantidad, responsable, tipo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (data["codigo"], data["nombre"], data["descripcion"], data["cantidad"], data["responsable"], data["tipo"]))
    conn.commit()
    return {"ok": True, "message": "Objeto registrado"}

@bp.route("/", methods=["GET"])
def get_objects():
    conn = get_connection()
    with conn.cursor() as c:
        c.execute("SELECT * FROM objetos ORDER BY fecha DESC")
        rows = c.fetchall()
    return jsonify(rows)
