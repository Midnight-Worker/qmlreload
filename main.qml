import QtQuick
import QtQuick.Controls

Item {
    anchors.fill: parent

    ListView {
        anchors.fill: parent

        model: ["Anna", "Julian", "Maik"]

        delegate: Rectangle {
            width: ListView.view.width
            height: 50
            border.width: 1

            Text {
                anchors.centerIn: parent
                text: modelData
            }
        }
    }
}
