from typing import Optional
from django.contrib.auth import get_user_model

User = get_user_model()

# сопоставляем коду процесса (Process.code) поля в CheckDocumentWorkflow:
#  - кто отвечает за шаг (FK на User)
#  - булевый флаг "шаг подписан/подтверждён"
#  - поле для комментария/причины возврата
PROCESS_FIELD_MAP = {
    "it_requirements": {
        "responsible": "check_it_requirements_responsible",         # FK User
        "signature": "check_it_requirements_signature",             # Bool
        "comment": "check_it_requirements_comment",                 # Text
    },
    "tech_requirements": {
        "responsible": "check_technical_requirements_responsible",
        "signature": "check_technical_requirements_signature",
        "comment": "check_technical_requirements_comment",
    },
    "norm_control": {
        "responsible": "norm_control_responsible",
        "signature": "norm_control_signature",
        "comment": "norm_control_comment",
    },
    "3D_model": {
        "responsible": "3D_model_responsible",
        "signature": "3D_model_signature",
        "comment": "3D_model_comment",
    },
}


def wf_step_is_signed(wf, process_code: str) -> bool:
    """возвращает True, если текущий шаг (по коду процесса) уже подписан (…_signature=True)"""
    cfg = PROCESS_FIELD_MAP.get(process_code)
    if not cfg:
        return False
    return bool(getattr(wf, cfg["signature"], False))


def wf_step_responsible(wf, process_code: str) -> Optional[User]:
    """даёт ответственного (User) для шага (по коду процесса)"""
    cfg = PROCESS_FIELD_MAP.get(process_code)
    if not cfg:
        return None
    return getattr(wf, cfg["responsible"], None)


def wf_step_set_comment(wf, process_code: str, text: str) -> None:
    """записывает причину возврата в поле комментария соответствующего шага"""
    cfg = PROCESS_FIELD_MAP.get(process_code)
    if not cfg:
        return
    setattr(wf, cfg["comment"], text or "")


def first_incomplete_step_code(route, wf) -> Optional[str]:
    """
    берём шаги маршрута по порядку (RouteProcess.order) и ищем первый НЕподтверждённый.
    если всё подтверждено — возвращаем None.
    """
    if not wf or not route:
        return None
    for rp in route.routeprocess_set.select_related("process").order_by("order"):
        code = rp.process.code
        if not wf_step_is_signed(wf, code):
            return code
    return None


def next_step_code_after(route, current_code: str) -> Optional[str]:
    """даёт код следующего шага после current_code в рамках данного маршрута"""
    if not route or not current_code:
        return None
    ordered_codes = [
        rp.process.code
        for rp in route.routeprocess_set.select_related("process").order_by("order")
    ]
    try:
        i = ordered_codes.index(current_code)
    except ValueError:
        return None
    return ordered_codes[i + 1] if i + 1 < len(ordered_codes) else None

