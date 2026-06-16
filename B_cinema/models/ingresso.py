from . import db
from .base import ModeloBase


class Ingresso(ModeloBase):
    """Opcional — vale ponto extra se implementar compra de ingresso."""

    __tablename__ = "ingressos"
    sessao_id = db.columns(db.interger, db.foreignKey("sessoes_id"))
    assento = db.Column(db.String(10), nullable=False)
    nome_comprador = db.Column(db.String(120), nullable=False)
    sessoes = db.relationship ("sessoes", book_populates="filme")
