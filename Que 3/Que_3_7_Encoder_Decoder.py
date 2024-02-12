# 7) Write a message encoder - decoder program using a nested function. Define outer function
# as encodeMsg() which will accept a message to encode and a key to encode with. Define the
# inner function as encoder() which will encode the message with a given key (how to encode,
# that is up to you). The outer function then returns this encoded message to the main
# program. Similarly, do the task of decoding the encoded message, by writing outer function
# as decodeMsg() and inner function as decoder().

def encodeMsg(message, key):
    def encoder(message, key):
        encoded_message = ""
        for char in message:
            encoded_char = chr(ord(char) + key) 
            encoded_message += encoded_char
        return encoded_message

    return encoder(message, key)

def decodeMsg(encoded_message, key):
    def decoder(encoded_message, key):
        decoded_message = ""
        for char in encoded_message:
            decoded_char = chr(ord(char) - key)  # Reverse the encoding by shifting back
            decoded_message += decoded_char
        return decoded_message

    return decoder(encoded_message, key)

message = "India is my country!"
key = 3
encoded_message = encodeMsg(message, key)
print("Encoded message:", encoded_message)

decoded_message = decodeMsg(encoded_message, key)
print("Decoded message:", decoded_message)
