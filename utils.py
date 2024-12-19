from typing import Dict, Any, Optional, Tuple, List
from flask import jsonify, request


def validate_request_json(required_fields: List[str]) -> Tuple[bool, Optional[str]]:
    data = request.get_json()
    if not data:
        return False, "Missing JSON body in the request."
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    return True, None


def paginate_items(items: List[Any], page: int, per_page: int) -> Dict[str, Any]:
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_items = items[start_index:end_index]
    return {
        "items": paginated_items,
        "page": page,
        "per_page": per_page,
        "total_items": len(items),
        "total_pages": (len(items) + per_page - 1) // per_page,
    }


def create_response(data: Any, status_code: int = 200) -> Tuple[Any, int]:
    return jsonify(data), status_code
