def reset_servos():
    print("Resetting all servos to 0 degrees...")
    for pin in pins:
        board.digital[pin].write(0)

# Integrate this into the main script
try:
    if r.recognize_google(audio) == "stop":
        reset_servos()
        print("Emergency stop activated.")
