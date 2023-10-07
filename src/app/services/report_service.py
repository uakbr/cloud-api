```python
# src/app/services/report_service.py

from ..models.scan_result import ScanResult
from ..app import db
from sqlalchemy import func

class ReportService:
    @staticmethod
    def generate_user_report(user_id):
        """
        Generate a report for a specific user, summarizing all their API scan results.
        """
        scan_results = ScanResult.query.filter_by(user_id=user_id).all()

        report = {
            'total_scans': len(scan_results),
            'vulnerabilities': {}
        }

        for result in scan_results:
            if result.vulnerabilities not in report['vulnerabilities']:
                report['vulnerabilities'][result.vulnerabilities] = 0
            report['vulnerabilities'][result.vulnerabilities] += 1

        return report

    @staticmethod
    def generate_overall_report():
        """
        Generate an overall report, summarizing all API scan results in the system.
        """
        total_scans = db.session.query(func.count(ScanResult.id)).scalar()
        total_vulnerabilities = db.session.query(func.count(ScanResult.vulnerabilities)).scalar()

        report = {
            'total_scans': total_scans,
            'total_vulnerabilities': total_vulnerabilities,
            'vulnerabilities': {}
        }

        scan_results = ScanResult.query.all()

        for result in scan_results:
            if result.vulnerabilities not in report['vulnerabilities']:
                report['vulnerabilities'][result.vulnerabilities] = 0
            report['vulnerabilities'][result.vulnerabilities] += 1

        return report
```
