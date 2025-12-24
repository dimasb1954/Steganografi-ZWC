ZWC_ZERO = '\u200b'  # bit 0
ZWC_ONE = '\u200c'   # bit 1
TERMINAL = "TERMINAL"


def text_to_binary(text):
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))


def encode_message(cover_text, secret_message):
    message_with_terminal = secret_message + TERMINAL
    binary_message = text_to_binary(message_with_terminal)

    zwc_sequence = ''
    for bit in binary_message:
        zwc_sequence += ZWC_ZERO if bit == '0' else ZWC_ONE

    return cover_text + zwc_sequence


if __name__ == "__main__":
    print("=== ENCODING STEGANOGRAFI ZERO-WIDTH CHARACTER ===")

    cover_text = input("Masukkan cover text:\n> ")
    secret_message = input("\nMasukkan pesan rahasia:\n> ")

    stego_text = encode_message(cover_text, secret_message)

    print("\n=== TEKS STEGO (SALIN UNTUK MEDIA SOSIAL) ===")
    print(stego_text)
