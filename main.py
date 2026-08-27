import sys
from pathlib import Path

from PySide6.QtCore import QFileSystemWatcher, QTimer, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlComponent, QQmlEngine
from PySide6.QtQuick import QQuickView


app = QGuiApplication(sys.argv)

qml_file = Path("main.qml").resolve()

view = QQuickView()
view.setWidth(400)
view.setHeight(300)
view.setTitle("QML Hot Reload")
view.show()

engine = view.engine()

current_item = None


def reload_qml():
    global current_item

    print("Reload:", qml_file)

    engine.clearComponentCache()

    component = QQmlComponent(
        engine,
        QUrl.fromLocalFile(str(qml_file))
    )

    if component.isError():
        for error in component.errors():
            print(error.toString())
        return

    new_item = component.create()

    if new_item is None:
        return

    new_item.setParentItem(view.contentItem())

    if current_item is not None:
        if isValid(current_item):
            current_item.deleteLater()

        current_item = None

    current_item = new_item

reload_qml()


watcher = QFileSystemWatcher([str(qml_file)])


def file_changed(path):
    # Kleiner Delay, weil manche Editoren die Datei beim Speichern
    # kurz löschen/ersetzen.
    QTimer.singleShot(100, reload_qml)

    if path not in watcher.files():
        watcher.addPath(path)


watcher.fileChanged.connect(file_changed)

sys.exit(app.exec())
