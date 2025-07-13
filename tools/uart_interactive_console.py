
import serial

def main():
    port = 'COM7'  # Change this if needed
    baud = 74880

    try:
        ser = serial.Serial(port, baud, timeout=1)
        print(f"[+] Connected to {port} at {baud} baud.")
        print("Type commands to send over UART. Type 'exit' to quit.\n")

        while True:
            cmd = input("UART> ")
            if cmd.lower() == 'exit':
                break
            ser.write((cmd + '\r\n').encode())
            response = ser.read(1024)
            print("[<] Response:", response.decode(errors='ignore'))

        ser.close()
        print("[+] Connection closed.")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == '__main__':
    main()
