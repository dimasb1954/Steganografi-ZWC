ZWC_ZERO = '\u200b'  # bit 0
ZWC_ONE = '\u200c'   # bit 1
TERMINAL = "TERMINAL"


def binary_to_text(binary):
    bytes_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    byte_array = bytearray(int(b, 2) for b in bytes_list)
    return byte_array.decode('utf-8', errors='ignore')


def decode_message(stego_text):
    binary_message = ''

    for char in stego_text:
        if char == ZWC_ZERO:
            binary_message += '0'
        elif char == ZWC_ONE:
            binary_message += '1'

    decoded_text = binary_to_text(binary_message)

    if TERMINAL in decoded_text:
        return decoded_text.split(TERMINAL)[0]
    else:
        return "[Pesan tidak ditemukan]"


if __name__ == "__main__":
    print("=== DECODING STEGANOGRAFI ZERO-WIDTH CHARACTER ===")

    stego_text = input("Masukkan teks stego:\n> ")

    secret_message = decode_message(stego_text)

    print("\n=== PESAN RAHASIA ===")
    print(secret_message)
