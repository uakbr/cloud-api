```python
# src/app/controllers/api_controller.py

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models.scan_result import ScanResult
from ..services.api_service import APIService
from ..app import db

bp = Blueprint('api', __name__, url_prefix='/api')

@api.route('/scan', methods=['POST'])
@login_required
def scan_api():
    data = request.get_json()
    api_id = data.get('api_id')
    cloud_provider = data.get('cloud_provider')

    # Validate input
    if not api_id or not cloud_provider:
        return jsonify({'error': 'Invalid input'}), 400

    # Perform API scan
    vulnerabilities = APIService.scan(api_id, cloud_provider)

    # Save scan result
    scan_result = ScanResult(
        user_id=current_user.id,
        api_id=api_id,
        cloud_provider=cloud_provider,
        scan_date=datetime.utcnow(),
        vulnerabilities=vulnerabilities
    )
    db.session.add(scan_result)
    db.session.commit()

    return jsonify({'message': 'Scan completed successfully'}), 200

@api.route('/scan_results', methods=['GET'])
@login_required
def get_scan_results():
    # Get scan results for current user
    scan_results = ScanResult.query.filter_by(user_id=current_user.id).all()

    # Convert scan results to JSON
    scan_results_json = [scan_result.to_json() for scan_result in scan_results]

    return jsonify(scan_results_json), 200
```
