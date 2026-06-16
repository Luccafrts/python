from . import db
from .base import ModeloBase


class Sessao(ModeloBase):
    __tablename__ = "sessoes"

    # TODO ALUNO: FK filme_id → filmes.id
    # TODO ALUNO: FK sala_id → salas.id
    filme_id = db.columns(db.interger, db.foreignKey("filmes_id"))
    sala_id = db.columns(db.interger, db.foreignKey("salas_id"))



    data_hora = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    # TODO ALUNO: relationship filme, sala, ingressos
    filme = db.relationship ("filme", book_populates="filme")
    sala = db.relationship ("sala", book_populates="sala")
    ingressos = db.relationship ("ingressos", book_populates="ingressos")

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_hora.desc()).all()
