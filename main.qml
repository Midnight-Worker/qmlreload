import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    width: 400
    height: 300
	
    color: "#20242b"

	ColumnLayout {
		anchors.centerIn: parent
		spacing: 15

		TextField {
			id: nameInput
			placeholderText: "Your Name"
			Layout.preferredWidth: 250
	
		}
		Label {
			text: nameInput.text === "" ? "Hello!" : "Hallo " + nameInput.text + "!"
			font.pixelSize: 28
			color: "white"  
		}
	}
}
