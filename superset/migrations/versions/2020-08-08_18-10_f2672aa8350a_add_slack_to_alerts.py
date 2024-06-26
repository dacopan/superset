# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_slack_to_alerts

Revision ID: f2672aa8350a
Revises: 2f1d15e8a6af
Create Date: 2020-08-08 18:10:51.973551

"""

# revision identifiers, used by Alembic.
revision = "f2672aa8350a"
down_revision = "2f1d15e8a6af"

import sqlalchemy as sa  # noqa: E402
from alembic import op  # noqa: E402


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("alerts", sa.Column("slack_channel", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("alerts", "slack_channel")
    # ### end Alembic commands ###
