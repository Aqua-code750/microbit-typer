serial.redirectToUSB()

input.onButtonPressed(Button.A, function () {
    serial.writeLine("DICTATE")
})
