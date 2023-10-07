```python
# src/app/models/scan_result.py

from flask_sqlalchemy import SQLAlchemy
from .app import db

class ScanResult(db.Model):
    __tablename__ = 'scan_results'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    api_id = db.Column(db.String(64), nullable=False)
    cloud_provider = db.Column(db.String(64), nullable=False)
    scan_date = db.Column(db.DateTime, nullable=False)
    vulnerabilities = db.Column(db.Text)

    def __repr__(self):
        return '<ScanResult {}>'.format(self.id)
```
