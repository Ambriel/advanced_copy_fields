from aqt.qt import qtmajor

if qtmajor > 5:
    from . import advanced_copy_fields_qt6
else:
    from . import advanced_copy_fields_qt5
