import serial

PORT = "COM7"      # Replace with your port if different
BAUD = 74880
TIMEOUT = 2

with serial.Serial(PORT, BAUD, timeout=TIMEOUT) as ser, open("uart_log.txt", "w", encoding="utf-8") as log:
    print(f"[+] Listening on {PORT} at {BAUD} baud. Press Ctrl+C to stop.")
    try:
        while True:
            line = ser.readline().decode(errors='ignore').strip()
            if line:
                print(line)
                log.write(line + '\n')
    except KeyboardInterrupt:
        print("\n[+] Logging stopped. Saved to uart_log.txt.")
