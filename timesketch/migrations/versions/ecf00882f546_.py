"""Add searchtemplate relationship to View model

Revision ID: ecf00882f546
Revises: 36e85b266dba
Create Date: 2016-09-30 11:42:03.009501

Auto generated code by flask-migrate and Alembic.
"""

# This code is auto generated. Ignore linter errors.


# revision identifiers, used by Alembic.
revision = "ecf00882f546"
down_revision = "36e85b266dba"

import sqlalchemy as sa
from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column("view", sa.Column("query_dsl", sa.UnicodeText(), nullable=True))
    op.add_column("view", sa.Column("searchtemplate_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "view", "searchtemplate", ["searchtemplate_id"], ["id"])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "view", type_="foreignkey")
    op.drop_column("view", "searchtemplate_id")
    op.drop_column("view", "query_dsl")
    ### end Alembic commands ###
